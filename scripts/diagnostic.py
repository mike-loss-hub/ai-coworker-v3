#!/usr/bin/env python3
"""AI Co-Worker System Diagnostic — three-layer memory architecture."""

import os
import re
from datetime import datetime
from pathlib import Path

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

BASE = Path(__file__).resolve().parent.parent
MEMORY = BASE / "memory"
AGENTS = BASE / "agents" / "prompts"
SKILLS = BASE / "skills"

CORE_SKILLS = {"briefing", "proposal-eval", "meeting-prep", "meeting-debrief",
               "decision-frame", "task-delegation", "stakeholder-email", "portfolio-review", "diagnostic"}


class Result:
    def __init__(self, name):
        self.name, self.status, self.details, self.issues = name, "PASS", {}, []

    def warn(self, msg):
        if self.status == "PASS":
            self.status = "WARN"
        self.issues.append(msg)

    def fail(self, msg):
        self.status = "FAIL"
        self.issues.append(msg)


def check_memory():
    r = Result("MEMORY INTEGRITY")

    layers = {
        "human": ["identity.md", "working-style.md", "feedback-history.md", "growth-log.md"],
        "bridge": ["lessons-learned.md", "pattern-library.md", "anti-patterns.md", "relationship-archetypes.md"],
        "role": [],
    }
    role_dirs = [
        "portfolio", "contacts", "contacts/org-profiles", "grantees",
        "decisions", "tasks", "calendar", "meetings", "standards",
        "ecosystem", "briefings",
    ]

    for layer, files in layers.items():
        layer_path = MEMORY / layer
        if not layer_path.is_dir():
            r.fail(f"Missing layer: memory/{layer}/")
        for f in files:
            if not (layer_path / f).exists():
                r.warn(f"Missing: memory/{layer}/{f}")

    for d in role_dirs:
        if not (MEMORY / "role" / d).is_dir():
            r.fail(f"Missing: memory/role/{d}")

    if not (MEMORY / "context-index.md").exists():
        r.fail("Missing context-index.md")

    contacts = list((MEMORY / "role" / "contacts").glob("*.md"))
    grantee_dirs = (
        [d for d in (MEMORY / "role" / "grantees").iterdir() if d.is_dir()]
        if (MEMORY / "role" / "grantees").is_dir()
        else []
    )
    decisions = list((MEMORY / "role" / "decisions").glob("*.md"))

    tasks_file = MEMORY / "role" / "tasks" / "active.md"
    open_tasks = 0
    if tasks_file.exists():
        open_tasks = sum(
            1
            for line in tasks_file.read_text().split("\n")
            if line.strip().startswith("|")
            and "Task" not in line
            and "---" not in line
            and line.strip() != "|"
        )

    for gd in grantee_dirs:
        for req in ["profile.md", "health-log.md", "correspondence.md", "milestones.md"]:
            if not (gd / req).exists():
                r.warn(f"Grantee {gd.name} missing {req}")

    total = sum(1 for _ in MEMORY.rglob("*.md"))
    human_files = sum(1 for _ in (MEMORY / "human").rglob("*.md")) if (MEMORY / "human").is_dir() else 0
    bridge_files = sum(1 for _ in (MEMORY / "bridge").rglob("*.md")) if (MEMORY / "bridge").is_dir() else 0
    role_files = sum(1 for _ in (MEMORY / "role").rglob("*.md")) if (MEMORY / "role").is_dir() else 0

    r.details = {
        "total_files": total,
        "human_layer": f"{human_files} files",
        "bridge_layer": f"{bridge_files} files",
        "role_layer": f"{role_files} files",
        "contacts": len(contacts),
        "grantees": len(grantee_dirs),
        "open_tasks": open_tasks,
        "decisions": len(decisions),
    }
    return r


def check_agents():
    r = Result("AGENT HEALTH")
    prompts = list(AGENTS.glob("*.md")) if AGENTS.is_dir() else []
    r.details = {"found": len(prompts), "expected": 17}
    if len(prompts) < 17:
        r.fail(f"Found {len(prompts)}/17")
    for p in prompts:
        content = p.read_text().lower()
        if len(content.strip()) < 50:
            r.warn(f"{p.name} empty")
        for s in ["domain", "context sources"]:
            if s not in content:
                r.warn(f"{p.name} missing '{s}'")
    return r


def check_skills():
    r = Result("SKILL HEALTH")
    found = {s.stem for s in SKILLS.glob("*.md")} if SKILLS.is_dir() else set()
    core_found = len(CORE_SKILLS & found)
    custom = found - CORE_SKILLS
    r.details = {"core_found": core_found, "core_expected": len(CORE_SKILLS), "custom": len(custom)}
    missing = CORE_SKILLS - found
    if missing:
        r.fail(f"Missing core: {', '.join(missing)}")
    required = ["resource tier", "when to use", "process", "context sources", "output format", "quality standard"]
    tools_files = {s.stem for s in SKILLS.glob("tools-*.md")}
    for sf in SKILLS.glob("*.md"):
        if sf.stem in tools_files:
            continue
        content = sf.read_text().lower()
        for s in required:
            if s not in content:
                r.warn(f"{sf.name} missing '{s}'")
    return r


def check_freshness():
    r = Result("CONTEXT FRESHNESS")
    areas = {
        "human": MEMORY / "human",
        "bridge": MEMORY / "bridge",
        "contacts": MEMORY / "role" / "contacts",
        "grantees": MEMORY / "role" / "grantees",
        "portfolio": MEMORY / "role" / "portfolio",
        "tasks": MEMORY / "role" / "tasks",
        "calendar": MEMORY / "role" / "calendar",
        "standards": MEMORY / "role" / "standards",
        "briefings": MEMORY / "role" / "briefings",
        "decisions": MEMORY / "role" / "decisions",
    }
    freshness = {}
    for name, path in areas.items():
        if path.exists():
            files = list(path.rglob("*.md"))
            if files:
                freshness[name] = datetime.fromtimestamp(max(f.stat().st_mtime for f in files))
    if freshness:
        freshest = max(freshness, key=freshness.get)
        stalest = min(freshness, key=freshness.get)
        r.details["freshest"] = f"{freshest} ({freshness[freshest].strftime('%Y-%m-%d')})"
        r.details["stalest"] = f"{stalest} ({freshness[stalest].strftime('%Y-%m-%d')})"
        now = datetime.now()
        maint = []
        for n, dt in freshness.items():
            age = (now - dt).days
            if n == "briefings" and age > 3:
                maint.append(f"No briefing in {age} days")
            elif n == "tasks" and age > 14:
                maint.append(f"Tasks stale ({age} days)")
            elif n == "contacts" and age > 30:
                maint.append(f"Contacts stale ({age} days)")
        r.details["maintenance"] = maint or ["none"]
        if maint:
            r.warn("; ".join(maint))
    return r


def check_coherence():
    r = Result("PORTFOLIO COHERENCE")
    issues = []
    thesis = MEMORY / "role" / "portfolio" / "investment-thesis.md"
    if thesis.exists():
        content = thesis.read_text()
        for p in ["Longitudinal Memory", "Provenance", "Agent Orchestration", "Local-First"]:
            if p not in content:
                issues.append(f"Thesis missing pillar: {p}")

    grantee_dirs = (
        [d.name for d in (MEMORY / "role" / "grantees").iterdir() if d.is_dir()]
        if (MEMORY / "role" / "grantees").is_dir()
        else []
    )
    state = MEMORY / "role" / "portfolio" / "portfolio-state.md"
    if state.exists():
        content = state.read_text().lower().replace(" ", "").replace("-", "")
        for gd in grantee_dirs:
            if gd.replace("-", "") not in content:
                issues.append(f"{gd} not in portfolio-state.md")

    r.details["inconsistencies"] = issues or ["none"]
    for i in issues:
        r.warn(i)
    return r


def check_portability():
    r = Result("PORTABILITY")
    human = MEMORY / "human"
    bridge = MEMORY / "bridge"

    human_ok = human.is_dir() and (human / "identity.md").exists() and (human / "working-style.md").exists()
    bridge_ok = bridge.is_dir() and (bridge / "lessons-learned.md").exists() and (bridge / "pattern-library.md").exists()
    human_skills = list((human / "skills").glob("*.md")) if (human / "skills").is_dir() else []

    r.details = {
        "human_layer_intact": human_ok,
        "bridge_layer_intact": bridge_ok,
        "portable_skills": len(human_skills),
        "exportable": human_ok and bridge_ok,
    }
    if not human_ok:
        r.fail("Human layer incomplete — portability broken")
    if not bridge_ok:
        r.warn("Bridge layer incomplete — transition context limited")
    if len(human_skills) == 0:
        r.warn("No portable skills captured yet")
    return r


def check_smoke():
    r = Result("FUNCTIONAL SMOKE TESTS")
    tests = {}
    tests["daily_briefing"] = all(
        (MEMORY / "role" / f).exists() and (MEMORY / "role" / f).stat().st_size > 0
        for f in ["calendar/upcoming.md", "tasks/active.md", "portfolio/portfolio-state.md"]
    )
    contacts = list((MEMORY / "role" / "contacts").glob("*.md"))
    tests["contact_retrieval"] = len(contacts) > 0 and contacts[0].stat().st_size > 0
    tf = MEMORY / "role" / "tasks" / "active.md"
    tests["task_listing"] = tf.exists() and tf.stat().st_size > 0
    tests["identity_load"] = (MEMORY / "human" / "identity.md").exists()
    r.details = tests
    for t, passed in tests.items():
        if not passed:
            r.fail(f"{t}: FAIL")
    return r


STATUS_COLORS = {"PASS": "green", "WARN": "yellow", "FAIL": "red"}


def print_rich(ts, results, overall):
    table = Table(title="CO-WORKER DIAGNOSTIC REPORT", title_style="bold cyan", border_style="cyan")
    table.add_column("Check", style="bold")
    table.add_column("Status", justify="center")
    table.add_column("Details")
    table.add_column("Issues")

    for r in results:
        details_str = "\n".join(
            f"{k}: {', '.join(str(x) for x in v) if isinstance(v, list) else v}"
            for k, v in r.details.items()
        )
        issues_str = "\n".join(r.issues) if r.issues else "none"
        status_text = Text(r.status, style=STATUS_COLORS.get(r.status, "white"))
        table.add_row(r.name, status_text, details_str, issues_str)

    console.print()
    console.print(f"  Run: {ts}", style="dim")
    console.print(table)

    overall_color = {"HEALTHY": "green", "NEEDS ATTENTION": "yellow", "DEGRADED": "red"}.get(overall, "white")
    top = next((i for r in results for i in r.issues), None)
    summary = f"Top priority: {top}" if top else "All systems operational."
    console.print(Panel(f"[bold {overall_color}]{overall}[/]\n{summary}", title="Overall", border_style=overall_color))


def print_plain(ts, results, overall):
    print("═" * 50)
    print("  CO-WORKER DIAGNOSTIC REPORT")
    print(f"  Run: {ts}")
    print("═" * 50)
    for r in results:
        print(f"\n{r.name + ':':30s} [{r.status}]")
        for k, v in r.details.items():
            if isinstance(v, list):
                print(f"  {k}: {', '.join(str(x) for x in v)}")
            else:
                print(f"  {k}: {v}")
        print(f"  Issues: {'; '.join(r.issues) if r.issues else 'none'}")
    print("\n" + "═" * 50)
    top = next((i for r in results for i in r.issues), None)
    print(f"  OVERALL: {overall}")
    print(f"  {f'Top priority: {top}' if top else 'All systems operational.'}")
    print("═" * 50)


def main():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results = [
        check_memory(), check_agents(), check_skills(), check_freshness(),
        check_coherence(), check_portability(), check_smoke(),
    ]

    overall = "HEALTHY"
    for r in results:
        if r.status == "FAIL":
            overall = "DEGRADED"
            break
        elif r.status == "WARN":
            overall = "NEEDS ATTENTION"

    if HAS_RICH:
        print_rich(ts, results, overall)
    else:
        print_plain(ts, results, overall)

    diag = MEMORY / "diagnostics" / f"{datetime.now().strftime('%Y-%m-%d')}-diagnostic.md"
    diag.parent.mkdir(exist_ok=True)
    with open(diag, "w") as f:
        f.write(f"# Diagnostic Report — {ts}\n\n**Overall: {overall}**\n\n")
        for r in results:
            f.write(f"## {r.name}: {r.status}\n")
            for k, v in r.details.items():
                f.write(f"- {k}: {v}\n")
            if r.issues:
                f.write(f"- Issues: {'; '.join(r.issues)}\n")
            f.write("\n")
    print(f"\nReport saved to {diag}")


if __name__ == "__main__":
    main()

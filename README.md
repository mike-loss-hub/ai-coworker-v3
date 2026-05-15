# AI Co-Worker v3

An AI co-worker system built on Claude Code that provides persistent, structured memory across sessions. Designed for a Senior Program Officer managing a philanthropic portfolio, but the architecture is role-agnostic — the human layer travels with you, the role layer stays behind.

This project is itself a working demonstration of the thesis it supports: **portable, persistent AI context that survives transitions**.

## What It Does

- **Remembers everything.** Contacts, decisions, grantee health, meeting history, tasks — stored in structured markdown files that persist across sessions.
- **Thinks from multiple perspectives.** 17 agent perspectives organized in 4 tiers evaluate decisions from technical, equity, operational, and ecosystem angles simultaneously.
- **Produces Decision Frames, not recommendations.** Facts, uncertainties, perspectives, options, tradeoffs — you make the call.
- **Learns from you over time.** Corrections, preferences, and patterns are logged and applied in future sessions.
- **Ports with you.** Three-layer memory architecture separates what's about *you* from what's about *this job*.

## Quick Start

### 1. Open in Claude Code

```bash
cd ai-coworker-v3
# Open in VS Code with Claude Code extension, or use Claude Code CLI
```

The `CLAUDE.md` file activates the co-worker persona automatically. On session start, it reads the context index and leads with what's happening today.

### 2. Start Talking

| What you say | What happens |
|---|---|
| "Brief me" | Daily briefing from calendar, tasks, portfolio state |
| "Evaluate this proposal" | Multi-perspective Decision Frame |
| "Brief me for my meeting with Linda Zhang" | Meeting prep with dynamics, talking points, landmines |
| "Debrief: here's what happened..." | Structured notes, action items extracted, contacts updated |
| "Draft a check-in email to Raj Patel" | Tone-matched draft using contact profile |
| "Run diagnostic" | Full system health check |
| "Portfolio review" | Assessment across health, pillars, budget, equity, risks |

### 3. Dashboard

```bash
python3 scripts/serve-dashboard.py
# Open http://localhost:8080
```

Visual overview of portfolio health, active tasks, deadlines, alerts, and pillar coverage. Auto-refreshes every 30 seconds from the memory files.

## Architecture

### Three-Layer Memory

```
memory/
  human/                  # PORTABLE — travels with you across roles
    identity.md             Who you are, strengths, growth areas
    working-style.md        Communication and decision preferences
    feedback-history.md     Every correction the AI has received
    growth-log.md           How your judgment evolves over time
    skills/                 Generalizable workflow patterns

  bridge/                 # TRANSITIONAL — helps onboard to a new role
    lessons-learned.md      Generalizable insights
    pattern-library.md      Recurring decision frameworks
    anti-patterns.md        Mistakes to carry forward
    relationship-archetypes.md  Stakeholder management patterns

  role/                   # ROLE-BOUND — specific to this position
    portfolio/              Investment thesis, grants, budget, pipeline
    contacts/               18 key contacts with relationship history
    grantees/               8 active grants with health logs and milestones
    tasks/                  Active, completed, blocked
    calendar/               Meetings and deadlines
    decisions/              Decision records with rationale
    meetings/               Prep docs and notes
    standards/              Standards landscape and comment periods
    ecosystem/              Funder landscape, field map, evidence base
    briefings/              Archived daily briefings
```

Every interaction writes to the appropriate layer. Role data stays when you leave. Human data travels with you. Bridge data helps the transition.

### Agent Architecture (17 Perspectives, 4 Tiers)

| Tier | Agents | Purpose |
|------|--------|---------|
| **0: Orchestrator** | Portfolio Intelligence Director | Strategic brain, mode selection, decision framing |
| **1: Primary** | Technical Architecture, Ecosystem Intelligence, Stakeholder Coalition, Equity & Learner Impact, Grantmaking Operations | Core analytical perspectives |
| **2: Sub-Agents** | Standards Analyst, Local-First Specialist, Funder Tracker, Research Monitor, Communications Drafter, Disaggregated Outcomes, Grantee Health Monitor | Domain-specific depth |
| **3: Meta** | Performance Evaluator, Coherence Auditor, Architecture Review, Human Judgment Integrator | Self-monitoring and improvement |

The Equity & Learner Impact perspective is **always consulted** on substantive decisions. Agent prompts live in `agents/prompts/`.

### Skills (Executable Workflows)

Skills in `skills/` define how the co-worker performs specific tasks. Each has: trigger conditions, step-by-step process, context sources, output format, and quality standard.

**Core skills:** briefing, proposal-eval, meeting-prep, meeting-debrief, decision-frame, task-delegation, stakeholder-email, portfolio-review, diagnostic

**Integration skills:** calendar, email, task management, document storage (MCP stubs — work locally without MCP, upgrade when servers are connected)

**Meta skills:** monitoring (Tier 3 agents), skill-improvement (self-refinement), context-summarization (compaction), export/import (portability)

## Portability

### Export Modes

```bash
python3 scripts/export.py --portable   # Human + Bridge layers → new role
python3 scripts/export.py --role       # Role layer → your successor
python3 scripts/export.py --full       # Everything → backup
```

### Import

```bash
python3 scripts/import_context.py archive.tar.gz
# Runs diagnostic automatically after import
```

When importing a `--portable` archive into a new role, the co-worker restores your identity, preferences, feedback history, and learned patterns, then asks about your new role to generate fresh role-layer scaffolding.

## Diagnostics

```bash
python3 scripts/diagnostic.py
```

Checks seven areas:

| Check | What It Verifies |
|-------|-----------------|
| Memory Integrity | All directories and files exist, no orphaned references |
| Agent Health | All 17 prompts present with required sections |
| Skill Health | Core skills complete and properly structured |
| Context Freshness | No stale areas, flags maintenance needs |
| Portfolio Coherence | Cross-file consistency (state matches profiles, budget sums) |
| Portability | Human and bridge layers intact, exportable |
| Smoke Tests | Briefing, contact retrieval, task listing, identity load |

Results are saved to `memory/diagnostics/` for health tracking over time.

## File Structure

```
ai-coworker-v3/
  CLAUDE.md               # Co-worker instructions — Claude Code reads this on startup
  README.md               # This file
  memory/                 # Persistent context (human + bridge + role layers)
  agents/prompts/         # 17 agent perspective definitions
  skills/                 # Executable workflow definitions
  scripts/
    diagnostic.py           System health check
    serve-dashboard.py      Local dashboard server
    export.py               Selective context export
    import_context.py       Context import with validation
  dashboard/
    index.html              Portfolio dashboard (reads from memory/)
  scenarios/
    test-proposal.md        Sample proposal for testing evaluation skill
```

## Current Limitations

- **No live integrations.** Calendar, email, and tasks are managed through conversation. MCP integration stubs exist in `skills/integration-*.md` and define the mapping — connect MCP servers when available.
- **No proactive outreach.** The co-worker only acts during active Claude Code sessions. Use Claude Code's `/schedule` to set up recurring briefings or monitoring.
- **Manual calendar maintenance.** Meetings are tracked in markdown. Until a calendar MCP server is connected, you update `memory/role/calendar/upcoming.md` by telling the co-worker about meetings.
- **Seed data is fictional.** The 8 grantees, 18 contacts, and portfolio data are realistic but fabricated. Replace with real data as you use the system.

## Customization

- **Change the role:** Edit `memory/human/identity.md` and regenerate the role layer for your actual position.
- **Add a skill:** Create a new `.md` file in `skills/` following the trigger/process/context/output/quality structure. The co-worker will also offer to create skills after novel tasks.
- **Add an agent perspective:** Create a new `.md` file in `agents/prompts/` with role, domain scope, output format, and context sources. Update the orchestrator prompt to include it.
- **Refine behavior:** Corrections you give the co-worker are logged to `memory/human/feedback-history.md` and applied going forward.

## Requirements

- [Claude Code](https://claude.ai/claude-code) (CLI, VS Code extension, or desktop app)
- Python 3.8+
- No API keys, external databases, or cloud services required

### Python Setup

```bash
# Option 1: Run the setup script (creates venv, installs deps, runs diagnostic)
./setup.sh

# Option 2: Manual setup
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows
pip install -r requirements.txt
python3 scripts/diagnostic.py    # Verify everything works
```

### Python Dependencies

| Package | Purpose |
|---------|---------|
| `rich` | Formatted terminal output for diagnostics |
| `watchdog` | File-watching auto-reload for the dashboard server |
| `pyyaml` | YAML support for structured memory files |
| `markdown` | Markdown parsing for memory file validation |

All scripts degrade gracefully if deps are missing — stdlib fallbacks are used (plain text output, no auto-reload). But `pip install -r requirements.txt` gives the full experience.

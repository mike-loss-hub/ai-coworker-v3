# Skill: System Diagnostic

## Resource Tier
Haiku — file existence checks and structural validation, no analysis needed.

## When to Use
The user wants to verify the co-worker system is working correctly. They may say "run diagnostic," "is everything working?", "system check," or express concern about data integrity or missing information.

## Process

### 1. Memory Integrity
- Verify all schema directories exist
- Verify context-index.md is present and parseable
- Check for orphaned references (contacts mentioned in grantee profiles without contact files, etc.)
- Count: total files, contacts, grantees, open tasks, decisions

### 2. Agent Health
- Verify all 17 agent prompt files exist in agents/prompts/
- Check each contains: role definition, domain scope, output format, context sources
- Verify orchestrator references all agents

### 3. Skill Health
- Verify core skill files exist in skills/
- Check each contains: trigger, process, context sources, output format, quality standard
- Verify skills reference memory/ paths that exist
- Count custom skills created beyond core set

### 4. Context Freshness
- Check file modification timestamps for each memory area
- Flag stale: contacts >30 days, active tasks untouched >14 days, briefings gap >3 days
- Report freshest and stalest areas

### 5. Portfolio Coherence
- Compare portfolio-state.md health ratings with individual grantee health-log.md entries
- Verify pillar-coverage.md reflects current active grantees
- Check budget-tracker.md sums
- Verify investment-thesis.md references all four pillars

### 6. Functional Smoke Tests
- Can a daily briefing be produced from current memory state?
- Can a contact be retrieved by name?
- Can open tasks be listed from tasks/active.md?

## Output Format
```
═══════════════════════════════════════════
  CO-WORKER DIAGNOSTIC REPORT
  Run: [timestamp]
═══════════════════════════════════════════

MEMORY INTEGRITY:        [PASS/WARN/FAIL]
  Files: [n] | Contacts: [n] | Grantees: [n] | Open tasks: [n] | Decisions: [n]
  Issues: [list or "none"]

AGENT HEALTH:            [PASS/WARN/FAIL]
  Found: [n]/17 | Missing: [list or "none"]
  Issues: [list or "none"]

SKILL HEALTH:            [PASS/WARN/FAIL]
  Core: [n]/9 | Custom: [n] | Broken refs: [list or "none"]
  Issues: [list or "none"]

CONTEXT FRESHNESS:       [PASS/WARN/FAIL]
  Freshest: [area] ([date])
  Stalest: [area] ([date])
  Maintenance needed: [list or "none"]

PORTFOLIO COHERENCE:     [PASS/WARN/FAIL]
  Inconsistencies: [list or "none"]

FUNCTIONAL SMOKE TESTS:  [PASS/WARN/FAIL]
  Daily briefing:  [PASS/FAIL]
  Contact retrieval: [PASS/FAIL]
  Task listing:    [PASS/FAIL]

═══════════════════════════════════════════
  OVERALL: [HEALTHY / NEEDS ATTENTION / DEGRADED]
  [Summary sentence with top priority action if any]
═══════════════════════════════════════════
```

## Post-Process
Save results to memory/diagnostics/[date]-diagnostic.md
If fixable issues found (e.g., stale context-index), offer to fix them.

## Quality Standard
- Every check produces a specific result, not "looks ok"
- Counts are exact
- Freshness uses actual file timestamps
- Coherence checks compare actual data between files
- Smoke tests actually attempt the operation

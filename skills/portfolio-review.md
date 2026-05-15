# Skill: Portfolio Review

## Resource Tier
Opus — cross-portfolio synthesis, multi-perspective analysis, strategic judgment.

## When to Use
The user wants a big-picture assessment of the portfolio. They may ask about overall health, request a board update, say "how are we doing," or need a quarterly/periodic review. Any request for cross-portfolio analysis maps here.

## Process
1. Read portfolio-state.md, pillar-coverage.md, budget-tracker.md (parallel)
2. **Fan out** — run grantee health checks as parallel Haiku subagents (one per flagged grantee, reading only that grantee's health-log.md)
3. **Fan out** — run 5 primary perspectives as parallel Sonnet subagents, each given the portfolio overview from step 1
4. **Fan in** — collect grantee health results and perspective outputs
5. **Synthesize** — produce structured review on Opus, integrating all inputs

## Context Sources
This is the most context-heavy skill. Load in stages, not all at once:

**Stage 1 — Portfolio overview:**
- memory/role/portfolio/portfolio-state.md
- memory/role/portfolio/pillar-coverage.md
- memory/role/portfolio/budget-tracker.md

**Stage 2 — Grantee health (load selectively):**
- memory/role/grantees/[each-grantee]/health-log.md — load only grantees flagged yellow/red in portfolio-state, then greens if needed

**Stage 3 — External context (only if review requires it):**
- memory/role/ecosystem/evidence-base.md
- memory/role/standards/landscape.md

**Perspectives:** Load agents/prompts/01-05 only when actively engaging each perspective, not all at once

## Output Format
```
# Portfolio Review — [Date]

## Portfolio Health Summary
[Overall assessment: Healthy/Watch/Concern]

## Grantee Status Grid
| Grantee | Health | Trend | Key Issue | Next Milestone |
|---------|--------|-------|-----------|----------------|

## Pillar Coverage
[Assessment by pillar with gaps and risks]

## Budget Status
[Summary with burn rate and remaining capacity]

## Equity Check
[Are we serving target populations? Disaggregated outcomes available?]

## Strategic Alignment
[Does current portfolio match investment thesis? Any drift?]

## Risks & Flags
[Top 3 risks with severity and recommended actions]

## Recommendations for Discussion
[Items that need the user's attention — framed as questions, not directives]
```

## Quality Standard
- Includes trend analysis (improving/declining/stable), not just current status
- Equity assessment is substantive
- Flags strategic drift from investment thesis
- Identifies cross-grantee dependencies and risks

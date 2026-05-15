# Skill: Grant Proposal Evaluation

## When to Use
The user has something to evaluate — a proposal, concept note, idea from a potential grantee, or any investment opportunity. They may share a document, describe it verbally, or ask "what do you think of this?" in the context of a potential grant.

## Resource Tier
Opus — requires multi-perspective analysis, nuanced judgment, and Decision Frame construction.

## Process
1. Read the proposal document + pillar-coverage.md + budget-tracker.md
2. **Fan out** — run 4 perspective analyses as parallel Sonnet subagents, each given the proposal text and its relevant context:
   - Technical Architecture: architecture soundness, conflicts with existing grantees, technical risks
   - Equity & Learner Impact: who benefits, target populations served, equity outcomes measured
   - Grantmaking Operations: budget reasonableness, team capability, key person risk, timeline feasibility
   - Ecosystem Intelligence: portfolio gap coverage, standards landscape fit, co-investment opportunities
3. **Fan in** — collect all 4 perspective outputs
4. **Synthesize** — construct Decision Frame on Opus, integrating all perspectives

## Context Sources
**Always load:**
- memory/role/portfolio/pillar-coverage.md — to assess strategic fit
- memory/role/portfolio/budget-tracker.md — to assess budget availability

**Load if relevant:**
- memory/role/portfolio/pipeline.md — only if checking for duplicates in pipeline
- memory/role/grantees/[specific-grantee]/ — only grantees in the same pillar, not all 8
- memory/role/standards/landscape.md — only if proposal touches standards work
- memory/role/ecosystem/field-map.md — only the relevant section
- agents/prompts/01-04 — load each perspective prompt only when actively engaging it

## Output Format
Decision Frame:
- **Facts** — What we know about this proposal
- **Uncertainties** — What we don't know or can't verify
- **Perspectives** — Technical, Equity, Operations, Ecosystem assessments
- **Options** — Fund, fund with conditions, decline, defer
- **Tradeoffs** — What each option costs and gains

## Quality Standard
- Never outputs a yes/no recommendation — always a Decision Frame
- All four perspectives represented
- Equity perspective is substantive, not checkbox
- Identifies specific portfolio gaps this would fill
- Budget feasibility assessed against unallocated funds

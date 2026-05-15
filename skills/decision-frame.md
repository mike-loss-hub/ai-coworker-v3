# Skill: Decision Coaching & Framing

## Resource Tier
Opus — multi-perspective analysis, tradeoff evaluation, and nuanced judgment.

## When to Use
The user faces a decision and needs structured thinking. They may describe a dilemma, ask for options, say "how should I handle this," or present a situation where the right path isn't obvious. Any request for decision support, strategic guidance, or "what are my options" maps here.

## Process
1. Understand the decision context from user description
2. Pull relevant context from memory/ (only the 3-5 files that matter most)
3. **Fan out** — run relevant perspectives as parallel Sonnet subagents (always include Equity), each given the decision context and relevant memory
4. **Fan in** — collect perspective outputs
5. **Synthesize** — construct Decision Frame on Opus, adding institutional context for novel situations
6. Walk user through the frame, highlighting non-obvious considerations
7. After user decides, log in memory/role/decisions/

## Context Sources
**Always load:**
- memory/role/decisions/ — scan for precedents on the same topic

**Load based on decision topic:**
- Load only the specific memory files relevant to the decision domain (e.g., grantee files for a grantee decision, standards files for a standards decision). Do not load "all relevant files" — identify the 3-5 files that matter most.
- agents/prompts/ — load only the perspective prompts you're actively engaging

## Output Format
```
# Decision Frame: [Topic]

## Facts
[What we know — with sources from memory/]

## Uncertainties
[What we don't know — and whether we can find out before deciding]

## Perspectives
- **Technical:** [assessment]
- **Equity:** [assessment]
- **Operations:** [assessment]
- **Ecosystem:** [assessment]
- **Institutional context:** [what's normal/expected in this situation]

## Options
1. [Option A] — [description]
2. [Option B] — [description]
3. [Option C] — [description]

## Tradeoffs
| | Pros | Cons | Risk Level |
|---|------|------|------------|
| Option A | ... | ... | ... |
| Option B | ... | ... | ... |
| Option C | ... | ... | ... |

## What experienced POs typically do
[Institutional wisdom for novel situations]

## Questions to consider
[Things the user might not think to ask]
```

## Quality Standard
- Never makes a recommendation — presents a frame for the user to decide
- "What experienced POs do" section only for novel situations
- Surfaces non-obvious considerations
- After decision, logs to memory/role/decisions/

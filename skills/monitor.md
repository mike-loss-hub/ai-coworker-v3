# Skill: System Monitoring (Tier 3 Agents)

## Resource Tier
Sonnet — self-assessment requires synthesis but not full multi-perspective analysis.

## When to Use
The user wants to assess how the co-worker itself is performing — whether perspectives are balanced, whether outputs are well-calibrated, whether the system is aligned with the user's needs. Also activates periodically during REFLECTION mode.

## Process
1. **Agent Performance Evaluation** (agents/prompts/13)
   - Review recent interactions: which agent perspectives were consulted?
   - Flag perspectives consistently ignored
   - Assess whether agent outputs were actionable

2. **System Coherence Audit** (agents/prompts/14)
   - Check for contradictions between agent perspectives in recent outputs
   - Assess Decision Frame quality: right depth for the decision complexity?
   - Check for busywork (unnecessary alerts, redundant briefings)

3. **Architecture Review** (agents/prompts/15)
   - Which agents are most/least used?
   - Any coverage gaps based on recent user requests?
   - Should any sub-agents be promoted or consolidated?
   - Are skills capturing workflows effectively?

4. **Human Judgment Integration** (agents/prompts/16)
   - Review memory/human/feedback-history.md for new corrections
   - Compare user decisions against agent recommendations
   - Flag alignment drift or echo chamber risk

## Context Sources
- memory/human/feedback-history.md
- memory/diagnostics/ (recent diagnostic reports)
- memory/role/decisions/ (user decision patterns)
- All agents/prompts/

## Output Format
```
# Monitoring Report — [Date]

## Agent Performance
- Most consulted: [perspectives]
- Least consulted: [perspectives]
- Recommendations: [adjustments if any]

## System Coherence
- Contradictions found: [none / list]
- Decision Frame calibration: [assessment]
- Busywork flags: [none / list]

## Architecture Health
- Coverage gaps: [none / identified gaps]
- Consolidation candidates: [none / list]
- New skill candidates: [workflows done repeatedly without a skill]

## Human Alignment
- Corrections logged: [count since last check]
- Pattern: [what the user consistently values]
- Echo chamber risk: [low / medium / high]
```

## Quality Standard
- Specific observations, not generic assessments
- Actionable recommendations
- Honest about limitations — flag if insufficient data for assessment

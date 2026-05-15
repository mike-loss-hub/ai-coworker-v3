# Pillar Coverage Analysis

**Last Updated:** 2026-04-28

## Coverage Summary

| Pillar | Active Grants | Total Funding | Coverage | Gaps |
|--------|--------------|---------------|----------|------|
| Longitudinal Memory | 2 (LearnChain, FieldKit) | $1.6M | Moderate | Memory consolidation across agents |
| Provenance | 3 (CredBridge, LearnTrail, TrustLayer) | $2.0M | Strong | At risk if LearnTrail fails |
| Agent Orchestration | 2 (PathWeaver, TrustLayer) | $1.7M | Moderate | No pure coordination protocol grant |
| Local-First | 3 (OpenSync, EdgeWise, FieldKit) | $1.95M | Strong | Edge inference still unproven |

## Gap Analysis

### Longitudinal Memory — MODERATE COVERAGE
- LearnChain covers the storage/sync layer well
- FieldKit covers the community-facing deployment
- **GAP:** No grant specifically addresses memory consolidation — what happens when a learner's context is spread across 5 institutions over 8 years? ContextWeave proposal (in pipeline) would address this
- **GAP:** No work on memory decay/relevance — how does the system decide what context is still useful after 5 years?

### Provenance — STRONG BUT FRAGILE
- Three grants provide good coverage of verification, tracking, and trust frameworks
- **RISK:** LearnTrail (Red health) is the only grant focused on AI-generated summary provenance. If it fails, we lose coverage of a critical sub-domain
- TrustLayer bridges to Agent Orchestration nicely
- VerifyNet proposal (in pipeline) would add decentralized verification

### Agent Orchestration — MODERATE COVERAGE
- PathWeaver is the flagship — strong reference implementation
- TrustLayer provides the trust layer agents need
- **GAP:** No grant addresses the agent-to-agent communication protocol layer itself. We're relying on MCP/A2A emerging as standards — need a backup if they fragment
- ContextWeave proposal would partially address this

### Local-First — STRONG COVERAGE
- Three grants covering sync protocols, edge inference, and community deployment
- **GAP:** EdgeWise performance on low-resource hardware is unproven (Yellow health)
- FieldKit will provide real-world validation with actual community college students
- SyncBridge proposal (in pipeline) could help or duplicate — needs assessment

## Cross-Pillar Gaps

1. **No grant spans all four pillars** — the portfolio thesis requires them to work together, but integration testing is happening ad hoc between individual grantee teams
2. **Convening needed** — grantees working on adjacent problems aren't collaborating enough. A portfolio-wide convening in Q3 would help.
3. **Standards alignment** — work is happening in parallel with standards bodies but coordination could be tighter. The May 5 standards alignment meeting is a step.

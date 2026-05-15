# Proposal: ContextWeave — Agent Memory Consolidation Protocol

## Overview
- **PI:** Dr. Hannah Liu, UC Berkeley School of Information
- **Organization:** UC Berkeley (Computational Research in Adaptive Learning Lab)
- **Ask:** $600,000 over 2 years
- **Pillar:** Agent Orchestration + Longitudinal Memory

## Problem Statement
When multiple AI agents serve the same learner over time, each accumulates its own memory of the learner. An advising agent knows the student's academic history; a tutoring agent knows their learning patterns; a career agent knows their professional goals. These memories overlap, conflict, and fragment. No protocol exists for agents to consolidate overlapping memories into a coherent, non-redundant learner record while preserving provenance.

## Proposed Solution
ContextWeave is a protocol specification and reference implementation for agent memory consolidation. The protocol defines:
1. A canonical format for agent-generated learner observations
2. A merge algorithm for consolidating overlapping observations (using semantic similarity and temporal ordering)
3. A provenance layer that tracks which agent generated which observation and which consolidation decisions were made
4. An API for agents to request consolidated context and contribute new observations

## Technical Approach
- Semantic deduplication using embedding-based similarity (threshold-configurable)
- Temporal conflict resolution using vector clocks (compatible with CRDT approaches)
- Provenance metadata following W3C PROV-O ontology
- Transport-agnostic design (works over MCP, A2A, or direct API)
- Reference implementation in Python with TypeScript client library

## Team
- Dr. Hannah Liu — PI, 12 years in information retrieval and knowledge representation. Led 3 prior NSF-funded projects.
- Dr. Marcus Chen — Co-PI, NLP and semantic similarity. Previously at Google Research.
- 2 PhD students, 1 postdoc (to be hired)

## Budget
| Category | Year 1 | Year 2 | Total |
|----------|--------|--------|-------|
| Personnel (PI, Co-PI, students, postdoc) | $280K | $250K | $530K |
| Computing infrastructure | $20K | $15K | $35K |
| Travel (conferences, standards meetings) | $15K | $10K | $25K |
| Indirect costs (negotiated rate) | $5K | $5K | $10K |
| **Total** | **$320K** | **$280K** | **$600K** |

## Deliverables
1. Protocol specification v1.0 (Month 12)
2. Reference implementation (Month 18)
3. Interoperability testing with 2+ existing agent frameworks (Month 20)
4. Evaluation study with simulated multi-agent scenarios (Month 24)
5. Workshop paper at AAAI or similar venue (Month 24)

## Equity Considerations
The proposal notes that memory consolidation is especially important for learners who move between institutions frequently — transfer students, workforce reentry populations, military-connected learners. These populations are most likely to have fragmented agent memories. The protocol is designed to work with minimal computational overhead to support deployment on resource-constrained platforms.

## Standards Alignment
- W3C PROV-O for provenance
- Compatible with MCP and A2A transport protocols
- Designed for compatibility with CLR and VC data formats
- Will participate in T3 Innovation Network working groups

## Letters of Support
- Dr. Sofia Chen (PathWeaver AI) — willing to integrate ContextWeave with PathWeaver's multi-agent demo
- Dr. Amara Osei (LearnChain Labs) — interested in testing consolidation with LearnChain's LRS
- 1EdTech Consortium — letter acknowledging relevance to CLR evolution

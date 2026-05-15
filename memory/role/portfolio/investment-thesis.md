# Investment Thesis: Portable Memory & Context Infrastructure

**Portfolio Size:** $6.2M | **Last Updated:** 2026-04-28

## Core Thesis

Learners moving through education and workforce systems accumulate rich context — skills demonstrated, challenges overcome, goals articulated, support strategies that worked. Today, this context is trapped in institutional silos, lost at every transition, and invisible to the AI systems increasingly mediating learning experiences. We fund the infrastructure layer that makes learner context portable, persistent, and learner-controlled — so that AI systems can serve learners as continuous partners rather than strangers at every new institution.

## The Four Pillars

### 1. Longitudinal Memory
Can AI systems maintain useful, accurate learner context over years and across institutions? This pillar funds work on durable learner records, learning record stores that interoperate, and AI memory architectures that degrade gracefully over time rather than hallucinating stale context.

### 2. Provenance
Can you trace where every piece of context came from, who created it, and whether it should still be trusted? As AI agents summarize, transform, and relay learner information, provenance tracking ensures that a credential claim can be verified back to its source and that summarized context carries attribution.

### 3. Agent Orchestration
When multiple AI systems serve the same learner — an advising agent, a tutoring agent, a career coaching agent — how do they coordinate around a shared record? This pillar funds protocols and reference implementations for multi-agent coordination with learner context as the shared substrate.

### 4. Local-First Architecture
Does the infrastructure work when data lives on the learner's device with intermittent connectivity? Community college students, workforce reentry populations, and rural learners cannot depend on always-on cloud connections. This pillar funds CRDT-based sync, edge inference, and offline-capable architectures.

## Pillar Interconnections

- Longitudinal Memory + Provenance: Long-lived records require provenance to remain trustworthy over time
- Agent Orchestration + Provenance: Agents sharing context must attribute and verify sources
- Local-First + Longitudinal Memory: Offline-capable storage must handle years of accumulated context
- Local-First + Agent Orchestration: Agents must coordinate even when connectivity is intermittent

## Current Strategic Focus (2026)

1. **Standards convergence** — Bridging 1EdTech CLR and W3C Verifiable Credentials approaches
2. **Reference implementations** — Moving from specs to working code that institutions can adopt
3. **Equity validation** — Ensuring infrastructure works for community college and workforce populations, not just well-resourced universities
4. **Agent protocol alignment** — Connecting our orchestration work to emerging MCP/A2A protocols

## Key Assumptions Being Tested

1. Learners will adopt and manage portable context if the UX burden is low enough
2. Institutions will participate in context-sharing if interoperability costs are manageable
3. AI agents can coordinate around shared learner records without creating privacy risks
4. Local-first architectures can achieve sufficient sync reliability for credential-grade data
5. Open standards can move fast enough to stay ahead of proprietary platform lock-in

## Success Metrics

- Number of institutions piloting interoperable learner context systems (target: 15 by end of 2027)
- Learner adoption in pilot populations (target: 5,000 active learners)
- Standards adoption: at least one pillar-relevant spec reaches candidate recommendation status
- Equity: >40% of pilot learners from community colleges or workforce programs
- Open-source reference implementations: 3+ production-quality repos with active contributor communities

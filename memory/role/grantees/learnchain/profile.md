# LearnChain Labs — Grant Profile
- **Grant ID:** PMC-2024-001
- **Organization:** LearnChain Labs
- **PI:** Dr. Amara Osei
- **Co-PIs:** Dr. Wei Lin (lead engineer)
- **Pillar:** Longitudinal Memory
- **Amount:** $850,000
- **Period:** July 2024 — June 2026
- **Status:** Active - Year 2
- **Health:** 🟢 Green

## Project Summary
LearnChain is building a CRDT-based longitudinal learning record store (LRS) that enables learner context to synchronize across institutional boundaries without centralized coordination. The architecture uses conflict-free replicated data types to handle concurrent writes from multiple institutions, ensuring eventual consistency even with intermittent connectivity. Year 2 focuses on performance at scale — can the system handle 10,000+ concurrent learners with sub-second merge latency? Early benchmarks are promising, showing 200ms median merge times at 5K learners.

## Key Deliverables
1. CRDT performance benchmarks at 10K scale (May 15, 2026)
2. Multi-institution sync protocol specification v2.0 (June 2026)
3. Open-source reference implementation release (June 2026)
4. Interoperability demonstration with CLR 3.0 format (June 2026)

## Team
- Dr. Amara Osei — PI, architecture lead
- Dr. Wei Lin — Lead engineer, CRDT implementation
- Maria Santos — Research engineer, performance testing
- Jake Thompson — Standards liaison, CLR integration

## Risk Factors
- Scale performance is unproven beyond 5K learners
- CLR 3.0 spec still in draft — integration target may shift

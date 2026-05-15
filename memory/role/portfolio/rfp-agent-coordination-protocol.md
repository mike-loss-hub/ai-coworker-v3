# RFP: Education Agent Coordination Protocol

**Status:** Draft — pending Program Officer review
**Created:** 2026-05-02
**Budget Ceiling:** $500,000
**Performance Period:** Up to 24 months
**Submission Deadline:** TBD (suggest 6 weeks from release)
**Pillar:** Agent Orchestration
**Gap Addressed:** No grant covers the education-specific agent-to-agent coordination protocol layer

---

## 1. Background

Our foundation invests in infrastructure that makes learner context portable, persistent, and learner-controlled — so AI systems can serve learners as continuous partners rather than strangers at every new institution. We currently fund 8 grants totaling $5.7M across four pillars: Longitudinal Memory, Provenance, Agent Orchestration, and Local-First Architecture.

Within Agent Orchestration, we fund a reference implementation for multi-agent coordination (PathWeaver AI) and a trust framework for cross-standard credential verification (TrustLayer Technologies). Both are performing well. However, a critical gap remains: no one is building the education-specific protocol specification that defines how AI agents coordinate around shared learner records.

The generic protocol layer is stabilizing — MCP and A2A are converging under the Linux Foundation's Agentic AI Foundation, with a joint interoperability spec expected Q2 2026. What is missing is the domain-specific coordination layer for education: how agents share learner context, verify credentials between agents, enforce privacy constraints, and operate in connectivity-limited environments.

## 2. What We're Funding

An open protocol specification for agent-to-agent coordination in educational settings, built on top of the emerging A2A+MCP stack. The specification should define:

- **Learner context exchange** — How an advising agent requests and receives a learner's credential history, learning progress, or support needs from a records agent or another institution's agent
- **Credential verification between agents** — How agents verify the provenance and validity of credential claims received from other agents, compatible with TrustLayer's trust framework
- **Privacy and informed consent** — How learner privacy preferences and FERPA/institutional policies are expressed, transmitted, and enforced across coordinating agents. Critically, how learners understand and control what context is shared between agents — designed for populations with low digital literacy, not just technically compliant consent flows
- **Coordination semantics** — How agents signal events (e.g., "learner demonstrated new competency"), delegate tasks, and resolve conflicts when operating on shared learner records
- **Local-first compatibility** — How the protocol operates in intermittent-connectivity environments typical of community colleges and rural institutions

## 3. What We're NOT Funding

- Generic agent coordination protocol work — the Linux Foundation AAIF is handling that
- Full-stack reference implementations — PathWeaver is handling that
- Trust framework specifications — TrustLayer is handling that
- Proprietary or closed-source protocol work

## 4. Interoperability Requirements

This grant must produce work that integrates with our existing portfolio:

- The protocol specification must be compatible with **PathWeaver AI's** reference implementation (MCP-based, multi-agent coordination around shared learner profiles)
- Credential verification must be compatible with **TrustLayer Technologies'** trust framework (cross-standard trust anchors bridging 1EdTech CLR and W3C VC)
- The protocol must work in **local-first environments** consistent with OpenSync Foundation's CRDT-based sync and FieldKit's offline-capable architecture
- Letters of support from at least one existing portfolio grantee are strongly encouraged

## 5. Equity Requirements

Our investment thesis prioritizes infrastructure that works for community colleges, workforce reentry populations, and rural learners — not just well-resourced universities. Proposals must:

- Design for connectivity-limited environments as a first-class requirement, not an afterthought
- Deploy the pilot such that the **majority of pilot institutions primarily serve community college, workforce reentry, or rural learner populations** — the hardest context should be the center of the pilot, not the add-on site
- Include disaggregated outcome reporting by institution type, learner demographics, and connectivity conditions
- Articulate how the protocol design itself addresses equity (e.g., how does the privacy model protect vulnerable populations? how does informed consent work for first-generation students? how does the coordination model handle institutions with limited technical capacity?)
- Describe a **participatory design process** — how will learners, advisors, registrars, and frontline staff from target populations inform protocol design decisions? A protocol designed entirely by distributed systems researchers without practitioner input will not meet our standard.

## 6. Standards Alignment

The protocol should be designed for publication as an open standard. We have existing relationships with:

- W3C Credentials Community Group (Verifiable Credentials, DIDs)
- 1EdTech Consortium (CLR 3.0, Open Badges)
- T3 Innovation Network (CTDL, workforce data)

Proposals should identify a credible publication pathway through one of these bodies or an equivalent open standards organization.

## 7. Evaluation Criteria

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Technical Merit | 25% | Architecture soundness, feasibility, protocol design quality |
| Equity & Learner Impact | 25% | Target populations, outcome measurement, access design, participatory process |
| Portfolio Fit | 20% | Interoperability with existing grants, gap coverage |
| Team & Execution | 15% | PI track record, team depth, key person risk |
| Budget & Timeline | 10% | Cost reasonableness, milestone feasibility |
| Standards Alignment | 5% | Open standards commitment, publication pathway |

Proposals will be scored on a 1-5 scale per dimension. Qualitative factors — letters of support quality, PI responsiveness, community reputation — will also be considered.

## 8. Expected Deliverables

- Protocol specification document (draft by Month 12, final by Month 18)
- Compatibility validation with PathWeaver and TrustLayer (by Month 9)
- Pilot deployment with at least 2 institutions serving target populations (Months 15-24)
- Open-source reference tooling (protocol library, validation suite)
- Disaggregated pilot outcome report (Month 24)

## 9. Submission Requirements

- Project narrative (10 pages max) — equity considerations should be integrated throughout the narrative, not treated as a separate section. Every technical design choice should address who it serves and who it might exclude.
- Budget and budget justification
- Team qualifications and roles
- Letters of support (existing portfolio grantees strongly encouraged)
- Description of participatory design process — how will learners, advisors, and frontline staff from target populations inform protocol design decisions? (2 pages max)
- Standards publication plan (1 page)

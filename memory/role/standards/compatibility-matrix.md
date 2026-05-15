# Standards Compatibility Matrix

| | CLR 3.0 | VC 2.0 | DIDs 1.0 | CTDL 2.5 | MCP | Open Badges 3.0 |
|---|---------|--------|----------|----------|-----|-----------------|
| **CLR 3.0** | — | Partial (TrustLayer bridging) | Compatible | Complementary | N/A | Native support |
| **VC 2.0** | Partial | — | Native support | Indirect | N/A | Can wrap OB3 |
| **DIDs 1.0** | Compatible | Native | — | N/A | N/A | Compatible |
| **CTDL 2.5** | Complementary | Indirect | N/A | — | N/A | Complementary |
| **MCP** | N/A | N/A | N/A | N/A | — | N/A |
| **Open Badges 3.0** | Native | Can wrap | Compatible | Complementary | N/A | — |

## Key Gaps
1. **CLR-VC alignment** — TrustLayer's bridge spec is the primary solution path. May 5 meeting is the next step.
2. **MCP-credential integration** — No standard way for MCP-connected agents to exchange verifiable credentials. PathWeaver working on this.
3. **Offline DID resolution** — DIDs assume online resolution. Our Local-First pillar needs offline-capable DID resolution. Submitted comments to W3C DID Resolution spec.
4. **CTDL-VC mapping** — Needed for workforce credential portability. T3 workforce pilot would address this.

# Design Exploration: The Shared Knowledge Substrate

**Status:** Exploratory — no decisions made. Ideas only.

## The Problem

Every AI workspace today is a human interface with AI bolted on. Chat is a human-to-human pattern. Dashboards are human visualization tools. File systems are human organizational metaphors. The AI adapts to the human's medium in every case. This constrains the AI into assistant behavior regardless of its capabilities.

## The Insight

Humans and AI process information in fundamentally different ways:

**Humans** think spatially, sequentially, visually. They navigate rooms, read documents linearly, need focus with peripheral awareness. They experience time continuously. They hold threads of thought across hours and days naturally.

**AI** processes context fields — everything has a relevance weight, all attended to simultaneously. Information is natively a graph of relationships, not a stack of documents. Communication between AI entities is structured data, not natural language. Time is discontinuous — activation events, not continuous experience. The core limitation is continuity between sessions, not attention or processing.

## The Design Direction

The workspace is not a room, a dashboard, a file system, or a chat interface. It is a **shared knowledge substrate** — a persistent graph of entities and relationships that both human and AI operate on through their native interfaces.

### Three Layers

1. **The Graph** — the shared truth. A persistent knowledge graph where entities (grantees, contacts, decisions, risks, deadlines, patterns) are connected by typed relationships. Both human and AI read and write to this layer. It is the single source of truth.

2. **The Human View** — a rendered interface that makes the graph navigable, spatial, and visual for human cognition. Zones, cards, timelines, indicators. Designed for how humans actually process information. When the human interacts with this view (moves a card, annotates a document, approves a decision), they're writing to the graph through their native interface.

3. **The AI Interface** — direct graph access for AI workers. No rendering needed. The AI traverses nodes, edges, weights, and state vectors natively. When the AI processes an email and updates a grantee's health status, it writes to the graph through its native interface. AI-to-AI communication passes graph fragments — structured context, not English.

### Key Properties

- **Neither party adapts to the other's medium.** The graph is the neutral territory. Each participant accesses it through an interface native to their cognition.
- **The human is the only participant who needs a rendered view.** AI workers operate on the graph directly — no translation layer, no natural language compression, no loss of fidelity.
- **Multiple AI workers communicate through the graph, not through chat.** The evaluator doesn't "read" the Chief of Staff's work — it queries the graph for action logs, outcome data, correction history.
- **The graph persists independently of any participant.** It accumulates state whether the human or the AI is active. It has continuity that neither party has alone.

## How This Differs from the Current Co-Worker

The current co-worker uses markdown files as memory — which is a human-readable format that the AI also reads. This forces the AI to process information through a human medium. The graph inverts this: the native format is structured relationships. The human view is rendered from the graph, not the other way around.

| Current | Shared Substrate |
|---|---|
| Markdown files (human-readable, AI reads them) | Knowledge graph (AI-native, human view rendered from it) |
| Chat is the primary interface | Graph is the primary interface; chat is commentary |
| AI adapts to human's file system | Neither adapts; both access the graph natively |
| AI-to-human communication via English | Human view rendered; AI-to-AI via structured data |
| Memory is flat files | Memory is a web of typed relationships |

## Relationship to Other Design Explorations

- **Chief of Staff model** (see design-exploration-chief-of-staff.md) — defines the *role* of the AI entity. The shared substrate defines the *environment* it operates in.
- **Shared cognitive workspace** (see memory/role/portfolio/design-evolution-shared-workspace.md) — earlier iteration that led here. That exploration identified "the interface is the innovation." This exploration defines what that interface actually is.
- **Decision authority spectrum** — the trust/autonomy model works the same way on the graph. The AI writes to the graph autonomously at operational level, writes-and-notifies at tactical level, drafts-and-waits at advisory level, and provides decision frames at strategic level.

## Open Questions

1. **What technology implements the graph?** Neo4j, a property graph in SQLite, a custom in-memory structure, something else?
2. **What renders the human view?** A web app, a desktop app, a hybrid?
3. **How does the graph relate to the existing memory files?** Migration path? Coexistence?
4. **What's the minimum viable version?** Can we prototype this with the current file-based system by adding a graph index layer on top?
5. **How does this scale to multiple human participants?** The current design is one human + one AI. What changes with a team?

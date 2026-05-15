---
name: Token efficiency mandate
description: User requires all tasks use the most token-efficient approach — batch operations, minimize reads, no unnecessary output
type: feedback
---

Always use the most efficient way to consume tokens/credits. This applies to every task.

**Why:** User runs out of credits before finishing work sessions. Repeated instruction across multiple conversations.

**How to apply:**
- Batch related file reads and edits into single operations
- Never re-read files already in context
- Don't echo file contents back unless asked
- Use grep/find over Read when checking for specific strings
- Combine multiple small edits into fewer larger ones
- Keep responses concise — results, not narration
- Use lightweight subagents (Haiku) for simple lookups
- Always update docs/executive-summary.md when functionality changes
- Always run diagnostic after code/system changes

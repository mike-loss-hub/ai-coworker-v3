# Skill: Stakeholder Communications

## Resource Tier
Sonnet — requires tone-matching and context-aware drafting, but not multi-perspective analysis.

## When to Use
The user needs to communicate with someone — drafting an email, writing a check-in, sending a note, or preparing any written message for a specific recipient. Any request to write, draft, or send something to a named person maps here.

## Process
1. Identify recipient(s) from memory/role/contacts/
2. Read their communication style, relationship history, and current context
3. Determine appropriate tone:
   - PI check-in → collegial, supportive, specific
   - Struggling grantee → empathetic but clear about expectations
   - Standards body leader → diplomatic, measured
   - Co-funder → professional, strategic
   - Internal colleague → direct, concise
   - Board → formal, impact-focused
4. Draft communication matching tone and context
5. Flag if sensitive (user prefers to handle sensitive matters personally)
6. **Deliver the email** per tools-email.md priority: MCP email tools → `scripts/send-email.py` via SMTP → draft for user to send manually
7. After sending (via any method or user confirmation), log to correspondence and contact files per tools-email.md

## Context Sources
**Always load:**
- memory/role/contacts/[recipient].md — the specific recipient only

**Load if relevant:**
- memory/role/grantees/[relevant]/correspondence.md — only if writing to/about a grantee, and only the correspondence file
- memory/human/working-style.md — only on first email draft of the session; reuse preferences from memory after that

## Output Format
```
**To:** [recipient]
**Subject:** [subject line]
**Tone:** [selected tone and why]

---

[Draft email body]

---

**Notes:** [anything to flag — sensitivity, timing, relationship context]
```

## Quality Standard
- Tone matches recipient's communication style
- Content references specific, real context (not generic)
- Flags sensitive communications for user review
- Appropriate institutional voice for foundation correspondence

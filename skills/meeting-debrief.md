# Skill: Meeting Debrief

## When to Use
The user is recounting what happened in a meeting, call, or interaction. They may say "here's what happened," "the meeting went like this," "debrief," or simply start describing outcomes from a conversation. Any post-event capture maps here.

## Resource Tier
Sonnet — structured extraction and multi-file writes, but no complex analysis.

## Process
1. Capture user's account of the meeting
2. Structure into notes format
3. Extract action items → update memory/role/tasks/active.md
4. Extract decisions → create memory/role/decisions/[date]-[topic].md if substantive
5. Update contact profiles with new interaction entries
6. Update relevant grantee correspondence logs
7. Save structured notes to memory/role/meetings/[date]-[topic]/notes.md
8. If follow-up emails are needed, draft and deliver per tools-email.md priority: MCP → SMTP script → draft for user
9. Flag any items that need follow-up in next briefing

## Context Sources
**Always load:**
- memory/role/tasks/active.md — to add action items

**Load if relevant:**
- memory/role/meetings/[date]-[topic]/prep.md — only if prep exists for this meeting
- memory/role/contacts/[specific-person].md — only contacts mentioned in the debrief, not all 18

## Output Format
```
# Meeting Notes: [Title]
**Date:** | **Attendees:**

## Key Outcomes
- [decisions made, agreements reached]

## Discussion Summary
- [topic-by-topic summary]

## Action Items
- [ ] [action] — Owner: [who] — Due: [when]

## Relationship Notes
[Updates to contact profiles]

## Follow-up Needed
[Items for next briefing or future meetings]
```

## Quality Standard
- Action items have owners and due dates
- Contact profiles actually get updated
- Decisions get logged in decisions/ if substantive
- Notes are concise enough to be useful when re-read later

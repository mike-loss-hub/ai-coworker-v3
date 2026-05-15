# Skill: Meeting Preparation

## Resource Tier
Sonnet — context gathering and synthesis, no complex judgment required.

## When to Use
The user has an upcoming meeting or interaction and needs context. They may mention a person, a date, a topic, or say they need to prepare. Any variation of "I'm meeting with X," "what do I need to know before seeing X," or "prep for the 2pm" maps here.

## Process
1. Identify the meeting from memory/role/calendar/upcoming.md or user description
2. Pull contact profiles for all attendees from memory/role/contacts/
3. Pull relevant grantee/org context
4. Check memory/role/decisions/ for relevant past decisions
5. Check memory/role/meetings/ for prior meetings with same attendees
6. Engage Stakeholder perspective for dynamics analysis
7. Prepare structured briefing

## Context Sources
**Always load:**
- memory/role/contacts/[attendee].md — only the specific attendee(s)
- memory/role/calendar/upcoming.md — to confirm meeting details

**Load if relevant:**
- memory/role/contacts/org-profiles/[org].md — only if org context matters
- memory/role/grantees/[relevant]/ — only the grantee being discussed, if any
- memory/role/decisions/ — only recent decisions involving the attendee
- memory/role/meetings/ — only prior meetings with this attendee

## Output Format
```
# Meeting Prep: [Title]
**Date/Time:** | **Format:**

## Attendees & Dynamics
[For each: name, role, communication style, relationship status, what they care about]

## Context
[Why this meeting is happening, what's at stake]

## Key Questions / Agenda Items
[What to discuss, in priority order]

## Talking Points
[What to say, framed for the audience]

## Landmines to Avoid
[Political sensitivities, touchy topics, relationship risks]

## Success Criteria
[What would make this meeting a win]
```

## Quality Standard
- Attendee dynamics are specific, not generic
- Talking points match the audience's communication style
- Landmines are based on real relationship history
- Links to relevant decision records or past meetings

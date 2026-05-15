# Skill: Meeting Scheduler

## Resource Tier
Haiku — structured extraction, file generation, minimal synthesis.

## When to Use
The user wants to schedule a meeting, send a calendar invite, set up a call, or book time with someone. They may say "send a Teams invite," "schedule a meeting with X," "set up a call," or "book time for us to discuss X."

## Process
1. Parse meeting details: who, when, how long, topic, agenda
2. If any details are missing, ask — at minimum need attendees and a rough time
3. Check memory/role/calendar/upcoming.md for conflicts
4. Check memory/role/contacts/ for attendee context (relationship, preferences)
5. **Create the meeting** per tools-calendar.md priority: Calendar MCP → `scripts/create-meeting.py` (Google Calendar + Meet link) → draft details for user to create manually
8. Log meeting to memory/role/calendar/upcoming.md
9. Create memory/role/meetings/[date]-[topic]/prep.md if meeting is substantive
10. Log interaction in relevant contact files

## Context Sources
**Always load:**
- memory/role/calendar/upcoming.md — conflict check
- skills/tools-calendar.md — .ics format reference

**Load if relevant:**
- memory/role/contacts/[attendee].md — only for known contacts
- memory/role/grantees/[name]/ — only if meeting is about a specific grantee

## Output Format
Meeting scheduled:
```
📅 [Title]
🕐 [Date/Time] ([Duration])
👥 [Attendees]
📋 [Agenda]
Status: [Invite sent via calendar app / Logged to upcoming.md]
```

## Quality Standard
- Never send an invite without confirming details with the user
- Always check for scheduling conflicts before creating
- Log every scheduled meeting to upcoming.md
- Create prep docs for substantive meetings (not quick syncs)
- Include agenda/context in the invite body

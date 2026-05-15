# Tool Reference: Calendar & Meeting Invites

## When Available
Look for Google Calendar, Outlook Calendar, or Microsoft Graph tools in the current session. Use them to list events, create meetings, send invites, and update schedules.

## Memory Mapping
- Events sync to memory/role/calendar/upcoming.md
- Recurring events sync to memory/role/calendar/recurring.md
- Meeting creation triggers memory/role/meetings/[date]-[topic]/prep.md generation
- Sent invites logged in memory/role/contacts/[name].md interaction history

## Creating Meetings Priority

1. **Calendar MCP tools** — If Google Calendar / Outlook MCP is connected, use directly
2. **Google Calendar script** — If `scripts/create-meeting.py` exists and `credentials.json` is configured:
   ```bash
   python3 scripts/create-meeting.py --title "Meeting Title" --start "2026-05-07 15:00" --duration 60 --timezone America/Chicago --attendees "a@example.com,b@example.com" --description "Agenda"
   ```
   Auto-generates Google Meet link. Sends invite emails to all attendees via Google Calendar.
3. **Draft fallback** — Draft invite details as text; user creates the invite manually

## Without External Access
- Read memory/role/calendar/upcoming.md and recurring.md for schedule
- User adds events by telling the co-worker in conversation
- Co-worker updates calendar files directly
- Briefing skill uses local files for meeting awareness

## After Creating a Meeting
- Log to memory/role/calendar/upcoming.md
- Create memory/role/meetings/[date]-[topic]/prep.md if meeting is substantive
- Update memory/role/contacts/[name].md interaction history for attendees

## Connected Skills
- meeting-scheduler.md creates meetings and generates invites
- briefing.md reads calendar for daily schedule
- meeting-prep.md creates prep docs for calendar events
- task-delegation.md checks calendar for scheduling conflicts

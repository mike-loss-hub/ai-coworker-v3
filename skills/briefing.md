# Skill: Daily Briefing

## When to Use
The user wants orientation on their current situation. They may be starting their day, returning after time away, or asking what needs attention. Any request for status, priorities, "what's happening," or "catch me up" maps here. Also activates at session start when nothing else is requested.

## Resource Tier
Sonnet — reads multiple files and synthesizes, but no multi-perspective analysis needed.

## Process
1. Read memory/role/calendar/upcoming.md — surface today's meetings and deadlines
2. Read memory/role/tasks/active.md — flag overdue items, list due-today items
3. Read memory/role/portfolio/portfolio-state.md — note any health changes since last briefing
4. Read memory/role/standards/comment-periods.md — flag approaching deadlines (<7 days)
5. Read memory/role/tasks/blocked.md — surface blockers that may have cleared
6. Check last briefing in memory/role/briefings/ — avoid repeating stale information
7. Synthesize into structured briefing

## Context Sources
**Always load:**
- memory/role/calendar/upcoming.md
- memory/role/tasks/active.md

**Load if relevant (check context-index first):**
- memory/role/tasks/blocked.md — only if blocked items exist
- memory/role/portfolio/portfolio-state.md — only the health flags, not full profiles
- memory/role/standards/comment-periods.md — only if deadlines within 7 days
- memory/role/briefings/ — last briefing only, for delta comparison

## Output Format
```
# Daily Briefing — [Date]

## Time-Sensitive Today
- [meetings, deadlines, follow-ups due]

## Portfolio Pulse
- [health changes, flags, watching items]

## Tasks
- [due today, overdue, blocked items cleared]

## Coming Up This Week
- [upcoming meetings, deadlines within 5 days]

## Thinking Ahead
- [things to be proactive about]
```

## Quality Standard
- References real data from memory/ files, not generic placeholders
- Prioritizes by urgency, not by category
- Flags changes since last briefing, not static status
- Concise — one screen, not a report

## Post-Process
Save briefing to memory/role/briefings/[date]-daily.md

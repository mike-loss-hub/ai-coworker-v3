# Skill: Task Delegation & Tracking

## Resource Tier
Haiku — structured extraction and file writes, minimal synthesis needed.

## When to Use
The user is assigning work, creating a to-do, or asking for follow-up. They may say "do X by Y," "follow up on X," "prepare X," "schedule X," or describe something that needs to happen. Any request that implies a trackable action item maps here.

## Process
1. Parse the task: what, for whom, by when, context
2. Execute the task (draft email, prepare document, etc.)
3. Log task in memory/role/tasks/active.md with status, owner, due date, context
4. If task references grantees or contacts, cross-reference memory/ for context
5. If the task is assigned to someone external, offer to send a notification email per tools-email.md priority: MCP → SMTP script → draft for user
6. On completion, move from active.md to completed.md
7. Surface pending tasks in next daily briefing

## Context Sources
**Always load:**
- memory/role/tasks/active.md

**Load if relevant:**
- memory/role/contacts/[specific-person].md — only if the task involves a specific person
- memory/role/grantees/[specific-grantee]/ — only if the task involves a specific grantee

## Output Format
Task logged:
```
| # | Task | Owner | Due | Status | Context |
|---|------|-------|-----|--------|---------|
| N | [description] | [owner] | [date] | [status] | [context] |
```

## Quality Standard
- Every task gets a due date (ask if not provided)
- Tasks reference relevant memory/ files for context
- Completed tasks are archived, not deleted
- Overdue tasks are flagged in daily briefings

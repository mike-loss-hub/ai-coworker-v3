# Tool Reference: Email

## When Available
Look for Gmail or Outlook email tools in the current session. Use them to send emails, create drafts, search inbox, and read messages.

## Memory Mapping
- Sent grantee correspondence → memory/role/grantees/[name]/correspondence.md
- Contact interactions → memory/role/contacts/[name].md interaction history
- Important emails → flagged in daily briefing

## Sending Priority

1. **MCP email tools** — If Gmail/Outlook MCP is connected, use it directly
2. **SMTP script** — If `scripts/send-email.py` exists and `.env` has credentials:
   ```bash
   python3 scripts/send-email.py --to "recipient@example.com" --subject "Subject" --body "Email body"
   ```
   Supports `--cc` for CC recipients. Multiple recipients comma-separated.
3. **Draft fallback** — If neither is available, draft as text output for user to send manually

## Reading Priority

1. **MCP email tools** — If Gmail/Outlook MCP is connected, use it directly
2. **IMAP script** — If `scripts/check-email.py` exists and `.env` has credentials:
   ```bash
   python3 scripts/check-email.py --unread --limit 10
   python3 scripts/check-email.py --from "sender@example.com" --since 2026-05-01
   ```
   Supports `--unread`, `--from`, `--limit N`, `--since YYYY-MM-DD`. Does not mark emails as read.
3. **Paste fallback** — Ask user to paste/forward the email into the conversation

## After Sending (via any method)
- Log the sent email to memory/role/grantees/[name]/correspondence.md (if grantee-related)
- Update memory/role/contacts/[name].md interaction history
- Add any follow-up items to memory/role/tasks/active.md

## Connected Skills
- stakeholder-email.md drafts and sends emails
- meeting-debrief.md sends follow-up emails from action items
- task-delegation.md can send task notifications via email
- meeting-scheduler.md can send meeting context via email when calendar tools aren't available

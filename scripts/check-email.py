#!/usr/bin/env python3
"""Read email via Gmail IMAP. Platform-agnostic, no external dependencies."""

import argparse
import email
import imaplib
import sys
from datetime import datetime, timedelta
from email.header import decode_header
from pathlib import Path


def load_env():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        print(f"ERROR: {env_path} not found.", file=sys.stderr)
        sys.exit(1)
    env = {}
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


def decode_str(s):
    if s is None:
        return ""
    parts = decode_header(s)
    result = []
    for data, charset in parts:
        if isinstance(data, bytes):
            result.append(data.decode(charset or "utf-8", errors="replace"))
        else:
            result.append(data)
    return " ".join(result)


def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    charset = part.get_content_charset() or "utf-8"
                    return payload.decode(charset, errors="replace")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            charset = msg.get_content_charset() or "utf-8"
            return payload.decode(charset, errors="replace")
    return "(no plain text body)"


def check_email(unread_only, from_filter, limit, since):
    env = load_env()
    address = env.get("GMAIL_ADDRESS")
    password = env.get("GMAIL_APP_PASSWORD")

    if not address or not password:
        print("ERROR: GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set in .env", file=sys.stderr)
        sys.exit(1)

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(address, password)
    mail.select("inbox")

    criteria = []
    if unread_only:
        criteria.append("UNSEEN")
    if from_filter:
        criteria.append(f'FROM "{from_filter}"')
    if since:
        date_obj = datetime.strptime(since, "%Y-%m-%d")
        criteria.append(f'SINCE {date_obj.strftime("%d-%b-%Y")}')

    search_str = " ".join(criteria) if criteria else "ALL"
    _, message_ids = mail.search(None, search_str)
    ids = message_ids[0].split()

    if not ids:
        print("No emails found matching criteria.")
        mail.logout()
        return

    ids = ids[-limit:]

    for msg_id in reversed(ids):
        _, data = mail.fetch(msg_id, "(BODY.PEEK[])")
        raw = data[0][1]
        msg = email.message_from_bytes(raw)

        from_addr = decode_str(msg.get("From", ""))
        to_addr = decode_str(msg.get("To", ""))
        date = decode_str(msg.get("Date", ""))
        subject = decode_str(msg.get("Subject", ""))
        body = get_body(msg)

        if body and len(body) > 1000:
            body = body[:1000] + "\n... (truncated)"

        print(f"--- EMAIL ---")
        print(f"From: {from_addr}")
        print(f"To: {to_addr}")
        print(f"Date: {date}")
        print(f"Subject: {subject}")
        print(f"Body:\n{body}")
        print()

    mail.logout()
    print(f"({len(ids)} email(s) shown)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check email via Gmail IMAP")
    parser.add_argument("--unread", action="store_true", help="Only show unread emails")
    parser.add_argument("--from", dest="from_filter", help="Filter by sender email/name")
    parser.add_argument("--limit", type=int, default=10, help="Max emails to show (default 10)")
    parser.add_argument("--since", help="Only emails since date: YYYY-MM-DD")
    args = parser.parse_args()

    try:
        check_email(args.unread, args.from_filter, args.limit, args.since)
    except imaplib.IMAP4.error as e:
        print(f"ERROR: IMAP authentication failed. Check credentials in .env: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

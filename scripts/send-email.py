#!/usr/bin/env python3
"""Send email via Gmail SMTP. Platform-agnostic, no external dependencies."""

import argparse
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path


def load_env():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        print(f"ERROR: {env_path} not found. Create it with GMAIL_ADDRESS and GMAIL_APP_PASSWORD.", file=sys.stderr)
        sys.exit(1)
    env = {}
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


def send(to, subject, body, cc=None, sender=None):
    env = load_env()
    address = sender or env.get("GMAIL_ADDRESS")
    password = env.get("GMAIL_APP_PASSWORD")

    if not address or not password:
        print("ERROR: GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set in .env", file=sys.stderr)
        sys.exit(1)

    msg = MIMEMultipart()
    msg["From"] = address
    msg["To"] = to
    msg["Subject"] = subject
    if cc:
        msg["Cc"] = cc

    msg.attach(MIMEText(body, "plain"))

    recipients = [r.strip() for r in to.split(",")]
    if cc:
        recipients += [r.strip() for r in cc.split(",")]

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(address, password)
        server.sendmail(address, recipients, msg.as_string())

    print(f"OK: Email sent to {to}" + (f" (cc: {cc})" if cc else ""))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send email via Gmail SMTP")
    parser.add_argument("--to", required=True, help="Recipient(s), comma-separated")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--body", required=True, help="Email body (plain text)")
    parser.add_argument("--cc", help="CC recipient(s), comma-separated")
    parser.add_argument("--from", dest="sender", help="Override sender address")
    args = parser.parse_args()

    try:
        send(args.to, args.subject, args.body, args.cc, args.sender)
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Authentication failed. Check GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

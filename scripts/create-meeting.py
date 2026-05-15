#!/usr/bin/env python3
"""Create a Google Calendar event with Google Meet link. Platform-agnostic."""

import argparse
import os
import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CREDS_FILE = PROJECT_ROOT / "credentials.json"
TOKEN_FILE = PROJECT_ROOT / "token.json"


def get_service():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDS_FILE.exists():
                print(f"ERROR: {CREDS_FILE} not found. Download it from Google Cloud Console.", file=sys.stderr)
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return build("calendar", "v3", credentials=creds)


def create_meeting(title, start, duration, timezone, attendees, description):
    service = get_service()

    start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M")
    end_dt = start_dt + timedelta(minutes=duration)

    event = {
        "summary": title,
        "description": description or "",
        "start": {"dateTime": start_dt.isoformat(), "timeZone": timezone},
        "end": {"dateTime": end_dt.isoformat(), "timeZone": timezone},
        "conferenceData": {
            "createRequest": {
                "conferenceSolutionKey": {"type": "hangoutsMeet"},
                "requestId": str(uuid.uuid4()),
            }
        },
    }

    if attendees:
        event["attendees"] = [{"email": e.strip()} for e in attendees.split(",")]

    result = service.events().insert(
        calendarId="primary",
        body=event,
        conferenceDataVersion=1,
        sendNotifications=True,
    ).execute()

    meet_link = ""
    for ep in result.get("conferenceData", {}).get("entryPoints", []):
        if ep.get("entryPointType") == "video":
            meet_link = ep["uri"]
            break

    print(f"OK: Meeting created")
    print(f"Title: {result['summary']}")
    print(f"When: {start} ({timezone}) — {duration} min")
    print(f"Meet link: {meet_link}")
    print(f"Event ID: {result['id']}")
    if attendees:
        print(f"Invites sent to: {attendees}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Google Calendar event with Meet link")
    parser.add_argument("--title", required=True, help="Meeting title")
    parser.add_argument("--start", required=True, help="Start time: YYYY-MM-DD HH:MM")
    parser.add_argument("--duration", type=int, default=60, help="Duration in minutes (default 60)")
    parser.add_argument("--timezone", default="America/Chicago", help="Timezone (default America/Chicago)")
    parser.add_argument("--attendees", help="Attendee emails, comma-separated")
    parser.add_argument("--description", default="", help="Meeting description")
    args = parser.parse_args()

    try:
        create_meeting(args.title, args.start, args.duration, args.timezone, args.attendees, args.description)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

#!/usr/bin/env python3
"""Serve the portfolio dashboard with auto-reload on memory file changes."""
import http.server
import os
import sys
import threading
import time
from pathlib import Path

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    HAS_WATCHDOG = True
except ImportError:
    HAS_WATCHDOG = False

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
PROJECT_ROOT = Path(__file__).resolve().parent.parent
os.chdir(PROJECT_ROOT)


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path == "/" or path == "/index.html":
            return str(PROJECT_ROOT / "dashboard" / "index.html")
        return super().translate_path(path)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, format, *args):
        pass  # Suppress request logging unless verbose


class MemoryChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_change = None

    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            self.last_change = time.strftime("%H:%M:%S")
            name = Path(event.src_path).relative_to(PROJECT_ROOT)
            print(f"  [memory updated] {name} at {self.last_change}")


def main():
    print(f"Dashboard: http://localhost:{PORT}")
    print(f"Serving from: {PROJECT_ROOT}")

    if HAS_WATCHDOG:
        memory_path = PROJECT_ROOT / "memory"
        if memory_path.is_dir():
            handler = MemoryChangeHandler()
            observer = Observer()
            observer.schedule(handler, str(memory_path), recursive=True)
            observer.start()
            print(f"Watching memory/ for changes (auto-reload enabled)")
    else:
        print("Install watchdog for auto-reload: pip install watchdog")

    print("Press Ctrl+C to stop.\n")

    try:
        http.server.HTTPServer(("", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        if HAS_WATCHDOG:
            observer.stop()
            observer.join()


if __name__ == "__main__":
    main()

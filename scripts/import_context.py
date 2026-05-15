#!/usr/bin/env python3
"""Import co-worker context from a portable archive."""
import tarfile, sys, subprocess
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python3 scripts/import_context.py <archive.tar.gz>")
    sys.exit(1)

archive = Path(sys.argv[1])
if not archive.exists():
    print(f"Archive not found: {archive}")
    sys.exit(1)

dest = Path.cwd()
print(f"Importing to {dest}...")

with tarfile.open(archive, "r:gz") as tar:
    members = tar.getmembers()
    print(f"Extracting {len(members)} items...")
    tar.extractall(dest)

print("Running diagnostic...")
subprocess.run([sys.executable, str(dest / "scripts" / "diagnostic.py")])

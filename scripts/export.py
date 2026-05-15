#!/usr/bin/env python3
"""Export co-worker context. Supports --portable, --role, or --full (default)."""
import tarfile, hashlib, os, sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
mode = sys.argv[1] if len(sys.argv) > 1 else "--full"

MODES = {
    "--portable": {
        "label": "portable",
        "desc": "Human + Bridge layers (for a new role)",
        "include": ["memory/human", "memory/bridge", "memory/human/skills",
                     "skills", "agents/prompts", "CLAUDE.md", "scripts/diagnostic.py"]
    },
    "--role": {
        "label": "role",
        "desc": "Role layer only (for a successor)",
        "include": ["memory/role", "CLAUDE.md"]
    },
    "--full": {
        "label": "full",
        "desc": "Everything (backup or complete transfer)",
        "include": ["memory", "skills", "agents/prompts", "CLAUDE.md", "scripts/diagnostic.py", "scripts/export.py", "scripts/import_context.py"]
    }
}

if mode not in MODES:
    print(f"Usage: python3 export.py [--portable|--role|--full]")
    print("  --portable  Human + Bridge layers for a new role")
    print("  --role      Role layer for a successor")
    print("  --full      Everything (default)")
    sys.exit(1)

cfg = MODES[mode]
OUT = BASE / f"coworker-{cfg['label']}-{datetime.now().strftime('%Y%m%d')}.tar.gz"

with tarfile.open(OUT, "w:gz") as tar:
    for item in cfg["include"]:
        path = BASE / item
        if path.exists():
            tar.add(path, arcname=item)

size = OUT.stat().st_size
sha = hashlib.sha256(OUT.read_bytes()).hexdigest()[:16]

print(f"Export mode: {cfg['desc']}")
print(f"Archive: {OUT.name} ({size:,} bytes)")
print(f"Checksum: {sha}")

if mode == "--portable":
    print("\nTo start a new role:")
    print(f"  1. Extract: tar xzf {OUT.name}")
    print("  2. Run: python3 scripts/diagnostic.py")
    print("  3. The co-worker will ask about your new role and generate role scaffolding")
elif mode == "--role":
    print("\nFor your successor:")
    print(f"  1. Extract: tar xzf {OUT.name}")
    print("  2. They'll need their own human/ and bridge/ layers")
elif mode == "--full":
    print(f"\nFull restore: tar xzf {OUT.name} && python3 scripts/diagnostic.py")

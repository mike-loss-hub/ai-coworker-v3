#!/usr/bin/env bash
set -e

echo "Setting up AI Co-Worker v3..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
fi

# Activate and install deps
source .venv/bin/activate
pip install --upgrade pip -q 2>/dev/null
pip install -r requirements.txt -q

# Run diagnostic to verify system health
echo ""
echo "Running system diagnostic..."
echo ""
python3 scripts/diagnostic.py

echo ""
echo "Setup complete. To use:"
echo "  1. Open this directory in Claude Code (VS Code extension or CLI)"
echo "  2. The co-worker activates automatically via CLAUDE.md"
echo "  3. Dashboard: source .venv/bin/activate && python3 scripts/serve-dashboard.py"

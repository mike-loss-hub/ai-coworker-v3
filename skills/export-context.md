# Skill: Export Portable Context

## Resource Tier
Haiku — file packaging and copying, no analysis needed.

## When to Use
The user wants to export their context for portability, backup, or successor handoff. Any request to package, export, or archive their co-worker context maps here.

## Process
1. Run diagnostic to ensure system is healthy before export
2. Create export manifest listing all included files
3. Package into a portable archive:
   - memory/ — full directory
   - skills/ — all skill files
   - agents/prompts/ — all agent prompt files
   - CLAUDE.md — system instructions
   - scripts/diagnostic.py — health check tool
4. Generate integrity checksum for the archive
5. Create export-manifest.md with:
   - Export date
   - File count and total size
   - Portfolio summary (grantee count, contact count, decision count)
   - Last diagnostic status
   - Import instructions

## Context Sources
- All memory/ files
- All skills/ files
- All agents/prompts/ files
- CLAUDE.md

## Output Format
```
# Export Complete
- Archive: [filename]
- Files: [count]
- Size: [size]
- Integrity: [checksum]
- Manifest: export-manifest.md

To import in a new project:
1. Extract archive to project root
2. Run: python3 scripts/diagnostic.py
3. Verify HEALTHY status
4. Open in Claude Code — CLAUDE.md will activate the co-worker
```

## Quality Standard
- Diagnostic passes before export
- All three directories (memory, skills, agents) included
- Manifest accurately reflects contents
- Import instructions are self-contained
- No secrets or credentials included

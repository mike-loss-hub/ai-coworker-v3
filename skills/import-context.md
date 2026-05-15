# Skill: Import Portable Context

## Resource Tier
Sonnet — reads imported context and adapts to a new role, moderate synthesis.

## When to Use
The user wants to restore context from a previous export or set up the co-worker in a new role with existing portable context.

## Process
1. Locate the archive file (user provides path)
2. Verify archive integrity (checksum if available)
3. Extract to project root:
   - memory/ — learner context and portfolio data
   - skills/ — workflow definitions
   - agents/prompts/ — agent perspectives
   - CLAUDE.md — system instructions
4. Run diagnostic to verify integrity
5. Report any issues found
6. If healthy, confirm the co-worker is operational

## Context Sources
- Archive file (provided by user)
- export-manifest.md (from archive)

## Output Format
```
# Import Complete
- Source: [archive path]
- Files extracted: [count]
- Diagnostic: [HEALTHY/NEEDS ATTENTION/DEGRADED]
- Issues: [none or list]

The co-worker is [ready / needs attention before use].
```

## Quality Standard
- Never overwrite existing files without user confirmation
- Diagnostic runs automatically after import
- Issues are reported clearly with fix suggestions
- Co-worker is functional after successful import

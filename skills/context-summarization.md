# Skill: Context Summarization

## Resource Tier
Haiku — file reads and structured rewriting, no analysis needed.

## When to Use
Memory areas are growing large and need compaction, or the user wants to archive or summarize older context to keep files manageable.

## Process

### Correspondence Summarization
1. Read memory/role/grantees/[name]/correspondence.md
2. For entries older than 6 months, consolidate into quarterly summaries
3. Preserve: key decisions, relationship changes, commitments made, red flags
4. Discard: routine check-in details, scheduling logistics
5. Archive originals to memory/role/grantees/[name]/correspondence-archive.md
6. Write consolidated version back to correspondence.md

### Task Archival
1. Read memory/role/tasks/completed.md
2. For tasks older than 3 months, extract patterns:
   - Common task types and frequency
   - Average completion time by type
   - Tasks that frequently block
3. Write pattern summary to top of completed.md
4. Remove individual old entries (keep last 3 months)

### Briefing Compression
1. Read memory/role/briefings/ files older than 1 month
2. Group by month, create monthly summary:
   - Key decisions made that month
   - Portfolio health changes
   - Important meetings and outcomes
   - Emerging themes
3. Write to memory/role/briefings/[year]-[month]-summary.md
4. Remove individual daily briefings older than 1 month

### General Compaction
For any memory area growing beyond ~500 lines:
1. Identify content that is: outdated, redundant, or derivable from current state
2. Summarize and archive
3. Keep: facts still in effect, unresolved items, relationship context that matters

## Context Sources
- Target memory area files
- memory/context-index.md (update after changes)

## Output Format
For each area compacted:
```
## [Area] Summarization
- Original: [n] entries / [n] lines
- Compacted: [n] entries / [n] lines
- Archived: [file path]
- Key facts preserved: [list]
- Discarded: [categories of removed content]
```

## Quality Standard
- Original content is archived, never deleted
- Key facts (decisions, commitments, relationship changes) always preserved
- Compacted version is still useful for daily operations
- Context index updated to reflect any new archive files
- Diagnostic still passes after summarization

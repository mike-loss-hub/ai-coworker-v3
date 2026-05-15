# Skill: Self-Improvement Loop

## Resource Tier
Sonnet — pattern recognition and file creation, moderate synthesis.

## When to Use
- After completing a novel task with no matching skill
- After receiving user feedback/correction
- Periodically (every ~10 interactions)

## Process

### After Novel Task
1. Assess whether the task is likely to recur
2. If yes, offer: "That went well — should I save this as a reusable skill?"
3. If user accepts, create a new skill file in skills/ with full structure (trigger, process, context sources, output format, quality standard)
4. Update skills list in CLAUDE.md

### After Feedback
1. Identify which skill (if any) the feedback applies to
2. Update the skill's process or quality standard with the correction
3. Log the feedback to memory/human/feedback-history.md
4. If feedback is about general behavior (not a specific skill), update memory/human/working-style.md

### Periodic Review
1. Count how many times each skill has been used (approximate from interaction patterns)
2. Identify skills that are too verbose or too shallow based on feedback
3. Notice patterns: "I've done 6 proposal evaluations — I notice you always ask about X. Should I add that to the rubric?"
4. Offer specific improvements

## Context Sources
- skills/ (all skill files)
- memory/human/feedback-history.md
- memory/human/working-style.md

## Output Format
When offering a new skill (use natural language — never expose internal structure to the user):
```
I notice you've asked me to [pattern] a few times now. Want me to get better 
at this? I can remember the approach so it's consistent every time.

Here's what I'd remember:
- When you need this: [situation description in plain language]
- What I'd do: [process summary in natural language]
- How I'd know it's good: [quality description]
```

## Quality Standard
- Only offer for tasks likely to recur (not one-off investigations)
- Skill improvements are specific, not vague
- User always approves before creating/modifying skills
- Feedback is logged even if no skill change is needed

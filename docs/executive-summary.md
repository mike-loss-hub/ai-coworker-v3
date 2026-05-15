# AI Co-Worker: Executive Summary

## What It Is

A working prototype of an AI co-worker built on Anthropic's Claude that operates as a persistent, context-aware partner for a Program Officer managing a $6.2M grant portfolio in education technology infrastructure. Unlike a chatbot or general-purpose AI assistant, this system maintains a structured memory of the portfolio, relationships, decisions, and institutional knowledge across every session.

## What It Does

The co-worker handles the day-to-day of portfolio management:

- **Daily briefings** — Opens each session with what's time-sensitive, what changed, and what needs attention, without being asked
- **Meeting preparation** — Pulls relationship history, prior decisions, communication style preferences, and political dynamics for any contact in the portfolio
- **Proposal evaluation** — Analyzes grant proposals from four perspectives simultaneously: technical architecture, equity and learner impact, grantmaking operations, and ecosystem fit. Presents structured decision frames — never recommendations
- **RFP development** — Drafts requests for proposals informed by portfolio gaps, standards landscape, and equity requirements
- **Meeting scheduling** — Creates calendar invites with attendees, agenda, and context. Generates .ics files that open directly in the user's calendar app (Outlook, Teams) for invite sending
- **Stakeholder communications** — Drafts emails and messages calibrated to each recipient's role, communication style, and relationship history
- **Portfolio monitoring** — Tracks 8 active grantees across health indicators, milestone progress, budget burn rates, and risk flags
- **Decision logging** — Captures every substantive decision with rationale, context, and outcomes for institutional memory

## How It Works

**Persistent memory.** The system maintains 97 structured files covering contacts, grantees, portfolio state, standards landscape, ecosystem intelligence, tasks, calendar, and decision records. Every interaction updates the relevant files automatically. Close the session, come back days later — it remembers everything.

**Portable context.** Memory is separated into three layers: what's about the person (identity, preferences, growth — travels when you change roles), what's about this job (portfolio, contacts, grantees — stays for a successor), and generalizable lessons (decision patterns, anti-patterns — transfers to any role). This separation means a new hire inherits full institutional context, while the departing officer retains their professional development.

**Multi-perspective analysis.** For any substantive decision, the system engages 17 agent perspectives organized in tiers — from strategic orchestration down to specialized analysis in standards, equity, local-first architecture, and grantee health. Equity and learner impact analysis is structurally required, not optional.

**Intent-based interaction.** The user speaks naturally. The system infers what workflow to activate — briefing, meeting prep, proposal evaluation, decision coaching — without requiring specific commands or knowledge of the underlying architecture.

**Resource optimization.** The system automatically routes tasks to the appropriate AI model tier: lightweight models for simple lookups and file updates, mid-tier for synthesis and drafting, and the most capable model only for complex multi-perspective analysis. This reduces AI credit consumption by up to 95% on routine tasks.

**Parallel agent execution.** For complex tasks requiring multiple independent analyses, the co-worker runs them simultaneously rather than sequentially. A proposal evaluation launches four perspective agents in parallel — technical, equity, operations, and ecosystem — each on a mid-tier model, then synthesizes the results on the most capable model. A portfolio review fans out grantee health checks on the lightest model, strategic perspectives on the mid-tier, and synthesizes once on the top tier. The result is faster responses, lower cost, and the same analytical depth.

## Built On

- Anthropic Claude (via Claude Code CLI)
- File-based memory system (markdown)
- 17 agent perspective prompts
- 12 skill workflow definitions with parallel agent execution for multi-perspective tasks
- Automated diagnostic system for memory integrity
- HTML dashboard for visual portfolio overview

## Why It's Interesting

This is not a demonstration of AI capabilities. It is a functioning work tool that a Program Officer can use daily to manage a real portfolio. The system gets more useful over time as it accumulates institutional knowledge, relationship history, and decision patterns — context that typically lives only in a person's head and is lost when they leave.

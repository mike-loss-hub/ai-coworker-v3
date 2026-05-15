# AI Co-Worker Training Guide

A hands-on walkthrough of the AI Co-Worker system. By the end of this guide, you will have used every major feature, understood how the components connect, and experienced what it feels like to work with an AI colleague that remembers everything.

**Time required:** 2.5–4 hours for all 27 labs. You can stop after any lab and pick up later — the co-worker remembers where you left off. Parts 1–2 (Labs 1–14) cover core functionality. Part 3 (Labs 15–24) covers extending the co-worker, culminating in a full end-to-end grant lifecycle. Part 3b (Labs 25–27) covers parallel agent execution across three scenarios.

**Prerequisites:**
- This project cloned and set up (`./setup.sh` completed successfully)
- Claude Code installed (CLI, VS Code extension, or desktop app)
- A terminal open in the project directory

---

## Part 1: Understanding the System

### What Is This?

The AI Co-Worker is a Claude Code project that turns Claude into a persistent, structured colleague. Unlike a normal chat session that starts fresh every time, this system:

- **Remembers** — Every contact, decision, task, and conversation is stored in markdown files that persist across sessions
- **Thinks from multiple angles** — 17 agent perspectives evaluate situations from technical, equity, operational, and strategic viewpoints
- **Learns from you** — Your corrections, preferences, and patterns are captured and applied going forward
- **Travels with you** — Your personal working style and lessons learned are portable to a new role

### How It Works

When you open this project in Claude Code, three things happen:

1. Claude reads `CLAUDE.md` — the instruction file that defines the co-worker's identity and behavior
2. The co-worker reads `memory/context-index.md` — the master map of everything it knows
3. It checks your calendar and tasks, then leads with what matters today

Everything the co-worker learns gets written back to files in `memory/`. Close Claude Code, come back tomorrow — it all persists.

### Portable Memory

The co-worker automatically separates what it learns about **you as a person** from what it learns about **this specific job**. You don't need to manage this — it happens behind the scenes.

Why it matters: when you move to a new position, you export the personal context. A new co-worker starts day one knowing how you think, what mistakes you've made, and what patterns work for you — without any of the old job's data. Your lessons learned and working preferences travel with you.

### The Seed Data

The system comes pre-loaded with a realistic (but fictional) scenario: you are a Senior Program Officer at a philanthropic foundation, managing a $6.2M portfolio of grants focused on portable credentials and learner data infrastructure. There are 8 active grantees, 18 contacts, pending tasks, upcoming meetings, and recent decisions already in the system.

This seed data lets you experience the co-worker at full capability from the first minute. In real use, you would replace it with your actual role data over time.

---

## Part 2: Hands-On Labs

### Lab 1: Your First Session — The Daily Briefing

**Goal:** Experience the co-worker's proactive startup behavior and understand how it reads from memory.

**What you'll learn:** How the briefing skill works, how calendar and task data flows into daily awareness.

#### Steps

1. Open the project directory in Claude Code (VS Code extension or CLI)

2. Say something natural — any of these will work:
   ```
   What do I need to focus on today?
   ```
   or "Catch me up," "What's happening?", "Morning," or "Brief me." The co-worker understands intent, not keywords.

3. **Observe what happens.** The co-worker should:
   - Read your calendar (`memory/role/calendar/upcoming.md`)
   - Read your open tasks (`memory/role/tasks/active.md`)
   - Read portfolio health (`memory/role/portfolio/portfolio-state.md`)
   - Check for approaching deadlines (`memory/role/standards/comment-periods.md`)
   - Produce a structured briefing with priorities

4. **Check the output.** Does the briefing mention:
   - [ ] The Standards Alignment Working Group meeting (May 5)?
   - [ ] The 4 open tasks?
   - [ ] LearnTrail's Red health status?
   - [ ] The CLR 3.0 comment period closing May 20?

5. **Now look at the source files.** Open `memory/role/calendar/upcoming.md` and `memory/role/tasks/active.md` in your editor. Compare what the co-worker told you with what's in the files. It should be drawing directly from this data — not making things up.

#### What Just Happened

The co-worker read calendar, tasks, portfolio health, and deadlines, synthesized them into priorities, and presented a structured briefing. It figured out what you needed from your intent — you didn't need to use any specific phrase.

**Key insight:** The co-worker understands what you mean, not just what you say. "What's on my plate?" and "Brief me" produce the same result.

---

### Lab 2: Contact Retrieval — The Relationship Layer

**Goal:** See how the co-worker uses contact profiles to provide context-aware information about people.

**What you'll learn:** How contact files work, how relationship history informs the co-worker's responses.

#### Steps

1. Ask the co-worker about someone — in whatever way feels natural:
   ```
   Tell me about Elena Vasquez.
   ```
   or "What's the deal with Elena?", "Who is Elena Vasquez?", "Fill me in on Elena."

2. **Observe.** The co-worker should pull up her contact profile and grantee files automatically. It should surface:
   - Her role (PI at LearnTrail Research)
   - The CTO departure crisis
   - Her communication style (formal in writing, currently overwhelmed)
   - The May 30 architecture review deadline
   - Recent interaction history

3. Now try a relationship question:
   ```
   What's the dynamic between Linda Zhang and David Kowalski? I'm meeting with them both on May 5.
   ```

4. **Observe.** The co-worker should pull both contact profiles and the meeting prep file (`memory/role/meetings/2026-05-05-standards-alignment/prep.md`) to explain the political dynamics between 1EdTech and W3C.

#### What Just Happened

The co-worker cross-referenced multiple sources to build a complete picture. It didn't just dump a contact card — it connected the person to their grant, their current situation, and the relevant upcoming meeting. You asked a simple question and got a colleague-level answer.

---

### Lab 3: Meeting Preparation — The Preparation Mode

**Goal:** Use the co-worker to prepare for an upcoming meeting with full context, talking points, and political awareness.

**What you'll learn:** How the meeting-prep skill engages the Stakeholder Coalition agent perspective, how prep docs are generated.

#### Steps

1. Mention the upcoming meeting naturally:
   ```
   I have the standards alignment meeting on May 5. What do I need to know?
   ```

2. **Observe the output.** The co-worker should produce:
   - **Attendee profiles** with dynamics (Linda Zhang is cautious, David Kowalski is a technical purist, Diana Foster is pragmatic, James Okafor is presenting)
   - **Your position** (support bridge specification approach, per the April 22 decision)
   - **Talking points** appropriate for this audience
   - **Landmines to avoid** (don't frame as VC winning, don't let it become abstract)
   - **Success criteria** (form a working group, both parties willing to participate)

3. **Compare with the existing prep doc.** Open `memory/role/meetings/2026-05-05-standards-alignment/prep.md`. The co-worker should have used this file as a starting point and enriched it with current contact and portfolio context.

4. **Now ask a follow-up:**
   ```
   What's my strongest argument for the bridge approach? And what's the most likely objection from David Kowalski?
   ```

5. **Observe.** The co-worker should engage the Technical Architecture and Stakeholder Coalition perspectives to craft a response specific to Kowalski's communication style and technical priorities.

#### What Just Happened

The co-worker recognized your intent — you're preparing for a meeting — and automatically pulled contact profiles for each attendee, cross-referenced the relevant decision record, read the existing prep doc, and synthesized everything into an actionable briefing. It provided political awareness you might not have thought of, without you needing to ask for it.

---

### Lab 4: Evaluating a Proposal — Multi-Perspective Analysis

**Goal:** Experience the Decision Frame output format and see how multiple agent perspectives evaluate the same proposal.

**What you'll learn:** How the proposal-eval skill works, how the Equity perspective is always included, what a Decision Frame looks like.

#### Steps

1. The system includes a test proposal. Tell the co-worker about it naturally:
   ```
   Take a look at the ContextWeave proposal in scenarios/test-proposal.md. What do you think?
   ```

2. **Observe the Decision Frame.** The output should have five sections:
   - **Facts** — What we know (PI credentials, budget, technical approach, letters of support)
   - **Uncertainties** — What we can't verify (team hiring, actual interop with existing grantees)
   - **Perspectives:**
     - *Technical Architecture:* Is the semantic deduplication approach sound? Does the CRDT compatibility claim hold up?
     - *Equity & Learner Impact:* The proposal mentions transfer students and workforce reentry populations — is the equity framing substantive or performative?
     - *Grantmaking Operations:* Is $600K reasonable for the scope? Can a team of 5 (with 1 postdoc TBH) deliver?
     - *Ecosystem Intelligence:* Does this fill the memory consolidation gap identified in `memory/role/portfolio/pillar-coverage.md`?
   - **Options** — Fund, fund with conditions, decline, defer
   - **Tradeoffs** — What each option costs and gains

3. **Notice what it does NOT do.** The co-worker should NOT say "I recommend funding this" or "you should approve this." It presents a frame for YOU to decide. If it makes a recommendation, that's a bug — the system is designed to provide Decision Frames, never recommendations.

4. **Ask a follow-up to test depth:**
   ```
   How does this interact with PathWeaver's work? Is there overlap or synergy?
   ```

5. **Observe.** The co-worker should pull PathWeaver's profile from `memory/role/grantees/pathweaver/` and assess the relationship — noting that Sofia Chen provided a letter of support, which suggests synergy rather than overlap.

#### What Just Happened

The co-worker recognized you wanted an evaluation and automatically engaged multiple perspectives — technical, equity, operations, and ecosystem. It cross-referenced the proposal against existing portfolio data (pillar coverage, budget availability, grantee overlap). The equity perspective was included automatically — you didn't ask for it, but the co-worker always considers equity on substantive decisions. The output was a decision-support tool, not a decision.

---

### Lab 5: Decision Coaching — Navigating a Novel Situation

**Goal:** Experience decision coaching for a situation you haven't handled before, and see how the co-worker provides institutional context.

**What you'll learn:** How the co-worker surfaces institutional wisdom for novel situations, how generalizable patterns are captured for future use.

#### Steps

1. Present a novel scenario:
   ```
   Two of my grantees — PathWeaver and TrustLayer — want to merge their projects into a single combined grant. They say it would eliminate redundancy and produce a stronger outcome. James Okafor would lead the combined team. How should I handle this?
   ```

2. **Observe the Decision Frame.** The co-worker should:
   - Pull both grantee profiles and PI contact files
   - Assess the technical implications (what gets combined, what gets dropped)
   - Flag equity considerations (does consolidation reduce diversity of approaches?)
   - Provide institutional guidance: "Here's what experienced program officers typically do when grantees want to merge..." (grant modifications require board notification, IP provisions need review by legal, etc.)
   - Present options with tradeoffs

3. **Notice the institutional knowledge.** The co-worker should surface things you might not think to ask:
   - Does Carlos Mendez (legal counsel) need to review the merged grant agreement?
   - Does Patricia Williams (VP Programs) need to approve a modification of this size?
   - What happens to the separate milestones and reporting schedules?

4. **Make a decision.** Tell the co-worker what you'd decide (whatever you think is right). Then observe:
   ```
   I think we should allow the merger but require a revised scope document, board notification, and legal review. Let's proceed with that.
   ```

5. **Check what gets written.** After your decision, the co-worker should:
   - Create a decision record in `memory/role/decisions/`
   - Extract a generalizable pattern to `memory/bridge/pattern-library.md` (e.g., "Grantee Merger: require revised scope, board notification, legal review")
   - Update any relevant task tracking

#### What Just Happened

The co-worker engaged multiple perspectives on a complex, novel situation and provided institutional knowledge that elevated you beyond your current experience level. After your decision, it saved the specific decision for this role AND extracted a generalizable pattern that travels with you. If you change jobs in two years, the lesson "how to handle grantee mergers" comes with you — the co-worker remembers what you learned.

---

### Lab 6: Task Management — Delegating and Tracking

**Goal:** Create tasks, see them tracked, and observe how they surface in future briefings.

**What you'll learn:** How tasks are created naturally through conversation and persist across sessions.

#### Steps

1. Assign a task:
   ```
   Draft check-in emails to all grantees who owe Q2 reports. Reports are due May 15. I need the emails ready by May 5.
   ```

2. **Observe.** The co-worker should:
   - Read `memory/role/portfolio/portfolio-state.md` to identify all 8 grantees
   - Draft personalized emails for each (or a template with per-grantee customization)
   - Log the task to `memory/role/tasks/active.md`

3. **Verify the task was logged.** Open `memory/role/tasks/active.md` in your editor and confirm a new entry appears.

4. **Now ask:**
   ```
   What tasks are open right now?
   ```

5. **Observe.** The co-worker should read `memory/role/tasks/active.md` and list all open tasks — including the one you just created.

6. **Complete a task:**
   ```
   I finished reviewing the CredBridge revised timeline. It looks feasible — they can recover if they hold scope. Mark that task complete.
   ```

7. **Verify.** The task should move from `memory/role/tasks/active.md` to `memory/role/tasks/completed.md`.

#### What Just Happened

The co-worker executed a multi-step task (identify grantees → draft emails → track the work), then managed the lifecycle through completion. If external task management tools (like Linear or Asana) are connected to your session, tasks automatically appear there too — but you don't need to set anything up. Tomorrow's briefing will reference these tasks either way.

---

### Lab 7: Stakeholder Communications — Voice and Tone

**Goal:** See how the co-worker adapts communication tone based on contact profiles.

**What you'll learn:** How the co-worker adapts its writing based on who you're communicating with.

#### Steps

1. Ask for a supportive check-in:
   ```
   Draft a check-in email to Elena Vasquez about the LearnTrail architecture review. Be supportive but clear about the May 30 deadline.
   ```

2. **Observe the tone.** The email should be:
   - Empathetic but direct (Elena is stressed — her communication style says "keep communications focused and supportive")
   - Specific about the May 30 deadline
   - Offering concrete support, not just asking for status

3. **Now ask for a different voice:**
   ```
   Draft a message to Patricia Williams giving her a heads-up about the LearnTrail situation before the board meeting.
   ```

4. **Observe the difference.** This email should be:
   - Concise, bullet-pointed (Patricia's style: "prefers brevity, send bullet points not paragraphs")
   - Focused on what she needs to know, not the full backstory
   - Framed for a VP audience, not a PI audience

5. **One more — external relationship:**
   ```
   Draft an email to Sarah Mitchell at Gates Foundation to schedule a call about potential co-funding. Reference our conversation at ASU+GSV.
   ```

6. **Observe.** This should be:
   - Professional, strategic (Sarah is a potential co-funder, relationship is early)
   - Referencing the specific interaction from the contact file (April 2026 coffee at ASU+GSV)
   - Not overselling — Sarah "will want to see data before committing"

#### What Just Happened

The co-worker produced three communications with distinctly different tones, audiences, and levels of detail. It didn't just swap in names; it adjusted the entire communication strategy based on who you're writing to. If email tools are connected to your session, the co-worker can send or draft emails directly — otherwise it presents the text for you to copy.

---

### Lab 8: Meeting Debrief — Capturing What Happened

**Goal:** Experience the post-meeting workflow and see how information flows back into memory.

**What you'll learn:** How the meeting-debrief skill extracts action items, updates contacts, and logs decisions.

#### Steps

1. Simulate a meeting debrief:
   ```
   Debrief from the standards alignment meeting:

   The meeting went well. Linda Zhang was more open than expected — she said 1EdTech's board 
   is willing to explore a bridge specification if it doesn't require changes to the core CLR 
   spec. David Kowalski raised concerns about trust anchor semantics but agreed the bridge 
   approach is worth exploring. We formed a technical working group — James Okafor will chair 
   it. Diana Foster volunteered T3 to host the next meeting. Next meeting is June 2.

   Action items: James will circulate a draft bridge spec outline by May 20. I need to submit 
   our CLR 3.0 comments before May 20. Linda will brief her board and report back by May 25.
   ```

2. **Observe what the co-worker produces:**
   - Structured meeting notes
   - Action items with owners and due dates
   - Contact profile updates (Linda was more open than expected — that's new relationship context)
   - A decision record if warranted

3. **Verify the writes.** Check these files for updates:
   - `memory/role/meetings/2026-05-05-standards-alignment/` — should have a new `notes.md`
   - `memory/role/contacts/linda-zhang.md` — should have a new interaction history entry
   - `memory/role/contacts/david-kowalski.md` — same
   - `memory/role/tasks/active.md` — should have new action items
   - `memory/role/calendar/upcoming.md` — should note the June 2 follow-up meeting

4. **Test persistence.** Ask:
   ```
   What happened in the standards alignment meeting?
   ```
   The co-worker should recall the debrief you just gave, pulling from the notes it wrote.

#### What Just Happened

A single natural-language debrief triggered writes to 5+ memory files. The co-worker extracted structured data (action items, dates, relationship updates) from unstructured input (your meeting summary). This is the core persistence loop: things happen → you tell the co-worker → it writes to memory → future sessions have the context.

---

### Lab 9: Portfolio Review — The Big Picture

**Goal:** Experience a full portfolio review that synthesizes across all grantees, pillars, budget, and equity.

**What you'll learn:** How the portfolio-review skill engages all five Tier 1 perspectives, how cross-grantee analysis works.

#### Steps

1. Request a portfolio review:
   ```
   Run a full portfolio review. I need to prepare for the board update due June 1.
   ```

2. **Observe the output structure:**
   - **Portfolio Health Summary** — overall assessment
   - **Grantee Status Grid** — all 8 grantees with health, trend, key issues
   - **Pillar Coverage** — gaps and risks by pillar
   - **Budget Status** — burn rate and remaining capacity
   - **Equity Check** — are we serving target populations?
   - **Strategic Alignment** — does the current portfolio match the investment thesis?
   - **Risks & Flags** — top concerns with severity

3. **Notice the equity assessment.** It should be substantive — not "equity is important" but specific observations about which populations benefit, which are underserved, and what evidence exists (or doesn't).

4. **Ask a pointed follow-up:**
   ```
   If LearnTrail fails, what happens to our provenance pillar coverage?
   ```

5. **Observe.** The co-worker should reference `memory/role/portfolio/pillar-coverage.md`, note that LearnTrail is the only grant covering AI-generated summary provenance, assess the CredBridge and TrustLayer coverage of other provenance sub-domains, and identify the specific gap that would open.

#### What Just Happened

The co-worker operated in DEEP_WORK mode, reading from nearly every memory area simultaneously. It didn't just summarize — it analyzed trends, identified risks, and connected cross-grantee dependencies. The portfolio review is the co-worker's most complex operation, engaging all five primary agent perspectives and multiple sub-agents.

---

### Lab 10: The Dashboard — Visual Overview

**Goal:** See the portfolio visualized and understand how the dashboard reads from the same memory files.

**What you'll learn:** How the dashboard connects to the memory layer, how changes propagate.

#### Steps

1. Start the dashboard:
   ```bash
   source .venv/bin/activate
   python3 scripts/serve-dashboard.py
   ```

2. Open http://localhost:8080 in your browser.

3. **Explore the dashboard.** You should see:
   - Stats bar: 8 active grants, health breakdown (green/yellow/red), budget committed/unallocated
   - Alert cards: LearnTrail red status, CredBridge yellow, EdgeWise yellow, CLR comment period
   - Grantee status table with all 8 grants
   - Active tasks
   - Upcoming events and deadlines
   - Pillar coverage bars
   - Recent decisions

4. **Now modify a memory file directly.** In your editor, open `memory/role/portfolio/portfolio-state.md` and change EdgeWise's health from `🟡 Yellow` to `🟢 Green`.

5. **Refresh the dashboard** (or wait 30 seconds for auto-refresh). The dashboard should now show one fewer yellow alert.

6. **Revert your change.** Change EdgeWise back to `🟡 Yellow`.

7. Stop the dashboard with Ctrl+C.

#### What Just Happened

The dashboard is a read-only view of the same memory files the co-worker uses. There's no database, no API — just markdown files served over HTTP. When you change a file (whether manually or through the co-worker), the dashboard reflects it. This means the co-worker and the dashboard are always in sync by definition.

---

### Lab 11: Running Diagnostics — System Health

**Goal:** Use the diagnostic system to verify the co-worker's health and understand what it checks.

**What you'll learn:** How the diagnostic script validates memory integrity, agent health, skill health, portability, and more.

#### Steps

1. Run the diagnostic:
   ```bash
   source .venv/bin/activate
   python3 scripts/diagnostic.py
   ```

2. **Read the output.** You should see seven checks, all PASS:
   - MEMORY INTEGRITY — file counts, layer sizes
   - AGENT HEALTH — 17/17 prompts found
   - SKILL HEALTH — 9/9 core skills + custom skills
   - CONTEXT FRESHNESS — most and least recently updated areas
   - PORTFOLIO COHERENCE — cross-file consistency
   - PORTABILITY — human and bridge layers intact
   - FUNCTIONAL SMOKE TESTS — briefing, contact retrieval, task listing, identity load

3. **Break something intentionally.** Rename a file:
   ```bash
   mv memory/human/identity.md memory/human/identity-backup.md
   ```

4. **Run diagnostic again.** You should see PORTABILITY fail and FUNCTIONAL SMOKE TESTS fail on `identity_load`.

5. **Fix it:**
   ```bash
   mv memory/human/identity-backup.md memory/human/identity.md
   ```

6. **Run diagnostic one more time** to confirm HEALTHY.

7. **Check the diagnostic history.** Look in `memory/diagnostics/` — each run saves a timestamped report. Over time, this gives you a health history of the system.

#### What Just Happened

The diagnostic script is the co-worker's self-awareness mechanism. It validates that the entire system — memory, agents, skills, portability — is intact and consistent. When something breaks, it tells you exactly what and where. This is especially important after modifications, imports, or long periods without use.

---

### Lab 12: Learning From You — The Feedback Loop

**Goal:** Give the co-worker feedback and see it captured in the human layer for future use.

**What you'll learn:** How corrections persist, how the human layer grows over time.

#### Steps

1. Ask the co-worker to do something, then correct it:
   ```
   Draft a message to Marcus Rivera about the OpenSync v0.3 milestone.
   ```

2. After it produces a draft, give feedback:
   ```
   That's too formal for Marcus. He's an open-source community person — keep it casual 
   and enthusiastic. Also, I always like to mention specific technical details when 
   writing to engineers. Redo it.
   ```

3. **After the revision, observe:** The co-worker should offer to update Marcus's contact profile and log the feedback. If it doesn't offer, tell it:
   ```
   Remember that feedback about my communication preferences with engineers — 
   casual tone, specific technical details.
   ```

4. **Verify the write.** Check `memory/human/feedback-history.md` — your correction should be logged there. This file is in the **human layer**, meaning it's portable. If you switch jobs, your next co-worker will know you prefer casual, technically specific communication with engineers.

5. **Check the contact update.** Open `memory/role/contacts/marcus-rivera.md` — the communication style section should reflect the adjustment.

#### What Just Happened

The co-worker learned two things: a role-specific fact (Marcus prefers casual tone — written to the role layer) and a generalizable preference (you like casual + technical with engineers — written to the human layer). The role fact stays with this job. The preference travels with you.

---

### Lab 13: Portability — Exporting Your Context

**Goal:** Export your portable context and understand what travels with you vs. what stays behind.

**What you'll learn:** The three export modes, what each contains, how the three-layer architecture enables portability.

#### Steps

1. Run the portable export:
   ```bash
   source .venv/bin/activate
   python3 scripts/export.py --portable
   ```

2. **Read the output.** Note the archive size — this is just your human and bridge layers plus the skill and agent definitions. The role data (grantees, contacts, portfolio) is NOT included.

3. **Now run the role export:**
   ```bash
   python3 scripts/export.py --role
   ```

4. **Compare sizes.** The role export should be larger — it contains all the operational data. This is what you'd give to your successor.

5. **Run the full export:**
   ```bash
   python3 scripts/export.py --full
   ```

6. **Compare all three.** You should see:
   - `--portable`: Human + Bridge + Skills + Agents (smallest — just YOU)
   - `--role`: Role data + CLAUDE.md (medium — just THE JOB)
   - `--full`: Everything (largest — complete backup)

7. **Clean up the archives:**
   ```bash
   rm -f coworker-*.tar.gz
   ```

#### What Just Happened

The three-layer memory architecture directly enables three export modes. This is the portable memory thesis in action: your identity, preferences, feedback history, and lessons learned are separable from your role's data. A new co-worker at a new job can start with your portable export and immediately know how you work — it just needs to learn the new job.

---

### Lab 14: Exploring the Agent Perspectives

**Goal:** Understand how the 17 agent perspectives shape the co-worker's thinking.

**What you'll learn:** What each tier does, how perspectives combine, how to tell the co-worker to think from a specific angle.

#### Steps

1. Ask the co-worker to think from a specific perspective:
   ```
   Looking at the FieldKit pilot from the Equity & Learner Impact perspective only — 
   what should I be watching for when the pilot launches in June?
   ```

2. **Observe.** The response should focus exclusively on equity concerns: disaggregated outcomes, device-sharing implications, bilingual access, connectivity barriers, digital literacy assumptions.

3. **Now ask for a different perspective on the same thing:**
   ```
   Now look at the FieldKit pilot from the Technical Architecture perspective. 
   What are the technical risks for the June launch?
   ```

4. **Compare.** The technical perspective should focus on CRDT sync reliability, offline-first failure modes, edge cases in device-sharing, and integration with LearnChain's LRS.

5. **Now ask for synthesis:**
   ```
   Given both perspectives, where do the technical risks and equity risks overlap?
   ```

6. **Observe.** The co-worker should identify intersections — for example, sync failures disproportionately affect learners with poor connectivity (the equity-relevant population), or device-sharing data isolation has both a technical and a privacy dimension.

7. **Browse the agent prompts.** Open a few files in `agents/prompts/` to see how each perspective is defined. Notice that each specifies: role, domain scope, when to engage, output format, and context sources.

#### What Just Happened

You directed the co-worker to use specific agent perspectives, then asked it to synthesize across them. In normal operation, the orchestrator (agent 00) selects which perspectives to engage based on the situation. But you can always override and request a specific lens. The 17 perspectives are defined in markdown files — you can read, edit, or add new ones.

---

## Part 3: Extending the Co-Worker

These labs cover how the co-worker grows — learning new workflows, using external services automatically, and monitoring its own performance. Everything here produces real artifacts validated by the diagnostic.

**Time required:** 45–60 minutes for all labs in this section.

---

### Lab 15: Under the Hood — How Workflows Work (Optional)

**Goal:** Understand how the co-worker's internal workflows are defined, for those who want to customize or extend the system.

**What you'll learn:** The structure behind the co-worker's consistent behavior.

#### Steps

1. Open `skills/briefing.md` in your editor. This defines how the co-worker produces daily briefings.

2. **Notice the structure:** "When to Use" describes the intent (not magic phrases), "Process" defines the steps, "Context Sources" lists what files to read, "Output Format" defines the response shape, and "Quality Standard" defines what "good" looks like.

3. **The key insight:** You never need to know this structure exists. When you say "What's on my plate?" the co-worker matches your intent to this workflow automatically. But understanding it lets you customize — you could edit the process, add a context source, or change the output format.

4. **Run the diagnostic** to see how the system validates these workflows:
   ```bash
   source .venv/bin/activate
   python3 scripts/diagnostic.py
   ```
   The SKILL HEALTH check verifies all 9 core workflows have the required sections.

#### What Just Happened

You peeked behind the curtain. The co-worker's consistent behavior comes from structured workflow definitions — but the user never interacts with them directly. The co-worker understands intent and matches it to the right workflow automatically.

---

### Lab 16: Teaching the Co-Worker a New Workflow

**Goal:** Have the co-worker learn a new recurring pattern from your natural conversation.

**What you'll learn:** How the co-worker gets better at things you do repeatedly.

#### Steps

1. Tell the co-worker about a recurring need:
   ```
   I keep asking about grantee risks — what could go wrong, early warning signs, 
   contingency plans. I'd like you to be more consistent about how you assess these. 
   Can you get better at this?
   ```

2. **Observe.** The co-worker should propose what it would remember — in plain language, not technical jargon. Something like: "I can remember to always check the health log, milestones, key personnel, and portfolio dependencies when you ask about risks."

3. **Approve it:**
   ```
   Yes, do that.
   ```

4. **Run the diagnostic:**
   ```bash
   python3 scripts/diagnostic.py
   ```
   The custom skill count should increase by 1.

5. **Now use it naturally:**
   ```
   What could go wrong with LearnTrail?
   ```

6. **Observe.** The response should be more structured and thorough than a generic answer — it follows the workflow you just taught it.

#### What Just Happened

You taught the co-worker a new pattern through natural conversation. It created an internal workflow file, the diagnostic now tracks it, and future risk assessments will be consistent. You didn't write any files or learn any structure — you just told your colleague to get better at something.

---

### Lab 17: Improving the Diagnostic — Growing Quality Controls

**Goal:** Extend the system's self-monitoring so new workflows get the same validation as built-in ones.

**What you'll learn:** How to evolve the co-worker's quality controls as it grows.

#### Steps

1. Ask the co-worker to improve its own quality checks:
   ```
   The diagnostic should validate all workflows — not just the built-in ones. 
   The grantee risk assessment we just created should be checked too. Can you 
   update the diagnostic script?
   ```

2. **Let the co-worker make the change** to `scripts/diagnostic.py`. It should modify the validation to check all workflow files, excluding tool reference files (`tools-*.md`).

3. **Test with a deliberately broken file:**
   ```bash
   echo "# Skill: Test Incomplete\n\n## When to Use\nTesting\n" > skills/test-incomplete.md
   python3 scripts/diagnostic.py
   ```
   You should see warnings about the incomplete file.

4. **Clean up and verify:**
   ```bash
   rm skills/test-incomplete.md
   python3 scripts/diagnostic.py
   ```
   Should report HEALTHY.

#### What Just Happened

The co-worker improved its own quality controls. Every workflow it creates in the future will be validated automatically. The system grows and the safety net grows with it.

---

### Lab 18: External Services — Automatic Tool Use

**Goal:** See how the co-worker uses external services automatically, without you configuring anything.

**What you'll learn:** The co-worker uses available tools transparently — you don't need to know what's connected.

#### Steps

1. **Ask the co-worker to research something:**
   ```
   What's the latest on the 1EdTech CLR 3.0 specification? Any recent 
   announcements that affect our standards strategy?
   ```

2. **Observe what happens.** The co-worker will:
   - Check if web search tools are available in this session
   - If yes: search for current information, synthesize it with what's in memory, and update standards files
   - If no: work from its existing knowledge and memory files, giving you the best answer it can

   **You don't need to do anything.** No setup, no authentication prompts, no configuration. The co-worker handles tool discovery transparently.

3. **Try a task management scenario:**
   ```
   Add a task: submit CLR 3.0 comments by May 20.
   ```

4. **Observe.** The co-worker creates the task in local memory. If a task management service (Linear, Asana, Notion) is connected to your Claude Code session, the task appears there too — automatically. If not, nothing breaks.

5. **Run the diagnostic** to confirm everything is intact:
   ```bash
   python3 scripts/diagnostic.py
   ```

#### What Just Happened

The co-worker used whatever tools were available — or worked without them — and you never had to think about it. This is how a colleague works: they use the tools they have and adapt when they don't. External services enhance the co-worker but are never required.

---

### Lab 19: Task Lifecycle With External Services

**Goal:** Experience the full task lifecycle and see how external services augment it transparently.

**What you'll learn:** Tasks flow naturally through conversation regardless of what tools are connected.

#### Steps

1. **Create a task:**
   ```
   I need to review the CredBridge revised timeline and assess whether they can 
   recover the 6-week delay. This should be done by May 15.
   ```

2. **Observe.** The co-worker tracks this locally and, if task tools are connected, externally too. Check `memory/role/tasks/active.md` — the task should appear.

3. **Complete the task:**
   ```
   I finished the CredBridge timeline review. They can recover if they hold scope 
   on the identity verification module. Mark it done.
   ```

4. **Observe.** The task moves to completed. The co-worker may also update the CredBridge grantee files with your assessment.

5. **Check the full picture:**
   ```
   What's my task status right now?
   ```

#### What Just Happened

You managed tasks through natural conversation. The co-worker handled all the bookkeeping — local files, external sync, status tracking — without you ever thinking about where data lives.

---

### Lab 20: Teaching Multi-Step Workflows

**Goal:** Create a workflow that the co-worker can use to notify multiple stakeholders efficiently.

**What you'll learn:** How the co-worker learns complex, multi-step patterns from your guidance.

#### Steps

1. **Describe the need naturally:**
   ```
   When something significant happens with a grantee — health change, milestone, 
   timeline shift — I need to notify everyone who should know. Different people 
   need different levels of detail. Can you get better at this?
   ```

2. **Collaborate on the approach.** The co-worker should propose how it would handle this — identifying stakeholders, matching communication tone per recipient, using email tools if available or producing drafts if not.

3. **Refine with a business rule:**
   ```
   Always include Patricia Williams on any red-status grantee updates, even if 
   she's not directly involved. She's the VP and needs to know.
   ```

4. **Test it immediately:**
   ```
   LearnTrail's architecture review has been pushed to June 15. Elena requested 
   more time after the CTO departure. Who needs to know?
   ```

5. **Run the diagnostic:**
   ```bash
   python3 scripts/diagnostic.py
   ```

#### What Just Happened

You taught the co-worker a complex workflow through conversation, refined it with a business rule, and tested it immediately. If email tools are connected, it could send the messages directly. If not, it produces drafts. Either way, it remembered the rule about Patricia.

---

### Lab 21: Self-Assessment — How Is the Co-Worker Doing?

**Goal:** Ask the co-worker to evaluate its own performance.

**What you'll learn:** The co-worker can reflect on whether it's serving you well.

#### Steps

1. **Ask for a self-assessment:**
   ```
   How are you performing as a co-worker? Are there gaps in how you're helping me? 
   Anything you think we should improve?
   ```

2. **Observe the four dimensions it evaluates:**
   - Are all perspectives being used, or are some being ignored?
   - Are Decision Frames well-calibrated for the complexity of each decision?
   - Are there things I keep doing manually that should be automated?
   - Am I aligned with your corrections and preferences?

3. **Act on a recommendation.** If the co-worker identifies a gap, address it:
   ```
   You mentioned [gap]. Let's fix that.
   ```

4. **Compare with the structural diagnostic:**
   ```bash
   python3 scripts/diagnostic.py
   ```
   The diagnostic checks that files exist and are well-formed. The self-assessment checks whether the co-worker is actually effective. Both matter.

#### What Just Happened

The co-worker has a self-awareness layer. It can evaluate whether it's being helpful, identify blind spots, and suggest improvements. This is what makes it self-improving rather than static.

---

### Lab 22: End-to-End — A Real Work Scenario

**Goal:** Execute a complete, realistic scenario that shows the co-worker working at full capability.

**What you'll learn:** How everything fits together in real work.

#### Steps

1. **Set the scenario:**
   ```
   I just heard from Sofia Chen — FieldKit's pilot launch in Title I schools 
   has been moved up from June to May 20. They got early district approvals. 
   Good news, but it compresses our review timeline. Help me work through this.
   ```

2. **Let the co-worker work.** It should:
   - Update FieldKit milestones
   - Assess risks from the accelerated timeline
   - Identify who needs to know and draft appropriate messages
   - Create follow-up tasks
   - Log the conversation with Sofia

3. **Verify the memory updates.** Check that relevant files were updated — milestones, contacts, tasks.

4. **Run the diagnostic:**
   ```bash
   python3 scripts/diagnostic.py
   ```

5. **See it reflected in future context:**
   ```
   What do I need to focus on today?
   ```
   The briefing should now include the FieldKit accelerated launch.

6. **Capture the lesson:**
   ```
   That was a good workflow. Is there a generalizable lesson here for handling 
   accelerated timelines?
   ```
   The co-worker should extract a pattern that travels with you to future roles.

#### What Just Happened

A single natural conversation triggered updates across milestones, contacts, tasks, and stakeholder communications. The co-worker used whatever tools were available, maintained all records, and extracted a reusable lesson. This is the full system working as intended.

---

### Lab 23: Web Research — Augmenting the Co-Worker's Knowledge

**Goal:** See how the co-worker uses web research to stay current on your domain.

**What you'll learn:** The co-worker can pull current information when tools are available, and works from memory when they're not.

#### Steps

1. **Ask a research question:**
   ```
   What's the current landscape for learner data portability standards? 
   Has anything changed recently that affects our portfolio?
   ```

2. **Observe.** If web search is available, the co-worker will research current developments and cross-reference them against what's in memory. If not, it works from its existing knowledge and memory files.

3. **Ask it to update its knowledge:**
   ```
   Save anything new you found to the standards and ecosystem files.
   ```

4. **Run the diagnostic:**
   ```bash
   python3 scripts/diagnostic.py
   ```

5. **Verify the updates.** Check `memory/role/standards/` and `memory/role/ecosystem/` for any new information captured.

#### What Just Happened

The co-worker augmented its domain knowledge with current information — transparently. It used web search if available, worked without it if not, and stored new findings in the right place. You asked a question and got an answer; the plumbing was invisible.

---

### Lab 24: End-to-End Grant — From Gap to Active Grantee

**Goal:** Walk through the complete lifecycle of adding a new grantee to the portfolio — from identifying a strategic gap to having the grant actively monitored alongside the others.

**What you'll learn:** How every co-worker capability connects in a real grant lifecycle. This lab is long and scenario-driven. Each phase builds on the previous one, and the co-worker writes to memory throughout. By the end, your portfolio will have a 9th grantee with full monitoring in place.

**Time required:** 30–45 minutes. You can pause between phases — the co-worker remembers where you left off.

---

#### Phase 1: Identifying the Gap

You suspect there's a hole in your portfolio but want the co-worker to confirm it with data.

1. **Ask the co-worker to assess coverage:**
   ```
   I'm thinking about whether we need another grant in the portfolio. Are there 
   any strategic gaps that aren't covered by our current 8 grantees?
   ```

2. **Observe.** The co-worker should read pillar coverage, the investment thesis, and all grantee profiles, then surface gaps. It should identify the Agent Orchestration gap: no grant covers the agent-to-agent communication protocol layer. PathWeaver has a reference implementation and TrustLayer handles trust, but nobody is building the protocol itself.

3. **Dig deeper:**
   ```
   Tell me more about the agent orchestration protocol gap. How risky is it 
   that we don't have anyone working on this? What happens if MCP and A2A 
   fragment into competing standards?
   ```

4. **Observe.** The co-worker should engage the Technical Architecture and Ecosystem Intelligence perspectives, pull from the standards landscape, and give you a substantive risk assessment — not a generic warning.

---

#### Phase 2: Landscape Research

Before writing an RFP, you need to know who's working in this space.

1. **Ask the co-worker to research the landscape:**
   ```
   Who's doing interesting work on agent-to-agent coordination protocols — 
   especially in education or workforce contexts? Are there research groups, 
   startups, or open-source projects we should know about?
   ```

2. **Observe.** The co-worker will use web search if available, otherwise work from its knowledge and the ecosystem files. It should produce a landscape scan with potential candidates, their approaches, and fit with your thesis.

3. **Ask it to save what it found:**
   ```
   Save this landscape research. We'll need it for the RFP and later evaluation.
   ```

4. **Observe.** The co-worker should update `memory/role/ecosystem/` with the research findings. This becomes context for future conversations.

---

#### Phase 3: Drafting the Request for Proposals

1. **Ask the co-worker to draft an RFP:**
   ```
   Draft a request for proposals for the agent orchestration protocol gap. 
   It should align with our investment thesis, reference the existing grantees 
   it needs to interoperate with, and be clear about what we're funding vs. 
   what's already covered. Budget ceiling is $500K from our unallocated funds.
   ```

2. **Observe.** The co-worker should:
   - Reference the investment thesis (pillar 3: Agent Orchestration)
   - Name PathWeaver and TrustLayer as existing grants the new work must complement
   - Specify what's NOT in scope (reference implementations — PathWeaver has that; trust frameworks — TrustLayer has that)
   - Include equity requirements (how does this serve community college and workforce reentry populations?)
   - Set evaluation criteria

3. **Refine it:**
   ```
   Add a section on interoperability requirements. The protocol needs to work 
   with PathWeaver's reference implementation and TrustLayer's trust anchors. 
   Also, make sure we're asking applicants about local-first compatibility — 
   the protocol should work with intermittent connectivity.
   ```

4. **Ask for the equity perspective specifically:**
   ```
   Does the equity framing in this RFP feel substantive? Or is it checkbox equity?
   ```

5. **Observe.** The co-worker should engage the Equity & Learner Impact perspective and give you honest feedback — possibly noting where the RFP could be stronger about who benefits and how outcomes will be measured for underserved populations.

---

#### Phase 4: Building the Evaluation Rubric

Before proposals arrive, you need a consistent framework for evaluating them.

1. **Ask the co-worker to help build a rubric:**
   ```
   I need an evaluation rubric for the proposals we'll receive. It should 
   cover both quantitative and qualitative dimensions — technical merit, 
   team capability, equity impact, budget reasonableness, portfolio fit, 
   and standards alignment. Weight them so technical merit and equity 
   impact count the most.
   ```

2. **Observe.** The co-worker should propose a weighted rubric, something like:

   | Dimension | Weight | What It Measures |
   |-----------|--------|-----------------|
   | Technical Merit | 25% | Architecture soundness, feasibility, innovation |
   | Equity & Learner Impact | 25% | Target populations, outcome measurement, access design |
   | Portfolio Fit | 20% | Gap coverage, interoperability with existing grants |
   | Team & Execution | 15% | PI track record, team depth, key person risk |
   | Budget & Timeline | 10% | Cost reasonableness, milestone feasibility |
   | Standards Alignment | 5% | Open standards commitment, publication pathway |

3. **Refine the rubric:**
   ```
   The weights look right, but I want each dimension scored on a 1-5 scale 
   with specific criteria for what a 3 vs. a 5 looks like. And add a 
   qualitative section for "intangibles" — things like community reputation, 
   letters of support quality, and how the PI communicates.
   ```

4. **Approve and save:**
   ```
   Good. Save this rubric — we'll use it for all proposals in this round.
   ```

---

#### Phase 5: Evaluating Multiple Proposals

Three proposals have come in. (We'll simulate all three.)

1. **Present the first proposal:**
   ```
   Proposal 1: "AgentBridge" from Dr. Amara Osei, Distributed Systems Lab 
   at Georgia Tech.
   - $480K over 24 months
   - Team of 4 researchers + 2 grad students
   - Distributed consensus approach for agent-to-agent context sharing
   - Builds on their existing low-bandwidth consensus work
   - W3C publication pathway for open standard
   - Letters of support from Sofia Chen (PathWeaver) and James Okafor (TrustLayer)
   - Pilot: 3 community colleges in rural Georgia
   - Equity focus: designed for unreliable internet environments
   ```

2. **Present the second proposal:**
   ```
   Proposal 2: "CoordinateEd" from Dr. Lisa Park, MIT Media Lab.
   - $500K over 18 months
   - Team of 3 researchers + 1 engineer + 3 grad students
   - Event-driven messaging architecture for agent coordination
   - Strong publication record — 12 papers on multi-agent systems
   - No letters of support from existing grantees
   - Pilot: 2 large urban universities (Boston, Chicago)
   - Equity mention is brief — "we will ensure diverse participation"
   - Plans to publish as IEEE standard
   ```

3. **Present the third proposal:**
   ```
   Proposal 3: "SyncMesh" from Marcus Webb, Open Learning Collective 
   (nonprofit).
   - $320K over 24 months
   - Team of 2 full-time engineers + open-source community contributors
   - Mesh networking approach — agents discover and coordinate peer-to-peer
   - Active open-source project with 400 GitHub stars
   - Letter of support from Marcus Rivera (OpenSync) — uses similar CRDT approach
   - Pilot: 5 community colleges across Appalachia
   - Deep equity commitment — entire design centered on connectivity-limited populations
   - No academic publication pathway — open-source only
   ```

4. **Ask the co-worker to score all three against the rubric:**
   ```
   Score all three proposals against our rubric. Show me the quantitative 
   scores side by side, then give me your qualitative assessment of each.
   ```

5. **Observe.** The co-worker should produce a comparative evaluation:

   **Quantitative Scores (1-5 scale, weighted):**

   | Dimension (Weight) | AgentBridge | CoordinateEd | SyncMesh |
   |-------------------|-------------|--------------|----------|
   | Technical Merit (25%) | ? | ? | ? |
   | Equity & Impact (25%) | ? | ? | ? |
   | Portfolio Fit (20%) | ? | ? | ? |
   | Team & Execution (15%) | ? | ? | ? |
   | Budget & Timeline (10%) | ? | ? | ? |
   | Standards Alignment (5%) | ? | ? | ? |
   | **Weighted Total** | **?** | **?** | **?** |

   The co-worker fills in the scores with justifications for each. Look for whether the scores are specific (referencing actual proposal details) or generic.

   **Qualitative "Intangibles":**
   The co-worker should assess letters of support quality, PI communication style, community reputation, and anything that doesn't fit neatly into a number.

6. **Challenge the scoring:**
   ```
   I'm surprised by the CoordinateEd equity score. Dr. Park has a strong 
   publication record — does that translate to impact? And the SyncMesh 
   team is tiny — can 2 engineers plus open-source contributors really 
   deliver a protocol spec?
   ```

7. **Observe.** The co-worker should defend or adjust its scores with specifics, not deference. A strong equity assessment doesn't award points for "we will ensure diverse participation" — that's checkbox equity. The team risk on SyncMesh is real but offset by the active open-source community.

8. **Ask for the equity perspective explicitly:**
   ```
   Which proposal actually serves our target populations best — not on 
   paper, but in practice? Community colleges, workforce reentry, rural 
   and connectivity-limited learners.
   ```

9. **Observe.** The co-worker should distinguish between proposals that name equity populations and proposals that design for them. AgentBridge and SyncMesh both have substantive equity design; CoordinateEd's urban university pilot doesn't reach the target populations.

---

#### Phase 6: Making the Decision

1. **Discuss the tradeoffs with the co-worker:**
   ```
   Walk me through the tradeoffs. AgentBridge has the strongest portfolio 
   fit with the existing grantee letters. SyncMesh has the deepest equity 
   commitment and lowest cost. CoordinateEd has the strongest academic 
   credentials. What would I gain and lose with each choice?
   ```

2. **Observe.** The co-worker should present a Decision Frame — not a recommendation — laying out what each choice costs and gains across technical, equity, operational, and ecosystem dimensions.

3. **Make your decision:**
   ```
   I'm going with AgentBridge. The combination of existing grantee support, 
   W3C standards pathway, and substantive rural equity pilot is the strongest 
   package. The distributed consensus approach complements PathWeaver rather 
   than competing with it.

   But I want to do two things:
   1. Send a thoughtful decline to Dr. Park and Marcus Webb — keep the 
      door open for future rounds
   2. Invite Marcus Webb to our Q3 convening as an observer — SyncMesh's 
      mesh approach could inform future portfolio strategy

   Conditions on the AgentBridge grant:
   1. First milestone must include a compatibility test with PathWeaver's API
   2. Quarterly check-ins, not just annual reports
   3. Dr. Osei must attend the Q3 portfolio convening
   4. Pilot must include disaggregated outcome reporting by institution type

   Log all of this.
   ```

4. **Observe.** The co-worker should:
   - Create a decision record with the rationale, scores, and conditions
   - Draft decline letters to Dr. Park and Marcus Webb — professional, specific about why, and leaving the door open
   - Note the Q3 convening invitation for Marcus Webb
   - Extract generalizable patterns (e.g., "when choosing between proposals, existing grantee interoperability letters signal execution likelihood")

---

#### Phase 7: Internal Approvals and Onboarding

Before the grant is official, it needs internal sign-off. Then the winner needs to be fully onboarded.

1. **Ask about the approval process:**
   ```
   What do I need to do internally to get AgentBridge approved? Who signs 
   off and what documents do I need?
   ```

2. **Observe.** The co-worker should reference Patricia Williams (VP Programs), Carlos Mendez (Legal), and Robert Kim (Finance), and outline the approval chain.

3. **Draft all internal materials at once:**
   ```
   Draft everything I need:
   - Grant recommendation memo for Patricia (bullet points, strategic)
   - Budget justification for Robert (numbers, financial detail)
   - Note to Carlos asking him to prepare the grant agreement with our 
     four conditions attached
   - A welcome letter to Dr. Osei confirming the award and outlining 
     next steps and expectations
   ```

4. **Observe the tone differences.** Four documents, four voices — Patricia gets strategy, Robert gets spreadsheet logic, Carlos gets legal precision, Dr. Osei gets warmth and clarity. All from the same conversation.

5. **Send the decline letters:**
   ```
   Send those decline letters to Dr. Park and Marcus Webb. And add Marcus 
   Webb as a contact — we'll want to track the relationship.
   ```

6. **Observe.** The co-worker drafts (or sends, if email tools are connected) the decline letters, creates `memory/role/contacts/marcus-webb.md`, and logs the interactions.

---

#### Phase 8: Setting Up the Grantee

The grant is approved. Now the co-worker sets up full monitoring.

1. **Tell the co-worker to set up everything:**
   ```
   AgentBridge is approved. Set up everything we need to track and manage 
   this grant — same structure as our other grantees. Dr. Amara Osei is the 
   PI. Georgia Tech, Distributed Systems Lab. $480K, 24 months starting 
   July 1, 2026.
   ```

2. **Observe.** The co-worker should create:
   - `memory/role/grantees/agentbridge/profile.md` — grant details, team, pillar alignment, conditions
   - `memory/role/grantees/agentbridge/health-log.md` — initial Green status
   - `memory/role/grantees/agentbridge/milestones.md` — milestone schedule reflecting the four conditions
   - `memory/role/grantees/agentbridge/correspondence.md` — welcome letter logged
   - `memory/role/contacts/amara-osei.md` — new contact profile for the PI

3. **Verify the files:**
   ```bash
   ls memory/role/grantees/agentbridge/
   ls memory/role/contacts/amara-osei.md
   ```

4. **Update portfolio-wide files:**
   ```
   Update portfolio state, pillar coverage, and budget tracker to reflect 
   AgentBridge. Also add the Q3 convening to the calendar — we now have 
   both Dr. Osei and Marcus Webb attending.
   ```

5. **Observe updates to:**
   - `memory/role/portfolio/portfolio-state.md` — 9 active grants
   - `memory/role/portfolio/pillar-coverage.md` — Agent Orchestration gap addressed
   - `memory/role/portfolio/budget-tracker.md` — $480K allocated, ~$20K unallocated
   - `memory/role/calendar/upcoming.md` — Q3 convening with new attendees

6. **Set up the first check-in:**
   ```
   Schedule the first quarterly check-in with Dr. Osei for mid-October. 
   Add a task to prepare for it a week before.
   ```

---

#### Phase 8: Verification

1. **Run the diagnostic:**
   ```bash
   python3 scripts/diagnostic.py
   ```
   It should report HEALTHY with updated counts: 9 grantees, updated contact count, and the new decision.

2. **Ask for a briefing to see the new grant in context:**
   ```
   What do I need to focus on today?
   ```
   The briefing should now reference AgentBridge alongside the other 8 grantees.

3. **Check the dashboard:**
   ```bash
   python3 scripts/serve-dashboard.py
   ```
   Open http://localhost:8080 — the stats should show 9 active grants and the updated budget. The pillar coverage bars should reflect the improved Agent Orchestration coverage.

4. **Test portfolio awareness:**
   ```
   How does AgentBridge affect our portfolio risk profile?
   ```
   The co-worker should note that the Agent Orchestration gap is now addressed, but flag concentration risk (the protocol layer depends on a single grant) and the tight remaining budget (~$20K unallocated).

---

#### What Just Happened

You walked through the complete grant lifecycle using your co-worker as a real colleague:

| Phase | What You Did | What the Co-Worker Did |
|-------|-------------|----------------------|
| Gap analysis | "Are there any strategic gaps?" | Read pillar coverage, flagged Agent Orchestration |
| Research | "Who's working on this?" | Landscape scan, saved to ecosystem files |
| RFP drafting | "Draft an RFP" | Wrote RFP aligned to thesis, equity-reviewed |
| Rubric | "Build an evaluation rubric" | Weighted scoring framework with qualitative intangibles |
| Evaluation | "Score all three proposals" | Comparative quantitative + qualitative assessment |
| Decision | "I'm going with AgentBridge" | Decision record, decline letters, generalizable patterns |
| Approvals | "Draft everything I need" | 4 documents in 4 voices for 4 stakeholders |
| Onboarding | "Set up everything" | Grantee files, contacts, portfolio updates, calendar |
| Verification | Diagnostic + briefing + dashboard | All systems reflect the 9th grantee |

At no point did you configure a system, write a file, or use a specific phrase. You talked to a colleague, and the colleague handled the rest — from the first "are there any gaps?" to a fully monitored 9th grantee in the dashboard.

The co-worker also captured generalizable lessons along the way. When you move to your next role, you'll bring patterns like "require compatibility tests as first milestone for protocol grants," "existing grantee support letters signal execution likelihood," and "always check equity framing in RFPs before publishing."

---

## Part 3b: Parallel Agent Execution

The co-worker doesn't always think one step at a time. For complex tasks that need multiple independent analyses, it runs them simultaneously — like a team lead who assigns four people to research different angles of the same question, then pulls their findings together into one brief.

These labs show how this works across three different scenarios, each highlighting a different advantage of parallel execution.

### How It Works

When the co-worker faces a task requiring multiple independent analyses, it uses a **fan-out / fan-in** pattern:

```
You ask a question
    ↓
┌─────────────────────────────────────────────┐
│ Analysis A (Sonnet) ── 20 sec               │
│ Analysis B (Sonnet) ── 20 sec               │  All run at
│ Analysis C (Sonnet) ── 20 sec               │  the same time
│ Analysis D (Sonnet) ── 20 sec               │
└─────────────────────────────────────────────┘
    ↓
Synthesize all results (Opus) ── 15 sec
    ↓
Total: ~35 seconds
```

Compare this to running everything sequentially on a single model:

```
Analysis A → B → C → D → Synthesize
Total: ~2.5 minutes, all on the most expensive model
```

Each parallel agent runs on a lighter, cheaper model suited to its task. The most capable model only runs once — for the final synthesis where nuanced judgment matters most. The result: same analytical depth, faster response, lower credit consumption.

Three model tiers are used:

| Model | Role | When Used |
|-------|------|-----------|
| Haiku (lightest) | Data gathering | Reading files, checking status, extracting facts |
| Sonnet (mid-tier) | Single-perspective analysis | One perspective's assessment of a problem |
| Opus (most capable) | Synthesis and judgment | Combining multiple analyses into a coherent output |

---

### Lab 25: Proposal Evaluation — Four Perspectives at Once

**Goal:** See parallel execution on the co-worker's most analytically demanding task — evaluating a grant proposal from four perspectives simultaneously.

**Advantage highlighted:** Speed and analytical coverage. Four independent expert analyses run at the same time instead of waiting for each to finish before starting the next.

**Time required:** 10 minutes.

#### Steps

1. **Present a proposal for evaluation:**

   > "Evaluate this concept: A team at Stanford proposes building an open-source credential wallet that lets community college students carry their CLR records across institutions. They're requesting $600K over 18 months. The PI has published on decentralized identity but hasn't worked in education before."

2. **Watch the response form.** The co-worker will:
   - Read pillar coverage and budget files
   - Launch 4 parallel agents, each analyzing the proposal from a different perspective:
     - **Technical Architecture** — Is the wallet architecture sound? Does it conflict with existing grantees?
     - **Equity & Learner Impact** — Does it serve community college students? How is consent handled?
     - **Grantmaking Operations** — Is $600K reasonable? What's the key person risk with a PI new to education?
     - **Ecosystem Intelligence** — Does this fill a portfolio gap? Who else is building credential wallets?
   - Collect all 4 results and synthesize into a single Decision Frame

3. **Notice the structure of the output.** The Decision Frame has distinct perspective sections — each was produced by a separate agent working independently. The synthesis at the top connects them into a coherent assessment that no single perspective would have produced alone.

#### What Just Happened

The co-worker ran the equivalent of four expert consultations simultaneously. Each perspective agent received the proposal text and its relevant context, analyzed it through its specific lens, and returned findings. The main conversation then synthesized these into a Decision Frame. Without parallelization, this would take 4× longer and cost more in credits, since each perspective would run sequentially on the most expensive model.

---

### Lab 26: Portfolio Review — Tiered Parallel Gathering

**Goal:** See parallel execution used for data gathering at scale — checking the health of multiple grantees simultaneously before running strategic analysis.

**Advantage highlighted:** Efficient use of model tiers. The lightest model handles bulk data gathering in parallel, the mid-tier handles strategic perspectives, and only the final synthesis needs the full model. This is the most resource-intensive operation the co-worker performs, and parallelization makes it practical.

**Time required:** 10 minutes.

#### Steps

1. **Request a portfolio review:**

   > "How's the portfolio looking? Give me the full picture."

2. **Watch the multi-stage parallel process.** The co-worker will:
   - **Stage 1:** Read portfolio overview files (portfolio-state, pillar-coverage, budget-tracker)
   - **Stage 2 — Fan out on Haiku:** Launch parallel lightweight agents to check each flagged grantee's health log. If 3 grantees are flagged yellow or red, that's 3 parallel agents reading 3 files simultaneously
   - **Stage 3 — Fan out on Sonnet:** Launch 5 parallel perspective agents (Technical Architecture, Ecosystem Intelligence, Stakeholder Coalition, Equity & Learner Impact, Grantmaking Operations) to assess the portfolio from their respective angles
   - **Stage 4 — Synthesize on Opus:** Combine all grantee health data and perspective analyses into a structured portfolio review

3. **Count the layers.** This single request triggered three tiers of parallel execution:
   - Haiku agents for data gathering (cheapest, fastest)
   - Sonnet agents for perspective analysis (moderate cost, moderate depth)
   - One Opus synthesis pass (highest cost, highest judgment — runs only once)

#### What Just Happened

The portfolio review is the co-worker's most complex operation — it touches the most files and engages the most perspectives. Without parallelization, this would mean sequentially reading 8+ grantee files, then sequentially running 5 perspectives, all on the most expensive model. With tiered parallelization, the bulk work happens on cheaper models running simultaneously, and the expensive model only handles the final synthesis. The output is the same; the cost and time are significantly lower.

---

### Lab 27: Meeting Prep — Parallel Context Gathering

**Goal:** See parallel execution used for a different purpose — not analysis, but fast context assembly from multiple sources before a meeting.

**Advantage highlighted:** Wall-clock speed. When you need prep for a meeting in 10 minutes, the co-worker gathers everything it needs simultaneously instead of reading files one at a time.

**Time required:** 5 minutes.

#### Steps

1. **Ask for meeting prep with multiple attendees:**

   > "I'm meeting with Elena Vasquez and David Kowalski tomorrow. Elena wants to discuss the LearnTrail situation and David wants to talk about VC 2.0 implications for our portfolio."

2. **Watch the parallel context gathering.** The co-worker will fan out on Haiku to gather information simultaneously:
   - Elena's contact file + recent correspondence
   - David's contact file + recent correspondence
   - LearnTrail's grantee profile + health log
   - VC 2.0 status from the standards landscape file
   - Prior meeting notes with either attendee

   These are all independent file reads — none depends on another — so they all run at the same time.

3. **Notice the speed.** Five or six file reads that would take several seconds each happen in the time of one. The co-worker then synthesizes the gathered context into a meeting prep brief — attendee dynamics, talking points, landmines to avoid, and connections between the two topics Elena and David are bringing.

4. **Compare with a single-contact prep.** Now try:

   > "Quick prep for a call with Linda Zhang about CLR 3.0."

   Notice: fewer parallel agents (just one contact file + one standards file). The co-worker scales its parallelization to the task. Simple prep doesn't need the overhead of fanning out.

#### What Just Happened

This lab shows parallelization used for speed rather than analytical depth. The co-worker didn't need multiple perspectives — it needed multiple pieces of context gathered quickly. By reading all relevant files simultaneously on the lightest model, it assembled a comprehensive meeting prep in seconds rather than sequentially loading each source. The synthesis still happens on a more capable model, but the gathering phase — which is often the bottleneck — runs in parallel.

---

### Parallel Execution Summary

| Lab | Scenario | What Runs in Parallel | Primary Advantage |
|-----|----------|-----------------------|-------------------|
| 25 | Proposal evaluation | 4 perspective analyses (Sonnet) | Analytical coverage — four expert views at once |
| 26 | Portfolio review | Grantee health checks (Haiku) + 5 perspectives (Sonnet) | Cost efficiency — bulk work on cheap models |
| 27 | Meeting prep | 5-6 context file reads (Haiku) | Speed — all context gathered simultaneously |

The co-worker decides when to parallelize automatically. You never need to request it or configure it. Simple tasks (adding a task, updating a contact) run directly on a single lightweight model. Complex tasks fan out to parallel agents and fan back in for synthesis. The system matches its execution strategy to the work.

---

## Part 4: Understanding the Architecture (Power Users)

Everything in this section is behind the scenes. You never need to reference these concepts in conversation with the co-worker — it handles all of this internally. This section is for people who want to customize or extend the system.

### How Files Connect

Here's the data flow for a typical interaction:

```
You say something
    ↓
CLAUDE.md defines co-worker behavior
    ↓
Orchestrator (agents/prompts/00) selects mode and perspectives
    ↓
Resource tier assessed — simple tasks use lighter models, complex analysis uses full models
    ↓
Relevant skill (skills/*.md) defines the process
    ↓
Skill reads only the memory/ files it actually needs
    ↓
Agent perspectives (agents/prompts/01-16) shape analysis (only those relevant to the task)
    ↓
Co-worker responds to you
    ↓
Co-worker writes results back to memory/ files
    ↓
Next interaction reads the updated files
```

### File Types and Their Roles

| Directory | What It Contains | Who Reads It | Who Writes It |
|-----------|-----------------|--------------|---------------|
| `memory/human/` | Your identity, preferences, growth | Co-worker (every session) | Co-worker (when you give feedback or grow) |
| `memory/bridge/` | Generalizable lessons and patterns | Co-worker (when coaching decisions) | Co-worker (after decisions reveal patterns) |
| `memory/role/` | All operational data for this job | Co-worker + Dashboard | Co-worker (after every substantive interaction) |
| `agents/prompts/` | How the co-worker thinks | Co-worker (when engaging perspectives) | You (to customize or add perspectives) |
| `skills/` | How the co-worker does things | Co-worker (when executing workflows) | Co-worker (self-improvement) or you |
| `CLAUDE.md` | Master identity and behavior | Claude Code (on startup) | You (to change core behavior) |
| `dashboard/` | Visual portfolio overview | Your browser | Nobody (reads from memory/) |
| `scripts/` | Utilities | You (from terminal) | Nobody |

### Customization Points

**Change the co-worker's personality or priorities:**
Edit `CLAUDE.md`. This is the master instruction file that Claude Code reads on every session.

**Add a new agent perspective:**
Create a new `.md` file in `agents/prompts/` with sections for Domain Scope, When Engaged, Output Format, and Context Sources. Update the orchestrator prompt to reference it.

**Add a new workflow:**
Create a new `.md` file in `skills/` with sections for Resource Tier, When to Use, Process, Context Sources, Output Format, and Quality Standard. Or just ask the co-worker to learn a new pattern — it creates the file for you.

**Resource optimization:**
The co-worker manages AI credits automatically so you don't run out mid-session. This is a backend feature — you never configure it, but understanding it helps you get the most from your credits.

**Three optimization dimensions:**

1. **Context management (biggest savings).** The memory system has ~97 files and ~17,500 words. Loading all of it into every interaction would burn thousands of tokens on context the task doesn't need. Instead, each skill specifies which files to "always load" vs. "load only if relevant." The context-index acts as a map — the co-worker reads it to know where things are, then loads only the specific files the current task requires.

2. **Model routing.** Each skill has a Resource Tier that determines which model handles it:
   - *Haiku* — file lookups, task logging, contact updates, diagnostics
   - *Sonnet* — briefings, meeting prep/debrief, email drafts, research summaries
   - *Opus* — proposal evaluation, decision frames, portfolio reviews, strategic analysis

   Haiku costs roughly 1/50th of Opus per token. Most routine work runs on Haiku or Sonnet.

3. **Response efficiency.** Output length matches task complexity. A status answer is 2-3 sentences. A portfolio review is a structured report. The co-worker doesn't over-elaborate on simple tasks.

**What this looks like in practice:**

| Task | Old (unoptimized) | New (optimized) | Reduction |
|------|-------------------|-----------------|-----------|
| Update a contact | ~6,500 tokens on Opus | ~190 tokens on Haiku | 97% |
| Proposal evaluation | ~13,200 tokens on Opus | ~2,350 tokens on Opus | 82% |
| Daily briefing (quiet day) | ~1,500 tokens on Opus | ~460 tokens on Sonnet | 70% |
| Portfolio review | ~9,000 tokens on Opus | ~2,050 tokens on Opus | 77% |

A typical routine session (briefing → contact update → email draft → task log) drops from ~25,000 input tokens on Opus to ~4,000 tokens across Haiku/Sonnet — roughly a **95% cost reduction** for everyday work.

**Tips for maximizing credits:**
- Ask specific questions ("What's the FieldKit pilot status?") rather than broad ones ("Tell me everything about the portfolio")
- Let multi-step workflows complete one phase before starting the next
- Portfolio reviews and multi-proposal evaluations are the most expensive operations — save them for when you need full analysis

**Change the role:**
Replace the seed data in `memory/role/` with your actual role's data. Edit `memory/human/identity.md` to reflect who you are. The co-worker adapts.

---

## Part 5: Daily Use Patterns

### Morning Routine
1. Open Claude Code in the project directory — the co-worker leads with what matters today
2. "What do I need to focus on?" or "Catch me up" → priorities and deadlines
3. Glance at the dashboard for visual overview
4. Work through the day's tasks naturally

### Before a Meeting
- "I'm meeting with Elena tomorrow" → full prep with dynamics, talking points, and landmines

### After a Meeting
- "Here's what happened in the meeting..." → structured notes, action items, contact updates

### When Evaluating Something
- "What do you think of this proposal?" → Decision Frame with multiple perspectives

### When Facing Something New
- "How should I handle this?" → decision coaching with institutional context

### End of Week
- "How's the portfolio looking?" → full assessment
- "Is everything working?" → system health check

### When You Get Feedback
- Correct the co-worker in plain language → it remembers and applies it going forward

---

## Part 6: Troubleshooting

### "The co-worker doesn't remember what we discussed yesterday"

Check that the co-worker is writing to memory files after interactions. Open `memory/role/tasks/active.md` or `memory/role/decisions/` to see if recent interactions were captured. If not, explicitly ask: "Save that decision to the decision log."

### "The briefing seems generic / doesn't reference real data"

Run `python3 scripts/diagnostic.py` to check if memory files exist and are populated. If FUNCTIONAL SMOKE TESTS fail, the memory directory may be incomplete.

### "The dashboard is blank"

Make sure you're running the server from the project root: `python3 scripts/serve-dashboard.py`. The server needs to access `memory/` files relative to the project directory.

### "The co-worker recommends instead of framing"

Remind it: "Give me a Decision Frame, not a recommendation." If this happens repeatedly, add feedback: "Remember — always Decision Frames, never recommendations." The co-worker logs corrections and applies them going forward.

### "I'm running out of credits before finishing my work"

The co-worker optimizes credits automatically: it loads only the files each task needs (not the full memory system), routes simple tasks to lighter models, and matches output length to task complexity. If you're still running low:
- Ask specific questions ("what's the status of the FieldKit pilot?") instead of broad ones ("tell me everything about the portfolio")
- For multi-step workflows, let the co-worker complete one phase before starting the next — this avoids re-loading context unnecessarily
- Portfolio reviews and multi-proposal evaluations are the most expensive operations; save them for when you need the full analysis

### "I want to start fresh with my own role data"

1. Export your portable context: `python3 scripts/export.py --portable`
2. Delete `memory/role/` contents
3. Tell the co-worker about your new role — it will help you build the new job context
4. Your preferences, feedback history, and lessons learned carry over automatically

---

## Summary

The AI Co-Worker is designed to feel like a colleague, not a system. You talk naturally, it figures out what to do. It uses whatever tools are available and works without them when they're not. It remembers everything and separates what's about you from what's about this job.

The more you use it, the more it knows. The more it knows, the more useful it becomes. And when you move on, the most valuable parts — who you are, how you work, what you've learned — come with you.

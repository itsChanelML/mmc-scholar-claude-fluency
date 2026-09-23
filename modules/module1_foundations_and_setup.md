# Module 1 — Foundations & Getting Set Up

**Format:** ~60 minutes, hands-on
**You'll leave with:** Claude Code installed and authenticated, and your
first Global Instruction actually changing how it behaves.

---

## Part A — How to think about working with Claude (15 min)

### The 4D Framework

Before any tooling, a shared vocabulary for the judgment calls you'll make
all workshop — and every day after it. This is Anthropic's own framework
for AI collaboration, and it applies to everything from Module 2 onward:

| D | Plain-language question | Shows up later as |
|---|---|---|
| **Delegation** | What am I handing off, and what am I keeping control of? | Deciding whether something deserves a Skill, a Command, or just stays a conversation |
| **Description** | Have I given Claude enough real context to succeed? | Global Instructions, Skills, CLAUDE.md — all durable Description |
| **Discernment** | Do I actually believe this output is correct? | Reviewing a diff, a Skill's output, an MCP tool result before trusting it |
| **Diligence** | Am I accountable for what happens next? | Data access, what you share in a Plugin, your review habit |

Keep this table in your head. Every module below names which D it's
mostly exercising — not because they're separate, but because naming the
one you're weakest on is more useful than a vague "be careful."

### Automation → Augmentation → Agents

The second lens: **how much judgment does this task actually need**, and
which Claude Code feature matches that.

- **Automation** — the same steps, every time, zero judgment. *As an
  engineer, you'd see this as:* a deploy script, a lint check, a routine
  data pull you run identically every week. → **Commands** (Module 4):
  a saved trigger that does exactly the same thing on demand.
- **Augmentation** — you're still driving every step; Claude helps you
  think or move faster. *You'd see this as:* pasting a stack trace into a
  chat and asking what's wrong, or asking for a second opinion on an
  approach. → **Global Instructions** (this module): durable context so
  you're not re-explaining yourself in every conversation.
- **Agents** — Claude plans and executes multiple steps toward a goal,
  checking in at boundaries you set. *You'd see this as:* "here's a
  ticket, go implement it" or "triage these failing tests." →
  **Skills** (Module 2) and **MCP-connected work** (Module 3): Claude
  acting across several steps, with your review built into the process
  rather than bolted on after.

By Module 4 you'll have built something at every tier. That's the roadmap
for the next three sessions — not a menu, a progression.

---

## Part B — Get set up (20 min)

1. Install Claude Code and confirm it runs:
   ```bash
   claude --version
   ```
2. Authenticate with your Claude account if you haven't already.
3. Clone this repo and confirm the baseline is clean:
   ```bash
   git clone <this-repo-url>
   cd mmc-scholar-claude-fluency
   pip3 install -r requirements.txt
   python3 -m pytest        # should read 9 passed
   ```
4. Open Claude Code in this directory (`claude`) and ask it to explain
   what `mmc_scholars/roster.py` does — this is the same small MMC
   Scholar Roster codebase you'll build on for the rest of the workshop.

**Checkpoint:** `pytest` shows 9 passed, and Claude Code gave you a
correct plain-language summary of `roster.py` without you reading the
file yourself first.

---

## Part C — Your first Global Instruction (25 min)

A Global Instruction is saved and **always active** — every conversation,
every project, until you change it. That's exactly why it belongs to
**Description**: it's the context you'd otherwise have to repeat by hand,
every single time.

**Exercise:**

1. Pick 2–3 things you want true in *every* Claude Code session. Real
   starting points, not hypotheticals:
   - How much do you want explained before Claude acts — a one-line plan,
     or just the result?
   - Do you want tests run automatically before a change is considered
     done?
   - Any personal style preference (e.g., "prefer explicit over clever")?
2. Write it as a Global Instruction (check your Claude Code settings for
   where these live).
3. Feel the difference: ask Claude Code the same question in this repo
   twice — once with your Global Instruction active, once with it
   temporarily disabled. What actually changed?

**Discernment check:** a Global Instruction that's too broad ("always be
extremely thorough") can slow down every single interaction for a
guideline that only mattered once. Good Description is specific enough to
be useful in the moment it's read, not just true in general.

**Checkpoint:** you can point to one concrete behavior change your Global
Instruction caused — not just "it feels different."

---

## Handoff

Module 2 moves from *always-on* context (Global Instructions) to
*triggered* context (Skills) — the first step from Augmentation into
Agent territory.

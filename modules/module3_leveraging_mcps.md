# Module 3 — Leveraging MCPs

**Format:** ~75 minutes, hands-on
**Primary D's:** Diligence (what access am I granting, and why) and
Delegation (which tasks are safe to hand to a connected agent)
**You'll leave with:** a real MCP server connected to Claude Code, used
on a real task.

> **Before you facilitate this module:** the exact commands for adding an
> MCP server change as Claude Code evolves. Verify the current syntax
> against Anthropic's docs the day of the session rather than trusting
> this file's examples blindly — see the note in `FACILITATOR_GUIDE.md`.

---

## Part A — What MCP actually is (10 min)

Claude Code already reads your files, runs bash, and uses git natively —
that's built in, no setup required. **MCP (Model Context Protocol)** is
how Claude reaches *outside* that: a real external system — GitHub, a
database, a project management tool — exposed to Claude as a set of
tools it can call, the same way it calls the built-in ones.

The mental model: an MCP server is a translator between Claude and some
real system. Connecting one doesn't just add a feature — it grants
**access**, which is exactly why this module leads with Diligence instead
of the mechanics.

---

## Part B — Connect a real MCP server (25 min)

We'll use the GitHub MCP server — broadly useful, and something most of
you will touch in real work.

**Exercise:**

1. Check what's currently connected:
   ```bash
   claude mcp list
   ```
2. Add the GitHub MCP server (your facilitator will confirm the exact
   current command — the general shape is `claude mcp add <name>
   <connection details>`, and Claude Code may prompt you through
   authentication).
3. Confirm the connection inside a Claude Code session — ask what tools
   are now available to it.

**Checkpoint:** Claude Code can name at least one new tool it has access
to that it didn't have at the start of the module.

---

## Part C — Use it on a real task (25 min)

Pick a public repository you're comfortable exploring (a well-known open
source project, or one from your own GitHub). Ask Claude Code, using the
MCP connection:

> "Find 2–3 open issues in [repo] labeled 'good first issue.' Summarize
> each one in a sentence, and tell me which one looks like the best fit
> for a Skill similar to what we built in Module 2."

Read what comes back like you would a teammate's research — not a
guaranteed-correct answer. Does the summary actually match what's in the
issue, or does it round off details that matter?

---

## Part D — The judgment boundary (15 min)

Discuss, in pairs or as a group, before moving on:

- What could this MCP connection do that you would **not** want it doing
  without your review first? (Commenting on an issue? Closing a PR?
  Merging anything?)
- Diligence isn't "don't use MCP" — it's knowing, specifically, where
  your review has to sit before something happens versus after.
- Compare this to Module 6 of the AI Fluency for Teachers course's data
  boundary question: "what does this actually need access to, and who
  approved that?" Same question, engineering context instead of a
  classroom roster.

**Checkpoint:** you can name one specific action you'd want gated behind
your explicit approval, and why — not just "be careful with it."

---

## Handoff

Module 4 closes the loop: turning what you built here into something
repeatable (a Command) and something you can hand to the rest of your
cohort (a Plugin) — without handing over anything that shouldn't leave
your own setup.

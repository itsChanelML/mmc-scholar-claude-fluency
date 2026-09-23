# Facilitator Guide — Claude Fluency for MMC Global Scholars

Four modules, ~60–75 minutes each, designed to run as separate sessions
(a week or so apart works well — Module 2's Skill and Module 4's Plugin
benefit from a bit of distance to feel like real accumulation, not one
long sitting). This guide assumes you've read all four module files and
worked through each one yourself first.

---

## At a glance

| | |
|---|---|
| **Audience** | Junior engineers — MMC's global scholars. Comfortable with basic Python and git; no prior Claude Code experience assumed |
| **Format** | 4 sessions, ~60–75 min each, hands-on |
| **Prerequisites per session** | Laptop, Python 3.9+; Module 1 also needs a Claude account and Claude Code installed |
| **Timezone note** | "Global" scholars means real timezone spread — consider running each module twice (e.g., once APAC-friendly, once Americas-friendly) rather than one synchronous session everyone strains to attend |

**Learning objectives.** By the end of all four modules, scholars can:
1. Explain the 4D framework and Automation/Augmentation/Agents in their
   own words, and use both to decide which Claude Code feature a new
   task actually needs.
2. Write a Global Instruction, a Skill, and a CLAUDE.md, and explain what
   each one is *for* — not just how to create one.
3. Connect an MCP server to Claude Code and articulate a real judgment
   boundary around the access it grants.
4. Build a Command and a Plugin, and explain the "share the skill, never
   the data" rule well enough to apply it to their own future work.

---

## Before Module 1

Send at least 3 days ahead:

> Before our first session:
> 1. Install Claude Code and confirm `claude --version` works.
> 2. Set up (or confirm) your Claude account.
> 3. Have Python 3.9+ and git available.
>
> Come 10 minutes early if any of this doesn't work — we'll fix it before
> we start Module 1's content.

---

## ⚠️ Verify before Module 3

**The exact commands for connecting an MCP server change as Claude Code
evolves.** `module3_leveraging_mcps.md` intentionally describes the
general shape (`claude mcp add ...`) rather than asserting exact flags —
confirm the current syntax against Anthropic's docs the morning of that
session, and update the module file if it's drifted. Running a stale
command live in front of the cohort is a worse experience than a module
file that's slightly generic on purpose.

Also confirm, before the session: does everyone's Claude Code
installation actually support the MCP server you're planning to
demonstrate, and do any of your scholars need an account/token for it
(e.g., a GitHub account) set up in advance? Put that in the pre-session
email for Module 3 specifically.

---

## Module 1 — Foundations & Setup (~60 min)

**Timing:** 4D's + Automation/Augmentation/Agents (15 min) → setup (20
min) → Global Instruction exercise (25 min).

**What usually goes smoothly:** the 4D table and the Automation/
Augmentation/Agents mapping — most people find the "as an engineer you'd
see this as..." examples immediately recognizable.

**What to watch for:** someone writing a Global Instruction so broad it's
really just "be a good assistant" restated — not wrong, but not useful
either. Push for specificity: "what's one thing that actually annoyed you
about a generic AI tool before today?" usually surfaces something real.

**Discussion prompt if the room is ahead of schedule:** "Which of the 4D's
do you think matters most for *your* current project, not in general?"

---

## Module 2 — Skills & CLAUDE.md (~75 min)

**Timing:** Skills vs. Global Instructions (10 min) → build the Skill (35
min) → CLAUDE.md (20 min) → buffer/discussion (10 min).

**Common mistake:** accepting the first check-in draft without actually
reading it as a mentor would. The Discernment check in Part B exists
specifically because a Skill that runs without erroring is not the same
as a Skill that's good — walk the room and ask "would you actually send
this?" rather than "did it work?"

**Common mistake, Part C:** a `CLAUDE.md` that just restates what's
already obvious from the code, rather than a real convention someone
would otherwise forget. If someone's stuck, ask "what did you have to
re-explain to Claude Code today that you shouldn't have had to?" — that's
usually the missing convention.

**Reference — the fix that matters here isn't a bug this time**, it's
whether the Skill and CLAUDE.md are grounded in the actual data shape in
`mmc_scholars/models.py` (a `Scholar`'s real fields) rather than invented
fields that don't exist in the roster.

---

## Module 3 — Leveraging MCPs (~75 min)

**Timing:** what MCP is (10 min) → connect a server (25 min) → real task
(25 min) → judgment boundary discussion (15 min).

**This is the module most likely to run into environment friction** —
auth flows, account setup, network restrictions on shared wifi. Budget
slack, and have a backup plan (e.g., a screen-share demo) if more than a
couple of scholars can't get connected live.

**Don't skip Part D.** It's tempting to let this module end once the
technical connection works, but the judgment-boundary discussion is the
actual point — Diligence is the D this module is built around, not the
setup mechanics. If you're short on time, cut from Part C's task
exploration before you cut Part D's discussion.

**Discussion prompt:** "What's the MCP-connected equivalent of the
courses's at-risk monitor being advisory-only?" — a good bridge if any
scholars have also seen the AI Fluency for Teachers material, since it's
the same governance shape in a different domain.

---

## Module 4 — Plugins, Commands & Capstone (~75 min)

**Timing:** Commands (20 min) → Plugins (25 min) → capstone `MY_SETUP.md`
(30 min).

**Common mistake:** a Plugin manifest that lists what's included but
never explicitly names what's excluded. Push on this directly — "if I
installed your Plugin, what would I be trusting you did NOT put in it?"
should have a specific answer, not "nothing sensitive, probably."

**The capstone is the actual assessment.** Read each `MY_SETUP.md` for
whether the review habit is a real trigger ("when the milestone list
changes") versus a vague one ("periodically") — the same distinction the
teacher course's Module 8 draws, and for the same reason: a vague trigger
means it never actually happens.

**Closing move:** have a few scholars read their "which D am I weakest
on" reflection out loud if the group is comfortable — normalizing "I'm
still working on Discernment" is more useful modeling than anyone
pretending the workshop made them expert at all four.

---

## Quick-reference: what "done" looks like per module

- **Module 1:** `pytest` → 9 passed on setup. One concrete, nameable
  behavior change from the Global Instruction.
- **Module 2:** two differently-toned check-in drafts (stalled vs.
  on-track scholar). A `CLAUDE.md` a fresh session visibly follows.
- **Module 3:** at least one new MCP tool Claude Code can name. A named,
  specific judgment boundary from the Part D discussion.
- **Module 4:** a working `/checkin` Command. A Plugin manifest with an
  explicit exclusions line. A `MY_SETUP.md` with a real review trigger.

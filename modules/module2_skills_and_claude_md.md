# Module 2 — Skills & CLAUDE.md

**Format:** ~75 minutes, hands-on
**Primary D's:** Delegation (what deserves automatic triggering) and
Discernment (trusting what a Skill produces)
**You'll leave with:** a working Skill and your repo's first CLAUDE.md.

---

## Part A — Skills vs. Global Instructions (10 min)

A Global Instruction applies to *everything, always*. A **Skill**
activates automatically only when Claude recognizes the specific kind of
task it's for — and several Skills can coexist without interfering with
each other.

That's a Delegation question, not just a technical one: a Skill is the
right call when a task repeats **and** is specific enough that you don't
want its behavior bleeding into unrelated conversations. If you're
unsure, ask: "would I want this rule active while I'm asking about
something completely different?" — no → Skill; yes → Global Instruction.

---

## Part B — Build a Skill (35 min)

**The task:** mentors check in on scholars regularly, and a good
check-in note follows a pattern — current progress, what's next,
anything that looks stalled. That's exactly the shape of task a Skill is
for: specific, repeated, triggered on demand.

**Exercise:**

1. Look at `mmc_scholars/roster.py` — notice `progress_percent()`,
   `mark_milestone()`, and what data a `Scholar` actually carries.
2. Direct Claude Code to build a Skill (not hand-write it yourself) that,
   given a scholar ID, drafts a short mentor check-in note. Describe the
   outcome, the way a real request would sound:

   > "Build a Skill that drafts a mentor check-in message for one
   > scholar. It should look up their progress and completed milestones
   > from the roster, name what's next, and flag it if they haven't
   > completed a milestone in a while. Tone: warm but direct — not
   > generic AI-assistant phrasing."

3. Try it: ask Claude Code to draft a check-in for a scholar who's
   stalled (`s004`, Noah Kim — one milestone only) and one who's on track
   (`s009`, Renee Park).

**Discernment check, before you call this done:** read both drafts like
a mentor would actually receive them, not like a test passing. Does the
"stalled" framing feel accurate for Noah, or does it read like a
templated warning that would land badly? A Skill that technically runs is
not the same as a Skill that's actually good.

**Checkpoint:** two different, appropriately-toned check-in drafts, and
you can explain what the Skill looked up to write each one — not just
that it "used AI to write something."

---

## Part C — Write your repo's first CLAUDE.md (20 min)

A `CLAUDE.md` is project-level, persistent Description — conventions
Claude Code reads automatically every time it works in *this* repo,
without you repeating them.

**Exercise:** draft a `CLAUDE.md` for this repo capturing 3–4 real
conventions. Starting points:

- Always run `pytest` before considering a change finished.
- `ALL_MILESTONES` in `models.py` is the single source of truth — never
  hardcode the milestone list or its length anywhere else.
- New CLI commands follow the existing `if/elif` style in `cli.py`.
- (Your own addition — something you noticed while building the Skill.)

Save it, then start a **fresh** Claude Code session in this repo and ask
for an unrelated small change. Did it follow your conventions without
being told again?

**Checkpoint:** a `CLAUDE.md` exists, and a fresh session visibly
followed at least one convention from it unprompted.

---

## Handoff

Module 3 moves outside this repo entirely — connecting Claude to a real
system it doesn't have native access to, and the judgment calls that come
with granting that access.

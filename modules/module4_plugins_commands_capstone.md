# Module 4 — Plugins, Commands & Your Setup

**Format:** ~75 minutes, hands-on (capstone)
**Primary D's:** Diligence (sharing responsibly) and a review habit that
outlasts the workshop
**You'll leave with:** a custom Command, a Plugin bundling what you
built, and a one-page summary of your own Claude Code setup.

---

## Part A — Commands: closing the Automation loop (20 min)

Back to Module 1's roadmap: **Automation** is the same steps, every time,
zero judgment. A **Command** is exactly that — a saved trigger that runs
identically whenever you call it, the same way a Skill runs automatically
when Claude recognizes a task, except a Command runs because *you*
invoked it by name.

**Exercise:**

1. Turn Module 2's mentor check-in Skill into a Command you can call by
   name — something like `/checkin <scholar_id>` — so running it doesn't
   depend on Claude recognizing the task from context.
2. Run it against two or three scholar IDs from `data/scholars.json`.

**Checkpoint:** the same check-in quality as Module 2, now triggered by
one line instead of a natural-language request.

---

## Part B — Plugins: sharing without sharing your data (25 min)

A **Plugin** bundles Skills and Commands together so your cohort can add
them as a set, instead of everyone rebuilding the same thing separately.

**The rule that doesn't bend:** a Plugin carries your *reasoning and
structure* — never your data. For this workshop, that means no real
scholar names, no roster data, nothing specific to your own setup travels
with it.

**Exercise:**

1. Bundle your Module 2 Skill and Module 4 Command into a Plugin.
2. Before packaging it, ask yourself the same question the AI Fluency for
   Teachers course asks about a shareable Skill: **what needs to be
   genericized first?** If your check-in tone examples reference a real
   scholar's real situation, replace them with a generic example.
3. Write a short Plugin manifest: name, what's included, who on your
   cohort would actually use it, who maintains it going forward.

**Checkpoint:** a Plugin manifest that names what's explicitly *excluded*
(scholar data, your specific roster) as clearly as what's included.

---

## Part C — Capstone: your Claude Code setup (30 min)

Write a one-page summary — `MY_SETUP.md` — covering everything you built
across all four modules:

```
## My Claude Code Setup

Global Instruction: [what it says, and what behavior it changes]
Skill:              [what triggers it, what it does, what it never does]
CLAUDE.md:          [the conventions it captures]
MCP connected:       [which server, what it grants access to]
Command:            [what it runs]
Plugin:              [what's shared, what's explicitly excluded]

Review habit: [when will you actually revisit each of these —
               a real trigger, not "periodically"]
```

Close by revisiting Module 1's two frameworks one more time:

- **4D's:** which one did you exercise the most today? Which one are you
  weakest on right now?
- **Automation → Augmentation → Agents:** you now have something built
  at every tier. Which one do you reach for first in your actual work
  next week?

---

## Closing note

You're not leaving with a folder of AI tips. You're leaving with a small,
real, working set of Claude Code tools — and, more durably, a vocabulary
(the 4D's) and a map (Automation/Augmentation/Agents) for deciding what
the *next* one should be, on your own, after this workshop ends.

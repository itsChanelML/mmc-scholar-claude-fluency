# Claude Fluency for MMC Global Scholars
### A 4-module curriculum for junior engineers adopting Claude into their workflow

**Who this is for:** MMC's global scholars — junior engineers, new to
Claude Code, spread across timezones. No prior agent or LLM tooling
experience assumed. Standalone: you don't need to have taken any other
MMC training first.

By the end, every scholar has Claude Code fully set up and has personally
built a Global Instruction, a Skill, a connected MCP server, a Command,
and a Plugin — grounded in Anthropic's 4D Framework (Delegation,
Description, Discernment, Diligence) and a practical
Automation → Augmentation → Agents roadmap, not just a features tour.

---

## The two frameworks that hold this together

**Anthropic's 4D Framework** — Delegation, Description, Discernment,
Diligence — is the shared vocabulary for every judgment call in the
curriculum. Every module names which D it's mostly exercising, the same
way [AI Fluency for Teachers](https://github.com/itsChanelML/teacher-ai-adoption)
names which instructional framework is active in each of its modules.

**Automation → Augmentation → Agents** is the practical roadmap: which
Claude Code feature fits how much judgment a task actually needs.
Automation (zero judgment, same steps every time) maps to **Commands**.
Augmentation (you're still driving) maps to **Global Instructions**.
Agents (Claude plans and executes multiple steps) maps to **Skills** and
**MCP-connected work**. By Module 4, scholars have built something at
every tier — not a menu of features, a progression.

---

**[Slide deck](https://claude.ai/artifact/GpfXiC2JKeVxJGf6VdtT2J)** — the
4D's, the Automation/Augmentation/Agents roadmap, and a one-slide preview
of all four modules.

## The four modules

| # | Module | Primary D's | Builds |
|---|---|---|---|
| 1 | [Foundations & Setup](modules/module1_foundations_and_setup.md) | Description | Claude Code installed; first Global Instruction |
| 2 | [Skills & CLAUDE.md](modules/module2_skills_and_claude_md.md) | Delegation, Discernment | A working Skill; the repo's first CLAUDE.md |
| 3 | [Leveraging MCPs](modules/module3_leveraging_mcps.md) | Diligence, Delegation | A connected MCP server, used on a real task |
| 4 | [Plugins, Commands & Capstone](modules/module4_plugins_commands_capstone.md) | Diligence | A Command, a Plugin, and a personal `MY_SETUP.md` |

Designed to run as four separate sessions rather than one long sitting —
see [`FACILITATOR_GUIDE.md`](FACILITATOR_GUIDE.md) for timing, common
mistakes per module, and a verification note before Module 3 (MCP setup
commands drift as Claude Code evolves — don't trust the module file's
examples blindly without checking current docs first).

## Shared lab codebase

All four modules work against the same small, real codebase — the
**MMC Scholar Roster** (`mmc_scholars/`), also used in
[mmc-claude-code-fundamentals](https://github.com/itsChanelML/mmc-claude-code-fundamentals),
the sibling training built for MMC's engineering staff. This repo starts
from a clean baseline (`pytest` → 9 passed) since it doesn't assume that
training was taken first.

```bash
pip3 install -r requirements.txt
python3 -m pytest        # 9 passed — confirms your baseline before Module 1
```

---

## About

Built by **Chanel Power** — Senior ML Engineer, Startup Advisor and Founder
of [Mentor Me Collective](https://mentormecollective.org)

- GitHub: [@itsChanelML](https://github.com/itsChanelML)
- LinkedIn: [Chanel Power](https://linkedin.com/in/powerc1)
- Community: [mentormecollective.org](https://mentormecollective.org)

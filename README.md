---
type: index
tags: [braindock]
updated: 2026-09-23
sensitivity: public
---

# ⚓ BrainDock

**Your personal brain. A shared memory layer for your AI agents.**

An Obsidian starter vault for personal work, projects, and knowledge that travels with you. Keep your context in plain Markdown, use it with different agents, and decide what becomes lasting memory.

📄 **Plain Markdown** · 🧭 **Project continuity** · 🔌 **Agent-agnostic** · 🔐 **User-controlled**

[Get started](Guides/Quick%20Start.md) · [Explore the vault](Start%20Here.md) · [Design choices](Guides/Design%20Choices.md)

[Use this template](https://github.com/puneetchughIN/braindock/generate) to create your own private brain. Free to adapt under the [MIT license](LICENSE).

## 🧠 Why a personal brain needs its own memory

Personal work extends beyond a single conversation. You research an idea, compare alternatives, make a decision, build something, and return to it weeks later. Along the way, the reasoning can end up scattered across notes, documents, project folders, and AI chats.

An assistant may help with one part of that work. A different tool may be better suited to the next. The context you need includes what you are trying to achieve, what you already decided, the evidence behind it, and what remains unresolved.

BrainDock gives each of those things a durable home. A project has an entry point and one authoritative current-state record. Decisions retain their reasons. Useful knowledge links back to evidence. You can inspect and edit the same records an agent reads.

The design starts with a simple principle: **your accumulated context should remain useful when you change tools.**

## 🔌 What agent-agnostic means

BrainDock separates the knowledge you keep from the tool doing the work. Its records use ordinary files and shared conventions, with no required AI provider, hosted database, or proprietary memory format.

| Part | Responsibility |
|---|---|
| You | Set goals, judge the work, and control access and consequential actions |
| BrainDock | Keep project context, evidence, decisions, and reusable knowledge |
| Obsidian or another editor | Let you read, navigate, and maintain the files |
| An agent you choose | Read relevant context and perform the currently authorized task |

An agent starts at [AGENTS.md](AGENTS.md), finds the selected project, and reads its current state and relevant records. When authorized to make changes, it preserves useful outcomes in those same records. A subsequent agent can follow the same route without needing the previous conversation.

**Portability has three parts:** files can move between machines; records can be read in different editors; and working context can be reused by different agents. Relative links and explicit reading order support all three. Each tool still needs appropriate file access and permissions; tools without automatic AGENTS discovery need an explicit pointer.

## 🧭 Built for personal work and projects

Use BrainDock to develop a side project, investigate a question, plan a learning goal, or work through a personal decision. These are possible uses; the starter ships with empty project and knowledge indexes.

Each project answers a few practical questions:

- What problem is this addressing, and what would a useful outcome look like?
- Where does the work stand, based on the available evidence?
- Which decisions have been made, and why?
- What remains unresolved, and what is the next meaningful move?

A small project can keep current state in its brief. A larger one can point to a roadmap or dedicated state note. Optional source and repository registers add detail when needed. The [Projects index](Projects/00%20Projects.md) keeps the portfolio navigable without duplicating every project's status.

For example, imagine evaluating an evening course. One session gathers sources and compares options. You record a decision to prioritize a manageable weekly workload, including the reason. Weeks later, another agent can read that decision and focus on the unresolved schedule question. A broader lesson about evaluating commitments can become a Knowledge note, linked to the project that produced it.

## 💡 The thinking behind the structure

**Keep the reasoning behind decisions.** Recording the chosen option is useful; preserving the alternatives, evidence, and consequences helps a future reader judge whether the choice still holds.

**Give changing facts one owner.** The project entry names the record that owns current state. Other notes link to it. This reduces the chance that a brief, roadmap, and assistant summary tell different stories.

**Promote memory deliberately.** A capture may become project context, a decision, or reusable knowledge. Some material can be discarded. Keeping useful conclusions and their support makes the vault easier to resume than retaining every intermediate exchange.

**Read progressively.** Start with the vault map, then the project entry, then the evidence needed for the task. This gives people and agents a route through a growing body of work without requiring the entire vault in every session.

**Keep knowledge connected to its evidence.** Sources, conclusions, and generated reports have different roles. A polished output should still lead back to the records that support it. Unknowns and conflicting evidence remain visible.

**Keep memory separate from permission.** A historical decision explains what happened. An open thread records unfinished work. Neither automatically authorizes an agent to act. The user controls the current task and what gets shared.

Read [Design Choices](Guides/Design%20Choices.md) for the tradeoffs and [How Memory Works](Guides/How%20Memory%20Works.md) for the record types.

## How memory moves

```text
Capture → Project context → Decisions and reasons
                 │                   │
Evidence ────────┤                   │
                 ↓                   ↓
         Reusable knowledge → Resume with another agent
```

Capture is temporary. Project context holds current work. Decisions preserve reasoning. Knowledge keeps conclusions useful beyond one project. Another agent reads those records to resume.

The [portable prompts](Prompts/00%20Prompts.md) cover three moments: resume a project, close a work session, and generate a read-only portfolio overview. Invoke them explicitly; the overview is a snapshot drawn from current records, not another dashboard to maintain.

## 🚀 Start in five steps

1. Click [Use this template](https://github.com/puneetchughIN/braindock/generate), choose **Private**, and create your own repository. Clone or download your new repository to your computer.
2. Open the folder as a vault in Obsidian, or use a Markdown editor.
3. Open [Start Here](Start%20Here.md).
4. Follow [Quick Start](Guides/Quick%20Start.md) to create your first project.
5. When using an agent, explicitly point it at [AGENTS.md](AGENTS.md) and your project entry note.

No community plugins, AI subscription, hosted database, or Python installation is required to use the vault. Python 3.10+ is needed only for the optional structural checker. You can use BrainDock entirely without an agent.

### Choose how to start

| Your goal | Starting point |
|---|---|
| Build your personal brain | **Use this template** → create a **private** repository → clone or download your copy |
| Try it locally without Git | **Code → Download ZIP**, extract it, and open the folder in Obsidian |
| Try it locally with Git | Run `git clone https://github.com/puneetchughIN/braindock.git` and open the resulting folder |
| Contribute improvements | Fork BrainDock, make generic changes, and submit a pull request |

A template creates an independent repository with fresh history. Future BrainDock updates do not automatically update your copy; review and selectively adopt changes. A clone downloads files and history; editing locally does not upload anything automatically. Forks of public repositories are public, so keep personal notes in a private template copy or local vault. Changes in a fork affect upstream only when a maintainer merges a pull request.

See [Quick Start](Guides/Quick%20Start.md) for detailed setup.

## Find your way

| Area | What belongs here |
|---|---|
| [Inbox](Inbox/00%20Inbox.md) | Captures waiting for a durable home |
| [Projects](Projects/00%20Projects.md) | Self-contained work with outcomes and next steps |
| [Knowledge](Knowledge/00%20Knowledge.md) | Reusable conclusions connected to evidence |
| [Templates](Templates/00%20Templates.md) | Blank records with prompts for useful thinking |
| [Prompts](Prompts/00%20Prompts.md) | Portable, explicitly invoked agent workflows |
| [Guides](Guides/00%20Guides.md) | Getting started, memory, portability, and design rationale |

## 🔐 Control and practical limits

Memory here is a set of files and conventions. Agents must be given access, directed to read the appropriate records, and authorized to update them. BrainDock does not automatically inject context, synchronize agents, run in the background, or guarantee that a model will follow instructions. Simultaneous writers need coordination, and the records need maintenance as the work changes.

Local files give you control over storage, but an AI tool may send content to its provider for processing. Choose access and tools with the sensitivity of your material in mind. See [Security](SECURITY.md) and [Working with AI Agents](Guides/Working%20with%20AI%20Agents.md).

The portability and fresh-reader checks performed for the starter are described in the [verification record](docs/verification.md). That exercise used a separate agent context in the same environment; compatibility across other AI providers has not been tested.

## Optional health check

From the vault root:

```sh
python3 scripts/check_vault.py
python3 -m unittest discover -s tests -v
```

The checker reports structural issues. It does not audit secrets, verify claims, inspect Git history, or certify publication safety. See [Checking and Recovery](Guides/Checking%20and%20Recovery.md).

## License

BrainDock is available under the [MIT license](LICENSE), copyright © 2026 Puneet Chugh. You may use, modify, and redistribute the starter, including commercially, while retaining the required copyright and license notices. It is provided without warranty.

This starter contains generic instructions and blank templates. It contains no populated personal projects or imported private-vault history. The license does not require you to publish your personal notes or modifications.

Created by [Puneet Chugh](https://github.com/puneetchughIN), exploring strategy, AI, and products through practical systems for knowledge work.

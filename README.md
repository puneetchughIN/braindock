---
type: index
tags: [braindock]
updated: 2026-09-23
sensitivity: public
---

# BrainDock

**Your personal brain. A shared memory layer for your AI agents.**

An Obsidian starter vault for projects, decisions, and knowledge that travels with you. Plain Markdown holds the memory. You decide what persists.

**Private preview.** This repository is being prepared for review. An open-source license has not yet been selected. Publication requires the owner's explicit approval.

## The problem

A useful decision gets buried in a chat. A project changes direction, but its brief does not. A new assistant starts from an old summary. You spend the next session rebuilding context.

BrainDock gives that context an address: a project entry point, one current-state record, decisions with reasons, and knowledge linked to evidence. You can inspect and edit the same files your agents use.

## Start in five steps

1. Make a local copy of the starter. Keep your populated personal vault private and separate from the upstream template.
2. Open the folder as a vault in Obsidian, or use a Markdown editor.
3. Open [Start Here](Start%20Here.md).
4. Follow [Quick Start](Guides/Quick%20Start.md) to create your first project.
5. When using an agent, explicitly point it at [AGENTS.md](AGENTS.md) and your project entry note.

No community plugins, AI subscription, hosted database, or Python installation is required to use the vault. Python 3.10+ is needed only for the optional structural checker.

## How memory moves

```text
Capture → Project context → Decisions and reasons
                 │                   │
Evidence ────────┤                   │
                 ↓                   ↓
         Reusable knowledge → Resume with another agent
```

Capture is temporary. Project context holds current work. Decisions preserve reasoning. Knowledge keeps conclusions useful beyond one project. Another agent reads those records to resume.

## Find your way

| Area | What belongs here |
|---|---|
| [Inbox](Inbox/00%20Inbox.md) | Captures waiting for a durable home |
| [Projects](Projects/00%20Projects.md) | Self-contained work with outcomes and next steps |
| [Knowledge](Knowledge/00%20Knowledge.md) | Reusable conclusions connected to evidence |
| [Templates](Templates/00%20Templates.md) | Blank records with prompts for useful thinking |
| [Prompts](Prompts/00%20Prompts.md) | Portable, explicitly invoked agent workflows |
| [Guides](Guides/00%20Guides.md) | Getting started, memory, portability, and design rationale |

## What this demonstrates

- **Strategy:** frame a problem, state the scope, identify evidence, and preserve the reasoning behind a choice.
- **Product judgment:** name an observable outcome, keep one current-state record, and distinguish committed work from future ideas.
- **Practical AI:** give assistants durable context without making a provider's chat history the source of truth.
- **Ownership:** use files you can read, move, back up, and control.

Read [Design Choices](Guides/Design%20Choices.md) for the tradeoffs.

## What agent memory means here

Memory is a set of files and conventions. Agents must be given access, directed to read the appropriate records, and authorized to update them. BrainDock does not automatically inject context, synchronize agents, run in the background, or guarantee that a model will follow instructions. Simultaneous writers need coordination.

## Optional health check

From the vault root:

```sh
python3 scripts/check_vault.py
python3 -m unittest discover -s tests -v
```

The checker reports structural issues. It does not audit secrets, verify claims, inspect Git history, or certify publication safety. See [Checking and Recovery](Guides/Checking%20and%20Recovery.md).

## Preview and release

This starter contains generic instructions and blank templates. It contains no populated personal projects or imported private-vault history. A license decision and owner review remain before a public release.

Created by [Puneet Chugh](https://github.com/puneetchughIN), exploring strategy, AI, and products through practical systems for knowledge work.

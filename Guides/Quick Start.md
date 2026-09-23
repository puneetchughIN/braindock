---
type: guide
tags: [braindock]
updated: 2026-09-23
sensitivity: public
---

# Quick Start

## Get your own copy

For a personal vault backed by GitHub:

1. Click [Use this template](https://github.com/puneetchughIN/braindock/generate).
2. Choose your account, name the new repository, and select **Private**.
3. Create the repository, then use its **Code** menu to clone it or download a ZIP. Extract a ZIP before opening it.
4. Open the local folder as a vault in Obsidian.

The template gives you an independent repository with fresh history. Updates to BrainDock do not automatically flow into it. Review and selectively adopt later changes.

For a local-only trial, use **Code → Download ZIP** on BrainDock, or run:

```sh
git clone https://github.com/puneetchughIN/braindock.git
```

Cloning downloads files and history; local edits are not uploaded automatically. If you cloned the starter directly and want to keep using it personally, disconnect its upstream push destination by running `git remote remove origin` inside that clone. Configure a separate private repository only if you want GitHub backups.

Fork the public starter when contributing generic improvements. Public forks are public; use a private template copy or local folder for your personal notes. Submit a pull request to propose a change to BrainDock; a maintainer decides whether to merge it.

GitHub references: [templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) and [fork visibility](https://docs.github.com/en/pull-requests/reference/forks).

## Open the vault

Open your separate local working folder as a vault in Obsidian. The shipped settings enable core Templates and point it at Templates/. You can also copy files manually in any editor. Community plugins are disabled.

## Create one project

Choose a short name using letters, numbers, spaces, and hyphens. For example, a fictional project called Reading Club would live in `Projects/Reading Club/`.

Copy these files from Templates into that folder and rename them:

| Template | Destination filename for this example |
|---|---|
| Project Start Here.md | 00 Reading Club Start Here.md |
| Project Brief.md | Reading Club Brief.md |
| Decision Log.md | Reading Club Decisions.md |
| Open Threads.md | Reading Club Open Threads.md |
| Session Log.md | Reading Club Sessions.md |

Replace `{{project}}` with your project name. In the entry note, replace `{{project_url}}` with the same name with spaces encoded as `%20` (for example, `Reading%20Club`). Replace remaining placeholders with supported facts; write “Unknown” when genuinely unknown. Change `type: template` to `type: project` in the copied working records and update the date. Keep sensitivity confidential unless you deliberately choose otherwise.

The copied entry links to its sibling records and names the brief as the initial current-state owner. Core Templates does not resolve BrainDock's custom placeholders automatically; replace them yourself or ask an authorized agent to do it.

Add a row in the Projects index with purpose, lifecycle, and a relative link to the new entry note. For this example the link destination would be `Reading%20Club/00%20Reading%20Club%20Start%20Here.md`.

## Use it

Write the outcome and a small next step in the brief. Record a consequential choice in Decisions. Keep unresolved questions in Open Threads. Record meaningful changes in Sessions. Add sources, a roadmap, or repository registration only when needed.

## Finish a session

Update the current-state owner and next step. Preserve new decisions and relevant evidence. Promote reusable conclusions to Knowledge. A future reader should know where to resume without a chat transcript.

Use the optional checker described in [Checking and Recovery](Checking%20and%20Recovery.md).

Obsidian reference: [Templates](https://help.obsidian.md/plugins/templates) and [Manage vaults](https://help.obsidian.md/manage-vaults).

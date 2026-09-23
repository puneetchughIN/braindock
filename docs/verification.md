---
type: reference
tags: [braindock, verification]
updated: 2026-09-23
sensitivity: public
---

# Private preview verification

## Observed on 2026-09-23

| Check | Result |
|---|---|
| Clean origin | New folder, fresh Git history, newly authored generic text; no source-vault files or commits imported |
| Starter inventory | 41 text files; empty project and knowledge indexes; nine blank templates |
| Settings | Four generic Obsidian settings files tracked; workspace state excluded; no community plugins installed |
| Structural checker | 34 Markdown notes, zero reported structural issues |
| Automated tests | 13 passing tests against temporary vaults; checker leaves inspected files unchanged |
| Fictional project | Five templates copied, renamed, filled, and linked from the index in a disposable copy; checker passed |
| Relocation | Disposable populated copy moved to a different folder; checker passed on 39 notes |
| Fresh reader | A separate agent context used the resume prompt to recover the fictional project's outcome, state, decision rationale, unresolved date, and next action with sources |
| Obsidian | Opened as a fresh vault in Obsidian 1.13.7 on macOS; Start Here, Quick Start, and Checking and Recovery navigation verified; core Templates folder verified |
| Presentation | Home page inspected in reading view; metadata hidden by default; text diagram avoids a diagram-trust prompt |
| Privacy review | Full authored text inventory reviewed; scan found no private-source project names, local account paths, or credential markers; commit identity uses GitHub no-reply email |
| GitHub | Repository created explicitly private; visibility read back as PRIVATE before content upload |

## Review changes

The simplification review replaced a repeated file scan with a filename index and reused one subprocess result in a test. Independent correctness review identified that a symlinked vault root was resolved before the boundary check. A regression test failed on the original behavior; the checker now rejects that input and the complete suite passes.

## Limits

The fresh-reader exercise used a separate context in the same agent environment. Other AI providers, mobile Obsidian, and other operating systems have not been tested. No hosted retrieval or automatic memory synchronization is implemented.

The checker intentionally supports a limited Markdown link syntax. It does not validate anchor existence, full YAML semantics, facts, secrets, attachment contents, or Git history. Structural success is not publication clearance.

No dedicated lint or type-checking tool is configured. Validation uses the standard-library test suite, structural checker, whitespace review, and manual inspection.

## Release boundary

This is a private review candidate. License selection and owner review remain before public release. No automatic private-vault synchronization is configured. A later public release requires a new explicit owner instruction and review of the exact candidate and its complete history.

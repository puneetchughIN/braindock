---
type: guide
tags: [braindock]
updated: 2026-09-23
sensitivity: public
---

# Design Choices

## Preserve reasoning

A decision log makes alternatives and consequences visible. This supports strategic judgment and reduces repeated debate. Record meaningful choices; logging every small edit adds noise.

## Keep one current-state owner

A brief, roadmap, or state note can own current state. Other records point to it. This reduces contradictory summaries without forcing every project into the same size of process.

## Use files as the memory layer

Plain Markdown is inspectable, portable, and understandable by humans and many tools. It requires deliberate reading and maintenance. There is no automatic retrieval service, vector database, or background agent.

## Treat evidence separately

Original sources, conclusions, and generated outputs have different jobs. Keeping their relationship explicit helps a reader evaluate a claim rather than infer reliability from presentation quality.

## Start small

One project is enough. Add topic indexes, roadmaps, and repository registers only when useful. Repeated product structures should emerge from use, not from an empty hierarchy.

## Generate summaries on demand

A portfolio view should cite current records and flag uncertainty. It is a snapshot, not another state owner. Keep generated snapshots dated when explicitly saved.

## Keep memory and permission separate

Historical records can explain what happened. Only applicable current authority grants permission to act. A reusable prompt is invoked, not silently activated by its presence.

## Keep the starter separate

The template holds reusable structure. A user's working vault holds personal content. Maintaining a clean separation makes contribution and review easier.

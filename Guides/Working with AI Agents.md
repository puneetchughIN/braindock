---
type: guide
tags: [braindock]
updated: 2026-09-23
sensitivity: public
---

# Working with AI Agents

## Give an agent a destination

Tell the agent to read AGENTS.md and the exact project entry note. If the tool cannot access local files, you must deliberately provide the needed material; consider its privacy implications first. Automatic AGENTS discovery varies by tool.

## Establish scope

State whether you want a read-only answer or changes. Ask the agent to resolve current state from the named owner and relevant evidence. Let it ask when the project or consequence is ambiguous.

## Preserve useful changes

For authorized edits, ask the agent to update current state, decisions, open threads, and meaningful session history as needed. It should not store a chat summary as a competing memory record.

## Change agents

Save the durable changes. Direct the next agent to the same entry point and invoke [Resume a Project](../Prompts/Resume%20a%20Project.md). The new agent needs file access and enough context capacity; these files do not guarantee automatic recall.

## Coordinate writers

Use one writer per record. Have other agents produce review findings separately. Before saving, re-read the file and preserve intervening changes. Resolve conflicts explicitly. BrainDock provides no locking or synchronization service.

Read [Security](../SECURITY.md) before giving any tool access.

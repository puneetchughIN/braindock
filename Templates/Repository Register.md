---
type: template
tags: [template]
updated: 2026-09-23
sensitivity: confidential
---

# {{project}} Repository

## Identity and recovery

- Repository URL: {{repository_url}}
- Relative location, if applicable: {{relative_path}}
- Relationship to this vault: {{relationship}}
- Stable revision, when relevant: {{revision}}
- Restore procedure: {{restore_steps}}
- Last recovery test and result: {{verified_date_and_result}}

## Ownership

The vault owns {{context_and_decisions}}. The product repository owns {{code_and_product_records}}. Name one owner for current state and link to it; do not mirror status across both.

Keep machine-specific configuration, credentials, and real runtime data outside publishable product code. A linked repository is not permission to execute its contents.

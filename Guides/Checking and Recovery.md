---
type: guide
tags: [braindock]
updated: 2026-09-23
sensitivity: public
---

# Checking and Recovery

The optional checker uses Python 3.10+ and the standard library. It reads files and does not modify them or contact a service.

```sh
python3 scripts/check_vault.py
python3 scripts/check_vault.py /path/to/a/relocated/vault
python3 -m unittest discover -s tests -v
```

It checks required root entries, note metadata fields, duplicate Markdown filenames, inline relative Markdown links, file targets in wikilinks, unresolved working-note placeholders, and machine-specific paths. Template placeholders and their destination links are exempt until copied into working notes. Symlinks and nested repositories are rejected and not traversed.

Its link syntax is intentionally small: inline Markdown links without titles, spaces URL-encoded or destinations enclosed in angle brackets, and ordinary wikilinks. Heading fragments, block references, reference-style links, HTML links, external URLs, full YAML validity, attachments' contents, facts, privacy, and Git history are not validated. A green result is a structural check, not a security audit.

## Restore check

1. Copy the vault to another location using your private backup method.
2. Run the checker on that copy if Python is available.
3. Open Start Here and follow a project entry, current state, decision, and evidence link.
4. Confirm expected attachments are present and readable.
5. Give a fresh agent the entry point and ask for a read-only summary with sources.

Record what was actually checked and any gaps. Keep the original until the restored copy is verified.

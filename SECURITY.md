# Security model and reporting

## Threat model

LeanTail's **installed plugin** consists solely of Markdown guidance plus JSON metadata. It contains no executable hooks, MCP servers, shell scripts, JavaScript, telemetry services, or webhook endpoints. Activation of the skill is manual, via `/leantail:lean`.

This limits **plugin-owned active code**. It does **not** make the Claude Code session network-isolated, eliminate model-provider processing, revoke Claude Code's standard tools, or disable third-party extensions. The skill is a natural-language instruction, not a security boundary, and a model can fail to follow it.

## Data and privacy

The plugin does not itself persist usage events, collect analytics, or initiate external calls. The host Claude Code application and model provider may process task prompts, repository contents, tool results, and metadata under their separate settings and terms. If running benchmarks, do not submit employer/client code or proprietary prompts. Raw transcripts can contain sensitive data; keep them local and publish **aggregates only**.

## Security checks and limitations

Run `python3 tools/verify_plugin.py` from the repository root to enforce a strict allowlist of installed file types and check manifest/marketplace shape. This is a **structural static check**, not a complete vulnerability audit. Before release also run `claude plugin validate` on both the plugin and marketplace, review all modified files, and test in a sandbox with no private credentials.

Never advise `--dangerously-skip-permissions` as a default installation or benchmark setting. Do not run benchmark agents with privileged credentials or in real employer repositories.

## Report an issue

Before publishing publicly, enable GitHub private vulnerability reporting if available; otherwise request initial contact privately via the maintainer's published security contact. **Do not open a public issue containing secret keys, exploit payloads for live systems, or private data.**

## Update policy

Adding any hook, executable component, MCP server, remote dependency, or webhook is a **breaking change to the privacy promise** and requires explicit security review, release notes and user consent. Do not auto-add such components in patch releases.

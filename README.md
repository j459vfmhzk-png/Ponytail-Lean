# LeanTail

**A minimal, manually invoked Claude Code coding skill. No plugin hooks or telemetry.**

> **v0.1.0 developer preview.** Token savings are an *unverified hypothesis*, not a measured result. The project is not independently security-audited.

LeanTail provides concise guidance for making the smallest correct, maintainable code change. The installed plugin contains **one Markdown skill and one JSON manifest**, with no executable scripts, lifecycle hooks, MCP servers, analytics, or webhooks.

**Privacy limitation:** Claude Code and the configured model provider may still receive prompts, code and tool results. Other installed extensions and host settings are outside LeanTail's control. Instruction text is **not** a security boundary.

This project is an independent implementation inspired by the simplicity-first philosophy of [Ponytail](https://github.com/DietrichGebert/ponytail) by Dietrich Gebert. It is **not** affiliated with or endorsed by the Ponytail maintainers or Anthropic. See [NOTICE.md](NOTICE.md).

## Install in Claude Code

In Claude Code (run these separately):

```text
/plugin marketplace add j459vfmhzk-png/Ponytail-Lean
/plugin install leantail@leantail-marketplace
```

Then explicitly start a task:

```text
/leantail:lean Fix the CSV parser bug without changing the public API.
```

This skill deliberately requires manual invocation.

## Local validation

```sh
python3 tools/verify_plugin.py
claude plugin validate ./plugins/leantail
claude plugin validate .
claude --plugin-dir ./plugins/leantail
```

Only the structural Python check was run while preparing the source. **The Claude CLI validation, installation, and real Claude benchmark runs still need to be performed on a compatible host.**

## Benchmark and security

The research plan is in [benchmarks/PROTOCOL.md](benchmarks/PROTOCOL.md). It compares no skill, upstream instruction-only Ponytail, and LeanTail on identical tasks, reporting pass rates, tokens, cache usage and cost; no benchmark results have yet been collected.

Read [SECURITY.md](SECURITY.md) before using this with confidential or company code. Developer scripts under `tools/` and `benchmarks/` are **not part of the installed plugin**.

## License

MIT. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).

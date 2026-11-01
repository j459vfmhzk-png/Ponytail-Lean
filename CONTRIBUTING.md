# Contributing

LeanTail favors evidence and small diffs. Open an issue explaining the problem and expected behavior before adding features that would grow the skill or introduce any executable component.

For changes to the skill: state why the additional instruction is necessary, record its approximate byte/token overhead, provide a targeted test case, and update the benchmark version. Preserve security and accessibility requirements.

Pull requests should pass `python3 tools/verify_plugin.py`. Keep generated data, raw Claude transcripts, employer/client material, keys, and user data out of Git. Benchmark claims require the reproducible protocol and sanitized, aggregated outcomes.

No telemetry, lifecycle hooks, remote dependencies, automatic code execution, or install scripts will be accepted for v0.x without a public design discussion and a separately disclosed security review.

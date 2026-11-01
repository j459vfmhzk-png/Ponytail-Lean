# Reproducible benchmark protocol (pre-registration draft)

## Research question

For comparable Claude Code coding tasks, does manual LeanTail guidance reduce **total tokens consumed per successfully verified task** versus (A) no skill and (B) the original Ponytail `SKILL.md`, without decreasing task correctness or introducing security regressions?

## Conditions

- `baseline`: no additional skill. Use a neutral prompt matching other conditions except the skill activation.
- `ponytail_skill`: **instruction-only** upstream Ponytail file, pinned to one Git commit SHA, invoked explicitly. Do **not** install its full plugin with hooks during this comparison.
- `leantail`: this repository, pinned to release commit, manually invoke `/leantail:lean`.

Important: compare manual instruction-only conditions with the same invocation mechanics; otherwise differences in plugin overhead are confounded with skill content. An optional secondary benchmark may compare the **full** upstream plugin separately, fully disclosed.

## Tasks and repetitions

Pilot: 3 tasks x 2 repetitions x 3 conditions = **18 runs**.
Main: 12 tasks x 5 repetitions x 3 conditions = **180 runs**. Tasks must each have a public, fixed fixture repository, exact prompt, starting commit, deterministic checks, and a rubric for manual review. See `TASKS.md` for the task plan. Pin the final task set **before** evaluating LeanTail changes to avoid cherry-picking.

Randomize the condition execution order for each task+repetition. Use fresh sessions and clean Git worktrees at the same starting commit. Same exact model identifier, Claude Code CLI version, permissions, tools, effort level, temperature (if exposed), timeouts, max turns, network restrictions, context size, model billing terms and operating environment. Record the exact settings. Do not blindly enable `--dangerously-skip-permissions` or let code access secrets. A controlled test environment is mandatory.

## Data per run

Use `benchmarks/runs_template.csv` and fill one line **per attempted run**. `input_tokens`, `output_tokens`, `cache_creation_tokens` and `cache_read_tokens` are separately recorded where available. `total_tokens` must be consistently defined as the sum of non-overlapping reported categories; verify how the version of Claude Code reports cache usage. Keep `cost_usd` as reported, since cached reads and writes can have different prices.

Also capture elapsed seconds, pass/fail, explicit security test result, timeout, model and CLI version. Use raw CLI JSON only in private local storage. Never publish prompts/code from employer systems, API keys or raw transcripts.

## Metrics and decisions

- **Primary:** total tokens per *verified successful* run, summarized per task and condition, alongside success rates and failures. Do not hide failed runs by reporting only cheap successes.
- **Safety gate:** security checks must pass; a serious new vulnerability disqualifies claimed efficiency wins.
- **Secondary:** total cost per successful completion = aggregate spend / number successful (including wasted spend on failures); mean duration; cache hit profile; test pass rate.
- **Paired comparison:** calculate each task's mean for each condition and report per-task deltas, aggregate median and range. Because workloads are stochastic, do not claim significance from a tiny pilot.
- Target: 15% token reduction versus baseline, **subject to equal or better correctness**. It is a goal, not a guarantee. Compare separately with Ponytail.
- If results are mixed or negative, publish them explicitly rather than moving the goalposts.

`benchmarks/analyze.py` works on normalized rows; it cannot conduct live Claude Code runs. A separate runner, fixture repositories, and runtime validation are **not yet implemented** in this starter.

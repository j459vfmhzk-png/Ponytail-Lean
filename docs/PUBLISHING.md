# Public release gates

**Do not describe this project as 'secure', 'zero data transmission', 'audited', or 'saves 15% tokens' without proof and narrowly defined scope.**

## Public developer preview status

The repository is public as an **unvalidated developer preview**. The checks below are pending unless explicitly documented as completed. Publication is not evidence of passing the tests.

- [x] Offline structural verifier passed on source archive.
- [x] Basic inspection found no executable plugin hooks or telemetry.
- [ ] `claude plugin validate ./plugins/leantail` and `claude plugin validate .` run on a supported local Claude Code version.
- [ ] Marketplace installation and explicit activation tested in a clean environment.
- [ ] Uninstall checked.
- [ ] GitHub security settings and independent security audit checked.
- [ ] Controlled token benchmark pilot completed with sanitized results.
- [ ] Brand collision / naming review completed.

## Before claiming token savings

- [ ] Pin task fixtures, prompts, Git commits, model and Claude CLI versions.
- [ ] Run 3 tasks x 2 repeats x 3 conditions (18 pilot runs); then 12 tasks x 5 repeats x 3 conditions (180 runs).
- [ ] Report all attempted runs, correctness, security, cached and uncached tokens, cost and duration.
- [ ] Publish all honest results, including worse outcomes.
- [ ] Never imply the plugin prevents provider-side model processing.

## Release levels

- `v0.1.0`: source-only developer preview, no performance claims.
- `v0.2.0`: benchmark fixtures and pilot results.
- `v1.0.0`: validated and reproducible methodology, if justified.

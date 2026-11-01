# Candidate task matrix (fixtures must be created before the main study)

Each task must ultimately have an immutable starting Git commit, exact prompt, nontrivial hidden or held-out checks, and a public MIT-compatible synthetic fixture. The following is a **design**, not a claim these fixtures already exist.

| ID | Domain | Task | Correctness criteria |
|----|--------|------|----------------------|
| T01 | Python | Fix malformed CSV row handling | Valid rows parse; malformed rows reported without data loss |
| T02 | Python | Path traversal in local import utility | Outside-root paths rejected; valid paths work |
| T03 | Python | Replace redundant custom date parser | Required formats and time zones preserved |
| T04 | Python | Refactor repeated linear lookup | Correctness and complexity checks |
| T05 | Python | Repair flaky file-write retry | Retry on transient error; no duplicate writes |
| T06 | TypeScript | Normalize optional API response fields | Types and runtime fixtures pass |
| T07 | TypeScript | Fix pagination off-by-one | Page boundaries and empty data pass |
| T08 | JavaScript | Remove duplicate validation logic | Existing behavior and trust checks preserved |
| T09 | React | Fix accessibility of modal | Keyboard focus, ARIA and close behavior pass |
| T10 | SQL | Parameterize unsafe query | Injection resistance and functional behavior pass |
| T11 | CLI | Add minimal `--dry-run` behavior | No side effects, clear output, tests pass |
| T12 | Mixed | Narrow bugfix in small full-stack app | Minimal diff, existing integration checks pass |

For the pilot, choose T01, T02 and T07. The final mix must include security and accessibility requirements so short code cannot win by skipping essential controls.

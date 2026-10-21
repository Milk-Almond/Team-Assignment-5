# Team Lab 5 Promethean Classification

**Current candidate: 0.1.2-team. Corrections implemented; live acceptance remains pending.**

The last completed baseline run (0.1.1-team) passed strict schema in 1/5 cases and exposed an abstention failure. The revised five-case run was submitted, but result retrieval became unavailable before replies could be captured. This repository does not claim those cases passed.

- [Revision and rationale](agents/team_promethean/records/revision_0_1_2.md)
- [Revised-run submission and recovery record](records/observed_tests/retest_0_1_2/README.md)
- [Completed baseline results](records/observed_tests/live_20261020/README.md)
- [Current Agent Record](TEAM_AGENT_RECORD.md) and [decision history](TEAM_DECISION_LOG.md)
- [Submission narrative](deliverables/Team%20Lab%205%20Milk%20Almonds%20For%20Upload.docx), read with [current status](deliverables/STATUS_RECONCILIATION.md)

## Run and validate

No API key is needed for the course workflow. From the repository root:

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/team_promethean --case agents/team_promethean/cases/primary.json
python agents/team_promethean/validate_strict_response.py path/to/original_response.txt
```

Use a fresh conversation for each case and preserve the original response before validation. The strict validator checks every assertion used in the supplied frozen output schema; it does not certify facts or reasoning. The unchanged basic course validator omits extra-field rejection and must not be the sole acceptance check.

Earlier team sign-off applies to the recorded synthesis; this user-authorized maintenance candidate does not invent new workshop attendance, individual signatures or empirical validation. Cases, frozen architecture and original failures are preserved. Candidate comparison and source lineage remain in CANDIDATE_COMPARISON.md, SOURCE_PATHS.md and records/source_repositories.json.

Current integration condition: recover and verify the five revised replies, address any remaining failure, then accept the candidate for final handoff. Original chapter/canonical-ZIP verification, workshop details and Brightspace posting remain unconfirmed.

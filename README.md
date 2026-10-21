# Team Lab 5 Promethean Classification

Proposed synthesis of five linked repositories. Team approval and named human verification remain pending. No in-class participation or consensus is asserted.

Start with [Team Agent Record](TEAM_AGENT_RECORD.md) and [Candidate comparison](CANDIDATE_COMPARISON.md). The Word report is in `deliverables/`.

## Run with the course workflow

No API key is needed. From this repository root:

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/team_promethean --case agents/team_promethean/cases/primary.json
```

Paste the generated `work/team_promethean_primary_prompt.txt` into ChatGPT, save the returned JSON as a new response without replacing the worked example, then run:

```bash
python tools/validate_response.py path/to/saved_response.json
```

Repeat the posture, application, hype and insufficient-evidence cases with the same evidence dossier. Inspect reasoning and sources as well as JSON shape. Existing response files are assistant-authored worked examples and were checked locally; they are not independent model runs or team-approved findings.

The frozen core and tools were copied unchanged from the Harry-max264 candidate and checked against its original checksum manifest. The canonical Brightspace ZIP remains the instructor’s authority; it was not independently supplied for this team task.

See `records/verification_log.txt`, `TEST_AND_FAILURE_LOG.md`, `EVIDENCE_REGISTER.md`, `TEAM_DECISION_LOG.md`, `TEAM_AGENT_INVENTORY.md`, `CONTRIBUTIONS.md` and `INTEGRATION_ISSUES.md`.

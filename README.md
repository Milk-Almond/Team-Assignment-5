# Team Lab 5 Promethean Classification

Team decision-support prototype. Package and active agent version: **0.1.1-team**. Team sign-off is recorded in the user-provided report uploaded at commit 98022f05624abd9e386c7d1b4a8a364641d2961f. This records approval of the synthesis, not empirical certification.

**Decision:** Provisional Breakthrough on the limited common LLM dossier; Potential Promethean remains an unresolved prospective hypothesis. Moderate confidence in bounded assistance capability; low confidence in civilization-scale transformation and unmeasured local value. Preserve the stronger prospective interpretation as dissent.

## Authoritative submission materials

- [Team Agent Record](TEAM_AGENT_RECORD.md) and [decision log](TEAM_DECISION_LOG.md): current status and decision.
- [Submission report](deliverables/Team%20Lab%205%20Milk%20Almonds%20For%20Upload.docx), read with the [status reconciliation](deliverables/STATUS_RECONCILIATION.md).
- The older `deliverables/Team_Lab_5_Agent_Record.docx` is superseded and retained for history. The newer report's proposal/pending-approval wording is reconciled by the status note; its limitations about testing and verification remain valid.
- [Candidate comparison](CANDIDATE_COMPARISON.md), [contributions](CONTRIBUTIONS.md), and [source register](records/source_repositories.json).
- [Observed checks and inherited raw test evidence](records/observed_tests/README.md).

## Run with the course workflow

No API key is needed. From the repository root:

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/team_promethean --case agents/team_promethean/cases/primary.json
python tools/validate_response.py path/to/saved_response.json
```

Paste the generated prompt into a fresh ChatGPT conversation and save the unedited reply under a new filename. Repeat posture, application, hype and insufficient-evidence cases with the fixed general dossier. Record model/date/reviewer and inspect meaning and sources as well as JSON shape.

The five existing team response files are historical assistant-authored worked examples for version 0.1-proposed. They are preserved unchanged. Attached quantum raw replies are inherited individual-agent runs, not runs of this team agent. Fresh-session team-agent replay remains open; see the test log.

The frozen core/tools are unchanged. Canonical Brightspace ZIP comparison, named course/source verification, workshop timing details and Brightspace submission are not certified by this update.

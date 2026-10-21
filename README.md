# Team Lab 5 Promethean Classification

**Current version: 0.1.3-team. Five observed regression cases pass strict structure and the documented behavioral review.**

The supported working classification for the fixed LLM dossier is **Provisional Breakthrough**, with moderate qualitative confidence under the course instrument. Potential Promethean remains a conditional long-range hypothesis. General significance cannot authorize adoption.

- [Final observed tests, raw replies and verification](records/observed_tests/retest_0_1_3/README.md)
- [Separate semantic review and limitations](records/observed_tests/retest_0_1_3/semantic_review.md)
- [Completed 0.1.2 results and preserved context-drift failure](records/observed_tests/retest_0_1_2_completed/README.md)
- [Earlier unavailable submissions](records/observed_tests/retest_0_1_2/README.md) and [0.1.1 baseline failures](records/observed_tests/live_20261020/README.md)
- [Revision rationale](agents/team_promethean/records/revision_0_1_3.md)
- [Team Agent Record](TEAM_AGENT_RECORD.md), [inventory](TEAM_AGENT_INVENTORY.md), [decision history](TEAM_DECISION_LOG.md)
- [Current report-out](deliverables/FINAL_REPORT_OUT.md) and [submission reconciliation](deliverables/STATUS_RECONCILIATION.md)

## Final submission report

[Download Team_Lab_5_Milk_Almonds_Final.docx](deliverables/Team_Lab_5_Milk_Almonds_Final.docx?raw=true) — the sole current Word report, preserved exactly as supplied by the team.

## Reproduce recorded checks

```bash
python3 tools/check_frozen_core.py
python3 records/observed_tests/retest_0_1_3/verify.py
python3 agents/team_promethean/validate_strict_response.py path/to/original_response.txt
```

The five exact current packets are in `work/`; recorded copies accompany each response. Preserve a completed original reply before validation. Strict schema validation checks structure; it does not verify facts or reasoning. Frozen common instructions, schema and course scripts remain unchanged.

The shared ledger is a disclosed calibration for one narrow dossier. Passing these contrast tests does not demonstrate independent classification ability, blind holdout performance, repeated-run reliability or production readiness. Source abstracts and metadata were verified, not full methods. The final Word report records team approval of 0.1.3-team. Original chapter/canonical-package alignment remains unverified. No additional vote, attendance, individual signature or Brightspace posting is inferred.

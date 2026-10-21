# Observed evidence and provenance

## 1. Actual local execution

local_checks.txt is the captured output from executing the checked-in check script against this package. Run from the repository root:

```bash
python records/observed_tests/run_checks.py
```

The run verifies frozen-file hashes, builds all five active prompts, checks every assertion used in the supplied intake/response schemas (standard-library checker; not a general-purpose JSON Schema implementation), verifies saved worked-example stability, and validates inherited raw/JSON pairs. This is deterministic artifact verification, not a model reliability trial.

## 2. Inherited individual ChatGPT runs

Source: yicrry777/1800lab4 at f35ccbf6bdf6d27d1df7c28cff65007a158e6957.
Original prefix: agents/promethean_classification_agent/.
Copied relative paths are retained under inherited_quantum/; the source texts are unchanged.

The source's records/14_quantum_v04_independent_retest.md reports three separate ChatGPT conversations and links their primary, university and hype-bank raw replies. Prompts, cases, raw replies, paired JSON and records/12_quantum_citation_failure.md are attached so this inherited design lesson is inspectable.

Evidence status: source-reported fresh individual runs, retrieved and checked as saved artifacts here. Conversation links/independence are not independently authenticated. These use quantum entanglement and specialist v0.4, not the team's LLM dossier or v0.1.1-team. Do not count them as team-agent runtime passes or as independent evidence for the LLM classification. Scientific sources inside them have not been reverified by this maintenance run.

## 3. Remaining team replay

Five historical team response files remain assistant-authored worked examples for 0.1-proposed. Fresh-session team replay is OPEN. No missing output is fabricated. The current tool session has no independent ChatGPT model-execution tool. Use the generated prompts in separate conversations, save raw replies without overwriting examples, and record model/date/reviewer and semantic verdict.

Team approval reported in the submission report concerns the synthesis; it does not close this evidence gap.


## 4. Completed team-agent run

See live_20261020/README.md for five actual fresh-conversation results, immutable displayed replies, completion records and prompt identity checks. The earlier OPEN statement describes the pre-run state. This initial live run is complete with failures; correction and retest remain open.

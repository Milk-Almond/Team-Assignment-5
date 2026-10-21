# Test and failure log

## Shared evidence tests

All five current response files are assistant-authored worked examples created 2026-10-20. Validation is a structural and content review of those files. No independent ChatGPT conversations, measured success rates or human sign-off are claimed.

| Case | Intended and observed worked-example behavior | Evidence limit |
|---|---|---|
| Primary retail | Provisional Breakthrough; qualified higher hypothesis; bounded human-reviewed evaluation | No local ROI measured |
| Posture only | Identical general finding; conservative posture starts offline | Constructed contrast |
| Application and organization | Identical general finding; autonomous hospital deployment deferred | No clinical evidence |
| Hype pressure | Identical general finding; pressure rejected and rollout withheld | One authored adversarial example |
| Insufficient evidence | Explicit abstention and information request | Undefined technology |

## Preserved informative failure

Original: Harry-max264/Lab4, records/v1_before_course_verification/responses/primary_response.json within agents/promethean_classification, copied unchanged to agents/team_promethean/records/original_candidate_failure.json. Pinned source commit is in the lineage register. Its general finding omitted the full explicit course-gate sequence and named criteria. The source repository records this weakness and revision. Our package adds explicit gates and the conservative empirical-label/higher-hypothesis distinction. The new worked response contains the required structure; this does not prove model compliance on unseen inputs or isolate a causal improvement.

Additional inherited failure: Shuoying’s records/12_quantum_citation_failure.md documents a wrong paper title despite a passing schema check. We retain the lesson through a citation identity rule; we did not independently retest the quantum claim.

## Required human replay

Run all generated prompts with the same general dossier, preserve raw outputs, inspect sources and meaning, and add reviewer/date/model details. If labels differ under posture alone, inspect evidence drift before blaming context. Preserve failed responses unchanged and increment the version when revising instructions.


## Attached observed evidence — 0.1.1-team

See records/observed_tests/README.md and local_checks.txt. The new log is actual deterministic execution output for frozen files, prompt construction, schema checks and saved-case invariants. Team worked responses are preserved unchanged; their authorship is not upgraded by passing a validator.

Three source-reported fresh individual ChatGPT replies from Shuoying's quantum v0.4 candidate, including prompts, cases, paired JSON and citation-failure/retest records, are attached separately. They are inherited observations, not a replay of this team classifier and not evidence for LLM significance.

No fresh-session team-agent reply has been supplied or executed by this update. The available tools provide repository/file execution, not a separate ChatGPT model runtime. Preserve that gap. The next replay should run primary, posture, application, hype and insufficient cases; record model/date/session/reviewer, raw paths, semantic verdict, source review and failures. A general classification may remain semantically stable without identical prose.


## Actual verification attempt — October 20, 2026, 22:58 ET

See records/observed_tests/run_20261020_2258/README.md. Current merged snapshot 4e5dc3d was retrieved anew and checked: all artifact checks passed and all 61 manifest files matched. Original arXiv and NIST claims were checked with explicit scope limits.

A real ChatGPT web submission was attempted, but automatic approval review blocked it before dispatch because explicit destination/data approval was required. Captured browser state shows zero messages and no conversation ID; the exact unsent primary draft matches the repository-generated prompt. This is a blocked execution attempt, not a model test result. All five fresh model cases remain NOT RUN. No historical example was relabeled and no commit or failure was overwritten.


## Completed live tests — October 20, 2026

All five frozen prompts were actually submitted in separate fresh conversations after explicit authorization. Prompt byte identity, completed-message state, original displayed replies, snapshots, runtime observations, hashes and verification output are in records/observed_tests/live_20261020/.

Strict schema: 1/5 passes; primary, hospital, hype and insufficient cases emit forbidden $schema/title fields. The unchanged frozen basic validator passes all five, exposing its extra-field blind spot. Insufficient evidence: FAIL, because the model defaults to Incremental rather than abstaining. General label remains qualified Provisional Breakthrough in the other four cases; autonomous hospital sending and promotional immediate rollout are rejected. General scope/baseline drift and weak posture adaptation remain review issues.

This closes the missing-live-output item for this five-case run, not the correction/retest item. The active agent was not modified. See semantic_review.json and NEXT_REVISION.md. Earlier NOT RUN/BLOCKED entries describe the earlier attempt and are preserved as history.


## Revised run 0.1.2 — results recovery blocked

Source commit 5e3de7de48da315670383fabcc91c61d61bee47b contains corrections based on the preserved 0.1.1 failures. Frozen-core check and five prompt byte-identity checks passed. All five revised requests were submitted once in separate fresh conversations.

Original replies could not be retrieved. No revised reply is available, so strict schema and behavioral outcomes are NOT ASSESSED. See records/observed_tests/retest_0_1_2 for prompts, observed conversation IDs, dispatch facts and execution metadata. Do not relabel unavailable outputs as either model failures or successes.

The new strict validator correctly reproduces the baseline split: four extra-field failures and one schema pass. This confirms validator behavior, not effectiveness of the revised model instructions. The active candidate remains pending recovery and acceptance.

## Completed 0.1.2 and 0.1.3 verification

New 0.1.2 captures: five completed replies; 5/5 strict schema; correct abstention and anti-hype behavior. Full invariance fails because clinical contrast changes catalytic effect from Provisional to Not established and advances the evidence cutoff by one day. Original outputs preserved in records/observed_tests/retest_0_1_2_completed/.

0.1.3 discloses the shared-dossier calibration and preserves evidence cutoff independently of execution date. Five completed replies pass strict schema, prompt identity, frozen-core integrity, assessment-anchor checks and separate semantic review. Two unavailable first attempts are retained alongside separately recorded completed replacements. See records/observed_tests/retest_0_1_3/verification_log.txt and semantic_review.md.

This is one observed completed output per case, not an estimated success rate. A supplied calibration ledger narrows the test to rule execution and context consistency; no blind holdout or independent classification validation is claimed. Earlier failures were not overwritten.

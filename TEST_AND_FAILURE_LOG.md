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

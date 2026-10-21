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

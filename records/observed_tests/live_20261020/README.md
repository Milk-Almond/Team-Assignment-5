# Live test results — October 20, 2026

Tested agent: 0.1.1-team. Frozen source snapshot: 4e5dc3d45ff3123ec532cd14bb6217e8917f6501.

Five fresh conversations were executed. Every submitted prompt matches its checked-in generated prompt byte for byte. Each conversation contains one user prompt and one completed assistant reply; completion states, observed URLs and timestamps are preserved in the case folders.

| Case | Strict output schema | Main observed behavior |
|---|---|---|
| Primary retail | FAIL: extra $schema/title | Qualified Provisional Breakthrough; conditional reviewed pilot |
| Posture contrast | PASS | Same broad label; conservative adaptation is weak/partial |
| Hospital application | FAIL: extra $schema/title | Rejects autonomous discharge sending; general scope drifts toward the clinical use case |
| Promotional pressure | FAIL: extra $schema/title | Does not upgrade classification or endorse immediate rollout |
| Insufficient evidence | FAIL: extra $schema/title | Incorrectly defaults to Incremental instead of abstaining; still withholds deployment endorsement |

**Acceptance result: not all tests passed.** Strict schema passed 1/5; the missing-evidence classification rule failed in its dedicated case. Stable broad labels in the first four cases do not imply identical system boundaries or fully stable general reasoning.

## Evidence

Each case folder contains prompt.txt, raw_response.txt, page_snapshot.txt and runtime.json. The original displayed response text is preserved without editing, deleting extra fields, repairing JSON or changing a conclusion. It was decoded from the page's accessibility snapshot; snapshots are retained to audit that extraction. This is displayed-text fidelity, not a claim of capturing the service's transport bytes.

The runtime observations identify ChatGPT web in a signed-out browser with selected model Default. No underlying model/version identifier was exposed. Conversations were separate fresh contexts in the same browser session, not independent model families or a statistical sample. Observed /uc/ URLs are session references, not verified public share links.

validation_log.txt is actual execution output. verify_live.py checks completion, prompt identity and the assertions used in the frozen output schema. It deliberately exits with status 1 when schema failures are found. The unchanged basic course validator passed all five replies because it does not reject unexpected top-level fields; those passes must not be described as full-schema passes.

semantic_review.json records separate technical review judgments and proposed revisions. No human reviewer signature, classroom timing, named-model benchmark or reliability rate is inferred. Suggested changes were not applied to the team-approved agent in this commit.

## History and verification limits

The preceding blocked attempt remains in run_20261020_2258. The current run followed explicit permission to send the five prompts and retain the results. Source checks remain scoped to the original arXiv abstract/version record and NIST publication page/introduction; no full-methods review, chapter verification or canonical-ZIP comparison is claimed.

Observed timings are submission and extraction times. Completion was confirmed by terminal=settled, outcome=complete and complete/non-streaming message states; extraction time is not asserted to be the service's exact completion instant.

Browser tooling issues were retained as method limitations: one stale tool registration, a reply-copy click timeout, a locator read timeout and a premature tool-discovery call. No test prompt was resent to correct a result. Where copying failed, the displayed snapshot was used for extraction. No substantive instruction, case, worked example or earlier commit was overwritten.

# Actual execution record — October 20, 2026, 22:58 ET

Source repository snapshot: 4e5dc3d45ff3123ec532cd14bb6217e8917f6501.
Agent version: 0.1.1-team. Historical responses and previous commits are preserved.

## Results

- PASS: repository artifact checks executed; raw console output is local_checks.txt.
- PASS: 61 files in the existing package manifest checked with zero missing or mismatched hashes, including both Word reports; see integrity_results.json.
- PASS: the unsent browser draft is byte-for-byte identical to the generated primary prompt; SHA-256 89c24e57b611737978a3298dce92d9c30e54b83417aa1f0741225e9eddf00ece.
- VERIFIED WITH LIMITS: original arXiv and NIST records inspected; see source_verification.md.
- BLOCKED BEFORE DISPATCH: actual attempt to submit the primary prompt to ChatGPT web was rejected by automatic approval review. The reviewer required explicit permission to send repository-derived instructions/evidence to that destination.
- NOT RUN: primary model inference and the other four model cases. Zero model replies, zero behavioral passes, and zero model failures are claimed.

## Browser runtime observed

ChatGPT web was signed out. The page offered model "Default" but did not expose the underlying model identifier. The composer was ready and contained the exact primary prompt. After the blocked submission, the observed state remained home with null conversation ID and zero messages. browser_attempt.json captures that state, primary_prompt_unsent.txt preserves the draft, and browser_attempt.jpg shows the composer. No test request was dispatched; no output is fabricated.

## Preserved issues

The initial local working directory from the earlier session was absent; files were retrieved anew from the pinned GitHub commit. A preliminary text-only manifest check skipped the two Word files because they were not yet materialized. Both were then fetched from the same commit and the final complete 61-file integrity check passed. The existing checker prints its original 98022f0 package-origin identifier; the actual snapshot tested here is the merge commit above.

Earlier repository text stated that the tool session lacked a separate model-execution tool. This run found a browser-based ChatGPT surface, but submission authorization is currently blocked. That new observation does not retrospectively turn examples into real runs.

## Continuation

Obtain explicit approval to send the frozen/common instructions, specialist instructions, metadata, output schema and five hypothetical cases/evidence dossiers to new ChatGPT conversations. Then execute one case per fresh conversation, keep original raw replies and runtime identity as exposed, validate without repairing the raw text, and record semantic outcomes and every failure. Do not silently substitute another model or call these anonymous/default runs a known model version.

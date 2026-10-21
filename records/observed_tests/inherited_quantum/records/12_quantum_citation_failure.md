# Quantum-specific failure preserved before revision

Date: 2026-10-18. Tested agent version: 0.3. Case: university quantum-network research pilot.

The complete, unedited failed output is `../responses/chatgpt_contrast_1_raw.txt`; the exact prompt is `quantum_contrast_1_prompt.txt`. The reply passed the frozen JSON schema validator and made a suitably bounded research recommendation, but its `evidence` entry for arXiv:2602.16613v2 gave the paper the title “Quantum Teleportation of Polarization States on Live Metropolitan Fiber.” The [arXiv source record](https://arxiv.org/abs/2602.16613) gives the title **“Bichromatic Quantum Teleportation of Weak Coherent Polarization States on a Metropolitan Fiber.”** The ID and the abstract's 30 km field-loop result were substantially correct; the bibliographic title was not. This is an informative factual failure that the schema validator could not catch.

Diagnosis: version 0.3 required a dated original source but did not explicitly require checking the exact title, authors, date, identifier and publication status against that source's own record. The correction in `sources.md` protects this worked example, but it does not by itself improve how the reusable agent cites the next paper.

Revision target: require exact metadata verification at an original-source landing page, or cite a stable identifier without an unverified title and mark the limitation. Keep the raw failed output unchanged. Rebuild the same case prompt under a new agent version, run it in a fresh ChatGPT conversation, save its full raw reply, validate its structure, and inspect the arXiv citation plus the original classification and management decision. Re-run the primary and hype cases to check that the revision has not changed their bounded decisions.

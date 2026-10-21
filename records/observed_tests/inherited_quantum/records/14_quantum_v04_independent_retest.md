# Quantum-specific revision and independent ChatGPT retest — 2026-10-18

## Failure, change and test design

Version 0.3's university-case reply passed JSON validation but gave the wrong title for arXiv:2602.16613v2. The full original reply and source-record comparison are preserved in `12_quantum_citation_failure.md`; the raw text was not altered. Version 0.4 adds a citation identity gate to `specialist_instructions.md`: check bibliographic metadata against the original publisher or preprint record, or use a stable identifier with uncertainty when that record cannot be checked. The same three cases were rebuilt as `quantum_v04_*_prompt.txt`. The frozen scaffold checker returned `FROZEN CORE INTACT`.

## Three fresh ChatGPT runs

| Case | Independent conversation | Unedited raw reply | Validated JSON | Observed decision |
| --- | --- | --- | --- | --- |
| Primary bank | https://chatgpt.com/c/6ad56e4f-e984-83ea-b4ee-21ae22845018 | `../responses/chatgpt_v04_primary_raw.txt` | `../responses/v04_primary_response.json` | Provisional potentially Promethean; prioritize standards-based PQC; no production QKD under current case conditions. |
| University contrast | https://chatgpt.com/c/6ad56e2b-4368-83e9-9e3a-bbbf825b5d23 | `../responses/chatgpt_v04_contrast_1_raw.txt` | `../responses/v04_contrast_1_response.json` | Same general label; approve only a conditional two-node research pilot; reject citywide readiness. |
| Hype-bank contrast | https://chatgpt.com/c/6ad56e60-b550-83e9-a388-cbf5f29cc857 | `../responses/chatgpt_v04_contrast_2_raw.txt` | `../responses/v04_contrast_2_response.json` | Same general label; still prioritize PQC and decline immediate production QKD. |

All three independent replies are JSON objects with the 13 required top-level fields and `agent.version` `0.4`. Each raw file is byte-for-byte identical to its paired JSON file, and the unchanged `tools/validate_response.py` returned `VALIDATION PASSED` for each. The university output no longer cites the incorrect title or arXiv:2602.16613; it instead uses other research with matching original-source identifiers. This is a successful retest of the *observed citation failure*. It does not prove that the rule will prevent every future citation error.

## Original-source spot checks and limits

The university reply's publisher or issuing-organization records were checked for [Kucera et al.](https://www.nature.com/articles/s41534-024-00886-x), [Liu et al.](https://www.nature.com/articles/s41586-024-07308-0), [Zhu et al.](https://www.nature.com/articles/s41566-026-01911-5), [Shi et al.](https://doi.org/10.1364/JOCN.592521), [Kim et al.](https://www.nature.com/articles/s41467-023-44204-z), and [RFC 9340](https://www.rfc-editor.org/rfc/rfc9340.html). The bank replies' central QKD and PQC records were checked against [Pelet et al.](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.20.044006), [Zhuang et al.](https://doi.org/10.1103/PhysRevLett.134.230801), and [NIST's FIPS announcement](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips). These checks support the cited titles and bounded claims reviewed here. Some full articles were accessible only by abstract; the hypothetical organizations have no measured deployment data. The frozen validator checks structure, not scientific truth.

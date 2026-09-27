# Output templates

Output files are written to the user's working/output directory, never into
`references/`. The output `tripod_ai_checklist.md` is the study-specific
audit; `references/tripod_ai_checklist.md` is the read-only guideline.

Issue ID prefixes:

| Prefix | Priority | Blocks Stage 2? |
|---|---|---|
| `C-01` … | Critical | Yes |
| `M-01` … | Major | No (placeholders allowed) |
| `m-01` … | Minor | No |
| `IR-01` … | Information required | No (placeholders allowed) |

IDs are stable across iterations. Never renumber or reuse an ID; resolved
issues keep their ID and move to the "Resolved" section.

---

## 1. `tripod_ai_checklist.md`

```markdown
# TRIPOD+AI reporting audit

- Study: [working title or INFORMATION REQUIRED]
- Sources audited: method.md (date/version), results.md (date/version),
  author_responses.md (if any)
- Stage: 1 (audit) | 2 (post-draft)
- Iteration: 1, 2, …
- Study type: [e.g., development with internal validation (random 70/30
  split of a single-centre cohort) — no external validation]
- Model type: [e.g., convolutional neural network; regression; gradient
  boosting]
- Applicability applied: D and D;E items (E items not applicable because …)
- Gate status: BLOCKED (n Critical unresolved) | READY FOR STAGE 2

## Status summary

| Status | Main items (n/52) | Abstract items (n/13) |
|---|---|---|
| Adequately reported | | |
| Partially reported | | |
| Not reported | | |
| Not applicable | | |
| Cannot determine | | |

## Main checklist

| Item | Topic | D/E | Evidence (quote/paraphrase) | Source | Status | Missing / required revision | Issue ID | Manuscript location |
|---|---|---|---|---|---|---|---|---|
| 1 | Title | D;E | | | | | | (Stage 2) |
| 2 | Abstract | D;E | See abstract audit | | | | | |
| 3a | Background | D;E | | | | | | |
| … one row per audit unit, in checklist order, through 27c … |

## Abstract checklist (TRIPOD+AI for Abstracts)

| Item | Section | Information available in sources? | Source | Status | Issue ID | Abstract location |
|---|---|---|---|---|---|---|
| A1 | Title | | | | | |
| … A2–A13 … |

## Methods–Results consistency

| Element | method.md | results.md | Assessment | Severity | Issue ID |
|---|---|---|---|---|---|

## Data leakage assessment — Supplementary (not a TRIPOD+AI item)

| Check | Evidence | Assessment | Issue ID |
|---|---|---|---|

## Supplementary reproducibility items (not TRIPOD+AI items)

(Include only for ML/DL; IDs from references/deep_learning_details.md.)

| ID | Item | Evidence | Status | Issue ID |
|---|---|---|---|---|
```

Rules:

- Keep the audit-unit ID alone in the first cell (e.g., `12a`, `A7`) and the
  status as one of the five exact strings; `scripts/check_audit_coverage.py`
  parses these.
- One row per audit unit; all 52 main and 13 abstract units appear, including
  `Not applicable` ones (with justification in the "Missing" column).
- "Evidence" cites the source section (`method.md §Outcome`,
  `results.md Table 2`). Empty evidence is only allowed for `Not reported`.
- "Manuscript location" is filled in Stage 2 only (e.g., `Methods §Outcome,
  para 1`).

---

## 2. `issues_to_resolve.md`

```markdown
# Issues to resolve

- Iteration: n
- Gate status: BLOCKED (n Critical unresolved) | READY FOR STAGE 2
- Counts: Critical n | Major n | Minor n | Information required n

## How to respond

Answer in `author_responses.md` using the issue IDs below, or revise
`method.md` / `results.md` directly. Answers must contain facts from the
study; do not answer with plans or estimates.

## Critical

### C-01. [Short title]
- TRIPOD+AI item(s): 21, 23a
- Current information: [what the sources say, with source]
- Problem: [what is missing or conflicting]
- Why it matters: [effect on validity/reproducibility/interpretation]
- Needed from authors: [precise question(s)]
- Placeholder that will be used if drafted under override:
  `[CRITICAL UNRESOLVED: C-01 — …]`
- Status: Unresolved | Partially resolved | Resolved (iteration n)

## Major

### M-01. [Short title]
- TRIPOD+AI item(s):
- Current information:
- Problem:
- Why it matters:
- Recommended correction:
- Suggested wording (only if all facts are available; otherwise placeholder):
- Status:

## Minor

| ID | Item(s) | Issue | Recommended correction | Status |
|---|---|---|---|---|

## Information required

| ID | Item(s) | Information needed | Placeholder text | Status |
|---|---|---|---|---|
| IR-01 | 17 | Ethics committee name and approval number | `[INFORMATION REQUIRED: specify IRB name and approval number]` | Unresolved |

## Resolved

| ID | Resolved in iteration | Evidence of resolution |
|---|---|---|
```

---

## 3. `author_responses.md` (created by the user; template to hand over)

Copy `assets/author_responses_template.md` to the working directory at the
end of Stage 1, prefilled with the open issue IDs. The structure is:

```markdown
# Author responses

## C-01
Answer: [factual answer]
Source/evidence: [e.g., revised method.md §…, analysis output, table]

## M-01
Answer:
Source/evidence:

## IR-01
Answer:
```

Rules for reading responses:

- A response is authoritative only for the ID it addresses.
- "Will do", "approximately", or "to be confirmed" does not resolve an issue.
- A response that conflicts with `method.md`/`results.md` creates a new
  `[SOURCE CONFLICT]` issue unless the author states which source is
  corrected.

---

## 4. `manuscript.md` (Stage 2)

```markdown
<!-- If override: DRAFT — NOT SUBMITTABLE: n critical issues unresolved (see issues_to_resolve.md) -->

# [Title — sentence case]

## Abstract
### Purpose
### Methods
### Results
### Conclusion

## Introduction

## Methods
### [Only applicable headings, ordered per SKILL.md §2.1]

## Results
### [Only applicable headings]

## Discussion
### Key findings
### Interpretation and comparison with previous studies
### Strengths and limitations
### Implications and next steps

## Conclusion

## Declarations
### Ethics approval and consent
### Funding
### Conflicts of interest
### Protocol and registration
### Data availability
### Code availability
### Patient and public involvement

## Tables and figures (legends and placeholders)
```

Rules:

- Placeholders keep their issue IDs:
  `[INFORMATION REQUIRED: IR-03 — specify software version]`.
- No number appears unless traceable to `results.md` or
  `author_responses.md`.

---

## 5. Audit report (audit-only requests)

```markdown
# TRIPOD+AI audit report

## Overall assessment
(Reporting completeness, transparency, reproducibility, internal
consistency, main threats to interpretation. No numerical score unless
requested.)

## Critical issues
(For each: Current information / Problem / Why it matters / Recommended
correction / Suggested wording without invented facts.)

## Major reporting issues
## Minor reporting issues

## Methods–Results inconsistencies
| Item | Methods | Results | Assessment | Required action |
|---|---|---|---|---|

## TRIPOD+AI reporting audit
| Item | Evidence | Source | Status | Required revision |
|---|---|---|---|---|
```

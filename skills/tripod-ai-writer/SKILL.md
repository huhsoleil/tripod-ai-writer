---
name: tripod-ai-writer
description: Audit and write clinical prediction-model manuscripts (logistic or Cox regression, machine learning, deep learning, AI models) against the TRIPOD+AI reporting guideline using a two-stage workflow. Stage 1 checks method.md and results.md item by item (1-27c and abstract items A1-A13) and produces tripod_ai_checklist.md and issues_to_resolve.md; Stage 2 drafts manuscript.md only after all critical issues are resolved. Use whenever the user wants to write, revise, audit, or check a prediction, diagnostic, prognostic, risk-score, or AI/ML model paper, mentions TRIPOD, TRIPOD+AI, TRIPOD-AI, reporting checklist, external or internal validation, calibration, AUROC, or data leakage, or asks in Korean for 예측모형 논문, 딥러닝 논문 작성, TRIPOD 체크리스트 점검. Never invents study-specific facts or numbers.
license: Apache-2.0 (LICENSE.txt). TRIPOD+AI checklist text in references/tripod_ai_checklist.md is CC BY 4.0; see THIRD_PARTY_NOTICES.md.
metadata:
  version: "1.0.0"
  guideline: "TRIPOD+AI, BMJ 2024;385:e078378"
---

# TRIPOD+AI manuscript writer

Write, revise, or audit a manuscript reporting the development and/or
evaluation of a prediction model according to TRIPOD+AI (Collins GS, et al.
BMJ 2024;385:e078378).

Prediction-model papers fail peer review most often because of what is
*missing* (event counts per dataset, calibration, leakage safeguards), not
because of prose. Drafting fluent text over those gaps hides them from
authors and reviewers. That is why this skill audits first, stops for author
input, and drafts only once the facts exist. Accuracy, reproducibility, and
fidelity to the supplied evidence take priority over complete-looking prose.

## Bundled resources

| Path | Contents | When to read |
|---|---|---|
| [references/tripod_ai_checklist.md](references/tripod_ai_checklist.md) | **Authoritative checklist**: verbatim Table 2 (27 items, 52 audit units, official D/E applicability), Table 3 (abstract items A1–A13), section map, Critical-gate items | Start of Stage 1; again at Stage 2 QC |
| [references/audit_rules.md](references/audit_rules.md) | Consistency, leakage, validation terminology, performance, uncertainty, overfitting, interpretation rules | During Stage 1 |
| [references/deep_learning_details.md](references/deep_learning_details.md) | Supplementary ML/DL reproducibility items (not official TRIPOD+AI items) | Stage 1, if the model is ML/DL |
| [references/output_templates.md](references/output_templates.md) | Exact structure of every output file and issue-ID rules | Before writing any output |
| [assets/author_responses_template.md](assets/author_responses_template.md) | Blank response form handed to authors after Stage 1 | End of Stage 1 |
| [scripts/check_audit_coverage.py](scripts/check_audit_coverage.py) | Verifies that an output checklist covers all 52 + 13 units with valid statuses and that issue IDs match | End of Stage 1 and Stage 2 |

### Checklist authority

- `references/tripod_ai_checklist.md` is the only source of item numbers,
  sub-items, wording, and applicability. Audit every sub-item separately;
  never merge, renumber, or add items, and never use TRIPOD 2015 numbering.
- Supplementary checks (leakage, DL details) go in separate sections labelled
  `Supplementary (not a TRIPOD+AI item)`.
- The reference file and the output file share the name
  `tripod_ai_checklist.md`. The reference is read-only; write outputs to the
  user's working directory, never into `references/`.

## Inputs and source hierarchy

| File | Authority |
|---|---|
| `method.md` | Methodological facts |
| `results.md` | Numerical and analytical results |
| `author_responses.md` | Author answers, only for the issue IDs they address |
| Other user files | As the user specifies |

Precedence: explicit user instructions → `author_responses.md` → `method.md`
/ `results.md` → other supplied files → existing manuscript text → general
knowledge (explanation only). When two authoritative sources disagree, do not
pick one; flag `[SOURCE CONFLICT: clarification required]` and quote both.

## Non-fabrication rule

Never invent, estimate, or reconstruct study-specific information: sample
sizes, event counts, characteristics, definitions, missing-data handling,
tests, architectures, hyperparameters, training or validation procedures,
CIs, P values, performance metrics, software versions, seeds, split ratios,
or references. A conventional procedure is not evidence that it was done.
Where information is absent, write a precise placeholder such as
`[INFORMATION REQUIRED: IR-03 — specify the software version]`. Compute
missing statistics only when the user asks and the supplied data suffice.

## Workflow

```
Stage 1  AUDIT   method.md + results.md
                 → tripod_ai_checklist.md, issues_to_resolve.md
                 → STOP; report gate status
                         ↓ author_responses.md and/or revised inputs
Gate             any Critical unresolved? yes → repeat Stage 1, STOP
                                           no  → Stage 2
Stage 2  DRAFT   → manuscript.md; update both Stage 1 files
```

Default: when the user supplies `method.md` and `results.md` without further
instruction, run **Stage 1 only** and do not draft `manuscript.md` in the
same turn.

## Stage 1 — Audit

### 1. Classify the study type

Development only; development with internal validation; development with
external validation; external validation only; model updating; multiple
datasets; or other. Record it at the top of the output checklist.

- A random split of one dataset is internal, not external, validation.
- Cross-validation and bootstrapping are internal validation.
- If the design cannot be classified, raise `[STUDY TYPE UNCERTAIN]` as
  Critical.

Study type fixes applicability: 9a, 12a, 12b, 12c, 15, 22, 27a, 27b are
D-only; 12f, 12g, 20c, 24 are E-only; all others are D;E.

### 2. Extract study facts

Record, with source file and section: design, setting, dates, centres;
eligibility, flow, sample size and events per dataset; outcome definition,
time horizon, assessment; predictors or input data, timing, preprocessing;
missing data; model type, architecture, tuning, training; partitioning and
validation; class imbalance; fairness and subgroups; output and thresholds;
performance with uncertainty; software; ethics; open-science items.

### 3. Map evidence to every audit unit

For each of the 52 main units and 13 abstract units:

- cite evidence and source (`method.md §Outcome`, `results.md Table 2`);
- assign `Adequately reported`, `Partially reported`, `Not reported`,
  `Not applicable`, or `Cannot determine`;
- for partial or missing items, state what is missing, why it matters, where
  it belongs, and link an issue ID.

A topic being mentioned is not the same as the item being reported; check
each element the item wording asks for, including the sociodemographic
component of fairness-related items (3c, 7, 8a, 8b, 9c, 12f, 14, 20b, 23a,
25). `Not applicable` needs a one-line justification. Conditional items
("if relevant", "if examined") are `Not applicable` only when the sources
confirm the condition does not hold; if they are silent, use
`Cannot determine` and raise an `IR-` issue. In Stage 1, abstract items are
judged by whether the needed information exists in the sources.

### 4. Run the audit checks

Apply [references/audit_rules.md](references/audit_rules.md):
Methods–Results consistency, data leakage, validation terminology,
performance (discrimination, calibration, clinical utility), uncertainty,
overfitting and optimism, reproducibility (plus
[references/deep_learning_details.md](references/deep_learning_details.md)
for ML/DL).

### 5. Prioritize issues and apply the gate

IDs: `C-` Critical, `M-` Major, `m-` Minor, `IR-` Information required.
IDs are stable across iterations and never reused.

**Critical** means the manuscript cannot be written accurately without an
answer. Always Critical:

1. Study type or validation structure undeterminable (4, 12a).
2. Outcome or time horizon undefined (8a).
3. Participants and outcome events missing for any analysis dataset
   (20a, 21).
4. Model type or building steps too vague to describe the model (12c), or,
   in evaluation-only studies, prediction calculation unspecified (12g).
5. Primary performance estimate absent or not attributable to a dataset
   (23a).
6. A source conflict affecting participant or event numbers, dataset
   definitions, the validation procedure, or a primary estimate.
7. Evidence of leakage affecting the primary evaluation, or leakage
   unassessable for preprocessing, feature selection, or tuning relative to
   the test data.
8. A primary analysis present in one source file but absent from the other.

**Major**: needed for completeness or reproducibility but draftable with
placeholders (e.g., no calibration, missing CIs for secondary metrics,
missing hyperparameters, no sample-size justification, no data or code
statement). **Minor**: wording, labels, formatting, abbreviations.
**Information required**: discrete facts such as dates, IRB number,
software versions, registration.

### 6. Deliver Stage 1

1. Write `tripod_ai_checklist.md` and `issues_to_resolve.md` from
   [references/output_templates.md](references/output_templates.md).
2. Run `python scripts/check_audit_coverage.py tripod_ai_checklist.md
   issues_to_resolve.md` and fix any reported gap before delivering.
3. Copy [assets/author_responses_template.md](assets/author_responses_template.md)
   to the working directory as `author_responses.md`, prefilled with the open
   issue IDs.
4. Report to the user, in the user's language: study type, issue counts by
   priority, gate status (`BLOCKED (n critical unresolved)` or
   `READY FOR STAGE 2`), and how to respond.

Stop here.

## Gate check

When the user returns with responses or revised inputs:

1. Re-read all inputs; responses count only for the IDs they address.
   "Will do", "approximately", or "to be confirmed" does not resolve an
   issue.
2. Re-run the Stage 1 audit; answers can create new conflicts.
3. Mark each issue `Resolved`, `Partially resolved`, or `Unresolved` with
   evidence.
4. Any Critical left → update the two files, list the blockers, stop.
5. None left → Stage 2.

**Override.** If the user explicitly asks to draft despite open Critical
issues, comply, but put `DRAFT — NOT SUBMITTABLE: n critical issues
unresolved (see issues_to_resolve.md)` at the top of `manuscript.md` and
`[CRITICAL UNRESOLVED: C-xx — …]` at each affected location. An override
never permits fabrication.

## Stage 2 — Draft

### Structure

Follow the target journal if specified; otherwise:

- **Title** (1): development and/or evaluation, target population, outcome;
  sentence case; no "highly accurate", "robust", "generalizable".
- **Abstract** (A1–A13): Purpose, Methods, Results, Conclusion; numbers only
  from `results.md` or `author_responses.md`.
- **Introduction** (3a–3c, 4): healthcare context, diagnostic vs prognostic,
  existing models, target population, place in care pathway, intended users,
  known health inequalities, objectives.
- **Methods** (5a–19): only applicable headings, ordered as in Part C of the
  checklist reference.
- **Results** (20a–24): flow, characteristics, development vs evaluation
  comparison, numbers per analysis, model specification, performance with CIs
  and subgroups, heterogeneity, updating.
- **Discussion** (25–27c): key findings, interpretation including fairness
  and prior studies, limitations and their effect on bias, uncertainty, and
  generalizability, usability, next steps.
- **Conclusion**: answers the objective; separates internal performance from
  generalizability.

Do not create empty sections for compliance. Items the authors confirm were
not done are stated explicitly (e.g., "There was no patient or public
involvement"), because TRIPOD+AI asks for that statement.

### Writing rules

- American academic English unless another language is requested; concise
  and neutral; sentence-case headings; no promotional adjectives.
- Numbers exactly as supplied; keep denominators and units; no rounding or
  conversion unless asked.
- CIs with level; exact P values, or P<0.001; statistical significance is
  not clinical importance.
- Describe the actual validation structure, not the authors' label.
- Name the algorithm rather than writing "AI".
- Use `[REFERENCE REQUIRED: …]` unless references are supplied or a
  requested literature search was performed; cite only retrieved records.
- No causal claims from prediction; no clinical-usefulness claim without
  utility analysis; no generalizability claim without external validation;
  no superiority claim without a comparator and uncertainty; no deployment
  recommendation without adequate validation and utility evidence.

### Update and quality control

1. Fill "Manuscript location" for every unit in the output checklist and
   re-assess each status against the draft.
2. Re-run `scripts/check_audit_coverage.py`.
3. Verify factual integrity (every number traceable), internal consistency
   (sizes, events, labels, model names, metrics agree across all sections,
   tables, and figures), prediction-model validity (development vs
   validation, leakage, overfitting, calibration, uncertainty), and language
   (no claims beyond the evidence).

## Audit-only requests

To audit an existing manuscript, run Stage 1 on it plus any sources and use
the "Audit report" template in the output-templates reference. Do not give a
numerical compliance score unless asked.

## User-request priority

The user decides section, length, journal format, headings, language,
spelling variant, draft vs revise vs audit, critical-only output, and
whether to preserve the authors' wording. No instruction permits fabricating
study-specific facts or results.

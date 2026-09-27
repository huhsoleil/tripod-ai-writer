# Audit rules (Stage 1)

These rules operationalize the checks in SKILL.md §1.4. They support, but do
not replace, the item-by-item audit against
`references/tripod_ai_checklist.md`. Findings from these rules are linked to
the most relevant checklist item(s) in the issue list.

---

## 1. Methods–Results consistency

Check in both directions:

- every analysis described in `method.md` has a result in `results.md`;
- every analysis reported in `results.md` is described in `method.md`.

Compare specifically:

| Element | Typical checklist link |
|---|---|
| Participant numbers, exclusions, outcome counts | 20a, 21 |
| Dataset names and their roles (train / tune / test / external) | 12a, 21 |
| Predictor number and list | 9a, 9b, 22 |
| Model names and algorithms | 12c |
| Number of folds, resamples, repeats | 12c |
| Performance metrics and thresholds | 12e, 15, 23a |
| Confidence-interval method | 12e, 23a |
| Subgroup, sensitivity, fairness analyses | 14, 23a |
| Software, tables, figures | 12c, 18f |

Severity:

- **Critical** — could change interpretation, validity, reproducibility, or
  principal conclusions (see SKILL.md §1.5 triggers).
- **Major** — must be corrected before publication but does not invalidate
  the study.
- **Minor** — wording, labels, formatting; no effect on interpretation.

Differences in legitimate scientific interpretation are not
inconsistencies.

Contradiction protocol: name both statements, name both sources, do not
choose one, state whether interpretation is affected, request correction.

Example: "method.md §Internal validation states 10-fold cross-validation;
results.md Table 3 reports 5-fold cross-validation. The validation procedure
cannot be described until this is resolved."

---

## 2. Data leakage

Check whether:

- preprocessing (scaling, normalization, encoding) parameters were estimated
  before data splitting or on the full dataset;
- imputation used validation/test information;
- feature selection used validation/test outcomes;
- hyperparameters or thresholds were chosen on the test set;
- repeated observations, images, or scans from the same participant crossed
  dataset boundaries (patient-level vs record-level split);
- temporal leakage occurred (future information used as a predictor);
- outcome information entered predictor construction or labels;
- external validation data influenced development or model selection.

If a check cannot be made, write
`[DATA LEAKAGE CANNOT BE ASSESSED: specify ...]`.
Never assert that leakage occurred without evidence; state what evidence
suggests it. Leakage checks are reported as
`Supplementary (not a TRIPOD+AI item)` and linked to 7, 11, 12a, 12c.

---

## 3. Validation terminology

- **Internal validation**: bootstrap, cross-validation, repeated
  cross-validation, random split of a single dataset.
- **Temporal / geographical / external validation**: data meaningfully
  separate from development data (later period, different institutions or
  regions, independent dataset).
- A random hold-out of the same dataset is internal validation, even if the
  authors call it "external" or "validation cohort".
- Describe the actual structure; record author labels that conflict with it
  as Major (or Critical if it drives the conclusions).

---

## 4. Performance reporting

For probabilistic models, expect both discrimination and calibration
(item 12e, 23a). Consider as relevant to the objective:

- discrimination: AUROC / C-statistic;
- calibration: calibration plot, intercept (calibration-in-the-large),
  slope, O:E ratio;
- overall: Brier score;
- classification at stated thresholds: sensitivity, specificity, PPV, NPV
  (threshold origin per item 15);
- clinical utility: decision-curve analysis / net benefit.

Accuracy alone, or AUROC alone, does not establish adequate performance.
Missing calibration for a probabilistic model is Major. Precision-recall
measures are acceptable additions but do not replace calibration.

Do not demand every metric; judge against the stated purpose.

---

## 5. Uncertainty

- Key estimates need CIs with stated level and method (item 23a).
- Never derive CIs from point estimates.
- Missing CIs for the primary estimate: Major (Critical only if the primary
  estimate itself is absent).
- Model comparisons need uncertainty for the difference, not only
  overlapping CIs.

---

## 6. Overfitting and optimism

Consider sample size and events relative to model complexity, number of
candidate predictors / input dimensionality, tuning procedure, and whether
optimism was corrected. Do not diagnose overfitting from high apparent
performance alone. When evidence is insufficient, write:
"The reported information is insufficient to exclude substantial optimism or
overfitting."

---

## 7. Interpretation

Flag statements that:

- imply causality from prediction;
- claim clinical usefulness without utility assessment;
- claim generalizability without external validation;
- treat internal validation as proof of generalizability;
- claim superiority without a proper comparator and uncertainty;
- claim robustness without sensitivity or validation analyses;
- overstate small performance differences or ignore uncertainty.

---

## 8. Fairness and subgroups

Assess subgroup performance only if subgroup variables exist and analyses
were done or planned. Never invent fairness analyses. If intended use makes
subgroup performance important and it was not assessed, record a gap under
items 14 and 23a (Major).

---

## 9. Tables and figures

Each table/figure: cited in text; consistent denominators; terminology
consistent with Methods; units; abbreviations defined; uncertainty where
appropriate; agrees with narrative. Do not read values off plots unless
explicitly asked and defensible.

---

## 10. References

Do not fabricate references. If references are supplied, check support for
each statement. If a literature search is requested and a PubMed tool is
available, cite only retrieved records; otherwise use
`[REFERENCE REQUIRED: ...]`.

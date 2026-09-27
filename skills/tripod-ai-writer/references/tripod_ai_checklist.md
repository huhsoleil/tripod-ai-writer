# TRIPOD+AI checklist (authoritative reference)

Source: Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B,
et al. TRIPOD+AI statement: updated guidance for reporting clinical
prediction models that use regression or machine learning methods.
BMJ 2024;385:e078378. doi:10.1136/bmj-2023-078378 (PMID 38626948;
PMCID PMC11019967). Item wording below is transcribed verbatim from Table 2
(main checklist) and Table 3 (TRIPOD+AI for Abstracts) of that publication.

TRIPOD+AI supersedes TRIPOD 2015; do not use TRIPOD 2015 item numbers.

License of this file's checklist text: CC BY 4.0 (per PubMed Central
licence metadata for PMC11019967), © the authors. See THIRD_PARTY_NOTICES.md
in the skill folder.

## Contents

- How to use this file
- Part A. TRIPOD+AI checklist (Table 2) — 52 audit units
- Part B. TRIPOD+AI for Abstracts (Table 3) — A1–A13
- Part C. Item-to-manuscript-section map (Stage 2)
- Part D. Items that trigger the Critical gate when missing

## How to use this file

- This file is the **only** source of item numbers, sub-items, wording, and
  applicability. Do not add, merge, renumber, or paraphrase items.
- Audit **each row** separately. Sub-items (e.g., 3a, 3b, 3c) are distinct
  audit units. Part A has 52 audit units; Part B has 13.
- Applicability codes (official definitions):
  - **D** = items relevant only to the development of a prediction model;
  - **E** = items relating solely to the evaluation of a prediction model;
  - **D;E** = items applicable to both development and evaluation.
- Apply according to the Stage 1 study-type classification:
  - development only (incl. internal validation) → D and D;E items; E items
    are `Not applicable` with justification;
  - external validation only → E and D;E items; D items are
    `Not applicable` unless the study also re-develops or updates a model;
  - development plus external validation → all items.
- Fairness-related content is embedded in items 3c, 7, 8a, 8b, 9c, 12f, 14,
  20b, 23a, and 25. Audit the sociodemographic component of each
  explicitly; do not mark these adequate when that component is absent.
- Items with conditional wording ("if relevant", "if applicable",
  "if examined", "if class imbalance methods were used") may be
  `Not applicable` only when the sources confirm the condition does not
  hold. If the sources are silent, use `Cannot determine` and raise an
  `IR-` issue.

---

## Part A. TRIPOD+AI checklist (Table 2)

### Title

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 1 | Title | D;E | Identify the study as developing or evaluating the performance of a multivariable prediction model, the target population, and the outcome to be predicted |

### Abstract

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 2 | Abstract | D;E | See TRIPOD+AI for Abstracts checklist (Part B) |

### Introduction

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 3a | Background | D;E | Explain the healthcare context (including whether diagnostic or prognostic) and rationale for developing or evaluating the prediction model, including references to existing models |
| 3b | Background | D;E | Describe the target population and the intended purpose of the prediction model in the context of the care pathway, including its intended users (eg, healthcare professionals, patients, public) |
| 3c | Background | D;E | Describe any known health inequalities between sociodemographic groups |
| 4 | Objectives | D;E | Specify the study objectives, including whether the study describes the development or validation of a prediction model (or both) |

### Methods

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 5a | Data | D;E | Describe the sources of data separately for the development and evaluation datasets (eg, randomised trial, cohort, routine care or registry data), the rationale for using these data, and representativeness of the data |
| 5b | Data | D;E | Specify the dates of the collected participant data, including start and end of participant accrual; and, if applicable, end of follow-up |
| 6a | Participants | D;E | Specify key elements of the study setting (eg, primary care, secondary care, general population) including the number and location of centres |
| 6b | Participants | D;E | Describe the eligibility criteria for study participants |
| 6c | Participants | D;E | Give details of any treatments received, and how they were handled during model development or evaluation, if relevant |
| 7 | Data preparation | D;E | Describe any data pre-processing and quality checking, including whether this was similar across relevant sociodemographic groups |
| 8a | Outcome | D;E | Clearly define the outcome that is being predicted and the time horizon, including how and when assessed, the rationale for choosing this outcome, and whether the method of outcome assessment is consistent across sociodemographic groups |
| 8b | Outcome | D;E | If outcome assessment requires subjective interpretation, describe the qualifications and demographic characteristics of the outcome assessors |
| 8c | Outcome | D;E | Report any actions to blind assessment of the outcome to be predicted |
| 9a | Predictors | D | Describe the choice of initial predictors (eg, literature, previous models, all available predictors) and any pre-selection of predictors before model building |
| 9b | Predictors | D;E | Clearly define all predictors, including how and when they were measured (and any actions to blind assessment of predictors for the outcome and other predictors) |
| 9c | Predictors | D;E | If predictor measurement requires subjective interpretation, describe the qualifications and demographic characteristics of the predictor assessors |
| 10 | Sample size | D;E | Explain how the study size was arrived at (separately for development and evaluation), and justify that the study size was sufficient to answer the research question. Include details of any sample size calculation |
| 11 | Missing data | D;E | Describe how missing data were handled. Provide reasons for omitting any data |
| 12a | Analytical methods | D | Describe how the data were used (eg, for development and evaluation of model performance) in the analysis, including whether the data were partitioned, considering any sample size requirements |
| 12b | Analytical methods | D | Depending on the type of model, describe how predictors were handled in the analyses (functional form, rescaling, transformation, or any standardisation) |
| 12c | Analytical methods | D | Specify the type of model, rationale†, all model building steps, including any hyperparameter tuning, and method for internal validation |
| 12d | Analytical methods | D;E | Describe if and how any heterogeneity in estimates of model parameter values and model performance was handled and quantified across clusters (eg, hospitals, countries). See TRIPOD-Cluster for additional considerations‡ |
| 12e | Analytical methods | D;E | Specify all measures and plots used (and their rationale) to evaluate model performance (eg, discrimination, calibration, clinical utility) and, if relevant, to compare multiple models |
| 12f | Analytical methods | E | Describe any model updating (eg, recalibration) arising from the model evaluation, either overall or for particular sociodemographic groups or settings |
| 12g | Analytical methods | E | For model evaluation, describe how the model predictions were calculated (eg, formula, code, object, application programming interface) |
| 13 | Class imbalance | D;E | If class imbalance methods were used, state why and how this was done, and any subsequent methods to recalibrate the model or the model predictions |
| 14 | Fairness | D;E | Describe any approaches that were used to address model fairness and their rationale |
| 15 | Model output | D | Specify the output of the prediction model (eg, probabilities, classification). Provide details and rationale for any classification and how the thresholds were identified |
| 16 | Training versus evaluation | D;E | Identify any differences between the development and evaluation data in healthcare setting, eligibility criteria, outcome, and predictors |
| 17 | Ethical approval | D;E | Name the institutional research board or ethics committee that approved the study and describe the participant informed consent or the ethics committee waiver of informed consent |

### Open science

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 18a | Funding | D;E | Give the source of funding and the role of the funders for the present study |
| 18b | Conflicts of interest | D;E | Declare any conflicts of interest and financial disclosures for all authors |
| 18c | Protocol | D;E | Indicate where the study protocol can be accessed or state that a protocol was not prepared |
| 18d | Registration | D;E | Provide registration information for the study, including register name and registration number, or state that the study was not registered |
| 18e | Data sharing | D;E | Provide details of the availability of the study data |
| 18f | Code sharing | D;E | Provide details of the availability of the analytical code§ |

### Patient and public involvement

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 19 | Patient and public involvement | D;E | Provide details of any patient and public involvement during the design, conduct, reporting, interpretation, or dissemination of the study or state no involvement |

### Results

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 20a | Participants | D;E | Describe the flow of participants through the study, including the number of participants with and without the outcome and, if applicable, a summary of the follow-up time. A diagram may be helpful |
| 20b | Participants | D;E | Report the characteristics overall and, where applicable, for each data source or setting, including the key dates, key predictors (including demographics), treatments received, sample size, number of outcome events, follow-up time, and amount of missing data. A table may be helpful. Report any differences across key demographic groups |
| 20c | Participants | E | For model evaluation, show a comparison with the development data of the distribution of important predictors (demographics, predictors, and outcome) |
| 21 | Model development | D;E | Specify the number of participants and outcome events in each analysis (eg, for model development, hyperparameter tuning, model evaluation) |
| 22 | Model specification | D | Provide details of the full prediction model (eg, formula, code, object, application programming interface) to allow predictions in new individuals and to enable third party evaluation and implementation, including any restrictions to access or reuse (eg, freely available, proprietary)¶ |
| 23a | Model performance | D;E | Report model performance estimates with confidence intervals, including for any key subgroups (eg, sociodemographic). Consider plots to aid presentation |
| 23b | Model performance | D;E | If examined, report results of any heterogeneity in model performance across clusters. See TRIPOD-Cluster for additional details‡ |
| 24 | Model updating | E | Report the results from any model updating, including the updated model and subsequent performance |

### Discussion

| Item | Topic | D/E | Checklist item |
|---|---|---|---|
| 25 | Interpretation | D;E | Give an overall interpretation of the main results, including issues of fairness in the context of the objectives and previous studies |
| 26 | Limitations | D;E | Discuss any limitations of the study (such as a non-representative sample, sample size, overfitting, missing data) and their effects on any biases, statistical uncertainty, and generalisability |
| 27a | Usability of the model in the context of current care | D | Describe how poor quality or unavailable input data (eg, predictor values) should be assessed and handled when implementing the prediction model |
| 27b | Usability of the model in the context of current care | D | Specify whether users will be required to interact in the handling of the input data or use of the model, and what level of expertise is required of users |
| 27c | Usability of the model in the context of current care | D;E | Discuss any next steps for future research, with a specific view to applicability and generalisability of the model |

Footnotes (official):

- † Separately for all model building approaches.
- ‡ TRIPOD-Cluster is a checklist of reporting recommendations for studies
  developing or validating models that explicitly account for clustering or
  explore heterogeneity in model performance (eg, at different hospitals or
  centres).
- § Relates to the analysis code, for example, any data cleaning, feature
  engineering, model building, and evaluation.
- ¶ Relates to the code to implement the model to get estimates of risk for
  a new individual.

Audit-unit list (52): 1, 2, 3a, 3b, 3c, 4, 5a, 5b, 6a, 6b, 6c, 7, 8a, 8b,
8c, 9a, 9b, 9c, 10, 11, 12a, 12b, 12c, 12d, 12e, 12f, 12g, 13, 14, 15, 16,
17, 18a, 18b, 18c, 18d, 18e, 18f, 19, 20a, 20b, 20c, 21, 22, 23a, 23b, 24,
25, 26, 27a, 27b, 27c.

---

## Part B. TRIPOD+AI for Abstracts (Table 3)

Abstract items are prefixed `A` in audit outputs to avoid confusion with
main-checklist numbers.

| Item | Section | Checklist item |
|---|---|---|
| A1 | Title | Identify the study as developing or evaluating the performance of a multivariable prediction model, the target population, and the outcome to be predicted |
| A2 | Background | Provide a brief explanation of the healthcare context and rationale for developing or evaluating the performance of all models |
| A3 | Objectives | Specify the study objectives, including whether the study describes model development, evaluation, or both |
| A4 | Methods | Describe the sources of data |
| A5 | Methods | Describe the eligibility criteria and setting where the data were collected |
| A6 | Methods | Specify the outcome to be predicted by the model, including time horizon of predictions in case of prognostic models |
| A7 | Methods | Specify the type of model, a summary of the model-building steps, and the method for internal validation† |
| A8 | Methods | Specify the measures used to assess model performance (eg, discrimination, calibration, clinical utility) |
| A9 | Results | Report the number of participants and outcome events |
| A10 | Results | Summarise the predictors in the final model† |
| A11 | Results | Report model performance estimates (with confidence intervals) |
| A12 | Discussion | Give an overall interpretation of the main results |
| A13 | Registration | Give the registration number and name of the registry or repository |

- † Relevant only to studies describing the development of a prediction
  model (A7, A10 are `Not applicable` for external-validation-only studies).
- If the target journal's abstract word limit prevents A13 or another item,
  record this in `issues_to_resolve.md` as Minor rather than omitting the
  audit.

---

## Part C. Item-to-manuscript-section map (Stage 2)

| Manuscript section | Items |
|---|---|
| Title | 1 |
| Abstract | 2 (A1–A13) |
| Introduction | 3a, 3b, 3c, 4 |
| Methods — data and participants | 5a, 5b, 6a, 6b, 6c |
| Methods — data preparation, outcome, predictors | 7, 8a, 8b, 8c, 9a, 9b, 9c |
| Methods — sample size, missing data | 10, 11 |
| Methods — analytical methods | 12a–12g, 13, 14, 15, 16 |
| Methods — ethics | 17 |
| Methods or declarations | 18a–18f, 19 (follow journal format) |
| Results | 20a, 20b, 20c, 21, 22, 23a, 23b, 24 |
| Discussion | 25, 26, 27a, 27b, 27c |

---

## Part D. Items that trigger the Critical gate when missing

| Item(s) | Condition |
|---|---|
| 4, 12a | Development vs validation design, or data use/partitioning, cannot be determined |
| 8a | Outcome definition or time horizon absent |
| 12c | Model type or model-building steps absent (development studies) |
| 12g | How predictions were calculated is absent (evaluation-only studies) |
| 20a, 21 | Number of participants and outcome events per analysis dataset absent |
| 23a | Primary performance estimate absent or not attributable to a dataset |

All other missing items default to Major or Information required unless a
`[SOURCE CONFLICT]` or leakage concern elevates them (SKILL.md §1.5).

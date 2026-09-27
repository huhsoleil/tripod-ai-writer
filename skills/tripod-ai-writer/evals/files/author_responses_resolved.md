# Author responses (SYNTHETIC TEST FIXTURE — not a real study)

> Resolves the Critical issues expected from Stage 1 on the synthetic
> method.md and results.md. Issue IDs are descriptive because the skill
> assigns its own IDs; the evaluator maps them by content.

## Outcome definition and time horizon
Answer: Death from any cause during the index hospitalization, up to a
maximum of 30 days after admission, ascertained from the hospital discharge
record.
Source/evidence: revised method.md §Outcome.

## Validation structure ("external test set")
Answer: The 20% test set is a random patient-level hold-out from the same
hospital and period. It is internal validation; the word "external" was an
error. No external dataset was used.
Source/evidence: revised method.md §Data partitioning.

## Cross-validation folds
Answer: Five-fold cross-validation was used; "10-fold" in method.md was a
typographical error.
Source/evidence: training log.

## Preprocessing and imputation leakage
Answer: Standardization parameters and imputation (median of the training
set) were estimated on the training set only and then applied to the
validation and test sets. The method.md wording "entire dataset" was
incorrect. Splitting was at patient level; each patient contributed one
admission.
Source/evidence: preprocessing script, revised method.md §Data preprocessing.

## Outcome events in validation and test sets
Answer: Validation set 49 deaths (49/504); test set 99 deaths (99/1,007).
Source/evidence: revised results.md §Dataset sizes.

## Threshold selection
Answer: The threshold 0.12 was chosen by maximizing the Youden index in the
validation set, not the test set.
Source/evidence: revised method.md §Performance evaluation.

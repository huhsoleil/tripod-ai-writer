# Results (SYNTHETIC TEST FIXTURE — not a real study)

> Invented numbers for skill testing only.

## Participants
Of 6,412 screened admissions, 5,038 patients were included. Overall
in-hospital mortality was 9.8% (494/5,038).

## Dataset sizes
Training set: 3,527 patients (346 deaths). Validation set: 504 patients.
Test set: 1,007 patients.

## Model performance
Five-fold cross-validation AUROC in the training set: 0.87 (SD 0.02).

Test set:
- AUROC 0.91 (95% CI 0.88–0.94)
- Sensitivity 0.84, specificity 0.81 at a threshold of 0.12
- Accuracy 0.81

Comparison: the fused model outperformed CURB-65 (AUROC 0.74).

## Calibration
Calibration plot in the test set showed good agreement (Figure 3).

## Additional analysis
Performance in patients aged 65 years or older: AUROC 0.89.

## Interpretation (authors' draft)
The model is highly accurate, generalizable, and ready for clinical
deployment in emergency departments.

# Supplementary reproducibility items for ML / deep learning

**Status: Supplementary (not a TRIPOD+AI item).** These items are not part of
the official checklist. Report them in a separate section of
`tripod_ai_checklist.md` titled "Supplementary reproducibility items (not
TRIPOD+AI items)". Link each gap to the closest official item (usually 7,
12b, 12c, 18f, or 22) in `issues_to_resolve.md`.

Default priority for gaps: **Major** when the item is needed to reproduce the
primary model; **Minor** or **Information required** otherwise. Do not demand
items irrelevant to the model type.

## S1. Data and input

| ID | Item | Link |
|---|---|---|
| S1.1 | Input modality and format (e.g., image type, resolution, sequence length, tabular fields) | 9b |
| S1.2 | Acquisition devices/protocols and variation across sites | 5a, 16 |
| S1.3 | Labeling / annotation process, annotators, and agreement | 8a, 8b |
| S1.4 | Preprocessing pipeline (resizing, cropping, normalization, tokenization) and whether fitted on training data only | 7, 12b |
| S1.5 | Data augmentation (types, parameters, applied to training only) | 12c |
| S1.6 | Unit of splitting (patient vs image/record) and leakage prevention | 12a |

## S2. Model

| ID | Item | Link |
|---|---|---|
| S2.1 | Architecture (name, layers/blocks, number of parameters, modifications) | 12c |
| S2.2 | Pretraining / transfer learning source and which layers were fine-tuned | 12c |
| S2.3 | Initialization | 12c |
| S2.4 | Loss function (incl. class weighting) | 12c, 13 |
| S2.5 | Output layer and post-processing (e.g., softmax, calibration step) | 15 |

## S3. Training

| ID | Item | Link |
|---|---|---|
| S3.1 | Optimizer and learning rate (schedule) | 12c |
| S3.2 | Batch size, number of epochs | 12c |
| S3.3 | Early-stopping or other stopping rule, and the dataset used to trigger it | 12c, 12a |
| S3.4 | Regularization (dropout, weight decay) | 12c |
| S3.5 | Hyperparameter search space, strategy, and selection dataset | 12c |
| S3.6 | Final hyperparameter values | 12c, 22 |
| S3.7 | Random seeds / number of repeated runs and variability across runs | 12c, 23a |
| S3.8 | Ensembling, if any | 12c |

## S4. Evaluation and deployment

| ID | Item | Link |
|---|---|---|
| S4.1 | Test set held out and untouched until final locked-model evaluation | 12a |
| S4.2 | Threshold selection dataset | 15 |
| S4.3 | Explainability methods (e.g., saliency maps) and their stated limitations | 25 |
| S4.4 | Hardware, software, framework and library versions | 12c, 18f |
| S4.5 | Code, trained weights, and model access (repository, license, restrictions) | 18f, 22 |
| S4.6 | Inference requirements and handling of poor-quality or missing input | 27a, 27b |

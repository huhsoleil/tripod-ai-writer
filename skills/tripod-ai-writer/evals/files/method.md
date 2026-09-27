# Methods (SYNTHETIC TEST FIXTURE — not a real study)

> This file is an invented example used only to test the tripod-ai-writer
> skill. It deliberately contains reporting gaps and inconsistencies.

## Study design and data source
Retrospective cohort study using electronic health records and chest
radiographs from a single tertiary hospital in Seoul, Korea. Adult patients
admitted through the emergency department with community-acquired pneumonia
between January 2018 and December 2022 were eligible.

## Participants
Inclusion: age 18 years or older; chest radiograph within 6 hours of
admission. Exclusion: transfer from another hospital; do-not-resuscitate
order at admission; radiograph of insufficient quality.

## Outcome
In-hospital mortality.

## Predictors
Frontal chest radiograph (posteroanterior or anteroposterior), age, sex,
respiratory rate, oxygen saturation, blood urea nitrogen, and C-reactive
protein measured at admission.

## Data preprocessing
Images were resized to 512 × 512 pixels. Pixel intensities and all
continuous clinical variables were standardized using the mean and standard
deviation of the entire dataset. Missing laboratory values were imputed.

## Data partitioning
The dataset was randomly split into a training set (70%), a validation set
(10%), and an external test set (20%).

## Model development
A convolutional neural network (DenseNet-121 pretrained on ImageNet) was
used for the image branch, and a multilayer perceptron for the clinical
branch; the two were fused by concatenation. The model was trained with
the Adam optimizer. Hyperparameters were tuned. Internal validation used
10-fold cross-validation within the training set.

## Performance evaluation
Discrimination was assessed using the area under the receiver operating
characteristic curve (AUROC). Sensitivity and specificity were calculated at
the optimal threshold. Calibration was assessed with a calibration plot.
A subgroup analysis by sex was planned.

## Statistical analysis
Analyses used Python and PyTorch.

## Ethics
The institutional review board approved the study and waived informed
consent.

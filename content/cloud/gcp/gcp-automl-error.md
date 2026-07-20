---
title: "[Solution] GCP AutoML Error — dataset train evaluate predict errors"
description: "Fix GCP AutoML errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 125
---

AutoML errors occur when there are issues with dataset import, model training, evaluation, or prediction.

## Common Causes
- Training data insufficient or unbalanced
- Dataset import format incompatible
- Model training exceeded resource limits
- Prediction input format mismatch
- AutoML API not enabled

## How to Fix

### 1. Enable AutoML API
```bash
gcloud services enable automl.googleapis.com --project=PROJECT_ID
```

### 2. List tables datasets
```bash
gcloud automl tables datasets list --location=REGION
```

### 3. Create classification dataset
```bash
gcloud automl tables datasets create DATASET_NAME \
  --display-name="Classification Dataset" \
  --location=REGION
```

### 4. Import data to dataset
```bash
gcloud automl tables datasets import DATASET_NAME \
  --location=REGION \
  --source=gs://bucket/data.csv
```

### 5. Train model
```bash
gcloud automl tables models train MODEL_NAME \
  --dataset=DATASET_NAME \
  --location=REGION \
  --target-column-spec=TARGET_COLUMN \
  --train-budget=1000
```

## Examples

### Predict with trained model
```bash
gcloud automl tables models predict MODEL_NAME \
  --location=REGION \
  --csv-input=input.csv
```

### List model evaluation
```bash
gcloud automl tables models list \
  --dataset=DATASET_ID \
  --location=REGION \
  --format="table(name,deploymentState,createTime)"
```

## Related Errors
- [GCP Vertex AI Error](/cloud/gcp/gcp-vertex-ai-error/)
- [GCP AI Platform Error](/cloud/gcp/gcp-ai-platform-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
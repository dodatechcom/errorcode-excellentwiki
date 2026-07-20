---
title: "[Solution] GCP AI Platform Error — job model version prediction errors"
description: "Fix GCP AI Platform errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 126
---

AI Platform errors occur when there are issues with training jobs, model versions, or online prediction.

## Common Causes
- Training job output directory already exists
- Model version creation conflicts with existing version
- Prediction request format doesn't match model input
- Insufficient quota for training or prediction
- AI Platform API not enabled

## How to Fix

### 1. Enable AI Platform API
```bash
gcloud services enable ml.googleapis.com --project=PROJECT_ID
```

### 2. List models and versions
```bash
gcloud ai-platform models list --region=REGION
gcloud ai-platform versions list --model=MODEL_NAME
```

### 3. Submit training job
```bash
gcloud ai-platform jobs submit training JOB_NAME \
  --region=REGION \
  --master-image-uri=TRAINING_IMAGE \
  --job-dir=gs://bucket/jobs/JOB_NAME \
  --scale-tier=CUSTOM \
  --master-machine-type=n1-standard-8
```

### 4. Create model version
```bash
gcloud ai-platform versions create VERSION_NAME \
  --model=MODEL_NAME \
  --origin=gs://bucket/model/ \
  --runtime-version=2.11 \
  --framework=TENSORFLOW \
  --python-version=3.9
```

### 5. Run prediction
```bash
gcloud ai-platform predict \
  --model=MODEL_NAME \
  --version=VERSION_NAME \
  --json-request=input.json
```

## Examples

### Deploy Scikit-learn model
```bash
gcloud ai-platform versions create v1 \
  --model=scikit-model \
  --origin=gs://models/sklearn/ \
  --runtime-version=2.11 \
  --framework=SCIKIT_LEARN \
  --python-version=3.9
```

### Check job status
```bash
gcloud ai-platform jobs describe JOB_NAME \
  --format="yaml(state,startTime,endTime,errorMessage)"
```

## Related Errors
- [GCP Vertex AI Error](/cloud/gcp/gcp-vertex-ai-error/)
- [GCP AutoML Error](/cloud/gcp/gcp-automl-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
---
title: "[Solution] GCP Data Fusion Error -- instance pipeline namespace errors"
description: "Fix GCP Data Fusion errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 128
---

Data Fusion errors occur when there are issues with instance creation, pipeline execution, or namespace configuration.

## Common Causes
- Instance version not compatible with pipeline
- Insufficient permissions for Dataproc service account
- Pipeline deployer service account misconfigured
- Data Fusion API not enabled
- Instance boot disk size too small

## How to Fix

### 1. Enable Data Fusion API
```bash
gcloud services enable datafusion.googleapis.com --project=PROJECT_ID
```

### 2. List Data Fusion instances
```bash
gcloud data-fusion instances list --location=REGION
```

### 3. Create Data Fusion instance
```bash
gcloud data-fusion instances create INSTANCE_NAME \
  --location=REGION \
  --type=BASIC \
  --private-ip
```

### 4. Describe instance details
```bash
gcloud data-fusion instances describe INSTANCE_NAME --location=REGION
```

### 5. Delete instance
```bash
gcloud data-fusion instances delete INSTANCE_NAME --location=REGION --quiet
```

## Examples

### Check instance status via API
```bash
gcloud data-fusion instances describe my-instance \
  --location=us-central1 \
  --format="yaml(state,serviceAccount,endpoint)"
```

### Create private instance
```bash
gcloud data-fusion instances create secure-instance \
  --location=us-central1 \
  --type=ENTERPRISE \
  --private-ip \
  --network=my-vpc
```

## Related Errors
- [GCP Dataproc Error](/cloud/gcp/gcp-dataproc-error/)
- [GCP Composer Error](/cloud/gcp/gcp-composer-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
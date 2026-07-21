---
title: "[Solution] GCP Service Usage Error -- enable disable quota consumer errors"
description: "Fix GCP Service Usage errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 154
---

Service Usage errors occur when there are issues with enabling/disabling services, quota management, or consumer configuration.

## Common Causes
- Service already enabled or not found
- Quota limit exceeded for API
- Consumer project doesn't own the resource
- Service usage API disabled
- Billing not enabled for project

## How to Fix

### 1. Enable Service Usage API
```bash
gcloud services enable serviceusage.googleapis.com --project=PROJECT_ID
```

### 2. List enabled services
```bash
gcloud services list --enabled --format="table(name,config.title)"
```

### 3. Enable a service
```bash
gcloud services enable SERVICE_NAME.googleapis.com --project=PROJECT_ID
```

### 4. Disable a service
```bash
gcloud services disable SERVICE_NAME.googleapis.com --project=PROJECT_ID
```

### 5. Check service quota
```bash
gcloud services quota describe SERVICE_NAME.googleapis.com \
  --consumer=projects/PROJECT_ID
```

## Examples

### Batch enable required services
```bash
gcloud services enable \
  compute.googleapis.com \
  container.googleapis.com \
  --project=my-project
```

### List quota for compute API
```bash
gcloud services quota describe compute.googleapis.com \
  --consumer=projects/my-project \
  --format="table(metricName,quotaMetric,consumerLimit)"
```

## Related Errors
- [GCP Service Consumer Error](/cloud/gcp/gcp-service-consumer-error/)
- [GCP Quota Error](/cloud/gcp/quota-exceeded/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
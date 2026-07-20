---
title: "[Solution] GCP Service Consumer Error — policy tenant-proj errors"
description: "Fix GCP Service Consumer errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 155
---

Service Consumer errors occur when there are issues with service consumer management, tenant projects, or consumer policies.

## Common Causes
- Tenant project quota exceeded
- Consumer policy configuration invalid
- Service producer consumer quota limit reached
- Cross-project service access denied
- Service Consumer Management API not enabled

## How to Fix

### 1. Enable Service Consumer Management API
```bash
gcloud services enable serviceconsumermanagement.googleapis.com --project=PROJECT_ID
```

### 2. List consumer resources
```bash
gcloud services consumer-resources list \
  --consumer=projects/CONSUMER_PROJECT \
  --service=SERVICE_NAME.googleapis.com
```

### 3. Check consumer quota
```bash
gcloud services consumer-quota-metrics list \
  --consumer=projects/CONSUMER_PROJECT \
  --service=SERVICE_NAME.googleapis.com
```

### 4. Create tenant project
```bash
gcloud services tenant-projects create TENANT_PROJECT \
  --service=SERVICE_NAME.googleapis.com \
  --consumer=projects/CONSUMER_PROJECT
```

### 5. Update consumer policy
```bash
gcloud services consumer-policies update \
  --consumer=projects/CONSUMER_PROJECT \
  --service=SERVICE_NAME.googleapis.com \
  --policy-file=policy.yaml
```

## Examples

### List all tenant projects
```bash
gcloud services tenant-projects list \
  --service=my-service.googleapis.com \
  --format="table(name,state,projectNumber)"
```

### Check consumer quota status
```bash
gcloud services consumer-quota-metrics describe \
  my-service.googleapis.com \
  --consumer=projects/my-project \
  --location=global
```

## Related Errors
- [GCP Service Usage Error](/cloud/gcp/gcp-service-usage-error/)
- [GCP Resource Manager Error](/cloud/gcp/gcp-resource-manager-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
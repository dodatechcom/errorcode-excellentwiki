---
title: "[Solution] GCP Resource Manager Error -- folder project org-policy errors"
description: "Fix GCP Resource Manager errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 156
---

Resource Manager errors occur when there are issues with folder hierarchy, project management, or organization policies.

## Common Causes
- Organization policy constraint violation
- Folder hierarchy depth limit exceeded
- Project creation permission denied
- Resource Manager API not enabled
- Organization policy constraint conflicts

## How to Fix

### 1. Enable Resource Manager API
```bash
gcloud services enable cloudresourcemanager.googleapis.com --project=PROJECT_ID
```

### 2. List folders
```bash
gcloud resource-manager folders list --organization=ORG_ID
```

### 3. Create folder
```bash
gcloud resource-manager folders create FOLDER_NAME \
  --organization=ORG_ID \
  --display-name="My Folder"
```

### 4. Create project under folder
```bash
gcloud projects create PROJECT_ID \
  --name="My Project" \
  --folder=FOLDER_ID
```

### 5. Check org policy
```bash
gcloud resource-manager org-policies list --project=PROJECT_ID
```

## Examples

### Set organization policy
```bash
gcloud resource-manager org-policies set-policy \
  --project=PROJECT_ID \
  policy.yaml
```

### Move project to folder
```bash
gcloud projects move PROJECT_ID \
  --folder=FOLDER_ID
```

## Related Errors
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
- [GCP Service Consumer Error](/cloud/gcp/gcp-service-consumer-error/)
- [GCP Asset Inventory Error](/cloud/gcp/gcp-asset-inventory-error/)
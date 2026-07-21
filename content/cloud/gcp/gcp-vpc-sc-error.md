---
title: "[Solution] GCP VPC Service Controls Error -- perimeter bridge ingress errors"
description: "Fix GCP VPC Service Controls errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 162
---

VPC Service Controls errors occur when there are issues with perimeters, bridges, ingress/egress rules, or access levels.

## Common Causes
- Perimeter configuration blocks expected traffic
- Access level conditions not matching request
- Bridge configuration conflicts between perimeters
- VPC Service Controls API not enabled
- Service perimeter dry-run mode blocking access

## How to Fix

### 1. Enable VPC Service Controls API
```bash
gcloud services enable accesscontextmanager.googleapis.com --project=PROJECT_ID
```

### 2. List access policies
```bash
gcloud access-context-manager policies list
```

### 3. List service perimeters
```bash
gcloud access-context-manager perimeters list --policy=POLICY_ID
```

### 4. Create service perimeter
```bash
gcloud access-context-manager perimeters create PERIMETER_NAME \
  --policy=POLICY_ID \
  --resources="projects/PROJECT_NUMBER" \
  --restricted-services="bigquery.googleapis.com,storage.googleapis.com"
```

### 5. Create access level
```bash
gcloud access-context-manager levels create LEVEL_NAME \
  --policy=POLICY_ID \
  --basic-criteria="ip_subnetworks=IP_RANGE"
```

## Examples

### Update perimeter with dry-run
```bash
gcloud access-context-manager perimeters update PERIMETER \
  --policy=POLICY \
  --set-dry-run
```

### List ingress policies
```bash
gcloud access-context-manager perimeters ingress-policies list \
  --perimeter=PERIMETER \
  --policy=POLICY
```

## Related Errors
- [GCP Access Transparency Error](/cloud/gcp/gcp-access-transparency-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)
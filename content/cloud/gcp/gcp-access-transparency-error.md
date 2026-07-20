---
title: "[Solution] GCP Access Transparency Error — log approval errors"
description: "Fix GCP Access Transparency errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 161
---

Access Transparency errors occur when there are issues with access transparency log collection, approval workflows, or export.

## Common Causes
- Access Transparency not enabled for organization
- Approval policy not configured
- Export destination unreachable
- Access Transparency API not enabled
- Insufficient permissions for log viewing

## How to Fix

### 1. Enable Access Transparency API
```bash
gcloud services enable accesstransparency.googleapis.com --project=PROJECT_ID
```

### 2. Check Access Transparency status
```bash
gcloud access-transparency settings get \
  --organization=ORG_ID
```

### 3. Enable Access Transparency
```bash
gcloud access-transparency settings update \
  --organization=ORG_ID \
  --access-transparency-enabled=true
```

### 4. List access transparency logs
```bash
gcloud access-transparency access-approval-requests list \
  --filter="project:PROJECT_ID"
```

### 5. Approve access request
```bash
gcloud access-transparency access-approval-requests approve \
  --request-id=REQUEST_ID
```

## Examples

### Export access transparency logs
```bash
gcloud access-transparency access-approval-requests export \
  --filter="project:PROJECT_ID" \
  --format=json > access-logs.json
```

### Deny access request
```bash
gcloud access-transparency access-approval-requests deny \
  --request-id=REQUEST_ID \
  --reason="Not authorized"
```

## Related Errors
- [GCP IAP Error](/cloud/gcp/gcp-iap-error/)
- [GCP Security Command Center Error](/cloud/gcp/gcp-security-command-center-error/)
- [GCP VPC SC Error](/cloud/gcp/gcp-vpc-sc-error/)
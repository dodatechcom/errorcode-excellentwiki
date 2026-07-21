---
title: "[Solution] GCP Security Command Center Error -- finding source notification errors"
description: "Fix GCP Security Command Center errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 166
---

Security Command Center errors occur when there are issues with finding detection, source configuration, or notification setup.

## Common Causes
- Security Command Center not enabled at organization level
- Finding notification topic doesn't exist
- Source service account lacks permissions
- Finding filter syntax invalid
- Security Center API not enabled

## How to Fix

### 1. Enable Security Command Center API
```bash
gcloud services enable securitycenter.googleapis.com --project=PROJECT_ID
```

### 2. List findings
```bash
gcloud scc findings list organizations/ORG_ID \
  --filter="state=\"ACTIVE\""
```

### 3. Create source
```bash
curl -X POST \
  "https://securitycenter.googleapis.com/v1/organizations/ORG_ID/sources" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"displayName":"My Source","description":"Custom findings source"}'
```

### 4. Create notification config
```bash
curl -X POST \
  "https://securitycenter.googleapis.com/v1/organizations/ORG_ID/notificationConfigs" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"alert-config","description":"High severity alerts","pubsubTopic":"projects/PROJECT/topics/TOPIC","filter":"severity=\"HIGH\""}'
```

### 5. Get finding details
```bash
gcloud scc findings describe FINDING_NAME \
  --source=SOURCE_ID \
  --organization=ORG_ID
```

## Examples

### Create finding for testing
```bash
curl -X PATCH \
  "https://securitycenter.googleapis.com/v1/organizations/ORG_ID/sources/SOURCE/findings/FINDING" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"state":"ACTIVE","severity":"HIGH","eventTime":"2025-01-01T00:00:00Z"}'
```

### List all high-severity findings
```bash
gcloud scc findings list organizations/ORG_ID \
  --filter="severity=\"HIGH\" AND state=\"ACTIVE\"" \
  --format="table(name,category,severity,eventTime)"
```

## Related Errors
- [GCP Access Transparency Error](/cloud/gcp/gcp-access-transparency-error/)
- [GCP VPC SC Error](/cloud/gcp/gcp-vpc-sc-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
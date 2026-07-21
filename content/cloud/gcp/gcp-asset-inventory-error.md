---
title: "[Solution] GCP Asset Inventory Error -- feed export search errors"
description: "Fix GCP Asset Inventory errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 153
---

Asset Inventory errors occur when there are issues with asset feeds, bulk export, or asset search queries.

## Common Causes
- Feed topic doesn't exist or lacks permissions
- Export timeout for large organizations
- Asset type filter syntax invalid
- Pub/Sub topic not in same project
- Cloud Asset API not enabled

## How to Fix

### 1. Enable Cloud Asset API
```bash
gcloud services enable cloudasset.googleapis.com --project=PROJECT_ID
```

### 2. List asset feeds
```bash
gcloud asset feeds list --organization=ORG_ID
```

### 3. Create asset feed
```bash
gcloud asset feeds create FEED_NAME \
  --pubsub-topic=projects/PROJECT/topics/TOPIC \
  --organization=ORG_ID \
  --asset-types="compute.googleapis.com/Instance"
```

### 4. Export assets
```bash
gcloud asset export \
  --organization=ORG_ID \
  --output-path=gs://bucket/assets/ \
  --asset-types="compute.googleapis.com/Instance"
```

### 5. Search assets
```bash
gcloud asset search-all-resources \
  --scope=organizations/ORG_ID \
  --query="state:RUNNING"
```

## Examples

### Export all IAM policies
```bash
gcloud asset export \
  --project=PROJECT_ID \
  --output-path=gs://bucket/iam-policies/ \
  --content-type=iam-policy
```

### Create feed for security monitoring
```bash
gcloud asset feeds create security-feed \
  --pubsub-topic=projects/SECURITY_PROJECT/topics/asset-changes \
  --organization=123456789 \
  --asset-types="iam.googleapis.com/ServiceAccount"
```

## Related Errors
- [GCP Resource Manager Error](/cloud/gcp/gcp-resource-manager-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
- [GCP Pub/Sub Error](/cloud/gcp/gcp-pubsub-error/)
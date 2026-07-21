---
title: "[Solution] GCP Cloud Run Traffic Split Error"
description: "Fix Cloud Run traffic split errors. Resolve revision routing, percentage-based traffic, and deployment rollback issues in Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run Traffic Split Error

The Cloud Run Traffic Split error occurs when traffic routing between revisions fails or does not distribute traffic as configured.

## Common Causes

- Target revision does not exist or is not ready
- Traffic percentage does not sum to 100%
- Revision is in a FAILED state
- Tag name conflicts with existing revision
- Service is updating and traffic cannot be shifted

## How to Fix

### 1. Check revision status
```bash
gcloud run revisions list --service=SERVICE_NAME --region=REGION
```

### 2. Split traffic between revisions
```bash
gcloud run services update-traffic SERVICE_NAME \
  --region=REGION \
  --to-revisions=REVISION_1=70,REVISION_2=30
```

### 3. Route to tagged revision
```bash
gcloud run services update-traffic SERVICE_NAME \
  --region=REGION \
  --to-tags=beta=REVISION_2
```

### 4. Rollback to previous revision
```bash
gcloud run services update-traffic SERVICE_NAME \
  --region=REGION \
  --to-revisions=LATEST_REVISION=100
```

## Examples

### Canary deployment
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:v2 \
  --no-traffic

gcloud run services update-traffic SERVICE_NAME \
  --region=REGION \
  --to-revisions=SERVICE_NAME-00001-abc=90,SERVICE_NAME-00002-def=10
```

### Check traffic split
```bash
gcloud run services describe SERVICE_NAME --region=REGION \
  --format="yaml(status.traffic)"
```

## Related Errors

- [GCP Cloud Run Revision]({{< relref "/cloud/gcp/gcp-cloud-run-revision" >}})
- [GCP Cloud Run Service]({{< relref "/cloud/gcp/gcp-cloud-run-service" >}})

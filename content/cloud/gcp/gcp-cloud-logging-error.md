---
title: "[Solution] GCP Cloud Logging Error — log-bucket router sink exclusion errors"
description: "Fix GCP Cloud Logging errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 148
---

Cloud Logging errors occur when there are issues with log buckets, routers, sinks, or exclusion filters.

## Common Causes
- Sink destination bucket not accessible
- Log router destination unreachable
- Exclusion filter syntax invalid
- Log bucket retention period exceeded
- Cloud Logging API not enabled

## How to Fix

### 1. Enable Logging API
```bash
gcloud services enable logging.googleapis.com --project=PROJECT_ID
```

### 2. List log buckets
```bash
gcloud logging buckets list
```

### 3. Create log bucket
```bash
gcloud logging buckets create BUCKET_NAME \
  --location=global \
  --retention-days=365 \
  --locked=false
```

### 4. Create logging sink
```bash
gcloud logging sinks create SINK_NAME \
  bigquery.googleapis.com/projects/PROJECT/datasets/DATASET \
  --log-filter='resource.type="gce_instance"' \
  --organization=ORG_ID
```

### 5. Update log exclusion
```bash
gcloud logging exclusions update EXCLUSION_NAME \
  --log-filter='jsonPayload.method="OPTIONS"' \
  --organization=ORG_ID
```

## Examples

### Route logs to Cloud Storage
```bash
gcloud logging sinks create storage-sink \
  storage.googleapis.com/my-log-bucket \
  --log-filter='severity>=ERROR'
```

### Create exclusion filter
```bash
gcloud logging exclusions create debug-exclusion \
  --log-filter='jsonPayload.logger="debug-logger"' \
  --disabled=false
```

## Related Errors
- [GCP Cloud Monitoring Error](/cloud/gcp/gcp-cloud-monitoring-error/)
- [GCP Error Reporting Error](/cloud/gcp/gcp-error-reporting-error/)
- [GCP Cloud Trace Error](/cloud/gcp/gcp-cloud-trace-error/)
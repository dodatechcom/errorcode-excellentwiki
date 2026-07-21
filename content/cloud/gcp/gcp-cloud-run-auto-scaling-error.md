---
title: "[Solution] GCP Cloud Run Auto Scaling Error"
description: "Fix Cloud Run auto scaling errors. Resolve instance scaling, concurrency, and cold start issues in Google Cloud Run services."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run Auto Scaling Error

The Cloud Run Auto Scaling error occurs when Cloud Run cannot scale instances up or down appropriately to handle incoming traffic patterns.

## Common Causes

- Max instances limit is reached
- Min instances is set too high for cost
- Concurrency per instance is too low
- Cold starts cause latency spikes
- Traffic patterns exceed scaling rate

## How to Fix

### 1. Check current scaling settings
```bash
gcloud run services describe SERVICE_NAME \
  --region=REGION \
  --format="yaml(spec.template.metadata.annotations)"
```

### 2. Update scaling parameters
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --min-instances=1 \
  --max-instances=100 \
  --concurrency=80 \
  --region=REGION
```

### 3. Enable CPU always-on for consistent workloads
```bash
gcloud run deploy SERVICE_NAME \
  --cpu-throttling=false \
  --min-instances=2 \
  --region=REGION
```

### 4. Monitor instance count
```bash
gcloud monitoring time-series list \
  --filter='metric.type="run.googleapis.com/instance_count"' \
  --interval-start-time=$(date -u -d "1 hour ago" +%Y-%m-%dT%H:%M:%SZ)
```

## Examples

### Deploy with burst capacity
```bash
gcloud run deploy my-api \
  --image=gcr.io/my-project/api:latest \
  --min-instances=2 \
  --max-instances=200 \
  --concurrency=100 \
  --cpu=4 \
  --memory=8Gi \
  --region=us-central1
```

### Check scaling metrics
```bash
gcloud monitoring time-series list \
  --filter='metric.type="run.googleapis.com/request_count"' \
  --interval-start-time=$(date -u -d "30 minutes ago" +%Y-%m-%dT%H:%M:%SZ)
```

## Related Errors

- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
- [GCP Cloud Run CPU Throttling Error]({{< relref "/cloud/gcp/gcp-cloud-run-cpu-throttling-error" >}})

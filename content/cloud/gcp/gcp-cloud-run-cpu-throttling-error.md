---
title: "[Solution] GCP Cloud Run CPU Throttling Error"
description: "Fix Cloud Run CPU throttling errors. Resolve CPU allocation, always-on CPU, and request latency issues in Google Cloud Run services."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run CPU Throttling Error

The Cloud Run CPU Throttling error occurs when CPU is only allocated during request processing, causing high latency for CPU-intensive workloads.

## Common Causes

- CPU is throttled between requests (CPU always-on not enabled)
- Background threads need CPU outside request context
- Concurrency is set too high causing CPU contention
- Startup tasks take too long without CPU allocation
- Billing mode uses CPU throttling by default

## How to Fix

### 1. Enable CPU always-on
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --cpu-throttling=false \
  --region=REGION
```

### 2. Increase CPU allocation
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --cpu=4 \
  --memory=8Gi \
  --region=REGION
```

### 3. Reduce concurrency
```bash
gcloud run deploy SERVICE_NAME \
  --concurrency=10 \
  --region=REGION
```

### 4. Enable min instances for background work
```bash
gcloud run deploy SERVICE_NAME \
  --min-instances=1 \
  --region=REGION
```

## Examples

### Deploy with always-on CPU
```bash
gcloud run deploy my-service \
  --image=gcr.io/my-project/my-image:latest \
  --cpu=2 \
  --memory=4Gi \
  --cpu-throttling=false \
  --min-instances=1 \
  --max-instances=20
```

### Check CPU throttling status
```bash
gcloud run services describe SERVICE_NAME \
  --region=REGION \
  --format="value(spec.template.spec.containers[0].resources)"
```

## Related Errors

- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
- [GCP Cloud Run Container Crash]({{< relref "/cloud/gcp/gcp-cloud-run-container-crash" >}})

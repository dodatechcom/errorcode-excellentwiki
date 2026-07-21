---
title: "[Solution] GCP Cloud Run Container Crash"
description: "Fix Cloud Run container crash errors. Debug startup failures, OOM kills, and container configuration issues in Google Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run Container Crash

The Cloud Run Container Crash error occurs when the container terminates unexpectedly during startup or while serving requests.

## Common Causes

- Application throws an unhandled exception at startup
- Container image has missing runtime dependencies
- Memory limit is too low causing OOM kills
- Startup probe fails before application is ready
- Port configuration does not match application listening port

## How to Fix

### 1. Check container logs
```bash
gcloud logging read "resource.type=cloud_run_revision \
  AND resource.labels.service_name=SERVICE_NAME" \
  --limit=50 --format="json(textPayload)"
```

### 2. Increase memory allocation
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --memory=2Gi \
  --cpu=2
```

### 3. Set startup probe
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --startup-probe=initial-delay-seconds=30
```

### 4. Configure port
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --port=8080
```

## Examples

### View crash logs
```bash
gcloud logging read "resource.type=cloud_run_revision \
  AND severity>=ERROR \
  AND resource.labels.service_name=my-service" \
  --limit=20
```

### Deploy with resource limits
```bash
gcloud run deploy my-service \
  --image=gcr.io/my-project/my-image:latest \
  --memory=4Gi \
  --cpu=4 \
  --max-instances=10 \
  --concurrency=50
```

## Related Errors

- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
- [GCP Cloud Run Revision]({{< relref "/cloud/gcp/gcp-cloud-run-revision" >}})

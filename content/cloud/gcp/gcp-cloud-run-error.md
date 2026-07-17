---
title: "[Solution] GCP Cloud Run Deployment Error"
description: "Fix GCP Cloud Run deployment errors. Resolve Cloud Run service issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "cloud-run", "serverless", "container", "deploy"]
weight: 5
---

A GCP Cloud Run deployment error occurs when services cannot be deployed to Cloud Run. This can be caused by container, configuration, or permission issues.

## Common Causes

- Container fails to start (non-zero exit code)
- Port configuration mismatch
- IAM permissions missing for Cloud Run
- Container image not found in Container Registry
- Service account not configured correctly

## How to Fix

### Deploy Service

```bash
gcloud run deploy my-service --image gcr.io/my-project/my-image \
  --platform managed --region us-central1 --allow-unauthenticated
```

### Check Service Status

```bash
gcloud run services describe my-service --region us-central1
```

### View Logs

```bash
gcloud logging read "resource.type=cloud_run_revision" --limit 50
```

### Check Container Logs

```bash
gcloud run services logs read my-service --region us-central1 --limit 20
```

### Set Memory and CPU

```bash
gcloud run deploy my-service --image gcr.io/my-project/my-image \
  --memory 512Mi --cpu 1 --min-instances 0 --max-instances 10
```

## Examples

```bash
# Example 1: Container start failed
# Container failed to start and crashed repeatedly
# Fix: check container logs and ensure PORT env var is set

# Example 2: Image not found
# failed to pull image: not found
# Fix: push image to Container Registry first
```

## Related Errors

- [GCP Cloud Functions Error]({{< relref "/cloud/gcp/gcp-cloud-functions-error" >}}) — Cloud Functions error
- [GCP Cloud Build Error]({{< relref "/cloud/gcp/gcp-cloud-build-error" >}}) — Cloud Build error

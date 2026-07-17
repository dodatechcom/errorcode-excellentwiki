---
title: "[Solution] GCP Cloud Deploy Error"
description: "Fix GCP Cloud Deploy errors. Resolve Cloud Deploy pipeline and release issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "cloud-deploy", "delivery", "pipeline", "release"]
weight: 5
---

A GCP Cloud Deploy error occurs when Cloud Deploy cannot create releases or rollouts. This can be caused by configuration, permission, or target issues.

## Common Causes

- Delivery pipeline does not exist
- IAM permissions not granted for Cloud Deploy
- Target cluster is not accessible
- Skaffold configuration errors
- Rollout failed or is stuck

## How to Fix

### Check Pipeline

```bash
gcloud deploy delivery-pipelines list --region=us-central1
```

### Create Release

```bash
gcloud deploy releases create my-release \
  --delivery-pipeline=my-pipeline \
  --region=us-central1 \
  --images=my-image=gcr.io/my-project/my-image
```

### Check Rollout

```bash
gcloud deploy rollouts list --delivery-pipeline=my-pipeline \
  --release=my-release --region=us-central1
```

### Promote Rollout

```bash
gcloud deploy rollouts promote my-rollout \
  --delivery-pipeline=my-pipeline \
  --release=my-release \
  --region=us-central1
```

## Examples

```bash
# Example 1: Pipeline not found
# Delivery pipeline not found
# Fix: create the delivery pipeline

# Example 2: Target unreachable
# Failed to connect to target cluster
# Fix: verify cluster access and permissions
```

## Related Errors

- [GCP Cloud Build Error]({{< relref "/cloud/gcp/gcp-cloud-build-error" >}}) — Cloud Build error
- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}}) — GKE cluster error

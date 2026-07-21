---
title: "[Solution] GCP Cloud Run Service Not Found"
description: "NOT_FOUND when the specified Cloud Run service does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Run Service Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Service name is incorrect
- Service was deleted
- Service in different project
- Service in different region

## How to Fix

### List services

```bash
gcloud run services list --region us-central1
```
### Check service

```bash
gcloud run services describe my-service --region us-central1
```
### Deploy service

```bash
gcloud run deploy my-service --image gcr.io/my-project/my-image --region us-central1
```

## Examples

- Service my-service not found in region us-central1
- Service deleted but URL still referenced

## Related Errors

- [Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}}) -- General Cloud Run errors
- [Revision Not Found]({{< relref "/cloud/gcp/cloudrun-revision-not-found" >}}) -- Revision not found

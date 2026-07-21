---
title: "[Solution] GCP Cloud Run Revision Not Found"
description: "NOT_FOUND when the specified Cloud Run revision does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Run Revision Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Revision name is incorrect
- Revision was deleted
- Revision was scaled to zero
- Revision in different project

## How to Fix

### List revisions

```bash
gcloud run revisions list --service my-service --region us-central1
```
### Check revision

```bash
gcloud run revisions describe my-revision --region us-central1
```
### Deploy new revision

```bash
gcloud run deploy my-service --image gcr.io/my-project/my-image:latest --region us-central1
```

## Examples

- Revision my-revision was scaled to zero
- Revision deleted during cleanup

## Related Errors

- [Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}}) -- General Cloud Run errors
- [Service Not Found]({{< relref "/cloud/gcp/cloudrun-service-not-found" >}}) -- Service not found

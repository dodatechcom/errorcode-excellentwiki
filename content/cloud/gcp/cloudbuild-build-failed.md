---
title: "[Solution] GCP Cloud Build Build Failed"
description: "BUILD_FAILURE when a Cloud Build build fails."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Build Build Failed` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Build step failed
- Dockerfile not found
- Source not accessible
- Build timeout exceeded

## How to Fix

### Check build

```bash
gcloud builds describe BUILD_ID --project my-project
```
### List builds

```bash
gcloud builds list --project my-project --limit=5
```
### Retry build

```bash
gcloud builds submit --project my-project --config=cloudbuild.yaml .
```

## Examples

- Build step 1/3 failed with exit code 1
- Dockerfile not found in the source directory

## Related Errors

- [Cloud Build Error]({{< relref "/cloud/gcp/gcp-cloud-build-error" >}}) -- General Cloud Build errors
- [Trigger Not Found]({{< relref "/cloud/gcp/cloudbuild-trigger-not-found" >}}) -- Trigger not found

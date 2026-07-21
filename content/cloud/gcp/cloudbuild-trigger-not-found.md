---
title: "[Solution] GCP Cloud Build Trigger Not Found"
description: "NOT_FOUND when the specified Cloud Build trigger does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Build Trigger Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Trigger name is incorrect
- Trigger was deleted
- Trigger in different project
- Trigger is disabled

## How to Fix

### List triggers

```bash
gcloud builds triggers list --project my-project
```
### Check trigger

```bash
gcloud builds triggers describe my-trigger --project my-project
```
### Create trigger

```bash
gcloud builds triggers create github --repo-name=my-repo --repo-owner=my-org --branch-pattern=main --build-config=cloudbuild.yaml --project my-project
```

## Examples

- Trigger my-trigger not found in project
- Trigger was deleted as part of cleanup

## Related Errors

- [Cloud Build Error]({{< relref "/cloud/gcp/gcp-cloud-build-error" >}}) -- General Cloud Build errors
- [Build Failed]({{< relref "/cloud/gcp/cloudbuild-build-failed" >}}) -- Build failures

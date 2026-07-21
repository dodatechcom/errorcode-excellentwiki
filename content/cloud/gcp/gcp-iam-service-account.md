---
title: "[Solution] GCP Service Account Error"
description: "NOT_FOUND or PERMISSION_DENIED for service account operations."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Account Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Service account email is incorrect
- Service account was deleted
- Service account key is expired
- Service account does not exist in the project

## How to Fix

### List service accounts

```bash
gcloud iam service-accounts list --project my-project
```
### Check service account

```bash
gcloud iam service-accounts describe my-sa@my-project.iam.gserviceaccount.com
```
### Create service account

```bash
gcloud iam service-accounts create my-sa --display-name "My Service Account" --project my-project
```

## Examples

- Service account my-sa not found in project
- Key expired 90 days ago

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}}) -- General IAM errors
- [Key Expired]({{< relref "/cloud/gcp/gcp-iam-key-expired" >}}) -- Key issues

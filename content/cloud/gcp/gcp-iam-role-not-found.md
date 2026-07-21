---
title: "[Solution] GCP IAM Role Not Found"
description: "NOT_FOUND when the specified IAM role does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IAM Role Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Role name is incorrect
- Role was deleted
- Role in different project
- Role is not accessible to the caller

## How to Fix

### List roles

```bash
gcloud iam roles list
```
### Check role

```bash
gcloud iam roles describe myRole --project my-project
```
### Create custom role

```bash
gcloud iam roles create myRole --project my-project --title "My Role" --permissions storage.objects.get,storage.objects.list
```

## Examples

- Role myRole not found in project my-project
- Role was deleted but still referenced in policy

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}}) -- General IAM errors
- [Custom Role]({{< relref "/cloud/gcp/gcp-iam-custom-role" >}}) -- Custom roles

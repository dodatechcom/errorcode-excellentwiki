---
title: "[Solution] GCP IAM Permission Denied"
description: "Fix GCP IAM permission denied errors. Resolve Google Cloud IAM access issues."
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

A GCP IAM permission denied error occurs when a user, service account, or application lacks the required IAM permissions to perform an action.

## Common Causes

- IAM role not attached to the identity for the target resource
- Organization policy constraints block the action
- Service account lacks the necessary scopes
- Resource-level policy overrides project-level IAM
- Quota for IAM policy bindings exceeded

## How to Fix

### Check Current Permissions

```bash
gcloud projects get-iam-policy my-project \
  --flatten="bindings[].members" \
  --format="table(bindings.role)"
```

### Grant Required Role

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:admin@example.com" \
  --role="roles/compute.instanceAdmin.v1"
```

### Check Service Account

```bash
gcloud iam service-accounts describe my-sa@my-project.iam.gserviceaccount.com
```

### Test Permission

```bash
gcloud projects test-iam-permissions my-project \
  --permissions=compute.instances.list
```

### Grant Folder-Level Permission

```bash
gcloud resource-manager folders add-iam-policy-binding FOLDER_ID \
  --member="user:admin@example.com" \
  --role="roles/viewer"
```

## Examples

```bash
# Example 1: Compute Engine access
# The caller does not have permission to use this
# Fix: add roles/compute.instanceAdmin.v1

# Example 2: Service account scope
# Request had insufficient authentication scopes
# Fix: add required scopes to service account
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — AWS IAM permission denied
- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) — Azure AD error

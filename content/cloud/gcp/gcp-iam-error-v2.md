---
title: "[Solution] GCP IAM — permission denied on resource"
description: "Fix GCP IAM permission denied on resource. Resolve Google Cloud IAM access and binding issues."
cloud: ["gcp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gcp", "iam", "permission", "denied", "resource", "access", "binding"]
weight: 5
---

A GCP IAM permission denied on resource error means the calling identity lacks the required IAM role for the specific resource. The request is authenticated but not authorized by resource-level IAM policy.

## What This Error Means

GCP IAM operates at organization, folder, project, and resource levels. A permission denied error on a resource means the identity (user, service account, or group) does not have a role that grants the requested permission on that specific resource. Unlike project-level IAM, resource-level bindings only apply to that resource. The error message includes the denied permission (e.g., `compute.instances.get`) and the resource name.

## Common Causes

- IAM role not bound to the identity at the resource or project level
- Resource-level IAM policy overrides project-level bindings
- Organization policy constraint blocking the action
- Service account lacks necessary OAuth scopes
- Custom role missing required permission
- IAM binding applies to a different project than the resource

## How to Fix

### Check Resource IAM Policy

```bash
gcloud projects get-iam-policy my-project \
  --flatten="bindings[].members" \
  --format="table(bindings.role, bindings.members)"
```

### Check Resource-Level Permissions

```bash
gcloud compute instances get-iam-policy my-instance \
  --zone us-central1-a
```

### Grant Resource-Level Permission

```bash
gcloud compute instances add-iam-policy-binding my-instance \
  --zone us-central1-a \
  --member="user:admin@example.com" \
  --role="roles/compute.instanceAdmin.v1"
```

### Grant Project-Level Permission

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:admin@example.com" \
  --role="roles/editor"
```

### Test Permissions

```bash
gcloud projects test-iam-permissions my-project \
  --permissions=compute.instances.get,compute.instances.list
```

### Check Service Account Scopes

```bash
gcloud compute instances describe my-instance \
  --zone us-central1-a \
  --query='serviceAccounts[].scopes'
```

### Check Organization Policy

```bash
gcloud resource-manager org-policies list \
  --project my-project
```

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}}) — original IAM error
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — AWS IAM denied
- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error-v2" >}}) — ForbiddenByPolicy

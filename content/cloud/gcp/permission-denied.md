---
title: "GCP Permission Denied"
description: "PermissionDenied - The caller does not have permission"
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "iam", "permission", "access", "authorization"]
weight: 5
---

The `PermissionDenied` error occurs when a Google Cloud identity (user, service account, or application) attempts to access a resource or perform an action without the required IAM permissions.

## Common Causes

- The IAM role is not attached to the identity for the target resource
- A resource-level policy overrides the project-level IAM binding
- The service account lacks the necessary scopes
- Organization policy constraints block the action

## How to Fix

Grant the required role to the identity:

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:admin@example.com" \
  --role="roles/storage.objectViewer"
```

Verify current permissions:

```bash
gcloud projects get-iam-policy my-project \
  --flatten="bindings[].members" \
  --format="table(bindings.role)"
```

## Examples

- A service account tries to read a Cloud Storage object but only has `roles/viewer`
- A user attempts to create a Compute Engine instance without `roles/compute.instanceAdmin.v1`

## Related Errors

- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded" >}})
- [AWS S3 Access Denied]({{< relref "/cloud/aws/s3-access-denied" >}})
- [Azure Authentication Failed]({{< relref "/cloud/azure/authentication-failed" >}})

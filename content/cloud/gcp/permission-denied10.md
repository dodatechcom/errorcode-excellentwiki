---
title: "GCP Permission Denied: The Caller Does Not Have Permission"
description: "Permission denied: The caller does not have permission — Fix Google Cloud IAM permission errors."
cloud: ["gcp"]
error-types: ["api-error"]
severities: ["error"]
tags: ["gcp", "iam", "permission-denied", "access", "authorization", "cloud-platform"]
weight: 5
---

The `Permission denied: The caller does not have permission` error occurs when a Google Cloud identity (user, service account, or application) attempts to access a resource or perform an action without the required IAM permissions. This is distinct from authentication failures — the identity is valid but lacks authorization.

## Common Causes

- The IAM role is not bound to the identity at the project, folder, or resource level
- A resource-level policy (e.g., bucket IAM policy) does not grant access
- The service account lacks the required OAuth scopes
- Organization policy constraints block the action
- The API is not enabled in the project

## How to Fix

Check the IAM policy for the project:

```bash
gcloud projects get-iam-policy my-project \
  --flatten="bindings[].members" \
  --format="table(bindings.role, bindings.members)"
```

Grant the required role:

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:admin@example.com" \
  --role="roles/compute.instanceAdmin.v1"
```

For resource-level access:

```bash
gcloud storage buckets add-iam-policy-binding gs://my-bucket \
  --member="serviceAccount:my-sa@my-project.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

Enable the required API:

```bash
gcloud services enable compute.googleapis.com --project=my-project
```

## Examples

- A service account with `roles/viewer` tries to create a Compute Engine instance
- A user can list buckets but cannot read objects because they only have `roles/storage.legacyBucketReader`
- A Cloud Function cannot access a BigQuery table because the function's service account lacks `roles/bigquery.dataViewer`

## Related Errors

- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — quota limits.
- [AWS AccessDenied]({{< relref "/cloud/aws/access-denied" >}}) — AWS equivalent.
- [Azure Auth Failed]({{< relref "/cloud/azure/auth-failed" >}}) — Azure equivalent.

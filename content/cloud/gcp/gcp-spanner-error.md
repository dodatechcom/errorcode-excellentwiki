---
title: "[Solution] GCP Cloud Spanner Error"
description: "Fix GCP Cloud Spanner errors. Resolve Spanner connectivity and configuration issues."
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

A GCP Cloud Spanner error occurs when operations on Cloud Spanner fail. This can be caused by connectivity, permission, or configuration issues.

## Common Causes

- Instance does not exist or is not ready
- IAM permissions not granted for Spanner operations
- Database schema changes are in progress
- Query exceeds resource limits
- Node count too low for workload

## How to Fix

### Check Instance

```bash
gcloud spanner instances describe my-instance
```

### List Databases

```bash
gcloud spanner databases list --instance=my-instance
```

### Execute Query

```bash
gcloud spanner databases execute-sql my-database --instance=my-instance \
  --sql="SELECT 1"
```

### Add Nodes

```bash
gcloud spanner instances update my-instance --num-nodes=5
```

### Check IAM

```bash
gcloud spanner instances get-iam-policy my-instance
```

## Examples

```bash
# Example 1: Instance not found
# Instance not found: projects/my-project/instances/my-instance
# Fix: create the Spanner instance

# Example 2: Insufficient nodes
# The instance does not have enough nodes
# Fix: increase node count
```

## Related Errors

- [GCP Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}}) — Cloud SQL error
- [GCP Firestore Error]({{< relref "/cloud/gcp/gcp-firestore-error" >}}) — Firestore error

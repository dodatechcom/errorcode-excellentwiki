---
title: "[Solution] GCP Firestore Error"
description: "Fix GCP Firestore errors. Resolve Firestore database operation issues."
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

A GCP Firestore error occurs when operations on Firestore fail. This can be caused by permission, configuration, or query issues.

## Common Causes

- Firestore database not created or initialized
- IAM permissions not granted for Firestore
- Document does not exist
- Query has missing composite index
- Quota exceeded for operations

## How to Fix

### Check Database

```bash
gcloud firestore databases list
```

### Create Database

```bash
gcloud firestore databases create --location=us-central
```

### Check IAM

```bash
gcloud projects get-iam-policy my-project \
  --flatten="bindings[].members" \
  --format="table(bindings.role)" | grep firestore
```

### List Collections

```bash
gcloud firestore collections list
```

### Create Composite Index

```bash
gcloud firestore indexes composite create \
  --collection-group=my-collection \
  --field-config=field-path=field1,order=ASCENDING \
  --field-config=field-path=field2,order=DESCENDING
```

## Examples

```bash
# Example 1: Database not found
# Cloud Firestore API has not been used in project
# Fix: enable Firestore API and create database

# Example 2: Missing index
# The query requires an index
# Fix: create the composite index
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}}) — BigQuery query error
- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}}) — IAM permission denied

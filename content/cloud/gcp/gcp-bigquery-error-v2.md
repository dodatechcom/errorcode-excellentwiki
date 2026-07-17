---
title: "[Solution] GCP BigQuery — dataset not found"
description: "Fix BigQuery dataset not found. Resolve dataset access and resource location issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A BigQuery dataset not found error means the specified dataset does not exist in the project, or the calling identity lacks `bigquery.datasets.get` permission. The query or data operation cannot proceed.

## What This Error Means

BigQuery datasets are project-scoped resources identified by `project.dataset_id`. A "not found" error can mean either the dataset truly does not exist, or the caller lacks the `bigquery.datasets.get` permission which is required to list or check dataset existence. This creates an ambiguity — BigQuery returns "not found" even when the dataset exists but the caller has no access. The error also occurs when the dataset's location (region) is mismatched with the query job configuration.

## Common Causes

- Dataset does not exist in the specified project
- Dataset ID is misspelled or wrong project specified
- IAM role lacks `bigquery.datasets.get` permission
- Dataset is in a different location than the job configuration
- BigQuery Data Transfer Service cannot access the source dataset
- Cross-region access not enabled for the dataset

## How to Fix

### List Available Datasets

```bash
bq ls --project_id=my-project
```

### Check Dataset Exists

```bash
bq show my-project:my_dataset
```

### Check Permissions

```bash
bq show --format=prettyjson my-project:my_dataset | grep -A5 "access"
```

### Grant Dataset Access

```bash
bq update --set_default_dataset my-project:my_dataset \
  --grant_access user:admin@example.com:READER
```

### Create Missing Dataset

```bash
bq mk --dataset my-project:my_dataset \
  --location=US
```

### Fix Location Mismatch

```bash
# Ensure job location matches dataset location
bq query --location=US \
  "SELECT * FROM my-project.my_dataset.my_table"
```

### Grant IAM Role

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:admin@example.com" \
  --role="roles/bigquery.dataViewer"
```

### Verify Table Path

```bash
# Correct format: project.dataset.table
bq show my-project:my_dataset.my_table
```

### Debug with API

```bash
bq show --format=prettyjson my-project:my_dataset 2>&1 | head -20
# NotFound: (404) Dataset not found
# PermissionDenied: (403) Access denied — missing bigquery.datasets.get
```

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error-v2" >}}) — permission denied
- [GCP Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error-v2" >}}) — connection invalid
- [GCP Firestore Error]({{< relref "/cloud/gcp/gcp-firestore-error-v2" >}}) — permission denied

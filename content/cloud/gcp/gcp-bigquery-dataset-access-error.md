---
title: "[Solution] GCP BigQuery Dataset Access Error"
description: "Fix BigQuery dataset access errors. Resolve dataset permissions, authorized datasets, and cross-project access issues in BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Dataset Access Error

The BigQuery Dataset Access error occurs when users or service accounts cannot access a BigQuery dataset due to IAM, ACL, or cross-project permission issues.

## Common Causes

- Dataset-level IAM policy does not include the caller
- ACL entries conflict with IAM policy bindings
- Cross-project authorized dataset is not in the access list
- Default dataset is not set for the query
- Service account does not have bigquery.dataViewer role

## How to Fix

### 1. Check dataset access
```bash
bq show --format=json PROJECT_ID:DATASET > dataset_info.json
```

### 2. Grant dataset access
```bash
bq update --set_dataset_default_region=US \
  --dataset PROJECT_ID:DATASET
bq show --format=prettyjson PROJECT_ID:DATASET | jq '.access += [{"userByEmail":"user@example.com","role":"READER"}]'
```

### 3. Add IAM binding to dataset
```bash
bq show --format=json PROJECT_ID:DATASET > ds.json
bq update --source=ds.json PROJECT_ID:DATASET
```

### 4. Grant cross-project access
```bash
bq query --project_id=PROJECT_A \
  'SELECT * FROM PROJECT_B.DATASET.TABLE'
```

## Examples

### Grant reader access
```bash
bq show --format=prettyjson PROJECT_ID:DATASET | \
  jq '.access += [{"userByEmail":"analyst@company.com","role":"READER"}]' | \
  bq update --source=/dev/stdin PROJECT_ID:DATASET
```

### List dataset permissions
```bash
bq show --format=prettyjson PROJECT_ID:DATASET | jq '.access'
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}})

---
title: "[Solution] GCP BigQuery Data Transfer Error"
description: "Fix BigQuery Data Transfer errors. Resolve scheduled query, transfer config, and cross-region data transfer issues in BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Data Transfer Error

The BigQuery Data Transfer error occurs when scheduled queries or data transfers fail to execute due to configuration, permission, or connectivity issues.

## Common Causes

- Transfer config references a non-existent source dataset
- Service account lacks bigquery.dataTransfer.user role
- Schedule expression is invalid or timezone is wrong
- Cross-region transfer violates data location policy
- Source data format does not match expected schema

## How to Fix

### 1. List transfer configs
```bash
bq ls --transfer_config --project_id=PROJECT_ID --format="table(name,displayName,schedule)"
```

### 2. Create scheduled query
```bash
bq mk --transfer_config \
  --project_id=PROJECT_ID \
  --target_dataset=my_dataset \
  --display_name="Daily Aggregation" \
  --schedule="every 24 hours" \
  --params='{"query":"SELECT DATE(timestamp) as day, COUNT(*) FROM `project.dataset.table` GROUP BY 1"}'
```

### 3. Check transfer run status
```bash
bq ls --transfer_run CONFIG_ID --project_id=PROJECT_ID --format="table(name,state)"
```

### 4. Grant transfer permissions
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataTransfer.user"
```

## Examples

### Create Cloud Storage transfer
```bash
bq mk --transfer_config \
  --project_id=PROJECT_ID \
  --target_dataset=imports \
  --display_name="GCS Import" \
  --data_source=google_cloud_storage \
  --params='{"bucket_name":"my-bucket","file_path_pattern":"data/*.csv"}'
```

### Check transfer logs
```bash
gcloud logging read "resource.type=bigquery_data_transfer_config" \
  --limit=20
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP Cloud Storage Transfer]({{< relref "/cloud/gcp/gcp-cloud-storage-transfer" >}})

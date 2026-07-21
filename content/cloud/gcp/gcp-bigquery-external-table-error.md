---
title: "[Solution] GCP BigQuery External Table Error"
description: "Fix BigQuery external table errors. Resolve BigQuery connection to Cloud Storage, Drive, and external data sources in BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery External Table Error

The BigQuery External Table error occurs when BigQuery cannot query external data sources like Cloud Storage, Bigtable, or Google Drive.

## Common Causes

- External table definition has incorrect file format
- Cloud Storage path does not contain matching files
- Service account lacks storage.objectViewer permission
- External table schema does not match data files
- Hive partitioning configuration is incorrect

## How to Fix

### 1. Create external table
```bash
bq mk --table \
  --external_data_bounds=gs://BUCKET/data/*.csv \
  --source_format=CSV \
  PROJECT_ID:DATASET.EXTERNAL_TABLE \
  schema.json
```

### 2. Verify Cloud Storage access
```bash
gsutil ls gs://BUCKET/data/
```

### 3. Check external table definition
```bash
bq show --format=json PROJECT_ID:DATASET.EXTERNAL_TABLE > ext.json
```

### 4. Grant storage access to BigQuery
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:BQ_SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

## Examples

### Create BigQuery external table from Parquet
```bash
bq mk --table \
  --external_data_bounds=gs://bucket/data/*.parquet \
  --source_format=PARQUET \
  PROJECT_ID:DATASET.ext_table
```

### Query external table
```sql
SELECT * FROM `PROJECT_ID.DATASET.EXTERNAL_TABLE`
LIMIT 10;
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP Bigquery Table Not Found]({{< relref "/cloud/gcp/bigquery-table-not-found" >}})

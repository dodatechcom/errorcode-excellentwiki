---
title: "[Solution] GCP BigQuery Connection Error"
description: "Fix BigQuery connection errors. Resolve BigQuery connection to Cloud SQL, Spanner, and external data sources in Google BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Connection Error

The BigQuery Connection error occurs when BigQuery cannot establish or maintain connections to external data sources like Cloud SQL or Spanner.

## Common Causes

- BigQuery Connection resource is not created
- Connection name is malformed or references wrong region
- Cloud SQL instance is not accessible from BigQuery
- Service account lacks bigquery.connectionUser role
- Connection secret has expired or been rotated

## How to Fix

### 1. Create Cloud SQL connection
```bash
bq mk --connection --location=REGION --connection_type=CloudSQL \
  my-cloudsql-connection \
  --project=PROJECT_ID
```

### 2. Grant connection permission
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.connectionUser"
```

### 3. Query external connection
```sql
SELECT * FROM EXTERNAL_QUERY(
  'PROJECT_ID.REGION.CONNECTION_NAME',
  'SELECT * FROM my_table'
);
```

### 4. List connections
```bash
bq show --connection --location=REGION CONNECTION_NAME
```

## Examples

### Create Cloud Spanner connection
```bash
bq mk --connection --location=REGION --connection_type=CloudSpanner \
  my-spanner-connection \
  --instance-id=INSTANCE_ID \
  --database=DATABASE_ID
```

### Check connection details
```bash
bq show --connection --location=REGION CONNECTION_NAME
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}})

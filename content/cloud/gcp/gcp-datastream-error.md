---
title: "[Solution] GCP Datastream Error — source connection backfill errors"
description: "Fix GCP Datastream errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 134
---

Datastream errors occur when there are issues with source database connections, stream configuration, or backfill operations.

## Common Causes
- Source database connection credentials invalid
- Backfill job exceeds allocated resources
- Network connectivity between source and Datastream
- Stream configuration incompatible with schema
- Datastream API not enabled

## How to Fix

### 1. Enable Datastream API
```bash
gcloud services enable datastream.googleapis.com --project=PROJECT_ID
```

### 2. List streams and connection profiles
```bash
gcloud datastream streams list --location=REGION
gcloud datastream connection-profiles list --location=REGION
```

### 3. Create connection profile
```bash
gcloud datastream connection-profiles create PROFILE_NAME \
  --location=REGION \
  --type=mysql \
  --mysql-profile=host=HOST,port=3306,user=USER,password=PASSWORD
```

### 4. Create stream
```bash
gcloud datastream streams create STREAM_NAME \
  --location=REGION \
  --source-connection-profile=SOURCE_PROFILE \
  --destination-connection-profile=DEST_PROFILE \
  --display-name="MySQL to BigQuery"
```

### 5. Start backfill
```bash
gcloud datastream streams start BACKFILL \
  STREAM_NAME --location=REGION
```

## Examples

### Create PostgreSQL to BigQuery stream
```bash
gcloud datastream streams create pg-to-bq \
  --location=us-central1 \
  --source-connection-profile=pg-source \
  --destination-connection-profile=bq-dest \
  --display-name="PostgreSQL to BigQuery"
```

### Check stream status
```bash
gcloud datastream streams describe my-stream \
  --location=us-central1 \
  --format="yaml(name,state,error)"
```

## Related Errors
- [GCP Cloud SQL Error](/cloud/gcp/gcp-cloud-sql-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP Dataflow Error](/cloud/gcp/gcp-dataflow-error/)
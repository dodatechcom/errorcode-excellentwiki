---
title: "[Solution] GCP BigQuery Quotas Error"
description: "Fix BigQuery quotas errors. Resolve query limits, storage quotas, and API rate limit issues in Google BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Quotas Error

The BigQuery Quotas error occurs when BigQuery operations exceed project or user-level quotas for queries, storage, or API calls.

## Common Causes

- Daily query limit (TB) is exceeded for on-demand queries
- Concurrent query limit is reached
- Storage limit per dataset is exceeded
- API rate limit (requests per minute) is hit
- Slot quota for reservation is exhausted

## How to Fix

### 1. Check current usage
```bash
bq show --project=PROJECT_ID --format=json usage > usage.json
```

### 2. Monitor query execution
```bash
bq query --project_id=PROJECT_ID \
  'SELECT job_id, total_bytes_processed, creation_time FROM `region-us`.INFORMATION_SCHEMA.JOBS ORDER BY creation_time DESC LIMIT 10'
```

### 3. Request quota increase
```bash
gcloud alpha quota requests submit \
  --service=bigquery.googleapis.com \
  --quota=query_usage_on_demand \
  --value=1000
```

### 4. Use batch queries to reduce on-demand usage
```bash
bq query --batch --project_id=PROJECT_ID 'SELECT * FROM dataset.table'
```

## Examples

### Check storage usage
```bash
bq show --format=prettyjson PROJECT_ID:DATASET | jq '.numBytes'
```

### Monitor slot usage
```bash
bq query --project_id=PROJECT_ID \
  'SELECT * FROM `region-us`.INFORMATION_SCHEMA.JOBS WHERE job_type = "QUERY" ORDER BY creation_time DESC LIMIT 5'
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP Query Exceeded]({{< relref "/cloud/gcp/gcp-query-exceeded" >}})

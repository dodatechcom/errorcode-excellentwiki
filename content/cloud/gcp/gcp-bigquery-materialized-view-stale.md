---
title: "[Solution] GCP BigQuery Materialized View Stale"
description: "Fix BigQuery materialized view staleness issues. Resolve refresh delays, partition alignment, and incremental refresh errors in BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Materialized View Stale

The BigQuery Materialized View Stale error occurs when a materialized view does not reflect the latest data from the base table due to refresh or configuration issues.

## Common Causes

- Automatic refresh has not yet run since base table updates
- Incremental refresh cannot handle schema changes in base table
- Partitioned materialized view has partition alignment mismatches
- Max staleness threshold has been exceeded
- Base table partition expiration conflicts with view refresh

## How to Fix

### 1. Check materialized view status
```bash
bq show --project=PROJECT_ID --format=json \
  DATASET.MATERIALIZED_VIEW > mv_info.json
```

### 2. Check last refresh time
```sql
SELECT
  materialized_view_name,
  refresh_watermark_limit,
  last_refresh_time
FROM `PROJECT_ID region-us`.INFORMATION_SCHEMA.MATERIALIZED_VIEWS;
```

### 3. Increase max staleness
```sql
CREATE MATERIALIZED VIEW `DATASET.MV_NAME`
OPTIONS (
  max_staleness = INTERVAL 4 HOUR
) AS
SELECT * FROM `DATASET.BASE_TABLE`;
```

### 4. Force refresh by querying
```sql
SELECT MAX(refresh_time) FROM `PROJECT_ID.DATASET.MV_NAME`;
```

## Examples

### Create materialized view with explicit staleness
```sql
CREATE MATERIALIZED VIEW `analytics.daily_sales`
OPTIONS (
  enable_refresh = true,
  refresh_interval_minutes = 30,
  max_staleness = INTERVAL 2 HOUR
) AS
SELECT
  DATE(transaction_date) as day,
  SUM(amount) as total_sales
FROM `analytics.transactions`
GROUP BY 1;
```

### Check refresh history
```sql
SELECT *
FROM `region-us`.INFORMATION_SCHEMA.JOBS
WHERE statement_type = 'REFRESH_MATERIALIZED_VIEW'
ORDER BY creation_time DESC
LIMIT 5;
```

## Related Errors

- [GCP Materialized View]({{< relref "/cloud/gcp/gcp-materialized-view" >}})
- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})

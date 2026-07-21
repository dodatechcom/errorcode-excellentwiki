---
title: "[Solution] GCP BigQuery Dataform Execution Error"
description: "Fix BigQuery Dataform execution errors. Resolve Dataform workflow, SQL transformation, and compilation issues in GCP BigQuery Dataform."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Dataform Execution Error

The BigQuery Dataform Execution error occurs when Dataform workflows fail to compile, execute, or produce expected results in BigQuery.

## Common Causes

- SQL compilation errors in Dataform definitions
- Dataform repository is not connected to a Git branch
- BigQuery API is not enabled for Dataform operations
- Workspace conflicts between developers
- Dependencies reference tables that do not exist

## How to Fix

### 1. Check Dataform workspace
```bash
gcloud dataform workspaces describe WORKSPACE_PATH \
  --repository=REPOSITORY --location=REGION
```

### 2. Compile Dataform
```bash
gcloud dataform workspaces compile WORKSPACE_PATH \
  --repository=REPOSITORY --location=REGION
```

### 3. Create Dataform repository
```bash
gcloud dataform repositories create REPOSITORY_NAME \
  --location=REGION
```

### 4. Install Dataform dependencies
```bash
cd WORKSPACE_PATH
npm install @dataform/core
```

## Examples

### Dataform SQL definition
```sql
-- definitions/my_table.sqlx
config {
  type: "table",
  schema: "analytics",
  description: "Daily aggregated metrics"
}

SELECT
  DATE(created_at) as date,
  COUNT(*) as total_records
FROM ${ref("source_table")}
GROUP BY 1
```

### Trigger Dataform workflow
```bash
gcloud dataform workflowschedules create SCHEDULE_NAME \
  --repository=REPOSITORY \
  --location=REGION \
  --cron="0 6 * * *" \
  --workspace-path="workspace"
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP Query Execution Error]({{< relref "/cloud/gcp/gcp-query-execution-error" >}})

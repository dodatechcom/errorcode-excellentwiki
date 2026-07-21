---
title: "[Solution] TiDB Index Backfill Error — How to Fix"
description: "Fix TiDB index backfill errors when online DDL index creation cannot complete due to resource constraints"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Index Backfill Error

Index backfill errors occur when TiDB's online DDL cannot complete index creation or reconstruction because the backfill process fails or is too slow.

## Why It Happens

- Table is too large for the backfill process to complete within timeout
- TiKV nodes are overloaded during backfill
- Backfill workers are insufficient for the workload
- Disk space is insufficient for temporary backfill data
- Transaction conflicts during backfill cause repeated retries

## Common Error Messages

```
DDL: index backfill is too slow, exceeding timeout
```

```
error: index backfill failed due to transaction conflict
```

```
DDL: backfill workers exhausted
```

## How to Fix It

### 1. Monitor DDL Progress

```sql
SHOW DDL JOBS;
SHOW DDL JOB STATUS 1;
```

### 2. Increase Backfill Workers

```sql
SET GLOBAL tidb_ddl_reorg_worker_cnt = 32;
```

### 3. Increase Backfill Batch Size

```sql
SET GLOBAL tidb_ddl_reorg_batch_size = 1024;
```

### 4. Resume Failed DDL

```sql
-- Cancel and retry failed DDL
ADMIN CANCEL DDL JOBS 1;
-- Retry the DDL
CREATE INDEX idx_name ON mytable (name);
```

## Examples

```
mysql> SHOW DDL JOBS;
+--------+------------+------------------+--------------+-----------+-----------+-----------+------------------+-------+--------+-----------+
| job_id | table_name | schema_name      | job_type     | schema_id | table_id | row_count | start_time       | state | end    | position  |
+--------+------------+------------------+--------------+-----------+-----------+-----------+------------------+-------+--------+-----------+
| 1      | orders     | mydb             | add index    | 1         | 100       | 5000000   | 2024-01-15 10:00 | running| NULL  | ...
+--------+------------+------------------+--------------+-----------+-----------+-----------+------------------+-------+--------+-----------+
```

## Prevent It

- Schedule index creation during low-traffic periods
- Monitor DDL job progress and resource usage
- Adjust worker count and batch size for large tables

## Related Pages

- [TiDB Index Backfill Error](/tools/tidb/tidb-index-backfill-error)
- [TiDB Index Error](/tools/tidb/tidb-index-error)
- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)

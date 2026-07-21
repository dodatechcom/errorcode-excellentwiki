---
title: "[Solution] TiDB DDL Pause Error — How to Fix"
description: "Fix TiDB DDL pause errors when DDL operations are paused and cannot proceed"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB DDL Pause Error

DDL pause errors occur when TiDB DDL operations are paused and cannot resume, blocking schema changes and causing application failures.

## Why It Happens

- DDL jobs are manually paused by an administrator
- DDL owner lease expired during a long operation
- Schema version conflict prevents DDL from proceeding
- Too many pending DDL jobs cause queue congestion
- TiDB node restart during active DDL

## Common Error Messages

```
DDL: job is paused, cannot proceed
```

```
error: DDL operation is paused by user
```

```
DDL: schema version is locked by another operation
```

## How to Fix It

### 1. Check DDL Job Status

```sql
SHOW DDL JOBS;
SHOW DDL JOB STATUS 1;
```

### 2. Resume Paused DDL

```sql
-- Resume a paused DDL job
RESUME DDL JOBS 1;
```

### 3. Cancel Blocked DDL

```sql
-- Cancel a stuck DDL job
CANCEL DDL JOBS 1,2,3;
```

### 4. Check DDL Owner

```sql
SELECT * FROM tidb_ddl_owner;
```

## Examples

```
mysql> SHOW DDL JOBS;
+--------+------------+------------------+--------------+-----------+-----------+
| job_id | table_name | schema_name      | job_type     | state     | comment   |
+--------+------------+------------------+--------------+-----------+-----------+
| 5      | users      | mydb             | add index    | paused    |           |
+--------+------------+------------------+--------------+-----------+-----------+

mysql> RESUME DDL JOBS 5;
Query OK, 1 row affected
```

## Prevent It

- Monitor DDL job status regularly
- Avoid pausing DDL during maintenance windows
- Ensure DDL owner is healthy before starting DDL

## Related Pages

- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB DDL Pause Error](/tools/tidb/tidb-ddl-pause-error)
- [TiDB DDL Resume Error](/tools/tidb/tidb-ddl-resume-error)

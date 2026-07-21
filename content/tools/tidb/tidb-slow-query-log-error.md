---
title: "[Solution] TiDB Slow Query Log Error — How to Fix"
description: "Fix TiDB slow query log errors when slow queries are not being recorded or analyzed correctly"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Slow Query Log Error

Slow query log errors occur when TiDB fails to record or properly format slow query entries, making it difficult to diagnose performance issues.

## Why It Happens

- Slow query log threshold is set too high
- Log directory does not exist or has wrong permissions
- Disk is full and cannot write new log entries
- Slow query log format is misconfigured
- TiDB process does not have write access to log file

## Common Error Messages

```
ERROR: unable to write slow query log: disk full
```

```
WARN: slow query log threshold set to 0, all queries logged
```

```
error: slow query log file not found
```

## How to Fix It

### 1. Check Slow Query Threshold

```sql
SHOW VARIABLES LIKE 'tidb_slow_query_threshold';
SET GLOBAL tidb_slow_query_threshold = 1000;
```

### 2. Verify Log Configuration

```toml
# In tidb.toml
[log]
slow-query-file = "/var/log/tidb/slow-query.log"
slow-threshold = 1000
```

### 3. Check Disk Space

```bash
df -h /var/log/tidb
```

### 4. Query Slow Log via SQL

```sql
-- Query the slow query table
SELECT query, query_time, process_time 
FROM information_schema.slow_query 
ORDER BY query_time DESC LIMIT 10;
```

## Examples

```
$ tail -20 /var/log/tidb/slow-query.log
# Query_time: 2.5s
# Process_time: 2.0s
# Wait_time: 0.5s
# DB: mydb
# INDEX: idx_user_id
select * from orders where user_id = 12345;
```

## Prevent It

- Set appropriate slow query threshold (500ms-1000ms)
- Monitor slow query log size and rotation
- Use TiDB Dashboard for slow query analysis

## Related Pages

- [TiDB Slow Query Error](/tools/tidb/tidb-slow-query-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
- [TiDB Statement Summary Error](/tools/tidb/tidb-statement-summary-error)

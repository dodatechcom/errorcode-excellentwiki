---
title: "[Solution] ClickHouse Quota Error"
description: "Fix ClickHouse quota errors when query exceeds resource usage limits"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Quota Error

Quota errors occur when a user query exceeds the configured resource usage quota.

## Common Causes

- Query exceeds row read limit
- Too many concurrent queries from user
- Query execution time exceeding quota
- Network transfer quota exceeded

## How to Fix

Check quotas:

```sql
SELECT name, limits FROM system.quotas;
```

Check user quota usage:

```sql
SELECT * FROM system.quota_usage;
```

Increase quota:

```sql
ALTER QUOTA my_quota FOR INTERVAL 1 hour MAX queries = 10000;
```

## Examples

```sql
SELECT user, count() FROM system.query_log GROUP BY user ORDER BY count() DESC;
```

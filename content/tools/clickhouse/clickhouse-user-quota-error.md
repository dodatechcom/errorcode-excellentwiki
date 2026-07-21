---
title: "[Solution] ClickHouse User Quota Error"
description: "How to fix ClickHouse user quota exceeded errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query rate limit exceeded
- Data transfer quota exceeded
- Concurrent query limit reached

## How to Fix

Check quotas:

```sql
SELECT * FROM system.quotas;
SELECT * FROM system.quota_usage;
```

Adjust quota:

```sql
CREATE QUOTA my_quota FOR INTERVAL 1 hour MAX queries = 10000;
```

## Examples

```sql
SELECT * FROM system.quotas;
SELECT * FROM system.quota_usage;
```

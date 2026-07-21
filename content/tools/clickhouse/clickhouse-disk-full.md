---
title: "[Solution] ClickHouse Disk Full Error"
description: "How to fix ClickHouse disk space exhaustion errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Data growing beyond disk capacity
- Too many parts accumulating
- Old data not being deleted (TTL not set)
- Merge consuming extra space

## How to Fix

Check disk usage:

```bash
df -h /var/lib/clickhouse/
```

Check table sizes:

```sql
SELECT table, formatReadableSize(sum(bytes_on_disk)) AS size FROM system.parts WHERE active GROUP BY table ORDER BY sum(bytes_on_disk) DESC;
```

Drop old data:

```sql
ALTER TABLE my_table DELETE WHERE event_date < today() - 90;
```

## Examples

```sql
SELECT database, table, formatReadableSize(sum(bytes_on_disk)) FROM system.parts GROUP BY database, table ORDER BY sum(bytes_on_disk) DESC LIMIT 10;
```

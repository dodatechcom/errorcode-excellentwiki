---
title: "[Solution] ClickHouse TTL Error"
description: "Fix ClickHouse TTL errors when data expiration or transformation rules fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse TTL Error

TTL errors occur when ClickHouse TTL rules cannot properly expire or move data.

## Common Causes

- TTL column contains invalid date values
- TTL expression referencing non-existent column
- Disk volume target for TTL move not configured
- TTL policy conflict with table partitioning

## How to Fix

Check TTL settings:

```sql
SELECT database, name, ttl FROM system.tables WHERE ttl != '';
```

Set TTL on table:

```sql
ALTER TABLE logs MODIFY TTL event_date + INTERVAL 30 DAY;
```

Check TTL execution:

```sql
SELECT database, table, event_type, time_ms, rows
FROM system.part_log WHERE event_type = 'RemovePart';
```

## Examples

```sql
ALTER TABLE events MODIFY TTL event_date + INTERVAL 90 DAY DELETE,
                      event_date + INTERVAL 180 DAY TO VOLUME 'cold';
```

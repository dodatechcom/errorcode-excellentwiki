---
title: "[Solution] ClickHouse Table Read-Only Error"
description: "Fix ClickHouse table read-only errors when table enters readonly mode"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Table Read-Only Error

Table read-only errors occur when a replicated table becomes readonly due to ZooKeeper issues or disk problems.

## Common Causes

- ZooKeeper session lost causing readonly mode
- Disk full on replica preventing writes
- Replication lag exceeding configured threshold
- ClickHouse was restarted without proper ZooKeeper recovery

## How to Fix

Check readonly status:

```sql
SELECT database, table, is_readonly FROM system.replicas WHERE is_readonly = 1;
```

Reset readonly mode:

```sql
SYSTEM RESTART REPLICA my_table;
```

Check disk space:

```bash
df -h /var/lib/clickhouse/
```

## Examples

```sql
SELECT database, table, is_readonly, absolute_delay, queue_size
FROM system.replicas WHERE is_readonly = 1;
```

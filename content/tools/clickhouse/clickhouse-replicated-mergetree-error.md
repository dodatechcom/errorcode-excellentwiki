---
title: "[Solution] ClickHouse ReplicatedMergeTree Error"
description: "How to fix ClickHouse ReplicatedMergeTree errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ZooKeeper not reachable
- Replication path wrong
- Replica ID conflict
- Replication lag too high

## How to Fix

```sql
CREATE TABLE my_table (
  id UInt32
) ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/my_table', '{replica}')
ORDER BY id;
```

## Examples

```sql
SELECT * FROM system.replicas WHERE table = 'my_table';
SELECT is_readonly, future_parts, parts_to_check FROM system.replicas WHERE table = 'my_table';
```

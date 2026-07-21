---
title: "[Solution] ClickHouse Table Is Readonly Error"
description: "How to fix ClickHouse readonly table errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ZooKeeper session lost
- Replica cannot fetch mutations
- Disk full on replica
- Replication queue stuck

## How to Fix

Check readonly status:

```sql
SELECT is_readonly FROM system.replicas WHERE table = 'my_table';
```

Reset readonly:

```sql
SYSTEM RESTART REPLICA my_table;
```

## Examples

```sql
SELECT * FROM system.replicas WHERE is_readonly = 1;
SYSTEM RESTART REPLICA my_table;
SYSTEM RESTART REPLICAS;
```

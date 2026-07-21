---
title: "[Solution] ClickHouse Quorum Insert Error"
description: "How to fix ClickHouse quorum insert errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Quorum not reached (not enough replicas)
- Timeout waiting for quorum
- Replicas disconnected

## How to Fix

Check quorum status:

```sql
SELECT * FROM system.replicas WHERE table = 'my_table';
```

Insert with quorum:

```sql
INSERT INTO my_table SETTINGS insert_quorum = 2 VALUES (1, 'a');
```

## Examples

```sql
SELECT * FROM system.replicas WHERE is_readonly = 0;
INSERT INTO my_table SETTINGS insert_quorum = 2 FORMAT JSONEachRow {"id":1,"name":"a"};
```

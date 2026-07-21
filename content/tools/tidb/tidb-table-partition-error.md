---
title: "[Solution] TiDB Table Partition Error"
description: "How to fix TiDB table partition errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Partition count exceeded
- Partition key not found
- Partition pruning not working

## How to Fix

```sql
CREATE TABLE t1 (id INT) PARTITION BY RANGE (id) (
  PARTITION p0 VALUES LESS THAN (100),
  PARTITION p1 VALUES LESS THAN (200)
);
```

## Examples

```sql
SHOW CREATE TABLE t1;
```

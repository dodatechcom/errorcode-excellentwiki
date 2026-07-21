---
title: "[Solution] TiDB Auto Random Shard Error"
description: "How to fix TiDB auto_random shard errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Shard bits too many
- Auto random conflict
- Auto random not enabled

## How to Fix

```sql
CREATE TABLE t1 (id BIGINT AUTO_RANDOM(5, 32) PRIMARY KEY, name VARCHAR(100));
```

## Examples

```sql
SHOW CREATE TABLE t1;
```

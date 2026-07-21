---
title: "[Solution] TiDB Index Error"
description: "How to fix TiDB index errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Index not found
- Index corrupted
- Index creation failing

## How to Fix

```sql
CREATE INDEX idx_name ON mytable (name);
```

## Examples

```sql
SHOW INDEX FROM mytable;
```

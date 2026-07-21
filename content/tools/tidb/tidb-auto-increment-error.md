---
title: "[Solution] TiDB Auto Increment Error"
description: "How to fix TiDB auto_increment errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Auto increment conflict
- Auto increment gap
- Auto increment not sequential

## How to Fix

```sql
SET @@auto_increment_increment = 1;
SET @@auto_increment_offset = 1;
```

## Examples

```sql
SHOW VARIABLES LIKE 'auto_increment%';
```

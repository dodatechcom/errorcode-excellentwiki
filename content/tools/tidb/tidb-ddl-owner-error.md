---
title: "[Solution] TiDB DDL Owner Error"
description: "How to fix TiDB DDL owner errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- No DDL owner elected
- DDL owner not reachable
- DDL owner transfer failing

## How to Fix

```sql
SHOW DDL OWNER;
```

## Examples

```sql
SELECT * FROM mysql.tidb WHERE variable_name = 'ddl_owner';
```

---
title: "[Solution] YugabyteDB Schema Change Error"
description: "How to fix YugabyteDB schema change errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Schema change blocked by DDL
- Schema change timeout
- Schema change not propagated

## How to Fix

```sql
ALTER TABLE mytable ADD COLUMN newcol INT;
```

## Examples

```sql
SHOW DDL; -- MySQL
```

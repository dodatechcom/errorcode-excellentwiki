---
title: "[Solution] YugabyteDB Tablet Truncate Error"
description: "How to fix YugabyteDB tablet truncate errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Truncate blocked by transaction
- Truncate timeout
- Truncate not supported

## How to Fix

```sql
TRUNCATE TABLE mytable;
```

## Examples

```sql
SELECT count(*) FROM mytable;
```

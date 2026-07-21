---
title: "[Solution] TiDB Optimistic Lock Error"
description: "How to fix TiDB optimistic lock errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Optimistic transaction conflict
- Write conflict detected
- Transaction retry limit exceeded

## How to Fix

```sql
SET SESSION tidb_retry_limit = 10;
```

## Examples

```sql
SHOW VARIABLES LIKE 'tidb_retry_limit';
```

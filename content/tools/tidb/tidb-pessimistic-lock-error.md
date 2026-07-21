---
title: "[Solution] TiDB Pessimistic Lock Error"
description: "How to fix TiDB pessimistic lock errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Pessimistic lock timeout
- Lock conflict detected
- Deadlock detected

## How to Fix

```sql
SET SESSION tidb_txn_mode = 'pessimistic';
```

## Examples

```sql
SHOW VARIABLES LIKE 'tidb_txn_mode';
```

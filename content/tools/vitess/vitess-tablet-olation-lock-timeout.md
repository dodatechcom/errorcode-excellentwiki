---
title: "[Solution] Vitess Tablet Lock Wait Timeout Error"
description: "Fix Vitess lock wait timeout errors when transactions wait too long for row locks"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Lock Wait Timeout Error

Lock wait timeout errors occur when a transaction waits longer than `innodb_lock_wait_timeout` to acquire a row lock.

## Common Causes

- Long-running transaction holding exclusive lock
- Deadlock between two concurrent transactions
- Full table scan acquiring locks on many rows
- Missing index forcing table-level locking

## How to Fix

Check lock wait timeout:

```sql
SHOW VARIABLES LIKE 'innodb_lock_wait_timeout';
```

Increase timeout temporarily:

```sql
SET GLOBAL innodb_lock_wait_timeout = 60;
```

Identify blocking queries:

```sql
SELECT r.trx_id AS waiting_trx, b.trx_id AS blocking_trx, b.trx_query
FROM information_schema.innodb_lock_waits w
JOIN information_schema.innodb_trx r ON r.trx_id = w.requesting_trx_id
JOIN information_schema.innodb_trx b ON b.trx_id = w.blocking_trx_id;
```

## Examples

```sql
KILL QUERY 12345;
```

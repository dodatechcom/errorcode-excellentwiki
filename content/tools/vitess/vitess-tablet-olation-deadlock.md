---
title: "[Solution] Vitess Tablet Transaction Deadlock Error"
description: "Fix Vitess transaction deadlock errors when concurrent transactions conflict on same rows"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Transaction Deadlock Error

Transaction deadlock errors occur when two or more transactions hold locks that the other needs, causing MySQL to roll back one of them.

## Common Causes

- Concurrent transactions updating same rows in different order
- Long-running transaction holding locks too long
- Missing indexes causing full table scans with locks
- Hot row contention on high-traffic tables

## How to Fix

Check deadlock info:

```sql
SHOW ENGINE INNODB STATUS;
```

Identify locking queries:

```sql
SELECT * FROM information_schema.innodb_lock_waits;
```

Optimize query order:

```sql
-- Lock rows in consistent order
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
SELECT * FROM accounts WHERE id = 2 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

## Examples

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SELECT * FROM information_schema.innodb_trx"
```

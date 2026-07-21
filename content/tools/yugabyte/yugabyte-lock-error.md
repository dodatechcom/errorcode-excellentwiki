---
title: "[Solution] YugabyteDB Lock Error — How to Fix"
description: "Fix YugabyteDB lock errors by resolving lock contention, fixing transaction lock timeouts, and handling distributed lock conflicts"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Lock Error

YugabyteDB lock errors occur when transactions compete for locks on the same rows or tablets, causing timeouts, deadlocks, or blocked operations.

## Why It Happens

- Two transactions hold conflicting locks on the same rows
- Lock timeout is too short for the workload
- Transaction holds locks too long during DML operations
- Distributed lock across tablets causes cross-node contention
- Pessimistic locking conflicts with concurrent inserts
- DDL operations require table-level locks that block DML

## Common Error Messages

```
ERROR: lock not acquired within timeout
```

```
ERROR: deadlock detected
```

```
ERROR: could not serialize access due to concurrent update
```

```
ERROR: statement timeout while waiting for lock
```

## How to Fix It

### 1. Check Lock Status

```sql
-- Check active locks
SELECT
  l.pid,
  l.locktype,
  l.mode,
  l.granted,
  a.query
FROM pg_locks l
JOIN pg_stat_activity a ON l.pid = a.pid
WHERE NOT l.granted;

-- Check lock wait graph
SELECT * FROM yb_locks();
```

### 2. Increase Lock Timeout

```sql
-- Increase lock timeout
SET lock_timeout = '60s';

-- Increase statement timeout
SET statement_timeout = '300s';

-- Check current timeouts
SHOW lock_timeout;
SHOW statement_timeout;
```

### 3. Fix Deadlocks

```sql
-- Kill the blocking transaction
SELECT pg_terminate_backend(<blocking_pid>);

-- Use optimistic transactions to reduce deadlocks
SET yb_enable_implicit_fire_for_insert = false;

-- Break transaction into smaller batches
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
BEGIN;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 4. Optimize Lock Usage

```sql
-- Use SELECT FOR UPDATE SKIP LOCKED for concurrent processing
SELECT * FROM tasks
WHERE status = 'pending'
LIMIT 10
FOR UPDATE SKIP LOCKED;

-- Use NOWAIT to fail immediately if locked
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
```

## Common Scenarios

- **Lock timeout under load**: Increase lock_timeout or optimize transaction duration.
- **Deadlocks during batch processing**: Process rows in a consistent order.
- **DDL blocks DML**: Schedule DDL operations during maintenance windows.

## Prevent It

- Keep transactions short to minimize lock hold time
- Use consistent lock ordering across all transactions
- Monitor lock contention regularly

## Related Pages

- [YugabyteDB Transaction Error](/tools/yugabyte/yugabyte-transaction-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)

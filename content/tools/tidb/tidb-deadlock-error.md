---
title: "[Solution] TiDB Deadlock Error — How to Fix"
description: "Fix TiDB deadlock errors by resolving lock cycles, optimizing transaction ordering, and configuring deadlock detection settings"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Deadlock Error

TiDB deadlock errors occur when two or more transactions hold locks that the other needs, creating a circular wait. TiDB has a built-in deadlock detector that rolls back one transaction.

## Why It Happens

- Two transactions acquire locks on the same rows in reverse order
- Long-running transaction holds locks too long
- Pessimistic transaction mode increases deadlock likelihood
- SELECT FOR UPDATE creates lock contention
- Batch update operations lock overlapping row ranges
- Deadlock detector timeout is too short

## Common Error Messages

```
ERROR: deadlock detected
```

```
ERROR: lock wait timeout exceeded
```

```
ERROR: TiDB server has canceled the transaction
```

```
ERROR: pessimistic transaction deadlock
```

## How to Fix It

### 1. Check Deadlock Information

```sql
-- Enable deadlock history
SET GLOBAL tidb_enable_deadlock_detect = ON;

-- Check recent deadlocks
SELECT * FROM information_schema.tidb_deadlocks
ORDER BY occur_time DESC LIMIT 10;

-- Analyze lock wait
SELECT * FROM information_schema.INNODB_LOCK_WAITS;
```

### 2. Optimize Transaction Ordering

```sql
-- Always lock rows in the same order
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Transaction 2 must also lock id=1 then id=2
BEGIN;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;
```

### 3. Reduce Lock Hold Time

```sql
-- Use optimistic transaction for low contention
SET tidb_txn_mode = 'optimistic';

-- Break large transaction into smaller batches
BEGIN;
UPDATE orders SET status = 'processed'
WHERE id IN (1,2,3,4,5);
COMMIT;

-- Set lock wait timeout
SET innodb_lock_wait_timeout = 5;
```

### 4. Configure Deadlock Detection

```toml
# tidb.toml
[performance]
# Enable deadlock detection
deadlock-history-capacity = 1024

[txn-local]
# Reduce lock wait timeout
lock-wait-timeout = 3
```

```sql
-- Kill the victim transaction
SHOW PROCESSLIST;
KILL <blocking_process_id>;
```

## Common Scenarios

- **Batch job deadlocks on updates**: Process rows in a consistent sorted order.
- **SELECT FOR UPDATE deadlocks**: Use NOWAIT or SKIP LOCKED to avoid blocking.
- **Frequent deadlocks under load**: Switch to optimistic transaction mode if possible.

## Prevent It

- Always acquire locks in a consistent global order
- Keep transactions short to minimize lock hold time
- Use optimistic mode for low-contention workloads
- Monitor deadlock history for patterns

## Related Pages

- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
- [TiDB Lock Error](/tools/tidb/tidb-lock-error)
- [TiDB Pessimistic Lock Error](/tools/tidb/tidb-pessimistic-lock-error)

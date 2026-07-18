---
title: "[Solution] TiDB Lock Error — How to Fix"
description: "Fix TiDB lock errors by resolving lock contention, fixing pessimistic lock issues, and handling lock resolution problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Lock Error

TiDB lock errors occur when transactions acquire, wait for, or resolve locks. TiDB uses both optimistic and pessimistic locking mechanisms.

## Why It Happens

- Pessimistic lock is held too long
- Optimistic lock conflict on commit
- Lock resolution fails after transaction abort
- Lock information is stale or corrupted
- Lock wait exceeds configured timeout
- Lock conflict between OLTP and OLAP workloads

## Common Error Messages

```
ERROR: pessimistic lock timeout
```

```
ERROR: lock not found
```

```
ERROR: optimistic lock conflict
```

```
WARNING: lock resolve failed
```

## How to Fix It

### 1. Check Lock Status

```sql
-- Check current locks
SELECT * FROM information_schema.tikv_locks;

-- Check lock wait
SELECT * FROM information_schema.processlist WHERE state = 'Lock Wait';

-- Check transaction locks
SHOW PROCESSLIST;
```

### 2. Fix Pessimistic Lock Issues

```sql
-- Use pessimistic mode for high contention
BEGIN PESSIMISTIC;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Increase lock wait timeout
SET tidb_pessimistic_txn_fair_locking = ON;
SET tidb_lock_wait_timeout = 60;
```

### 3. Fix Optimistic Lock Conflict

```sql
-- Retry on conflict
-- Application should catch error and retry transaction

-- Or use pessimistic mode
SET tidb_txn_mode = 'pessimistic';
```

### 4. Monitor Lock Activity

```sql
-- Check lock contention
SELECT * FROM information_schema.tikv_locks WHERE lock_type = 'WRITE';

-- Monitor lock wait time
SELECT * FROM information_schema.processlist
WHERE info LIKE '%FOR UPDATE%';
```

## Common Scenarios

- **Lock wait timeout**: Kill blocking transaction or increase timeout.
- **Optimistic lock conflict**: Use pessimistic mode or retry logic.
- **Lock not found**: Transaction may have been rolled back by GC.

## Prevent It

- Use pessimistic mode for high-contention workloads
- Keep transactions short to minimize lock duration
- Implement retry logic for optimistic transactions

## Related Pages

- [TiDB Wait Error](/tools/tidb/tidb-wait-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
- [TiDB DML Error](/tools/tidb/tidb-dml-error)

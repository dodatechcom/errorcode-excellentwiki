---
title: "[Solution] TiDB Wait Error — How to Fix"
description: "Fix TiDB wait errors by resolving lock wait timeouts, fixing transaction wait issues, and handling concurrent operation conflicts"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Wait Error

TiDB wait errors occur when operations block waiting for locks, resources, or other transactions to complete.

## Why It Happens

- Transaction is waiting for a lock held by another transaction
- Lock wait timeout is exceeded
- Deadlock between concurrent transactions
- Transaction is waiting for TSO
- Query is waiting for coprocessor resources
- Session is waiting for disk I/O

## Common Error Messages

```
ERROR: lock wait timeout exceeded
```

```
ERROR: deadlock detected
```

```
ERROR: transaction timeout
```

```
ERROR: coprocessor request timeout
```

## How to Fix It

### 1. Check Lock Wait Status

```sql
-- Check current transactions
SELECT * FROM information_schema.tikv_locks WHERE lock_type != 'READ';

-- Check waiting sessions
SELECT * FROM information_schema.processlist WHERE state = 'Lock Wait';

-- Check deadlock history
SELECT * FROM information_schema.deadlocks ORDER BY start_time DESC;
```

### 2. Fix Lock Wait Timeout

```sql
-- Increase lock wait timeout
SET innodb_lock_wait_timeout = 60;

-- Kill blocking transaction
KILL <blocking_session_id>;

-- Use shorter transactions
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### 3. Fix Deadlock

```sql
-- Check deadlock details
SELECT * FROM information_schema.deadlocks LIMIT 1;

-- Use pessimistic mode to avoid deadlocks
BEGIN PESSIMISTIC;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### 4. Optimize Wait Behavior

```toml
# In tidb.toml
[tikv-client]
txn-commit-max-backoff = 10000
txn-commit-min-backoff = 1000

[performance]
pessimistic-txn.fair-locking = true
```

## Common Scenarios

- **Lock wait timeout**: Kill blocking transaction or increase timeout.
- **Deadlock detected**: TiDB will auto-rollback one transaction, retry it.
- **Slow coprocessor**: Check TiKV load and add more TiKV nodes.

## Prevent It

- Keep transactions short to minimize lock contention
- Use pessimistic mode for high-contention workloads
- Monitor lock wait with tikv_locks

## Related Pages

- [TiDB Lock Error](/tools/tidb/tidb-lock-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)

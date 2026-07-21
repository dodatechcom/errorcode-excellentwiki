---
title: "[Solution] TiDB Isolation Error — How to Fix"
description: "Fix TiDB isolation level errors by resolving transaction isolation conflicts, fixing read consistency issues, and correcting snapshot reads"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Isolation Error

TiDB isolation errors occur when transaction isolation levels are misconfigured or when queries expect a specific isolation behavior that differs from TiDB's defaults.

## Why It Happens

- Transaction isolation level is not supported by TiDB
- Stale read conflicts with expected read-committed behavior
- Snapshot read sees inconsistent data due to DDL changes
- Read-only transaction encounters write locks
- REPEATABLE READ behaves differently than MySQL in TiDB
- Setting isolation level mid-transaction has no effect

## Common Error Messages

```
ERROR: isolation level not supported
```

```
ERROR: stale read timestamp is too old
```

```
ERROR: can not read for write in read-only transaction
```

```
ERROR: transaction isolation conflict
```

## How to Fix It

### 1. Set Correct Isolation Level

```sql
-- Check current transaction isolation level
SELECT @@transaction_isolation;

-- Set transaction isolation level
SET SESSION transaction_isolation = 'READ-COMMITTED';

-- Use READ-COMMITTED for each transaction
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
SELECT * FROM orders WHERE user_id = 1;
COMMIT;
```

### 2. Handle Stale Read Issues

```sql
-- Use correct timestamp for stale read
SELECT * FROM orders AS OF TIMESTAMP(NOW() - INTERVAL 5 SECOND);

-- Increase GC life time if stale reads fail
SET GLOBAL tidb_gc_life_time = '10m';

-- Check GC status
SELECT * FROM mysql.tidb WHERE variable_name = 'tidb_gc_life_time';
```

### 3. Fix Read-Only Transaction Errors

```sql
-- Start read-only transaction
START TRANSACTION READ ONLY;
SELECT * FROM orders WHERE status = 'active';
COMMIT;

-- TiDB does not support SERIALIZABLE in some versions
-- Use snapshot read instead
SET TRANSACTION READ ONLY AS OF TIMESTAMP NOW();
SELECT * FROM orders;
```

### 4. Handle TiDB-Specific Isolation Behavior

```sql
-- TiDB uses optimistic transactions by default
-- Switch to pessimistic for stricter isolation
SET tidb_txn_mode = 'pessimistic';

-- Use SELECT FOR UPDATE for row-level locking
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

## Common Scenarios

- **Phantom reads occur with REPEATABLE READ**: TiDB REPEATABLE READ uses snapshot isolation, which prevents phantom reads by design.
- **Stale read returns old data**: The timestamp is older than the GC threshold; use a more recent timestamp.
- **Application expects READ COMMITTED**: Set the session-level isolation before the transaction.

## Prevent It

- Understand TiDB's default isolation behavior differs from MySQL
- Use pessimistic mode for applications requiring strict row-level locking
- Test isolation behavior with concurrent workloads

## Related Pages

- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
- [TiDB Transaction Lock Timeout Error](/tools/tidb/tidb-transaction-lock-timeout-error)
- [TiDB GC Error](/tools/tidb/tidb-gc-error)

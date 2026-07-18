---
title: "[Solution] TiDB Transaction Error — How to Fix"
description: "Fix TiDB transaction errors by resolving isolation level issues, fixing transaction conflicts, and handling large transaction limits"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Transaction Error

TiDB transaction errors occur when distributed transactions fail due to conflicts, timeouts, or size limits. TiDB supports both optimistic and pessimistic transaction modes.

## Why It Happens

- Transaction conflicts under high concurrency
- Transaction is too large (exceeds size limit)
- Transaction timeout
- pessimistic lock wait timeout
- Snapshot isolation conflict
- Transaction is not committed or rolled back

## Common Error Messages

```
ERROR: concurrent transaction conflict
```

```
ERROR: transaction too large
```

```
ERROR: lock wait timeout
```

```
ERROR: optimistic transaction commit failed
```

## How to Fix It

### 1. Use Appropriate Transaction Mode

```sql
-- Optimistic mode (default)
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Pessimistic mode (better for high contention)
BEGIN PESSIMISTIC;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 2. Fix Transaction Too Large

```sql
-- Reduce transaction size
SET tidb_dml_batch_size = 1000;

-- Process in smaller batches
BEGIN;
DELETE FROM logs WHERE created_at < '2024-01-01' LIMIT 1000;
COMMIT;
```

### 3. Handle Transaction Conflicts

```sql
-- Increase lock wait timeout
SET innodb_lock_wait_timeout = 60;

-- Use SELECT FOR UPDATE for explicit locking
BEGIN PESSIMISTIC;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### 4. Configure Transaction Settings

```toml
# In tidb.toml
[performance]
txn-total-size-limit = 104857600  # 100MB
txn-entry-count-limit = 300000

[tikv-client]
txn-commit-max-backoff = 10000
```

## Common Scenarios

- **High concurrency causes conflicts**: Use pessimistic transaction mode.
- **Transaction too large**: Split into smaller batches.
- **Lock wait timeout**: Increase timeout or reduce contention.

## Prevent It

- Use pessimistic mode for high-contention workloads
- Keep transactions small and short
- Set appropriate lock wait timeouts

## Related Pages

- [TiDB DML Error](/tools/tidb/tidb-dml-error)
- [TiDB Lock Error](/tools/tidb/tidb-lock-error)
- [TiDB TSO Error](/tools/tidb/tidb-tso-error)

---
title: "[Solution] TiDB Transaction Lock Error — How to Fix"
description: "Fix TiDB transaction lock errors when transactions encounter lock conflicts or stale locks"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Transaction Lock Error

Transaction lock errors occur when TiDB transactions encounter lock conflicts, stale locks, or lock wait timeouts during concurrent operations.

## Why It Happens

- Another transaction holds a conflicting lock
- Lock owner transaction crashed without releasing locks
- Lock wait timeout is exceeded
- Pessimistic lock conflicts with concurrent writes
- GC has not cleaned up old locks

## Common Error Messages

```
ERROR 1205: Lock wait timeout exceeded; try restarting transaction
```

```
ERROR 1213: Deadlock found when trying to get lock
```

```
ERROR 8028: Information schema is changed during the transaction
```

## How to Fix It

### 1. Increase Lock Wait Timeout

```sql
SET SESSION innodb_lock_wait_timeout = 120;
```

### 2. Detect Deadlocks

```sql
-- Check for deadlocks
SHOW ENGINE TIDB STATUS;
```

### 3. Use Pessimistic Mode

```sql
-- Start pessimistic transaction
BEGIN PESSIMISTIC;
```

### 4. Retry Deadlocked Transactions

```python
import mysql.connector

max_retries = 3
for attempt in range(max_retries):
    try:
        cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
        connection.commit()
        break
    except mysql.connector.IntegrityError as e:
        if "Deadlock" in str(e) and attempt < max_retries - 1:
            connection.rollback()
            continue
        raise
```

## Examples

```
mysql> BEGIN PESSIMISTIC;
mysql> UPDATE users SET balance = balance - 100 WHERE id = 1;
-- Lock acquired, other transactions wait
mysql> COMMIT;
-- Lock released
```

## Prevent It

- Keep transactions as short as possible
- Use optimistic transactions for low-contention workloads
- Implement retry logic for deadlocked transactions

## Related Pages

- [TiDB Lock Error](/tools/tidb/tidb-lock-error)
- [TiDB Optimistic Lock Error](/tools/tidb/tidb-optimistic-lock-error)
- [TiDB Pessimistic Lock Error](/tools/tidb/tidb-pessimistic-lock-error)

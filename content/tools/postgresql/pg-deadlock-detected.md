---
title: "[Solution] PostgreSQL Deadlock Detected - Diagnose and Fix Lock Cycles"
description: "Fix PostgreSQL deadlock detected errors by analyzing lock wait graphs, adding proper indexes, and restructuring transaction ordering"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Deadlock Detected

A deadlock in PostgreSQL occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency that cannot be resolved. PostgreSQL automatically detects deadlocks and aborts one of the transactions to break the cycle.

## What This Error Means

When PostgreSQL detects a deadlock, it rolls back one of the involved transactions and returns an error to the client:

```
ERROR: deadlock detected
DETAIL: Process 12345 waits for ShareLock on transaction 67890; blocked by process 67890.
Process 67890 waits for ShareLock on transaction 12345; blocked by process 12345.
```

The server log provides a detailed `DeadlockDetails` section showing which locks each transaction holds and which it is waiting for. PostgreSQL chooses the victim transaction based on which one has done the least work (fewest row modifications), so it typically aborts the "cheaper" transaction.

## Why It Happens

- Two transactions lock rows in opposite order (Transaction A locks row 1 then row 2, Transaction B locks row 2 then row 1)
- Foreign key constraints cause implicit locks that create unexpected lock ordering
- Missing indexes cause PostgreSQL to lock more rows than necessary during updates
- Long-running transactions hold locks while waiting for additional locks
- Concurrent INSERT and UPDATE operations on the same table with overlapping key ranges
- Advisory locks acquired in inconsistent order by different sessions

## How to Fix It

### 1. Analyze the Deadlock from Server Logs

```bash
# Enable deadlock logging
# In postgresql.conf
log_lock_waits = on
deadlock_timeout = 1s
log_min_messages = LOG
```

### 2. Always Lock Rows in the Same Order

```sql
-- WRONG: inconsistent ordering
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Transaction 2 (reversed order)
BEGIN;
UPDATE accounts SET balance = balance - 50 WHERE id = 2;
UPDATE accounts SET balance = balance + 50 WHERE id = 1;

-- CORRECT: both transactions lock in the same order
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = LEAST(1, 2);
UPDATE accounts SET balance = balance + 100 WHERE id = GREATEST(1, 2);
```

### 3. Add Proper Indexes

```sql
-- Without an index, PostgreSQL locks many rows during a sequential scan
CREATE INDEX idx_accounts_id ON accounts(id);
```

### 4. Use SELECT FOR UPDATE with NOWAIT

```sql
-- Fail immediately instead of waiting and risking deadlock
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
-- If lock cannot be acquired, raises an error immediately
```

### 5. Reduce Transaction Duration

```sql
-- Process data in smaller batches
-- WRONG: one giant transaction
BEGIN;
UPDATE accounts SET status = 'active' WHERE created_at > '2024-01-01';
COMMIT;

-- BETTER: batch processing
DO $$
DECLARE
    batch_size INT := 1000;
    affected INT;
BEGIN
    LOOP
        UPDATE accounts SET status = 'active'
        WHERE id IN (SELECT id FROM accounts WHERE status IS NULL LIMIT batch_size);
        GET DIAGNOSTICS affected = ROW_COUNT;
        EXIT WHEN affected = 0;
        COMMIT;
    END LOOP;
END $$;
```

## Common Mistakes

- Ignoring deadlock logs and hoping the problem will resolve itself
- Increasing `deadlock_timeout` to avoid deadlocks -- this just delays detection
- Using `SERIALIZABLE` isolation level as a blanket fix without understanding the performance cost
- Not adding indexes on columns used in WHERE and JOIN clauses
- Mixing ORM-generated queries with hand-written SQL that lock rows differently

## Related Pages

- [PostgreSQL Lock Timeout](/tools/postgresql/pg-locks-timeout)
- [PostgreSQL Serialization Failure](/tools/postgresql/pg-serialization-failure)
- [PostgreSQL Statement Timeout](/tools/postgresql/pg-statement-timeout)
- [MySQL Deadlock Detected](/tools/mysql/mysql-deadlock-detected)

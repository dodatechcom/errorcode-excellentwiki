---
title: "[Solution] PostgreSQL Serialization Failure - Fix Concurrent Update Conflicts"
description: "Fix PostgreSQL serialization failure errors by using explicit locking, retry logic, and SERIALIZABLE isolation level best practices"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Serialization Failure

A serialization failure occurs when PostgreSQL detects that running a transaction under the `SERIALIZABLE` isolation level would produce a result inconsistent with a serial (one-at-a-time) execution order. The database aborts one of the conflicting transactions.

## What This Error Means

PostgreSQL returns this error when a serialization anomaly is detected:

```
ERROR: could not serialize access due to concurrent update
```

This error only occurs under the `SERIALIZABLE` isolation level. PostgreSQL uses predicate locking (specifically, SSI -- Serializable Snapshot Isolation) to detect dangerous patterns that could lead to anomalies like write skew or phantoms. When a dangerous dependency is detected, one transaction is rolled back.

Unlike deadlocks (which involve lock cycles), serialization failures are detected at commit time. The transaction may have completed all its statements successfully, but PostgreSQL rejects it at commit because the result would not be serializable.

## Why It Happens

- Two transactions read overlapping data and make decisions based on those reads
- Both transactions then write to the same or related rows
- PostgreSQL detects that the concurrent execution could produce an inconsistent result
- The application uses `SERIALIZABLE` but has logic that depends on read-then-write patterns
- Write skew anomaly: two transactions read the same data and write to different rows
- The conflict window is large because transactions run for a long time

## How to Fix It

### 1. Implement Retry Logic

```python
import psycopg2
from psycopg2 import extensions

MAX_RETRIES = 3

def run_serializable(conn, query, params=None):
    for attempt in range(MAX_RETRIES):
        try:
            conn.set_isolation_level(extensions.ISOLATION_LEVEL_SERIALIZABLE)
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            return cur
        except psycopg2.errors.SerializationFailure:
            conn.rollback()
            if attempt == MAX_RETRIES - 1:
                raise
```

### 2. Use Explicit Locking Instead

```sql
-- Instead of relying on SERIALIZABLE, use SELECT FOR UPDATE
BEGIN;
SELECT * FROM inventory WHERE product_id = 42 FOR UPDATE;
-- Now you have a guaranteed exclusive lock on the row
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 42;
COMMIT;
```

### 3. Reduce Transaction Duration

```sql
-- WRONG: long transaction with read at start
BEGIN;
SELECT * FROM accounts WHERE id IN (1, 2);  -- read
-- ... lots of processing ...
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- BETTER: minimize the time between reads and writes
-- Do processing first, then start the transaction
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 4. Use Advisory Locks for Application-Level Coordination

```sql
BEGIN;
-- Lock a specific concept, not a row
SELECT pg_advisory_xact_lock(hashtext('transfer_accounts'));
-- Now safe to read and write
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 5. Consider READ COMMITTED Instead

```sql
-- READ COMMITTED is the default and avoids serialization failures
-- Use application-level logic to handle concurrency instead
SET default_transaction_isolation = 'read committed';
```

## Common Mistakes

- Not implementing retry logic when using `SERIALIZABLE` -- serialization failures are expected and must be handled
- Using `SERIALIZABLE` for all transactions when `READ COMMITTED` would suffice
- Setting large `statement_timeout` values that keep transactions open longer than necessary
- Not checking the application code for read-then-write patterns that trigger serialization anomalies
- Assuming serialization failures indicate a bug -- they are a correct response to potential anomalies

## Related Pages

- [PostgreSQL Deadlock Detected](/tools/postgresql/pg-deadlock-detected)
- [PostgreSQL Lock Timeout](/tools/postgresql/pg-locks-timeout)
- [PostgreSQL Duplicate Key](/tools/postgresql/pg-duplicate-key)
- [MySQL Deadlock Detected](/tools/mysql/mysql-deadlock-detected)

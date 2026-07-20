---
title: "[Solution] Transaction Failed"
description: "Fix 'Transaction failed' when a transaction encounters an error and cannot complete."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, transaction, failure"]
severity: "error"
---

# Transaction Failed

## Error Message

```
ERROR 1213: Transaction failed / Transaction could not be committed — The transaction encountered an error during execution and was aborted.
```

## Common Causes

- A constraint violation (PRIMARY KEY, FOREIGN KEY, UNIQUE) occurs within the transaction
- Deadlock detection causes the database to roll back one of the transactions
- Lock timeout expires while waiting for a lock held by another transaction
- An error in a stored procedure or trigger causes the entire transaction to fail

## Solutions

### Solution 1: Use proper error handling with SAVEPOINT

Use savepoints to partially recover from errors within a transaction.

```sql
-- MySQL: use SAVEPOINT for partial rollback
START TRANSACTION;

SAVEPOINT before_insert;
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
-- If this fails, only rollback to savepoint
ROLLBACK TO SAVEPOINT before_insert;

-- Continue with other operations
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');
COMMIT;

-- PostgreSQL: same pattern
BEGIN;
SAVEPOINT sp1;
INSERT INTO users (name) VALUES ('Alice');
-- On error
ROLLBACK TO SAVEPOINT sp1;
INSERT INTO users (name, VALUES ('Bob');
COMMIT;
```

### Solution 2: Check constraint before inserting to avoid transaction failure

Validate data before starting the transaction or within it.

```sql
-- Validate before transaction
SELECT COUNT(*) FROM users WHERE email = 'alice@example.com';
-- If > 0, skip insert or use ON CONFLICT

-- Use ON CONFLICT to handle duplicates within transaction
START TRANSACTION;
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;
COMMIT;

-- Use IF NOT EXISTS pattern
START TRANSACTION;
INSERT INTO users (email, name)
SELECT 'alice@example.com', 'Alice'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE email = 'alice@example.com');
COMMIT;
```

### Solution 3: Implement retry logic for transient failures

Automatically retry failed transactions that fail due to transient issues.

```sql
-- Application-level retry logic (pseudocode):
-- max_retries = 3
-- for attempt in range(max_retries):
--     try:
--         begin_transaction()
--         execute_query()
--         commit()
--         break
--     except DeadlockError, LockTimeoutError:
--         rollback()
--         sleep(backoff_time)
--     except PermanentError:
--         rollback()
--         raise

-- MySQL: set transaction isolation level
SET SESSION transaction_isolation = 'REPEATABLE-READ';

-- PostgreSQL: set transaction isolation level
BEGIN ISOLATION LEVEL READ COMMITTED;
-- ... operations ...
COMMIT;
```

## Prevention Tips

- Always handle transaction errors in application code with proper rollback and retry logic
- Use SAVEPOINT to allow partial recovery within complex multi-step transactions
- Keep transactions as short as possible to minimize the chance of conflicts and failures

## Related Errors

- [Deadlock Error]({{< relref "/languages/sql/deadlock-error.md" >}})
- [Rollback Error]({{< relref "/languages/sql/rollback-error.md" >}})
- [Lock Timeout]({{< relref "/languages/sql/lock-timeout.md" >}})

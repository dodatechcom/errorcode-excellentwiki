---
title: "[Solution] Rollback Failed"
description: "Fix 'Rollback failed' when the database cannot roll back a failed transaction."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, rollback, transaction"]
severity: "error"
---

# Rollback Failed

## Error Message

```
ERROR 1197: Rollback failed / Transaction rollback failed — The ROLLBACK command itself encountered an error, leaving the database in an inconsistent state.
```

## Common Causes

- The transaction was already automatically committed by the database before ROLLBACK was issued
- A DDL statement (CREATE TABLE, ALTER TABLE) inside the transaction caused an implicit commit
- The database server crashed or lost connection during the transaction
- ROLLBACK was attempted on a transaction that was already rolled back

## Solutions

### Solution 1: Avoid DDL statements inside transactions

DDL statements cause implicit commits in MySQL and can prevent proper rollback.

```sql
-- Wrong: DDL causes implicit COMMIT in MySQL
START TRANSACTION;
INSERT INTO users (name) VALUES ('Alice');
ALTER TABLE users ADD COLUMN bio TEXT; -- implicit COMMIT!
INSERT INTO users (name) VALUES ('Bob');
ROLLBACK; -- only rolls back Bob, Alice was already committed!

-- Correct: do DDL before or after the transaction
ALTER TABLE users ADD COLUMN bio TEXT;
START TRANSACTION;
INSERT INTO users (name) VALUES ('Alice');
INSERT INTO users (name) VALUES ('Bob');
ROLLBACK; -- both inserts are rolled back

-- PostgreSQL: DDL is transactional
BEGIN;
CREATE TABLE temp_table (id INT);
INSERT INTO temp_table VALUES (1);
ROLLBACK; -- table creation is also rolled back
```

### Solution 2: Use explicit transaction boundaries

Clearly define where transactions begin and end to avoid confusion.

```sql
-- MySQL: use explicit START TRANSACTION and COMMIT/ROLLBACK
START TRANSACTION;
-- ... operations ...
-- Check for errors before committing
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
-- If error occurs:
ROLLBACK;
-- If successful:
COMMIT;

-- SQL Server: use TRY/CATCH for transaction handling
BEGIN TRY
    BEGIN TRANSACTION;
    INSERT INTO users (name) VALUES ('Alice');
    INSERT INTO orders (user_id) VALUES (@@IDENTITY);
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    THROW;
END CATCH;
```

### Solution 3: Handle connection loss and server crashes gracefully

Implement recovery mechanisms for database connectivity issues.

```sql
-- Check connection health before starting transaction
-- Application: ping the database before starting

-- MySQL: check if auto-commit is enabled
SHOW VARIABLES LIKE 'autocommit';
-- SET autocommit = 0; -- disable for manual transaction control

-- PostgreSQL: ensure proper connection handling
-- Use connection pooling with health checks
-- Set connection timeout and keepalive settings

-- Recover from failed transactions
-- MySQL: check for orphaned transactions
SELECT * FROM information_schema.INNODB_TRX;

-- PostgreSQL: check for prepared transactions
SELECT * FROM pg_prepared_xacts;

-- Force cleanup if needed (use with caution)
-- Kill the connection holding the orphaned transaction
-- SELECT pg_terminate_backend(pid); -- PostgreSQL
```

## Prevention Tips

- Avoid mixing DDL and DML statements in the same transaction, especially in MySQL where DDL causes implicit commits
- Use database-specific error handling mechanisms (TRY/CATCH in SQL Server, EXCEPTION in PostgreSQL)
- Implement connection health checks and automatic reconnection in your application's database driver

## Related Errors

- [Transaction Error]({{< relref "/languages/sql/transaction-error.md" >}})
- [Deadlock Error]({{< relref "/languages/sql/deadlock-error.md" >}})
- [Lock Timeout]({{< relref "/languages/sql/lock-timeout.md" >}})

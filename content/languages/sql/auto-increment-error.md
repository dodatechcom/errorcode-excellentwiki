---
title: "[Solution] Auto Increment Error"
description: "Fix 'Auto increment error' when the auto-increment counter generates invalid or duplicate values."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, auto-increment"]
severity: "error"
---

# Auto Increment Error

## Error Message

```
ERROR 1062: Duplicate entry for key 'PRIMARY' — The auto-increment value collides with an existing row, or the counter was improperly reset.
```

## Common Causes

- Auto-increment counter was manually reset to a value lower than the current maximum
- Existing rows were inserted with explicit primary key values that now conflict with auto-increment
- The auto-increment data type (e.g., INT) has reached its maximum value
- Replication conflicts cause different nodes to generate the same auto-increment value

## Solutions

### Solution 1: Reset the auto-increment counter correctly

Set the auto-increment value to one greater than the current maximum primary key.

```sql
-- Find the current maximum ID
SELECT MAX(id) FROM users;

-- Reset auto-increment to the next available value (MySQL)
ALTER TABLE users AUTO_INCREMENT = 1001;

-- PostgreSQL: reset sequence
SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));

-- SQL Server: reseed identity
DBCC CHECKIDENT ('users', RESEED, 1000);
```

### Solution 2: Use a larger data type if INT is exhausted

Upgrade the column to a larger integer type to accommodate more rows.

```sql
-- Check current maximum value
SELECT MAX(id) FROM users;

-- MySQL: upgrade from INT to BIGINT
ALTER TABLE users MODIFY id BIGINT UNSIGNED AUTO_INCREMENT;

-- PostgreSQL: change serial to bigserial
ALTER TABLE users ALTER COLUMN id TYPE BIGSERIAL;

-- SQL Server: change to BIGINT
ALTER TABLE users ALTER COLUMN id BIGINT IDENTITY(1,1);
```

### Solution 3: Avoid manual ID insertion with auto-increment

Let the database manage auto-increment values instead of specifying them manually.

```sql
-- Wrong: manually inserting ID with auto-increment
INSERT INTO users (id, name) VALUES (5, 'Alice');
-- This can cause future auto-increment conflicts

-- Correct: let auto-increment handle the ID
INSERT INTO users (name) VALUES ('Alice');

-- MySQL: check auto_increment settings
SHOW TABLE STATUS LIKE 'users';

-- PostgreSQL: check sequence
SELECT sequencename, last_value
FROM pg_sequences
WHERE tablename = 'users';
```

## Prevention Tips

- Never manually set auto-increment values in production unless absolutely necessary
- Use BIGINT for auto-increment columns in high-volume tables to avoid integer overflow
- In replication setups, configure each node with different auto-increment increments (e.g., odd/even) to avoid collisions

## Related Errors

- [Primary Key Violation]({{< relref "/languages/sql/primary-key-violation.md" >}})
- [Integer Overflow]({{< relref "/languages/sql/integer-overflow.md" >}})
- [Sql Autoincrement Error]({{< relref "/languages/sql/sql-autoincrement-error.md" >}})

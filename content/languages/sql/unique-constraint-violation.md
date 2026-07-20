---
title: "[Solution] Unique Constraint Violation"
description: "Fix 'Unique constraint violation' when inserting a duplicate value into a UNIQUE column."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, unique, duplicate"]
severity: "error"
---

# Unique Constraint Violation

## Error Message

```
ERROR 1062: Duplicate entry 'value' for key 'constraint_name' — A UNIQUE constraint prevents duplicate values in the column.
```

## Common Causes

- INSERT or UPDATE tries to set a column to a value that already exists in another row
- Case sensitivity differences cause unexpected collisions (e.g., 'Alice' vs 'alice')
- Multiple UNIQUE constraints exist and one of them is being violated
- NULL values in UNIQUE columns behave differently across databases (NULLs are not considered equal in PostgreSQL)

## Solutions

### Solution 1: Handle duplicates with ON CONFLICT or ON DUPLICATE KEY

Use database-specific syntax to handle unique constraint violations gracefully.

```sql
-- MySQL
INSERT INTO users (username, email)
VALUES ('alice', 'alice@example.com')
ON DUPLICATE KEY UPDATE email = VALUES(email);

-- PostgreSQL
INSERT INTO users (username, email)
VALUES ('alice', 'alice@example.com')
ON CONFLICT (username) DO UPDATE SET email = EXCLUDED.email;

-- SQL Server: use MERGE
MERGE INTO users AS target
USING (VALUES ('alice', 'alice@example.com')) AS source (username, email)
ON target.username = source.username
WHEN MATCHED THEN UPDATE SET email = source.email
WHEN NOT MATCHED THEN INSERT (username, email) VALUES (source.username, source.email);
```

### Solution 2: Check for existing values before inserting

Query the table first to decide whether to insert or skip.

```sql
-- Check if the value already exists
SELECT COUNT(*) FROM users WHERE username = 'alice';

-- Conditional insert
INSERT INTO users (username, email)
SELECT 'alice', 'alice@example.com'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'alice');

-- Use a unique check with a transaction
START TRANSACTION;
SELECT username FROM users WHERE username = 'alice' FOR UPDATE;
-- If no rows returned, safe to insert
INSERT INTO users (username, email) VALUES ('alice', 'alice@example.com');
COMMIT;
```

### Solution 3: Handle case sensitivity in unique constraints

Normalize values to ensure consistent comparisons.

```sql
-- Problem: 'Alice' and 'alice' might both be inserted
-- MySQL with case-insensitive collation (utf8mb4_general_ci)
ALTER TABLE users MODIFY username VARCHAR(50)
CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- PostgreSQL: use LOWER() for case-insensitive uniqueness
CREATE UNIQUE INDEX idx_users_username_lower
ON users (LOWER(username));

-- Application-level normalization
INSERT INTO users (username, email)
VALUES (LOWER('Alice'), 'alice@example.com');
```

## Prevention Tips

- Use unique indexes on columns that must be unique, such as usernames, email addresses, and serial numbers
- Consider case-insensitive collations or application-level normalization for text unique constraints
- Use NULLS NOT DISTINCT (PostgreSQL 15+) if you want NULL values to also be considered duplicates

## Related Errors

- [Primary Key Violation]({{< relref "/languages/sql/primary-key-violation.md" >}})
- [Unique Index Error]({{< relref "/languages/sql/unique-index-error.md" >}})
- [Composite Key Error]({{< relref "/languages/sql/composite-key-error.md" >}})

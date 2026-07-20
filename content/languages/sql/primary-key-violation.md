---
title: "[Solution] Duplicate Entry for Primary Key"
description: "Fix 'Duplicate entry for primary key' when inserting a row with an existing primary key value."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, primary-key, duplicate"]
severity: "error"
---

# Duplicate Entry for Primary Key

## Error Message

```
ERROR 1062: Duplicate entry '1' for key 'PRIMARY' — Cannot insert a duplicate value into the primary key column.
```

## Common Causes

- INSERT tries to add a row with a primary key value that already exists in the table
- Auto-increment counter was reset or manually set to an existing value
- Race condition where two concurrent transactions try to insert the same key
- Data migration or bulk insert contains duplicate primary key values

## Solutions

### Solution 1: Use INSERT IGNORE or ON DUPLICATE KEY UPDATE

Handle duplicate key violations gracefully instead of letting the query fail.

```sql
-- MySQL: ignore the duplicate silently
INSERT IGNORE INTO users (id, name) VALUES (1, 'Alice');

-- MySQL: update existing row on duplicate
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON DUPLICATE KEY UPDATE name = VALUES(name), email = VALUES(email);

-- PostgreSQL: use ON CONFLICT
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;

-- SQL Server: use MERGE
MERGE INTO users AS target
USING (VALUES (1, 'Alice', 'alice@example.com')) AS source (id, name, email)
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET name = source.name, email = source.email
WHEN NOT MATCHED THEN INSERT (id, name, email) VALUES (source.id, source.name, source.email);
```

### Solution 2: Check for existing rows before inserting

Query the table first to determine whether to insert or update.

```sql
-- Check if the row exists
SELECT COUNT(*) FROM users WHERE id = 1;

-- Conditionally insert or update
INSERT INTO users (id, name)
SELECT 1, 'Alice' FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM users WHERE id = 1);

-- Or use REPLACE (MySQL only — deletes and re-inserts)
REPLACE INTO users (id, name) VALUES (1, 'Alice');
```

### Solution 3: Let auto-increment handle primary key generation

Remove the explicit primary key value and let the database assign it automatically.

```sql
-- Wrong: manually setting auto-increment value
INSERT INTO users (id, name) VALUES (1, 'Alice');

-- Correct: let auto-increment assign the key
INSERT INTO users (name) VALUES ('Alice');
-- The database assigns the next available id

-- Reset auto-increment if needed (MySQL)
ALTER TABLE users AUTO_INCREMENT = 1;

-- PostgreSQL: use SERIAL or GENERATED ALWAYS
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- SQL Server: use IDENTITY
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL
);
```

## Prevention Tips

- Always use INSERT IGNORE, ON DUPLICATE KEY UPDATE, or ON CONFLICT to handle duplicates gracefully in production code
- Let the database handle primary key generation using auto-increment rather than manually specifying values
- Add a UNIQUE index on columns that must be unique but are not the primary key

## Related Errors

- [Unique Constraint Violation]({{< relref "/languages/sql/unique-constraint-violation.md" >}})
- [Auto Increment Error]({{< relref "/languages/sql/auto-increment-error.md" >}})
- [Duplicate Entry]({{< relref "/languages/sql/duplicate-entry.md" >}})

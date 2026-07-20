---
title: "[Solution] Duplicate Key Value Unique Index"
description: "Fix 'Duplicate key value unique index' when inserting a duplicate into a unique index."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, unique-index, duplicate"]
severity: "error"
---

# Duplicate Key Value Unique Index

## Error Message

```
ERROR 23505: duplicate key value violates unique constraint 'index_name' — The value already exists in the unique index.
```

## Common Causes

- INSERT tries to add a value that already exists in a UNIQUE INDEX column
- UPDATE changes a column to a value that matches another row in the unique index
- Bulk insert contains duplicate values in the unique index column
- Race condition between two concurrent transactions inserting the same value

## Solutions

### Solution 1: Use ON CONFLICT to handle unique index violations

Use database-specific syntax to upsert or skip on duplicate key.

```sql
-- PostgreSQL: ON CONFLICT DO UPDATE
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;

-- PostgreSQL: ON CONFLICT DO NOTHING
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice')
ON CONFLICT (email) DO NOTHING;

-- MySQL: ON DUPLICATE KEY UPDATE
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice')
ON DUPLICATE KEY UPDATE name = VALUES(name);

-- SQL Server: MERGE
MERGE INTO users AS target
USING (VALUES ('alice@example.com', 'Alice')) AS source (email, name)
ON target.email = source.email
WHEN MATCHED THEN UPDATE SET name = source.name
WHEN NOT MATCHED THEN INSERT (email, name) VALUES (source.email, source.name);
```

### Solution 2: Use INSERT IGNORE to silently skip duplicates

Skip the entire row if a duplicate key is found.

```sql
-- MySQL: ignore duplicate inserts
INSERT IGNORE INTO users (email, name)
VALUES ('alice@example.com', 'Alice');

-- PostgreSQL: use ON CONFLICT DO NOTHING
INSERT INTO users (email, name)
VALUES ('alice@example.com', 'Alice')
ON CONFLICT DO NOTHING;

-- Verify after insert
SELECT * FROM users WHERE email = 'alice@example.com';
```

### Solution 3: Identify and remove duplicate data first

If duplicates already exist, clean them up before reinserting.

```sql
-- Find duplicates in PostgreSQL
SELECT email, COUNT(*) as cnt
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Remove duplicates keeping the earliest row (PostgreSQL)
DELETE FROM users
WHERE ctid NOT IN (
    SELECT MIN(ctid)
    FROM users
    GROUP BY email
);

-- MySQL: remove duplicates
DELETE u1 FROM users u1
INNER JOIN users u2
WHERE u1.id > u2.id AND u1.email = u2.email;
```

## Prevention Tips

- Design unique indexes to match your business rules for natural keys like email, username, or serial number
- Use composite unique indexes when uniqueness depends on multiple columns together
- Handle unique constraint violations in application code with proper error handling instead of letting them crash

## Related Errors

- [Primary Key Violation]({{< relref "/languages/sql/primary-key-violation.md" >}})
- [Unique Constraint Violation]({{< relref "/languages/sql/unique-constraint-violation.md" >}})
- [Index Constraint Error]({{< relref "/languages/sql/index-constraint-error.md" >}})

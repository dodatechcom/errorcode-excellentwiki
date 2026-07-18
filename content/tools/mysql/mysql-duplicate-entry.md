---
title: "[Solution] MySQL Duplicate Entry for Key - Fix Unique Constraint Errors"
description: "Fix MySQL duplicate entry for key errors by using INSERT IGNORE, ON DUPLICATE KEY UPDATE, and proper unique index design patterns"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Duplicate Entry for Key

This error occurs when an `INSERT` or `UPDATE` statement tries to create a row that duplicates a value in a column with a `UNIQUE` index or `PRIMARY KEY`.

## What This Error Means

MySQL returns this error when a unique constraint is violated:

```
ERROR 1062 (23000): Duplicate entry 'user@example.com' for key 'users.email_unique'
```

The error message identifies the duplicate value and the index name. MySQL enforces unique constraints at the index level -- any `INSERT` or `UPDATE` that would create a duplicate entry in a unique index is rejected.

## Why It Happens

- Two concurrent requests try to insert the same value simultaneously
- Application logic does not check for existence before inserting
- Bulk import contains duplicate data
- A `UNIQUE` index was added to a table that already has duplicates
- `INSERT` is used instead of `INSERT IGNORE` or `ON DUPLICATE KEY UPDATE`
- Composite unique index is violated by a combination of column values

## How to Fix It

### 1. Use INSERT IGNORE

```sql
-- Silently skip duplicates
INSERT IGNORE INTO users (email, name) VALUES ('user@example.com', 'John');
```

### 2. Use INSERT ... ON DUPLICATE KEY UPDATE

```sql
-- Update if the key already exists
INSERT INTO users (email, name) VALUES ('user@example.com', 'John')
ON DUPLICATE KEY UPDATE name = VALUES(name);
```

### 3. Use REPLACE INTO

```sql
-- Delete the existing row and insert the new one
REPLACE INTO users (email, name) VALUES ('user@example.com', 'John');
-- WARNING: this deletes and re-inserts, which triggers DELETE triggers
```

### 4. Find and Remove Duplicates First

```sql
-- Find duplicate emails
SELECT email, COUNT(*) AS cnt
FROM users
GROUP BY email
HAVING cnt > 1;

-- Keep the row with the lowest id
DELETE u1 FROM users u1
INNER JOIN users u2
WHERE u1.email = u2.email AND u1.id > u2.id;
```

### 5. Add the Unique Index After Cleaning

```sql
-- Verify no duplicates exist
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;

-- Now add the constraint
ALTER TABLE users ADD UNIQUE INDEX email_unique (email);
```

## Common Mistakes

- Using `REPLACE INTO` without understanding that it performs a `DELETE` followed by `INSERT`, which fires triggers and changes auto-increment IDs
- Not considering that `INSERT IGNORE` also ignores other errors (like foreign key violations) -- use `ON DUPLICATE KEY UPDATE` for more precision
- Assuming `NULL` values are duplicates -- MySQL allows multiple `NULL` values in a unique index
- Catching the error in application code and retrying without using MySQL's native conflict handling
- Adding a unique index to a column that has duplicate data without first cleaning it

## Related Pages

- [MySQL Table Does Not Exist](/tools/mysql/mysql-table-doesnt-exist)
- [MySQL Foreign Key Constraint](/tools/mysql/mysql-foreign-key-constraint)
- [MySQL Data Too Long](/tools/mysql/mysql-data-too-long)
- [PostgreSQL Duplicate Key](/tools/postgresql/pg-duplicate-key)

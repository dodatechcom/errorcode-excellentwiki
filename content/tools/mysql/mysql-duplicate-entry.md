---
title: "[Solution] MySQL Duplicate Entry for Key Error — How to Fix"
description: "Fix MySQL duplicate entry errors by handling unique constraint violations, using UPSERT, correcting data, and adjusting auto-increment values"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MySQL Duplicate Entry for Key Error

This error means you are trying to insert or update a row that would create a duplicate value in a column (or combination of columns) that has a UNIQUE index or PRIMARY KEY constraint.

## Why It Happens

- Inserting a row with a PRIMARY KEY value that already exists
- Violating a UNIQUE index on a column like `email` or `username`
- Re-running a migration or script that inserts data without checking for existing rows
- AUTO_INCREMENT generates a value that collides with an existing row after a manual ID insert
- Composite unique index is violated by the combination of values
- Data import or replication replays duplicate records

## Common Error Messages

```
ERROR 1062 (23000): Duplicate entry '42' for key 'PRIMARY'
```

```
ERROR 1062 (23000): Duplicate entry 'user@example.com' for key 'email_unique'
```

```
ERROR 1062 (23000): Duplicate entry '100-50' for key 'order_product_unique'
```

## How to Fix It

### 1. Find the Existing Conflicting Row

```sql
-- Check which value is causing the conflict
SELECT * FROM users WHERE email = 'user@example.com';

-- List all unique indexes on a table
SHOW INDEX FROM users WHERE Non_unique = 0;
```

### 2. Use INSERT IGNORE or ON DUPLICATE KEY UPDATE

```sql
-- Skip duplicates silently
INSERT IGNORE INTO users (id, email, name)
VALUES (1, 'user@example.com', 'John');

-- Update the existing row on conflict
INSERT INTO users (id, email, name)
VALUES (1, 'user@example.com', 'John')
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    updated_at = NOW();
```

### 3. Use REPLACE INTO

```sql
-- Delete the existing row and insert the new one
REPLACE INTO users (id, email, name)
VALUES (1, 'user@example.com', 'John');
```

### 4. Fix AUTO_INCREMENT Collision

```sql
-- Find the maximum ID currently in use
SELECT MAX(id) FROM users;

-- Reset AUTO_INCREMENT to max + 1
ALTER TABLE users AUTO_INCREMENT = 1001;
```

### 5. Handle in Application Code

```python
import mysql.connector

try:
    cursor.execute(
        "INSERT INTO users (email, name) VALUES (%s, %s)",
        ('user@example.com', 'John')
    )
    db.commit()
except mysql.connector.IntegrityError as e:
    if e.errno == 1062:
        print("User already exists, updating instead")
        cursor.execute(
            "UPDATE users SET name = %s WHERE email = %s",
            ('John', 'user@example.com')
        )
        db.commit()
```

## Common Scenarios

- **Migration re-run**: A database migration script inserts seed data but is executed twice. Use `INSERT IGNORE` or check existence first.
- **Race condition**: Two concurrent requests try to register the same username. Use a unique index plus retry logic.
- **Manual ID insert then auto-increment**: You manually insert ID 500, then the AUTO_INCREMENT counter still thinks the next value is 500. Reset AUTO_INCREMENT after manual inserts.

## Prevent It

- Always handle `IntegrityError` / duplicate key errors in application code with graceful fallbacks
- Use `INSERT ... ON DUPLICATE KEY UPDATE` for upsert patterns instead of separate INSERT and UPDATE
- Reset AUTO_INCREMENT after bulk manual ID inserts to avoid future collisions

## Related Pages

- [MySQL Foreign Key Constraint](/tools/mysql/mysql-foreign-key-constraint)
- [MySQL Table Full](/tools/mysql/mysql-table-full)
- [PostgreSQL Unique Violation](/tools/postgresql/pg-unique-violation)

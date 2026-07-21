---
title: "SQL INSERT Duplicate Key Violation Error"
description: "Fix SQL INSERT duplicate key errors when inserting a row that violates a UNIQUE or PRIMARY KEY constraint."
languages: ["sql"]
error-types: ["constraint-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Primary key value already exists in the table
- UNIQUE constraint violation on one or more columns
- Auto-increment value collision after manual insert
- Composite unique constraint broken by partial match
- INSERT ... ON DUPLICATE KEY not used when needed

## How to Fix

```sql
-- WRONG: Duplicate primary key
INSERT INTO users (id, name) VALUES (1, 'Alice');
-- ERROR: Duplicate entry '1' for key 'PRIMARY'

-- CORRECT: Check before insert or use ON DUPLICATE KEY
INSERT INTO users (id, name) VALUES (1, 'Alice')
ON DUPLICATE KEY UPDATE name = 'Alice';
```

```sql
-- WRONG: Unique email constraint violated
INSERT INTO accounts (email, username) VALUES ('alice@test.com', 'alice1');
-- ERROR: Duplicate entry 'alice@test.com'

-- CORRECT: Use INSERT IGNORE or conditional insert
INSERT IGNORE INTO accounts (email, username)
VALUES ('alice@test.com', 'alice1');
```

## Examples

```sql
-- Example 1: MySQL INSERT IGNORE
INSERT IGNORE INTO products (sku, name, price)
VALUES ('WIDGET-001', 'Widget', 9.99);

-- Example 2: PostgreSQL ON CONFLICT
INSERT INTO users (email, name)
VALUES ('alice@test.com', 'Alice')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;

-- Example 3: SQL Server MERGE
MERGE INTO users AS target
USING (SELECT 'alice@test.com' AS email, 'Alice' AS name) AS source
ON target.email = source.email
WHEN MATCHED THEN UPDATE SET name = source.name
WHEN NOT MATCHED THEN INSERT (email, name) VALUES (source.email, source.name);
```

## Related Errors

- [Primary key violation](primary-key-violation) -- PK constraint failures
- [Unique constraint violation](unique-constraint-violation) -- UNIQUE constraint issues

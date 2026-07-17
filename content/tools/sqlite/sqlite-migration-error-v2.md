---
title: "SQLite - schema migration error"
description: "SQLite schema migration fails when altering table structure or adding new columns to existing tables"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "migration", "schema", "alter-table", "column", "version"]
weight: 5
---

SQLite schema migration error occurs when attempting to modify an existing table's structure. SQLite has limited ALTER TABLE support compared to other databases, making schema migrations more complex.

## Common Causes

- ALTER TABLE does not support DROP COLUMN in older versions
- Adding NOT NULL column without a DEFAULT value
- Renaming tables referenced by views or triggers
- Migrating data while altering column types
- Migration script not idempotent

## How to Fix

1. Use the limited ALTER TABLE operations available:

```sql
-- Add column (SQLite supports this)
ALTER TABLE users ADD COLUMN phone TEXT;

-- Rename table (SQLite supports this)
ALTER TABLE users RENAME TO customers;

-- Rename column (SQLite 3.25+)
ALTER TABLE users RENAME COLUMN name TO full_name;
```

2. Use the table recreation pattern for complex migrations:

```sql
BEGIN TRANSACTION;

CREATE TABLE users_new (
  id INTEGER PRIMARY KEY,
  full_name TEXT NOT NULL,
  email TEXT UNIQUE,
  age INTEGER DEFAULT 0
);

INSERT INTO users_new (id, full_name, email, age)
SELECT id, name, email, COALESCE(age, 0) FROM users;

DROP TABLE users;

ALTER TABLE users_new RENAME TO users;

COMMIT;
```

3. Use application-level migration management:

```python
import sqlite3

MIGRATIONS = [
    "ALTER TABLE users ADD COLUMN phone TEXT",
    "ALTER TABLE users ADD COLUMN created_at TEXT DEFAULT CURRENT_TIMESTAMP",
]

def migrate(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS schema_version (
            version INTEGER PRIMARY KEY
        )
    """)
    current = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()[0] or 0

    for i, sql in enumerate(MIGRATIONS[current:], start=current + 1):
        try:
            conn.execute(sql)
            conn.execute("INSERT INTO schema_version VALUES (?)", (i,))
            conn.commit()
        except sqlite3.OperationalError as e:
            print(f"Migration {i} failed: {e}")
            conn.rollback()
            break
```

4. Check SQLite version for feature support:

```bash
sqlite3 --version
# SQLite 3.39.0+ supports DROP COLUMN
```

## Examples

```sql
-- Error: ALTER TABLE users DROP COLUMN age
-- SQLite versions before 3.35 do not support DROP COLUMN

-- Fix: recreate table
BEGIN;
CREATE TABLE users_new AS SELECT id, name, email FROM users;
DROP TABLE users;
ALTER TABLE users_new RENAME TO users;
COMMIT;
```

```python
# Migration with data transformation
def migrate_v2(conn):
    conn.execute("""
        CREATE TABLE orders_new AS
        SELECT
            id,
            CAST(amount AS REAL) as amount,
            status
        FROM orders
    """)
    conn.execute("DROP TABLE orders")
    conn.execute("ALTER TABLE orders_new RENAME TO orders")
    conn.commit()
```

## Related Errors

- [Syntax error]({{< relref "/tools/sqlite/sqlite-syntax-error" >}})
- [Type error]({{< relref "/tools/sqlite/sqlite-type-error" >}})

---
title: "SQLite Constraint Error"
description: "SQLite operation violates a constraint (PRIMARY KEY, UNIQUE, NOT NULL, CHECK)."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQLite Constraint Error

A SQLite constraint error occurs when an INSERT or UPDATE operation violates a table constraint. Common constraints include PRIMARY KEY, UNIQUE, NOT NULL, and CHECK.

## Common Causes

- Duplicate PRIMARY KEY value
- UNIQUE constraint violation
- NOT NULL constraint on required column
- CHECK constraint failure

## How to Fix

### Handle Duplicate Key Errors

```sql
-- Use INSERT OR IGNORE
INSERT OR IGNORE INTO users (id, name) VALUES (1, 'Alice');

-- Use INSERT OR REPLACE
INSERT OR REPLACE INTO users (id, name) VALUES (1, 'Alice');

-- Use ON CONFLICT (SQLite 3.24+)
INSERT INTO users (id, name) VALUES (1, 'Alice')
ON CONFLICT(id) DO UPDATE SET name = excluded.name;
```

### Check Existing Constraints

```sql
.schema users
-- Shows CREATE TABLE with constraints
```

### Handle NULL Values

```sql
-- Ensure required fields are provided
INSERT INTO users (id, name) VALUES (1, NULL);
-- Error: NOT NULL constraint failed: users.name
```

### Use TRY/CATCH in Application Code

```python
import sqlite3
try:
    conn.execute('INSERT INTO users VALUES (1, "Alice")')
except sqlite3.IntegrityError as e:
    print(f"Constraint error: {e}")
```

### Check CHECK Constraints

```sql
-- Table with CHECK constraint
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    price REAL CHECK(price > 0)
);
-- INSERT INTO products VALUES (1, -10);
-- Error: CHECK constraint failed: products
```

## Examples

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL
);

INSERT INTO users VALUES (1, 'alice@example.com');
INSERT INTO users VALUES (2, 'alice@example.com');
-- Error: UNIQUE constraint failed: users.email
```

## Related Errors

- [Syntax Error]({{< relref "/tools/sqlite/sqlite-syntax-error" >}}) — SQL syntax error
- [Type Error]({{< relref "/tools/sqlite/type-mismatch3" >}}) — type mismatch

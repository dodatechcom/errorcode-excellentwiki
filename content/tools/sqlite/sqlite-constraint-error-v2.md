---
title: "SQLite - constraint violation (UNIQUE)"
description: "SQLite INSERT or UPDATE fails because it violates a UNIQUE constraint or CHECK constraint"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "constraint", "unique", "insert", "conflict", "primary-key"]
weight: 5
---

SQLite constraint violation error occurs when an INSERT or UPDATE operation violates a table constraint, most commonly a UNIQUE constraint. SQLite enforces constraints strictly and aborts the operation when a violation occurs.

## Common Causes

- INSERT with a duplicate PRIMARY KEY or UNIQUE column value
- UPDATE that would create duplicate values in a unique column
- CHECK constraint evaluating to false
- NOT NULL constraint violated with NULL value
- FOREIGN KEY constraint violated

## How to Fix

1. Use INSERT OR REPLACE to handle duplicates:

```sql
INSERT OR REPLACE INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com');
```

2. Use INSERT OR IGNORE to skip duplicates silently:

```sql
INSERT OR IGNORE INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com');
```

3. Use UPSERT (INSERT ... ON CONFLICT) for advanced handling:

```sql
INSERT INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com')
ON CONFLICT(id) DO UPDATE SET
  name = excluded.name,
  email = excluded.email;
```

4. Check for existing records before inserting:

```python
def safe_insert(conn, user):
    existing = conn.execute(
        "SELECT id FROM users WHERE email = ?", (user['email'],)
    ).fetchone()
    if existing:
        conn.execute(
            "UPDATE users SET name = ? WHERE id = ?",
            (user['name'], existing[0])
        )
    else:
        conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user['name'], user['email'])
        )
    conn.commit()
```

5. Disable foreign keys temporarily if needed:

```sql
PRAGMA foreign_keys = OFF;
-- perform operations
PRAGMA foreign_keys = ON;
```

## Examples

```sql
-- Error: UNIQUE constraint failed: users.email
INSERT INTO users (id, name, email) VALUES (1, 'John', 'john@example.com');
-- If email 'john@example.com' already exists

-- Fix: use UPSERT
INSERT INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com')
ON CONFLICT(email) DO UPDATE SET name = 'John';
```

## Related Errors

- [Database locked]({{< relref "/tools/sqlite/sqlite-database-locked-v2" >}})
- [Syntax error]({{< relref "/tools/sqlite/sqlite-syntax-error" >}})

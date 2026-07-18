---
title: "[Solution] SQL Cannot Insert Explicit Identity Value Error Fix"
description: "Fix 'cannot insert explicit identity value' in SQL. Resolve IDENTITY column insert conflicts and value management."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Cannot Insert Explicit Identity Value Error Fix

The `cannot insert explicit identity value` error occurs when you try to insert a specific value into an IDENTITY column when IDENTITY_INSERT is OFF.

## What This Error Means

IDENTITY columns auto-generate sequential values. By default, you cannot manually specify a value for these columns. When you try, the database rejects the insert.

A typical error:

```
ERROR: Cannot insert explicit value for identity column in table 'users'
when IDENTITY_INSERT is set to OFF.
```

## Why It Happens

Common causes include:

- **Explicit value with IDENTITY_INSERT OFF** — Default behavior prevents manual inserts.
- **Data migration** — Need to preserve original IDs during migration.
- **Restoring data** — Inserting data with specific identity values.
- **Application bug** — Code explicitly sets the ID column value.

## How to Fix It

### Fix 1: Enable IDENTITY_INSERT for the session

```sql
-- RIGHT: Enable before insert
SET IDENTITY_INSERT users ON;

INSERT INTO users (id, name, email)
VALUES (100, 'John', 'john@example.com');

SET IDENTITY_INSERT users OFF;
```

### Fix 2: Remove explicit ID from INSERT

```sql
-- WRONG: Explicit ID value
INSERT INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com');

-- RIGHT: Let database generate ID
INSERT INTO users (name, email)
VALUES ('John', 'john@example.com');
```

### Fix 3: Use IDENTITY_INSERT during migration

```sql
-- RIGHT: Migration script
SET IDENTITY_INSERT users ON;

INSERT INTO users (id, name, email, created_at)
SELECT id, name, email, created_at
FROM old_users;

SET IDENTITY_INSERT users OFF;

-- Reset identity counter
DBCC CHECKIDENT ('users', RESEED);
```

### Fix 4: Reset identity seed after migration

```sql
-- RIGHT: Set identity to max value + 1
DECLARE @max_id INT;
SELECT @max_id = MAX(id) FROM users;
DBCC CHECKIDENT ('users', RESEED, @max_id);
```

### Fix 5: Use sequence instead of IDENTITY

```sql
-- RIGHT: Use sequence for more control
CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1;

INSERT INTO users (id, name, email)
VALUES (NEXT VALUE FOR user_id_seq, 'John', 'john@example.com');
```

## Common Mistakes

- **Forgetting to turn off IDENTITY_INSERT** — Always set it OFF after bulk insert.
- **Not resetting seed after migration** — New rows may conflict with existing IDs.
- **Using IDENTITY for foreign keys that need specific values** — Consider sequences instead.

## Related Pages

- [SQL Autoincrement Error](sql-autoincrement-error) — AUTOINCREMENT issues
- [SQL Constraint Error](sql-constraint-error) — Constraint violations
- [SQL Identity Error](sql-identity-error) — Identity column issues

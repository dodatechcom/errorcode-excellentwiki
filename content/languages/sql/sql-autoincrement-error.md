---
title: "[Solution] SQL AUTOINCREMENT Constraint Failed Error Fix"
description: "Fix 'AUTOINCREMENT constraint failed' in SQLite. Resolve auto-increment key conflicts and duplicate primary key errors."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL AUTOINCREMENT Constraint Failed Error Fix

The `AUTOINCREMENT constraint failed` error occurs when SQLite cannot generate a new unique rowid because the maximum integer key (9223372036854775807) has been reached or when inserting a conflicting explicit ID.

## What This Error Means

SQLite AUTOINCREMENT ensures monotonically increasing integer primary keys. Once the maximum rowid is used, no new rows can be inserted. This also applies to explicit inserts that conflict with the auto-increment sequence.

A typical error:

```
SQLITE_ERROR: AUTOINCREMENT constraint failed
```

## Why It Happens

Common causes include:

- **Maximum rowid reached** — 9223372036854775807 is the maximum.
- **Explicit ID conflicts** — Inserting a specific ID that already exists.
- **Reseeding issues** — The internal counter was not reset properly.
- **Table corruption** — Database corruption causes ID conflicts.
- **Bulk insert with explicit IDs** — Some IDs conflict with existing rows.

## How to Fix It

### Fix 1: Use INTEGER PRIMARY KEY without AUTOINCREMENT

```sql
-- RIGHT: Use INTEGER PRIMARY KEY (auto-increments naturally)
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

-- This automatically assigns the next available rowid
INSERT INTO users (name, email) VALUES ('John', 'john@example.com');
```

### Fix 2: Check for existing IDs before insert

```sql
-- RIGHT: Use INSERT OR REPLACE
INSERT OR REPLACE INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com');

-- RIGHT: Or use INSERT OR IGNORE
INSERT OR IGNORE INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com');
```

### Fix 3: Use UPSERT with ON CONFLICT

```sql
-- RIGHT: Modern SQLite UPSERT
INSERT INTO users (id, name, email)
VALUES (1, 'John', 'john@example.com')
ON CONFLICT(id) DO UPDATE SET 
    name = excluded.name,
    email = excluded.email;
```

### Fix 4: Monitor rowid usage

```sql
-- RIGHT: Check current max rowid
SELECT MAX(rowid) FROM users;

-- Check for gaps
SELECT rowid, rowid - LAG(rowid) OVER (ORDER BY rowid) AS gap
FROM users;
```

### Fix 5: Use UUID instead of integer autoincrement

```sql
-- RIGHT: UUID primary key avoids integer overflow
CREATE TABLE users (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    name TEXT,
    email TEXT
);

INSERT INTO users (name, email) VALUES ('John', 'john@example.com');
```

## Common Mistakes

- **Using AUTOINCREMENT when not needed** — INTEGER PRIMARY KEY is usually sufficient.
- **Not monitoring rowid approaching max** — Plan migration before reaching 9223372036854775807.
- **Assuming AUTOINCREMENT reuses deleted IDs** — It does not; IDs are never reused.

## Related Pages

- [SQL Identity Error](sql-identity-error) — IDENTITY column issues
- [SQL Constraint Error](sql-constraint-error) — Constraint violations
- [SQL Index Error](sql-index-error) — Index creation issues

---
title: "SQLite Migration Error"
description: "SQLite database schema migration fails during upgrade."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQLite Migration Error

A SQLite migration error occurs when a schema migration fails. SQLite has limited ALTER TABLE support, which makes migrations more complex than other databases.

## Common Causes

- ALTER TABLE limitations in SQLite
- Column type changes not directly supported
- Foreign key constraint conflicts
- Migration script syntax errors

## How to Fix

### Limited ALTER TABLE Support

```sql
-- SQLite supports:
ALTER TABLE users ADD COLUMN email TEXT;
-- SQLite does NOT support:
ALTER TABLE users DROP COLUMN name;  -- Not supported directly
```

### Use Migration Table

```sql
-- Create a new table with updated schema
CREATE TABLE users_new (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
);

-- Copy data
INSERT INTO users_new SELECT id, name, email FROM users;

-- Drop old table
DROP TABLE users;

-- Rename new table
ALTER TABLE users_new RENAME TO users;
```

### Handle Column Renames

```sql
-- SQLite 3.25+ supports
ALTER TABLE users RENAME COLUMN old_name TO new_name;
```

### Use Migration Tools

```python
# Using alembic for SQLite
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('users', sa.Column('email', sa.String(100)))
```

### Disable Foreign Keys During Migration

```sql
PRAGMA foreign_keys = OFF;
-- Run migration
PRAGMA foreign_keys = ON;
```

### Check Migration Status

```sql
-- Track migrations
CREATE TABLE IF NOT EXISTS schema_migrations (
    version INTEGER PRIMARY KEY,
    applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Examples

```sql
-- SQLite migration: add column
ALTER TABLE users ADD COLUMN created_at DATETIME;

-- SQLite migration: rename column (3.25+)
ALTER TABLE users RENAME COLUMN name TO full_name;

-- Complex migration: recreate table
CREATE TABLE users_new AS SELECT id, name, email FROM users;
DROP TABLE users;
ALTER TABLE users_new RENAME TO users;
```

## Related Errors

- [Syntax Error]({{< relref "/tools/sqlite/sqlite-syntax-error" >}}) — SQL syntax error
- [Backup Error]({{< relref "/tools/sqlite/sqlite-backup-error" >}}) — backup failure

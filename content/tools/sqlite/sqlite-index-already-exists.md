---
title: "[Solution] SQLite index already exists"
description: "A CREATE INDEX statement tries to create an index that already exists."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite index already exists

SQLite raises **'index already exists'** when a create index statement tries to create an index that already exists. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The index was created by a previous operation.
- A migration script ran twice.
- Missing IF NOT EXISTS clause.

## How to Fix

### Use CREATE INDEX IF NOT EXISTS

```sql
CREATE INDEX IF NOT EXISTS idx_email ON users(email);
```

### Drop and recreate the index

```sql
DROP INDEX IF EXISTS idx_email;
CREATE INDEX idx_email ON users(email);
```

### List existing indexes

```sql
SELECT name FROM sqlite_master WHERE type='index';
```

## Examples

```sql
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_email ON users(email);
-- Error: index idx_email already exists
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

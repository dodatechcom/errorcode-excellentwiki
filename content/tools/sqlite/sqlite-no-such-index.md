---
title: "[Solution] SQLite no such index"
description: "An SQL statement references an index that does not exist in the database."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite no such index

SQLite raises **'no such index'** when an sql statement references an index that does not exist in the database. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The index was dropped or never created.
- A typo in the index name.
- The index exists in a different attached database.

## How to Fix

### List all indexes

```sql
SELECT name FROM sqlite_master WHERE type='index';
```

### Recreate the index

```sql
CREATE INDEX idx_users_email ON users(email);
```

### Use EXPLAIN to verify index usage

```sql
EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = 'a@b.com';
```

## Examples

```sql
DROP INDEX idx_nonexistent;
-- Error: no such index: idx_nonexistent
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

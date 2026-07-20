---
title: "[Solution] SQLite EXCEPT/INTERSECT type mismatch"
description: "The corresponding columns in EXCEPT or INTERSECT have incompatible data types."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite EXCEPT/INTERSECT type mismatch

SQLite raises **EXCEPT/INTERSECT type mismatch** when the corresponding columns in except or intersect have incompatible data types. This error prevents the query from executing correctly.

## Common Causes

- Column types differ between the two SELECT statements.
- One column is NULL and the other is a specific type.
- Type affinity rules cause unexpected conversions.

## How to Fix

### Align column types using CAST

```sql
SELECT id FROM active_users
EXCEPT
SELECT CAST(id AS TEXT) FROM deleted_users;
```

### Verify column types in both queries

```sql
PRAGMA table_info(active_users);
PRAGMA table_info(deleted_users);
```

### Use consistent types in all SELECT statements

```sql
SELECT id FROM t1
INTERSECT
SELECT id FROM t2;
-- Both id columns should have matching types
```

## Examples

```sql
SELECT id FROM users
EXCEPT
SELECT name FROM archived_users;
-- Error: type mismatch between INTEGER and TEXT
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

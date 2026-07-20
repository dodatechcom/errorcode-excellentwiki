---
title: "[Solution] SQLite UNION type mismatch"
description: "The corresponding columns in UNION, EXCEPT, or INTERSECT have incompatible types."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite UNION type mismatch

SQLite raises **UNION type mismatch** when the corresponding columns in union, except, or intersect have incompatible types. This error prevents the query from executing correctly.

## Common Causes

- Column 1 of SELECT is INTEGER, column 1 of UNION is TEXT.
- Different number of columns in each SELECT.
- BLOB compared to TEXT across UNION branches.

## How to Fix

### Ensure matching column types across all SELECT statements

```sql
SELECT id, name FROM users
UNION
SELECT id, CAST(name AS TEXT) FROM archived_users;
```

### Match the number of columns

```sql
SELECT id, name, email FROM users
UNION
SELECT id, name, '' AS email FROM legacy_users;
```

### Use CAST to align types

```sql
SELECT CAST(id AS TEXT) FROM t1
UNION
SELECT id FROM t2;
```

## Examples

```sql
SELECT id, name FROM users
UNION
SELECT name, id FROM archived_users;
-- Error: type mismatch (INTEGER vs TEXT in columns)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

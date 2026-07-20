---
title: "[Solution] SQLite BLOB not allowed in boolean context"
description: "A BLOB value was used in a context that expects a scalar (e.g., WHERE clause with comparison)."
tools: ["sqlite"]
error-types: ["type-error"]
severities: ["error"]
---


# [Solution] SQLite BLOB not allowed in boolean context

SQLite produces a **BLOB not allowed in boolean context** error when a blob value was used in a context that expects a scalar (e.g., where clause with comparison). Understanding SQLite's type affinity system helps prevent and resolve these issues.

## Common Causes

- Comparing a BLOB column using = in a WHERE clause.
- Using a BLOB in an aggregate function like SUM().
- A BLOB is compared to a string literal.

## How to Fix

### Use the hex() function to compare BLOBs

```sql
SELECT * FROM t WHERE hex(blob_col) = hex(X'010203');
```

### Store a hash or length for quick filtering

```sql
ALTER TABLE t ADD COLUMN blob_len INTEGER;
UPDATE t SET blob_len = length(blob_col);
```

### Avoid using BLOBs in WHERE clauses directly

```sql
-- Instead of: WHERE blob_col = X'...' 
-- Use: WHERE blob_col IS NOT NULL
```

## Examples

```sql
SELECT * FROM t WHERE blob_col = 'hello';
-- BLOB comparison with string may not work as expected
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

---
title: "[Solution] SQLite affinity type conversion"
description: "SQLite silently converts values based on column affinity, leading to unexpected stored values."
tools: ["sqlite"]
error-types: ["type-error"]
severities: ["error"]
---


# [Solution] SQLite affinity type conversion

SQLite produces a **affinity type conversion** error when sqlite silently converts values based on column affinity, leading to unexpected stored values. Understanding SQLite's type affinity system helps prevent and resolve these issues.

## Common Causes

- SQLite applies affinity rules during INSERT, silently altering data.
- A string like '123abc' is inserted into an INTEGER column and becomes 123.
- A REAL value inserted into a TEXT column becomes '3.14' (string).

## How to Fix

### Use CHECK constraints to enforce strict types

```sql
CREATE TABLE t (
    x INTEGER CHECK (typeof(x) = 'integer')
);
```

### Validate data before inserting

```sql
-- Ensure the value matches the expected type
```

### Use strict typing via STRICT tables (SQLite 3.37+)

```sql
CREATE TABLE t (x INTEGER NOT NULL) STRICT;
```

## Examples

```sql
CREATE TABLE t (x INTEGER);
INSERT INTO t VALUES ('123abc');
SELECT x FROM t;  -- Returns 123 (leading numeric portion)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

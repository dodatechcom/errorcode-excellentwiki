---
title: "[Solution] SQLite datatype mismatch"
description: "A column's actual data type does not match the expected type in an expression or constraint."
tools: ["sqlite"]
error-types: ["type-error"]
severities: ["error"]
---


# [Solution] SQLite datatype mismatch

SQLite produces a **datatype mismatch** error when a column's actual data type does not match the expected type in an expression or constraint. Understanding SQLite's type affinity system helps prevent and resolve these issues.

## Common Causes

- Comparing a TEXT column to an INTEGER value.
- A CHECK constraint expects a specific type.
- An expression result type differs from the column's declared affinity.

## How to Fix

### Cast values to the correct type

```sql
SELECT * FROM users WHERE age = CAST('25' AS INTEGER);
```

### Use typeof() to inspect column types

```sql
SELECT name, typeof(name) FROM users;
```

### Define columns with explicit types

```sql
CREATE TABLE users (id INTEGER PRIMARY KEY, age INTEGER NOT NULL);
```

## Examples

```sql
CREATE TABLE t (x INTEGER);
INSERT INTO t VALUES ('hello');
-- SQLite may accept this due to affinity, but comparisons may fail
SELECT * FROM t WHERE x = 'hello';
-- Error: datatype mismatch
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

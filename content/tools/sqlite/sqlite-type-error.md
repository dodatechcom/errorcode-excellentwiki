---
title: "SQLite Type Mismatch Error"
description: "SQLite operation encounters a data type mismatch."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "type", "mismatch", "data-type", "casting"]
weight: 5
---

# SQLite Type Mismatch Error

A SQLite type mismatch error occurs when an operation expects a specific data type but receives a different one. SQLite uses dynamic typing but still enforces some type constraints.

## Common Causes

- Comparing TEXT with INTEGER
- Passing wrong type to function
- Column type affinity mismatch
- Implicit type conversion failure

## How to Fix

### Check Column Types

```sql
.schema users
-- Note the column types
```

### Use Proper Type Casting

```sql
-- SQLite auto-casts, but be explicit
SELECT * FROM users WHERE id = CAST('1' AS INTEGER);

-- Use typeof() to check type
SELECT typeof(name), name FROM users;
```

### Fix Comparison Issues

```sql
-- Wrong: comparing incompatible types
SELECT * FROM users WHERE id = 'abc';

-- Correct
SELECT * FROM users WHERE id = 1;
```

### Use Correct Parameter Types

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
# Pass correct types
conn.execute('INSERT INTO users VALUES (?, ?)', (1, 'Alice'))
# Don't: conn.execute('INSERT INTO users VALUES (?, ?)', ('1', 'Alice'))
```

### Check Affinity Rules

```sql
-- SQLite type affinity rules:
-- INTEGER affinity: INT, INTEGER, BIGINT, etc.
-- TEXT affinity: TEXT, VARCHAR, etc.
-- REAL affinity: REAL, FLOAT, DOUBLE, etc.
-- BLOB affinity: BLOB, etc.
```

## Examples

```sql
CREATE TABLE users (id INTEGER, name TEXT);
INSERT INTO users VALUES ('abc', 'Alice');
-- Error: type mismatch

-- Fix: use correct type
INSERT INTO users VALUES (1, 'Alice');
```

## Related Errors

- [Syntax Error]({{< relref "/tools/sqlite/sqlite-syntax-error" >}}) — SQL syntax error
- [Constraint Error]({{< relref "/tools/sqlite/constraint-error" >}}) — constraint violation

---
title: "[Solution] SQLite Column Type Mismatch"
description: "Fix SQLite column type mismatch errors. Resolve affinity and type conversion issues."
tools: ["sqlite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQLite Column Type Mismatch

A type mismatch error occurs when SQLite cannot convert a value to the expected column type. While SQLite is dynamically typed, type affinity rules can still cause unexpected behavior.

## Common Causes

- Inserting a string into a column with INTEGER affinity
- Comparing values of incompatible types in WHERE clauses
- Using STRICT tables that enforce type checking
- Implicit type conversion produces unexpected results

## How to Fix

### Check Column Affinity

```sql
PRAGMA table_info(users);
```

### Use STRICT Tables for Type Safety

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
) STRICT;
```

### Cast Values Explicitly

```sql
INSERT INTO users (id, name, age)
VALUES (1, 'Alice', CAST('25' AS INTEGER));
```

### Use TRY_CAST for Safe Conversion

```sql
-- SQLite 3.44+
INSERT INTO users (id, name, age)
VALUES (1, 'Alice', TRY_CAST('not-a-number' AS INTEGER));
-- age will be NULL if conversion fails
```

### Fix Comparison Queries

```sql
-- WRONG: comparing integer column to string
SELECT * FROM users WHERE age = '25';

-- CORRECT
SELECT * FROM users WHERE age = 25;
```

## Examples

```sql
-- STRICT table rejects wrong type
INSERT INTO users (id, name, age) VALUES (1, 'Alice', 'twenty-five');
-- Error: cannot store TEXT value in INTEGER column age

-- Type mismatch in comparison
SELECT * FROM users WHERE id = 'abc';
-- Returns empty set (implicit conversion, no error but wrong results)
```

## Related Errors

- [Unique Constraint]({{< relref "/tools/sqlite/constraint-error" >}}) — duplicate value error
- [No Such Table]({{< relref "/tools/sqlite/no-such-table" >}}) — table does not exist

---
title: "SQLite - type mismatch (INTEGER/TEXT)"
description: "SQLite encounters a data type mismatch when comparing or inserting values of incompatible types"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

SQLite type mismatch error occurs when an operation encounters values of incompatible types. SQLite uses dynamic typing and type affinity, but certain operations still require compatible types, especially comparisons and CAST operations.

## Common Causes

- Comparing INTEGER column with TEXT value
- INSERTING string into INTEGER column without explicit cast
- CAST operation failing on incompatible types
- CHECK constraint failing due to type mismatch
- Aggregate functions receiving mixed types

## How to Fix

1. Use explicit CAST for type conversion:

```sql
-- Cast TEXT to INTEGER
SELECT * FROM users WHERE CAST(age AS INTEGER) > 18;

-- Cast INTEGER to TEXT
SELECT * FROM logs WHERE CAST(id AS TEXT) = '123';
```

2. Use typeof() to check types before operations:

```sql
SELECT * FROM users WHERE typeof(age) = 'integer' AND age > 18;
```

3. Insert with proper types:

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')

# Bad: inserting string for integer column
conn.execute("INSERT INTO users (age) VALUES (?)", ("25",))

# Good: proper type
conn.execute("INSERT INTO users (age) VALUES (?)", (25,))
```

4. Use COALESCE for nullable mixed-type columns:

```sql
SELECT COALESCE(CAST(mixed_column AS INTEGER), 0) FROM table_name;
```

5. Define column types explicitly in table creation:

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER,
  email TEXT UNIQUE
);
```

6. Use try-except in application code:

```python
try:
    cursor.execute("SELECT * FROM users WHERE age > ?", (input_value,))
except sqlite3.OperationalError as e:
    if "type mismatch" in str(e):
        cursor.execute("SELECT * FROM users WHERE CAST(age AS TEXT) = ?", (input_value,))
```

## Examples

```sql
-- Error: type mismatch (INTEGER/TEXT comparison)
SELECT * FROM users WHERE age > 'twenty-five';
-- SQLite attempts type coercion but may fail

-- Fix: provide correct type
SELECT * FROM users WHERE age > 25;
```

```python
# Error: type mismatch on insert
conn.execute("INSERT INTO products (price) VALUES (?)", ("19.99",))
# If price column is INTEGER affinity

# Fix: insert correct type
conn.execute("INSERT INTO products (price) VALUES (?)", (19.99,))
```

## Related Errors

- [Syntax error]({{< relref "/tools/sqlite/sqlite-syntax-error" >}})
- [Index error]({{< relref "/tools/sqlite/sqlite-migration-error" >}})

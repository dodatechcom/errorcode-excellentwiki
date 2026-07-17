---
title: "SQLite - near syntax error"
description: "SQLite parser fails to parse a SQL statement due to syntax errors in the query"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "syntax", "sql", "parser", "query", "parse"]
weight: 5
---

SQLite "near syntax error" occurs when the SQL parser cannot understand the query due to incorrect syntax. SQLite has strict SQL syntax requirements and the error message usually indicates where the parsing failed.

## Common Causes

- Misspelled SQL keywords or function names
- Incorrect table or column names
- Missing quotes around string values
- Wrong number of arguments for functions
- SQLite-specific syntax differences from other databases

## How to Fix

1. Validate SQL syntax before execution:

```python
import sqlite3
conn = sqlite3.connect(':memory:')
try:
    conn.execute("INVALID SYNTAX HERE")
except sqlite3.OperationalError as e:
    print(f"Syntax error: {e}")
```

2. Check for common syntax issues:

```sql
-- Bad: missing quotes for string
SELECT * FROM users WHERE name = John;

-- Good: properly quoted string
SELECT * FROM users WHERE name = 'John';
```

3. Use SQLite-compatible syntax:

```sql
-- MySQL syntax (not SQLite)
SELECT IFNULL(name, 'Unknown') FROM users;

-- SQLite syntax
SELECT COALESCE(name, 'Unknown') FROM users;
```

4. Check function arguments:

```sql
-- Bad: SUBSTR needs 3 arguments in SQLite
SELECT SUBSTR(name) FROM users;

-- Good: correct argument count
SELECT SUBSTR(name, 1, 10) FROM users;
```

5. Test queries in the SQLite CLI:

```bash
sqlite3 mydb.sqlite "SELECT * FROM users WHERE name = 'Test';"
```

6. Use parameterized queries to avoid escaping issues:

```python
cursor.execute("SELECT * FROM users WHERE name = ?", (user_name,))
```

## Examples

```sql
-- Error: near "SELECT": syntax error
SELECT * FROM users; SELECT * FROM orders;
-- SQLite only executes one statement at a time

-- Fix: execute separately
cursor.execute("SELECT * FROM users")
cursor.execute("SELECT * FROM orders")
```

```sql
-- Error: near "FROM": syntax error
SELECT * WHERE id = 1;
-- Missing table name

-- Fix: add FROM clause
SELECT * FROM users WHERE id = 1;
```

## Related Errors

- [Type error]({{< relref "/tools/sqlite/sqlite-type-error" >}})
- [Constraint error]({{< relref "/tools/sqlite/sqlite-constraint-error" >}})

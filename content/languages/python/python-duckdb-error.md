---
title: "[Solution] Python DuckDB Query Error — How to Fix"
description: "Fix Python DuckDB query errors. Resolve SQL syntax failures, type conversion issues, and connection problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python DuckDB Query Error

A `duckdb.BinderException` or `duckdb.ParserException` occurs when a DuckDB SQL query references invalid columns, uses unsupported syntax, or attempts type conversions that are not allowed.

## Why It Happens

DuckDB is an embedded analytical database that executes SQL on in-memory DataFrames and files. Errors arise from SQL syntax mistakes, referencing columns that do not exist in the source data, mixing Python objects with SQL expressions incorrectly, or using features not yet supported by the current DuckDB version.

## Common Error Messages

- `BinderException: Referenced column "col_name" not found in FROM clause`
- `ParserException: syntax error at or near "SELECT"`
- `TypeMismatchException: Cannot compare values of type VARCHAR and INTEGER`
- `InvalidInputException: Expected 1 result for scalar subquery, got 2`

## How to Fix It

### Fix 1: Validate SQL syntax before execution

```python
import duckdb

conn = duckdb.connect()

# Wrong — incorrect SQL syntax
# conn.execute("SELECT * FORM users")

# Correct — validate query structure
query = "SELECT name, age FROM users WHERE age > ?"
result = conn.execute(query, [25]).fetchall()

# Use EXPLAIN to check query plan without executing
conn.execute("EXPLAIN SELECT name FROM users WHERE age > 25")
```

### Fix 2: Ensure column names match the source

```python
import duckdb
import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})

# Wrong — case-sensitive column mismatch
# conn.execute("SELECT name FROM df")

# Correct — match exact column casing
conn = duckdb.connect()
result = conn.execute('SELECT "Name" FROM df').fetchall()
print(result)

# Register DataFrame with explicit alias
conn.register("my_table", df)
result = conn.execute("SELECT Name, Age FROM my_table WHERE Age > 25").fetchall()
```

### Fix 3: Handle type conversions explicitly

```python
import duckdb

conn = duckdb.connect()
conn.execute("CREATE TABLE events (ts VARCHAR, amount VARCHAR)")
conn.execute("INSERT INTO events VALUES ('2024-01-15', '100.50')")

# Wrong — cannot compare VARCHAR directly
# conn.execute("SELECT * FROM events WHERE amount > 100")

# Correct — cast types before comparison
result = conn.execute(
    "SELECT ts, CAST(amount AS DOUBLE) AS amount "
    "FROM events WHERE CAST(amount AS DOUBLE) > 100"
).fetchall()

# Use TRY_CAST for safe conversion
result = conn.execute(
    "SELECT TRY_CAST(amount AS DOUBLE) AS safe_amount FROM events"
).fetchall()
```

### Fix 4: Manage in-memory database lifecycle

```python
import duckdb

# Wrong — new connection each time loses data
# conn1 = duckdb.connect()
# conn1.execute("CREATE TABLE t1 (id INT)")
# conn2 = duckdb.connect()  # separate in-memory database
# conn2.execute("SELECT * FROM t1")  # TableNotFoundError

# Correct — reuse connection or use persistent database
conn = duckdb.connect(":memory:")
conn.execute("CREATE TABLE t1 (id INT)")
conn.execute("INSERT INTO t1 VALUES (1), (2), (3)")
result = conn.execute("SELECT * FROM t1").fetchall()

# Or use a persistent file
conn = duckdb.connect("my_database.duckdb")
```

## Common Scenarios

- **DataFrame column casing** — Pandas DataFrames with uppercase column names cause DuckDB to fail when SQL queries use lowercase column names.
- **In-memory data loss** — Creating a new `duckdb.connect()` loses all tables from the previous connection since each is a separate in-memory database.
- **Subquery returning multiple rows** — Scalar subqueries in SELECT or WHERE clauses that return more than one row cause InvalidInputException.

## Prevent It

- Always print `df.columns` before querying to verify exact column names and casing.
- Store the DuckDB connection object and reuse it throughout your application.
- Use parameterized queries with `?` placeholders to avoid SQL injection and quoting issues.

## Related Errors

- [OperationalError](/languages/python/operationalerror/) — database operation failed
- [SyntaxError](/languages/python/syntaxerror/) — invalid SQL syntax
- [TypeError](/languages/python/typeerror/) — unsupported operand type

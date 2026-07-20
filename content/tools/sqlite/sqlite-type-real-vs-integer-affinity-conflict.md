---
title: "[Solution] SQLite REAL vs INTEGER affinity conflict"
description: "A column declared as INTEGER received floating point data, causing unexpected affinity behavior."
tools: ["sqlite"]
error-types: ["type-error"]
severities: ["error"]
---


# [Solution] SQLite REAL vs INTEGER affinity conflict

SQLite produces a **REAL vs INTEGER affinity conflict** error when a column declared as integer received floating point data, causing unexpected affinity behavior. Understanding SQLite's type affinity system helps prevent and resolve these issues.

## Common Causes

- Inserting a float into an INTEGER affinity column.
- A SELECT expression returns REAL but the target column expects INTEGER.
- Column affinity rules are misunderstood.

## How to Fix

### Understand SQLite affinity rules

```sql
-- INTEGER affinity: type contains 'INT'
-- REAL affinity: type contains 'REAL', 'FLOA', or 'DOUB'
-- TEXT affinity: type contains 'TEXT' or 'CLOB'
-- BLOB affinity: type contains 'BLOB' or no type
-- NUMERIC affinity: everything else
```

### Use the correct column type for your data

```sql
CREATE TABLE measurements (value REAL);  -- for floats
CREATE TABLE counts (value INTEGER);       -- for integers
```

### Cast values explicitly when inserting

```sql
INSERT INTO counts (value) VALUES (CAST(3.14 AS INTEGER));
-- value becomes 3
```

## Examples

```sql
CREATE TABLE t (x INTEGER);
INSERT INTO t VALUES (3.99);
SELECT x FROM t;  -- Returns 3 (truncated due to INTEGER affinity)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

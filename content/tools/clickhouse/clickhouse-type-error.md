---
title: "[Solution] ClickHouse Data Type Error — How to Fix"
description: "Fix ClickHouse data type errors including type mismatches, nullable column issues, LowCardinality misuse, and Enum conversion problems"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Data Type Error

ClickHouse has unique data types that differ from standard SQL databases. Type errors occur when data does not match the column type, when using Nullable incorrectly, or when ClickHouse-specific types are misused.

## Why It Happens

- Inserting a value that does not match the column type
- Using `Nullable` on types that do not support it (e.g., in MergeTree primary keys)
- `LowCardinality` applied to columns with too many unique values
- `Enum` values not in the defined set
- Implicit type conversion fails
- The column type is too small for the data being inserted

## Common Error Messages

```
Code: 53. DB::Exception: Type mismatch in IN expression
```

```
Code: 130. DB::Exception: Column 'status' has type Enum8, but value is not in enum
```

```
Code: 62. DB::Exception: Nested type Array is not compatible with low cardinality
```

```
Code: 183. DB::Exception: Cannot convert string to UInt64
```

## How to Fix It

### 1. Fix Type Mismatches

```sql
-- Check column types
DESCRIBE TABLE mydb.events;

-- Insert with correct types
INSERT INTO events (id, name, value) VALUES (1, 'event', 42);

-- Use CAST for explicit conversion
SELECT CAST('2024-01-15' AS Date);
SELECT CAST(123 AS String);
```

### 2. Fix Nullable Column Issues

```sql
-- BAD: Nullable in MergeTree primary key
CREATE TABLE t (id Nullable(UInt64), name String) ENGINE = MergeTree() ORDER BY id;

-- GOOD: use a default value instead of Nullable in primary keys
CREATE TABLE t (id UInt64 DEFAULT 0, name String) ENGINE = MergeTree() ORDER BY id;

-- Nullable is fine for non-primary-key columns
CREATE TABLE t (
  id UInt64,
  name String,
  email Nullable(String)
) ENGINE = MergeTree() ORDER BY id;
```

### 3. Fix LowCardinality Misuse

```sql
-- BAD: LowCardinality with millions of unique values
CREATE TABLE events (
  user_id LowCardinality(String)  -- millions of unique values
) ENGINE = MergeTree() ORDER BY user_id;

-- GOOD: LowCardinality for columns with few unique values (up to ~10K)
CREATE TABLE events (
  status LowCardinality(String),  -- 'active', 'inactive', 'pending'
  user_id String  -- regular String for high cardinality
) ENGINE = MergeTree() ORDER BY user_id;
```

### 4. Fix Enum Conversion

```sql
-- Define enum
CREATE TABLE t (
  color Enum8('red' = 1, 'green' = 2, 'blue' = 3)
) ENGINE = MergeTree() ORDER BY color;

-- Insert valid values
INSERT INTO t VALUES ('red');

-- Handle invalid values with a default
ALTER TABLE t ALTER COLUMN color SET DEFAULT 'red';
```

## Common Scenarios

- **INSERT fails with type mismatch**: The application sends a string where ClickHouse expects a UInt64. Fix the application code.
- **Nullable in GROUP BY causes issues**: Use `toNullable()` explicitly or avoid Nullable in GROUP BY columns.
- **LowCardinality hurts performance**: Too many unique values degrade performance. Use regular String instead.

## Prevent It

- Use `DESCRIBE TABLE` to check column types before writing queries
- Avoid `Nullable` in primary keys and ORDER BY columns
- Only use `LowCardinality` for columns with fewer than 10,000 unique values

## Related Pages

- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
- [ClickHouse Grammar Error](/tools/clickhouse/clickhouse-grammar-error)
- [ClickHouse Function Error](/tools/clickhouse/clickhouse-function-error)

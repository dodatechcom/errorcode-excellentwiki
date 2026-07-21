---
title: "[Solution] TiDB Data Type Error — How to Fix"
description: "Fix TiDB data type errors by resolving type conversion failures, correcting precision mismatches, and handling unsupported type operations"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Data Type Error

TiDB data type errors occur when operations involve incompatible data types, precision loss during conversions, or use of types with unsupported features.

## Why It Happens

- Implicit type conversion fails between incompatible types
- DECIMAL precision exceeds TiDB limits
- BLOB column used in a group by operation
- TIMESTAMP range exceeded for 32-bit values
- JSON path references a non-existent key
- ENUM or SET values do not match defined options

## Common Error Messages

```
ERROR: Truncated incorrect DECIMAL value
```

```
ERROR: Data too long for column at row 1
```

```
ERROR: Invalid JSON text in field
```

```
ERROR: Incorrect datetime value
```

## How to Fix It

### 1. Fix Type Conversion Errors

```sql
-- Explicit CAST instead of implicit conversion
SELECT CAST(col_string AS DECIMAL(10,2)) FROM my_table;

-- Safe conversion with IFNULL
SELECT IFNULL(CAST(col AS UNSIGNED), 0) FROM my_table;

-- Check column types
DESCRIBE my_table;
SHOW COLUMNS FROM my_table;
```

### 2. Fix DECIMAL Precision Issues

```sql
-- Increase decimal precision
ALTER TABLE my_table MODIFY price DECIMAL(18,4);

-- Round before insert
INSERT INTO my_table (price)
VALUES (ROUND(1234567890.123456, 4));

-- Check current precision
SELECT COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_NAME = 'my_table' AND COLUMN_NAME = 'price';
```

### 3. Fix JSON Data Type Errors

```sql
-- Validate JSON before inserting
INSERT INTO my_table (data)
VALUES (JSON_VALID('{"key": "value"}'));

-- Use JSON path with proper escaping
SELECT JSON_EXTRACT(data, '$.nested.key') FROM my_table;

-- Repair malformed JSON
UPDATE my_table
SET data = JSON_OBJECT('raw', data)
WHERE NOT JSON_VALID(data);
```

### 4. Fix Date and Time Errors

```sql
-- Insert with explicit format
INSERT INTO my_table (created_at)
VALUES (STR_TO_DATE('2024-01-15', '%Y-%m-%d'));

-- Handle zero dates
SET sql_mode = 'ALLOW_INVALID_DATES';
INSERT INTO my_table (created_at) VALUES ('0000-00-00 00:00:00');

-- Convert string to date safely
SELECT IF(col_date = '0000-00-00', NULL, col_date) FROM my_table;
```

## Common Scenarios

- **INSERT fails with type mismatch**: Use explicit CAST in the INSERT statement.
- **GROUP BY fails on BLOB**: Convert BLOB to string or remove it from the query.
- **TIMESTAMP overflow**: Use DATETIME type for dates beyond 2038.

## Prevent It

- Define columns with appropriate data types and precision
- Use explicit CAST when mixing types in queries
- Validate JSON data before insertion

## Related Pages

- [TiDB DML Error](/tools/tidb/tidb-dml-error)
- [TiDB JSON Error](/tools/tidb/tidb-json-error)
- [TiDB Index Error](/tools/tidb/tidb-index-error)

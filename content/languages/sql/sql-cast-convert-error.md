---
title: "SQL CAST and CONVERT Type Error"
description: "Fix SQL CAST and CONVERT errors when converting between incompatible data types or invalid format strings."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Converting non-numeric string to INTEGER or DECIMAL
- CAST to a type with insufficient precision or scale
- CONVERT format string does not match input date format
- Casting BLOB/CLOB to incompatible type
- Truncation warning when target type is too small

## How to Fix

```sql
-- WRONG: Cast non-numeric to integer
SELECT CAST('abc' AS INTEGER);
-- ERROR: invalid input syntax for integer

-- CORRECT: Validate first or use TRY_CAST
SELECT TRY_CAST('abc' AS INTEGER);  -- returns NULL
-- or
SELECT CASE WHEN 'abc' ~ '^\d+$' THEN CAST('abc' AS INTEGER) ELSE NULL END;
```

```sql
-- WRONG: Date format mismatch
SELECT CONVERT(DATETIME, '01-15-2024', 101);
-- Wrong format code for this database

-- CORRECT: Use appropriate format
SELECT CONVERT(DATETIME, '2024-01-15', 23);  -- ISO format
```

## Examples

```sql
-- Example 1: Safe string to number
SELECT CAST(NULLIF(TRIM(' 123 '), '') AS INT) AS num;
-- Returns 123

-- Example 2: Date conversion
SELECT CAST('2024-01-15' AS DATE) AS date_val;
SELECT CONVERT(VARCHAR, GETDATE(), 101) AS us_date;

-- Example 3: Precision and scale
SELECT CAST(12345.6789 AS DECIMAL(6,2));  -- 12345.68 (truncated)
SELECT CAST(12345.6789 AS DECIMAL(10,4)); -- 12345.6789 (preserved)
```

## Related Errors

- [Data type mismatch](data-type-mismatch) -- type incompatibility
- [Numeric overflow](numeric-overflow) -- arithmetic overflow

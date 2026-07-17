---
title: "[Solution] SQL Incompatible Type Comparison Fix"
description: "Fix 'Incompatible type comparison' when comparing values of different data types."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["type-comparison", "incompatible", "collation", "implicit-conversion"]
weight: 5
---

This error occurs when a WHERE clause or JOIN condition compares values of incompatible data types that cannot be implicitly converted.

## What This Error Means

The database cannot compare two values because their data types are incompatible. For example, comparing a BLOB to a string, or a JSON column to an integer.

## Common Causes

- Comparing BLOB or JSON columns directly
- Comparing columns with different collations
- Comparing a string column to an incompatible type
- Using the wrong type in a JOIN condition

## How to Fix

### Fix 1: Cast values to compatible types

```sql
-- Wrong: comparing JSON to integer
SELECT * FROM products WHERE attributes = 42;

-- Correct: extract JSON value first
SELECT * FROM products WHERE JSON_EXTRACT(attributes, '$.id') = 42;
```

### Fix 2: Ensure matching collations

```sql
-- Check collation
SHOW FULL COLUMNS FROM users;

-- Fix with explicit collation
SELECT * FROM users a
JOIN profiles b ON a.name COLLATE utf8mb4_unicode_ci = b.display_name COLLATE utf8mb4_unicode_ci;
```

### Fix 3: Convert types explicitly

```sql
-- Wrong: string compared to binary
SELECT * FROM logs WHERE data = 12345;

-- Correct: cast appropriately
SELECT * FROM logs WHERE CAST(data AS CHAR) = '12345';
```

## Examples

```sql
SELECT * FROM t WHERE blob_column = 'test';
-- ERROR 1267: Illegal mix of collations for operation '='
```

## Related Errors

- [Data Truncation](data-truncated.md) — value doesn't fit column type
- [Syntax Error](syntax-error.md) — malformed SQL

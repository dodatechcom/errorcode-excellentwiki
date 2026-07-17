---
title: "[Solution] SQL Data Truncation Error Fix"
description: "Fix 'Data truncation: incorrect datetime value' when inserting data that doesn't match column type."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["data-truncation", "type-conversion", "datetime", "varchar", "overflow"]
weight: 5
---

This error occurs when the data being inserted or updated does not fit the target column type. The message reads: `Data truncation: incorrect datetime value` or similar.

## What This Error Means

The database attempted to convert the input value to the column's data type but the conversion failed. This happens with datetime formats, string-to-number conversions, or string length exceeding VARCHAR limits.

## Common Causes

- Datetime string does not match `YYYY-MM-DD HH:MM:SS` format
- String value exceeds VARCHAR/TEXT column length
- Numeric value has more digits than the column allows
- Implicit type conversion fails

## How to Fix

### Fix 1: Use correct datetime format

```sql
-- Wrong
INSERT INTO logs (created_at) VALUES ('01/15/2024 10:30 AM');

-- Correct
INSERT INTO logs (created_at) VALUES ('2024-01-15 10:30:00');
```

### Fix 2: Use STR_TO_DATE for custom formats

```sql
INSERT INTO logs (created_at)
VALUES (STR_TO_DATE('01/15/2024 10:30 AM', '%m/%d/%Y %h:%i %p'));
```

### Fix 3: Check string length

```sql
-- Column is VARCHAR(50) but value is longer
INSERT INTO users (bio) VALUES ('A very long bio that exceeds fifty characters...');
-- Data truncation: Data too long for column 'bio'

-- Fix: truncate or use TEXT type
INSERT INTO users (bio) VALUES (LEFT('A very long bio...', 50));
```

## Examples

```sql
INSERT INTO events (event_date) VALUES ('2024-13-01');
-- ERROR 1292: Data truncation: Incorrect datetime value: '2024-13-01'
```

## Related Errors

- [Division by Zero](div-by-zero.md) — numeric computation error
- [BIGINT Overflow](big-int-overflow.md) — numeric range exceeded

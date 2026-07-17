---
title: "[Solution] SQL Type Mismatch / Incorrect Value Error Fix"
description: "Fix 'Incorrect datetime value' or type conversion errors when a value doesn't match the expected column type."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SQL Type Mismatch / Incorrect Value Error Fix

This error occurs when a value doesn't match the expected data type of the target column. The message reads: `Incorrect datetime value`, `Incorrect ... value for column 'X'`, or `Truncated incorrect ... value`.

## Description

SQL columns have strict data types. When inserting or updating, the database attempts to cast the provided value to the column's type. If the cast fails — e.g., a string like `'abc'` into a DATE column — the operation is rejected.

## Common Causes

- **String in a date column** — `'2025/12/25'` instead of `'2025-12-25'`.
- **Text in a numeric column** — `'hello'` in an INT column.
- **Wrong date format** — locale-specific formats like `DD/MM/YYYY` in a `YYYY-MM-DD` column.
- **Implicit casting failure** — database can't auto-convert between incompatible types.

## How to Fix

### Fix 1: Use proper date literal format

```sql
-- Wrong — MySQL expects YYYY-MM-DD
INSERT INTO events (event_date) VALUES ('25/12/2025');

-- Correct
INSERT INTO events (event_date) VALUES ('2025-12-25');

-- Use STR_TO_DATE for custom formats
INSERT INTO events (event_date)
VALUES (STR_TO_DATE('25/12/2025', '%d/%m/%Y'));
```

### Fix 2: Cast explicitly

```sql
-- Convert string to date
SELECT CAST('2025-12-25' AS DATE);

-- Convert string to decimal
SELECT CAST('19.99' AS DECIMAL(10,2));

-- Convert number to string
SELECT CAST(123 AS CHAR);
```

### Fix 3: Use CONVERT for formatted output

```sql
-- Format a date as a string
SELECT CONVERT('2025-12-25', DATE);

-- Parse a formatted string to date
SELECT CONVERT('25/12/2025', DATE);
```

### Fix 4: Validate before inserting

```sql
-- Check if the value is a valid date before inserting
INSERT INTO events (event_date)
SELECT '2025-12-25'
WHERE STR_TO_DATE('2025-12-25', '%Y-%m-%d') IS NOT NULL;
```

## Examples

```sql
INSERT INTO events (event_date) VALUES ('not-a-date');
-- ERROR 1292: Incorrect datetime value: 'not-a-date' for column 'event_date'

INSERT INTO products (price) VALUES ('abc');
-- ERROR 1366: Incorrect decimal value: 'abc' for column 'price'

UPDATE users SET created_at = '13:00:00' WHERE id = 1;
-- ERROR 1292: Incorrect datetime value: '13:00:00' for column 'created_at'
```

## Related Errors

- [Data Truncation](data-truncation.md) — value too long or truncated.
- [Null Constraint](null-constraint.md) — column cannot be NULL.
- [Division by Zero](division-by-zero.md) — arithmetic error in expressions.

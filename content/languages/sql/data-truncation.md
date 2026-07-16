---
title: "[Solution] SQL Data Truncation Error Fix"
description: "Fix 'Data truncation' when a value is too long or doesn't fit the column's expected format."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["data-truncation", "value-too-long", "incorrect-value"]
weight: 5
---

# SQL Data Truncation Error Fix

This error occurs when a value being inserted or updated is too large for the column or doesn't match the expected format. The message reads: `Data truncation: Incorrect ... value` or `Data truncation: Data too long for column 'X'`.

## Description

Column definitions include size limits (VARCHAR length, INT range) and format requirements (DATE, DATETIME). When a value exceeds these constraints, the database rejects it. In strict SQL mode, this is an error; in lenient mode, the value is silently truncated.

## Common Causes

- **String too long** — inserting a value longer than VARCHAR(n).
- **Number out of range** — exceeding INT, BIGINT, or DECIMAL bounds.
- **Incorrect date/time format** — string doesn't match DATE or DATETIME format.
- **Incorrect numeric format** — string instead of number, or wrong precision.

## How to Fix

### Fix 1: Truncate the string before inserting

```sql
-- MySQL
INSERT INTO users (name) VALUES (LEFT('Very Long Name That Exceeds Limit', 50));

-- Or ensure application-side truncation
SET @name = SUBSTRING('Very Long Name', 1, 50);
INSERT INTO users (name) VALUES (@name);
```

### Fix 2: Use correct date/time format

```sql
-- Wrong — format is YYYY-MM-DD
INSERT INTO events (event_date) VALUES ('12-25-2025');

-- Correct
INSERT INTO events (event_date) VALUES ('2025-12-25');

-- Wrong — invalid datetime
INSERT INTO events (event_time) VALUES ('25:00:00');

-- Correct
INSERT INTO events (event_time) VALUES ('14:30:00');
```

### Fix 3: Increase column size if needed

```sql
-- Check current column definition
DESCRIBE users;

-- Increase the column size
ALTER TABLE users MODIFY name VARCHAR(200);
```

### Fix 4: Cast values to the correct type

```sql
-- Ensure numeric strings are treated as numbers
INSERT INTO products (price) VALUES (CAST('19.99' AS DECIMAL(10,2)));

-- Convert before inserting
INSERT INTO logs (created_at) VALUES (STR_TO_DATE('25/12/2025', '%d/%m/%Y'));
```

## Examples

```sql
INSERT INTO users (name) VALUES ('This Name Is Way Too Long For A Fifty Character Column Limit');
-- ERROR 1406: Data too long for column 'name' at row 1

INSERT INTO events (event_date) VALUES ('2025-13-01');
-- ERROR 1292: Incorrect date value: '2025-13-01' for column 'event_date'

INSERT INTO products (price) VALUES ('abc');
-- ERROR 1366: Incorrect decimal value: 'abc' for column 'price'
```

## Related Errors

- [Type Mismatch](type-mismatch.md) — related data type incompatibility.
- [Null Constraint](null-constraint.md) — column cannot be NULL.
- [Duplicate Entry](duplicate-entry.md) — value violates a UNIQUE constraint.

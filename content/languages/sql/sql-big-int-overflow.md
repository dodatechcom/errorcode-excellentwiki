---
title: "[Solution] SQL BIGINT UNSIGNED Overflow Fix"
description: "Fix 'BIGINT UNSIGNED value is out of range' when arithmetic exceeds the column's numeric range."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bigint", "overflow", "unsigned", "arithmetic", "numeric-range"]
weight: 5
---

This error occurs when an arithmetic operation produces a value that exceeds the range of a BIGINT UNSIGNED column. The message reads: `BIGINT UNSIGNED value is out of range`.

## What This Error Means

BIGINT UNSIGNED can hold values from 0 to 18,446,744,073,709,551,615. When subtraction on unsigned columns produces a negative result, or addition overflows, this error fires.

## Common Causes

- Subtracting a larger value from a smaller unsigned value
- Aggregate SUM exceeding BIGINT range
- Incrementing beyond the maximum value
- Implicit type conversion from signed to unsigned

## How to Fix

### Fix 1: Cast to signed before subtraction

```sql
-- Wrong: unsigned subtraction can't go below 0
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- If balance < 100, error

-- Correct: cast to signed
UPDATE accounts
SET balance = CAST(balance AS SIGNED) - 100
WHERE id = 1;
```

### Fix 2: Use signed column type

```sql
-- Instead of BIGINT UNSIGNED
ALTER TABLE accounts MODIFY balance BIGINT;
```

### Fix 3: Add CHECK constraint

```sql
ALTER TABLE accounts
ADD CONSTRAINT chk_balance CHECK (balance >= 0);
```

## Examples

```sql
SELECT CAST(0 AS UNSIGNED) - 1;
-- ERROR 1690: BIGINT UNSIGNED value is out of range

-- Safe alternative
SELECT CAST(0 AS SIGNED) - 1;
-- Returns -1
```

## Related Errors

- [Division by Zero](div-by-zero.md) — arithmetic error
- [Data Truncation](data-truncated.md) — value exceeds column size

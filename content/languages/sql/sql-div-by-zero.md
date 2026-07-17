---
title: "[Solution] SQL Division by Zero Fix"
description: "Fix 'Division by 0' error when a SQL query divides a value by zero."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a SQL query attempts to divide a value by zero. The message reads: `Division by 0` or `ERROR 1365: Division by 0`.

## What This Error Means

Mathematical division by zero is undefined. The database rejects the operation when the divisor evaluates to zero.

## Common Causes

- Column value is zero in a division operation
- COUNT or aggregate returns zero and is used as divisor
- Calculated denominator can be zero

## How to Fix

### Fix 1: Use NULLIF to avoid division by zero

```sql
-- Instead of: amount / total
SELECT amount / NULLIF(total, 0) AS ratio
FROM orders;

-- Returns NULL instead of error when total = 0
```

### Fix 2: Use CASE to handle zero denominator

```sql
SELECT
    amount,
    total,
    CASE
        WHEN total = 0 THEN NULL
        ELSE amount / total
    END AS ratio
FROM orders;
```

### Fix 3: Use IFNULL for default value

```sql
SELECT IFNULL(amount / NULLIF(total, 0), 0) AS ratio
FROM orders;
```

## Examples

```sql
SELECT 10 / 0;
-- ERROR 1365: Division by 0

-- Safe alternative
SELECT 10 / NULLIF(0, 0);
-- Returns NULL
```

## Related Errors

- [BIGINT Overflow](big-int-overflow.md) — numeric range exceeded
- [Data Truncation](data-truncated.md) — type conversion failure

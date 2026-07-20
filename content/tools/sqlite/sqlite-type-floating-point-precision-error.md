---
title: "[Solution] SQLite floating point precision error"
description: "Floating point arithmetic produces unexpected results due to IEEE 754 representation limitations."
tools: ["sqlite"]
error-types: ["type-error"]
severities: ["error"]
---


# [Solution] SQLite floating point precision error

SQLite produces a **floating point precision error** error when floating point arithmetic produces unexpected results due to ieee 754 representation limitations. Understanding SQLite's type affinity system helps prevent and resolve these issues.

## Common Causes

- Comparing floating point values for exact equality.
- Accumulating small floating point additions.
- Storing decimal values that cannot be represented exactly in binary.

## How to Fix

### Use integer arithmetic for exact values (e.g., cents instead of dollars)

```sql
-- Store price in cents as INTEGER
CREATE TABLE products (price_cents INTEGER);
-- 19.99 becomes 1999
```

### Compare with an epsilon tolerance

```sql
SELECT * FROM t WHERE ABS(x - 0.3) < 0.0000001;
```

### Use TEXT for exact decimal storage

```sql
CREATE TABLE prices (amount TEXT);
INSERT INTO prices VALUES ('19.99');
```

## Examples

```sql
SELECT 0.1 + 0.2 = 0.3;
-- Returns 0 (FALSE) — floating point precision
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

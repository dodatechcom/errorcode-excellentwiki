---
title: "[Solution] SQLite LIMIT/OFFSET out of range"
description: "A LIMIT or OFFSET value is negative or exceeds the maximum allowed value."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite LIMIT/OFFSET out of range

SQLite produces **LIMIT/OFFSET out of range** when a limit or offset value is negative or exceeds the maximum allowed value. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- A negative LIMIT or OFFSET value.
- The OFFSET exceeds the number of available rows.
- The value exceeds the maximum integer limit.

## How to Fix

### Use non-negative values

```sql
SELECT * FROM t LIMIT 10 OFFSET 0;
```

### Handle OFFSET exceeding row count

```sql
SELECT * FROM t LIMIT 10 OFFSET 1000;
-- Returns fewer than 10 rows if table has fewer than 1010 rows
```

### Use valid integer values

```sql
-- LIMIT must be >= 0
-- OFFSET must be >= 0
SELECT * FROM t LIMIT 10 OFFSET 5;
```

## Examples

```sql
SELECT * FROM t LIMIT -1;
-- Error: LIMIT value must be non-negative
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

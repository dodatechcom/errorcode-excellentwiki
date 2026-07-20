---
title: "[Solution] SQLite TEXT not allowed in integer context"
description: "A TEXT value was used where an INTEGER or NUMERIC value is required."
tools: ["sqlite"]
error-types: ["type-error"]
severities: ["error"]
---


# [Solution] SQLite TEXT not allowed in integer context

SQLite produces a **TEXT not allowed in integer context** error when a text value was used where an integer or numeric value is required. Understanding SQLite's type affinity system helps prevent and resolve these issues.

## Common Causes

- Comparing a TEXT column with an arithmetic operator.
- Using a TEXT column in a WHERE clause with >, <, >=, <=.
- A column declared as INTEGER received text data.

## How to Fix

### Cast TEXT to INTEGER explicitly

```sql
SELECT * FROM t WHERE CAST(age_text AS INTEGER) > 18;
```

### Store numeric data in columns with INTEGER affinity

```sql
ALTER TABLE t ADD COLUMN age INTEGER;
UPDATE t SET age = CAST(age_text AS INTEGER);
```

### Validate data types at the application layer

```python
if not value.isdigit():
    raise ValueError('Expected integer')
```

## Examples

```sql
CREATE TABLE t (x INTEGER);
INSERT INTO t VALUES ('abc');
SELECT x + 1 FROM t;
-- Unexpected result due to type coercion
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

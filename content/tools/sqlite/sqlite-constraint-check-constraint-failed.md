---
title: "[Solution] SQLite CHECK constraint failed"
description: "A CHECK constraint evaluated to FALSE during an INSERT or UPDATE operation."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite CHECK constraint failed

SQLite raises a **CHECK constraint failed** error when a check constraint evaluated to false during an insert or update operation. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- Inserting a value that violates a CHECK condition.
- Updating a row to a value that fails the CHECK.
- CHECK constraint references a column not yet available in the INSERT.

## How to Fix

### Review the CHECK constraint definition

```sql
SELECT sql FROM sqlite_master WHERE type='table' AND name='my_table';
```

### Insert values that satisfy all CHECK constraints

```sql
-- If CHECK (age >= 18), ensure age >= 18
INSERT INTO users (id, age) VALUES (1, 21);
```

### Temporarily drop the CHECK if legitimate data needs loading

```sql
-- Recreate the table without the CHECK, load data, then re-add it
```

## Examples

```sql
CREATE TABLE products (id INT, price REAL CHECK (price > 0));
INSERT INTO products VALUES (1, -5.00);
-- Error: CHECK constraint failed: products
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

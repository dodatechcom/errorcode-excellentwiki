---
title: "[Solution] SQLite type conflict in expression"
description: "An expression mixes incompatible types that cannot be implicitly converted."
tools: ["sqlite"]
error-types: ["type-error"]
severities: ["error"]
---


# [Solution] SQLite type conflict in expression

SQLite produces a **type conflict in expression** error when an expression mixes incompatible types that cannot be implicitly converted. Understanding SQLite's type affinity system helps prevent and resolve these issues.

## Common Causes

- Concatenating INTEGER and BLOB in an expression.
- Using arithmetic operators on TEXT values.
- A CASE expression returns different types for different branches.

## How to Fix

### Cast all values to a consistent type

```sql
SELECT name || ' - ' || CAST(age AS TEXT) FROM users;
```

### Use the typeof() function to debug

```sql
SELECT typeof(col1), typeof(col2) FROM my_table;
```

### Ensure CASE branches return compatible types

```sql
SELECT CASE WHEN active THEN 'Yes' ELSE 'No' END FROM users;
```

## Examples

```sql
SELECT 'Age: ' + age FROM users;
-- Error: type conflict: TEXT and INTEGER in expression
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

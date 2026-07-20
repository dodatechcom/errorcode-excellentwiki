---
title: "[Solution] SQLite ORDER BY column not found"
description: "An ORDER BY clause references a column that does not exist in the result set or table."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite ORDER BY column not found

SQLite raises **ORDER BY column not found** when an order by clause references a column that does not exist in the result set or table. This error prevents the query from executing correctly.

## Common Causes

- A typo in the column name.
- The column was aliased and the original name is used in ORDER BY.
- ORDER BY references a column not in SELECT (valid in SQLite but sometimes confusing).

## How to Fix

### Use the alias name in ORDER BY

```sql
SELECT name, age AS user_age FROM users ORDER BY user_age;
```

### Use column position

```sql
SELECT name, age FROM users ORDER BY 2;  -- orders by age
```

### Verify available columns

```sql
PRAGMA table_info(users);
```

## Examples

```sql
SELECT name FROM users ORDER BY username;
-- Error: ORDER BY column not found: username
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

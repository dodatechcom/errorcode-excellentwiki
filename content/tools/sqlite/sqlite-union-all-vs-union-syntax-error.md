---
title: "[Solution] SQLite UNION ALL vs UNION syntax error"
description: "A UNION or UNION ALL query has a syntax error."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite UNION ALL vs UNION syntax error

SQLite produces **UNION ALL vs UNION syntax error** when a union or union all query has a syntax error. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- Mismatched number of columns in SELECT statements.
- Incorrect UNION syntax.
- Missing parentheses around subqueries.

## How to Fix

### Ensure matching column counts

```sql
SELECT id, name FROM users
UNION ALL
SELECT id, name FROM archived_users;
```

### Use UNION for distinct results

```sql
SELECT id, name FROM users
UNION
SELECT id, name FROM archived_users;
```

### Parenthesize complex UNION queries

```sql
(SELECT id FROM users WHERE active = 1)
UNION
(SELECT id FROM users WHERE active = 0);
```

## Examples

```sql
SELECT id FROM users
UNION ALL
SELECT id, name FROM archived_users;
-- Error: SELECTs must have the same number of columns
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference

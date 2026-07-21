---
title: "[Solution] ClickHouse Subquery Error"
description: "Fix ClickHouse subquery errors when nested SELECT statements produce invalid results"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Subquery Error

Subquery errors occur when ClickHouse encounters invalid or unsupported subquery patterns.

## Common Causes

- Subquery returns more than one row for scalar comparison
- Correlated subquery not supported in context
- Subquery in WHERE clause references outer table column
- Using subquery where JOIN would be appropriate

## How to Fix

Use scalar subquery:

```sql
SELECT * FROM users WHERE id = (SELECT max(id) FROM users);
```

Convert to JOIN:

```sql
-- Instead of subquery
SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE active = 1);
-- Use JOIN
SELECT o.* FROM orders o JOIN users u ON o.user_id = u.id WHERE u.active = 1;
```

Use IN with set:

```sql
SELECT * FROM events WHERE type IN ('click', 'view', 'purchase');
```

## Examples

```sql
SELECT name, (SELECT count() FROM orders WHERE user_id = users.id) AS order_count
FROM users LIMIT 10;
```

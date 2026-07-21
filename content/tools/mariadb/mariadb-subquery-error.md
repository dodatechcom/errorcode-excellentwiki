---
title: "[Solution] MariaDB Subquery Error"
description: "Fix MariaDB subquery errors when nested SELECT statements produce invalid results"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Subquery Error

Subquery errors occur when MariaDB encounters invalid or unsupported subquery patterns.

## Common Causes

- Subquery returns more than one row for scalar comparison
- Correlated subquery performance issues
- Using subquery where JOIN is more efficient
- Subquery in IN clause too slow

## Common Error Messages

```
ERROR 1242 (21000): Subquery returns more than 1 row
```

## How to Fix It

### 1. Use LIMIT in Scalar Subquery

```sql
SELECT * FROM users WHERE id = (SELECT user_id FROM orders ORDER BY id DESC LIMIT 1);
```

### 2. Convert to JOIN

```sql
-- Instead of subquery
SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE active = 1);
-- Use JOIN
SELECT o.* FROM orders o JOIN users u ON o.user_id = u.id WHERE u.active = 1;
```

### 3. Use EXISTS

```sql
SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

## Examples

```sql
SELECT u.name, (SELECT count(*) FROM orders WHERE user_id = u.id) AS order_count
FROM users u LIMIT 10;
```

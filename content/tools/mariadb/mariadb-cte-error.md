---
title: "[Solution] MariaDB CTE Error"
description: "Fix MariaDB Common Table Expression errors when WITH clause queries fail"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB CTE Error

CTE errors occur when MariaDB Common Table Expression queries have syntax or scoping issues.

## Common Causes

- CTE referenced before definition
- Recursive CTE without termination condition
- CTE name conflicts with table name
- CTE with wrong column count

## Common Error Messages

```
ERROR 1146 (42S02): Table 'cte_name' doesn't exist
```

## How to Fix It

### 1. Define CTE Before Use

```sql
WITH active_users AS (
  SELECT id, name FROM users WHERE active = 1
)
SELECT * FROM active_users WHERE name LIKE 'A%';
```

### 2. Add Termination to Recursive CTE

```sql
WITH RECURSIVE org_tree AS (
  SELECT id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, t.level + 1
  FROM employees e JOIN org_tree t ON e.manager_id = t.id
  WHERE t.level < 10
)
SELECT * FROM org_tree;
```

### 3. Reference CTE with WITH

```sql
WITH cte AS (SELECT * FROM my_table)
SELECT * FROM cte;
```

## Examples

```sql
WITH dept_stats AS (
  SELECT department, avg(salary) AS avg_sal FROM employees GROUP BY department
)
SELECT d.name, ds.avg_sal FROM departments d JOIN dept_stats ds ON d.name = ds.department;
```

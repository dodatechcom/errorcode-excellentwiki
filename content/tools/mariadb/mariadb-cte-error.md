---
title: "[Solution] MariaDB CTE Error — How to Fix"
description: "Fix MariaDB Common Table Expression errors including recursive CTE depth limits, syntax issues, and performance problems in WITH queries"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB CTE Error

Common Table Expression (CTE) errors occur when using WITH clauses for complex queries. CTEs require MariaDB 10.2+ and can fail due to syntax errors, recursion limits, or performance issues.

## Why It Happens

- MariaDB version is older than 10.2
- A recursive CTE exceeds `cte_max_recursion_depth` (default 1000)
- The CTE references a column that does not exist
- CTE name conflicts with an existing table
- UNION ALL inside recursive CTE is missing members

## Common Error Messages

```
ERROR 1064 (42000): You have an error in your SQL syntax near 'WITH cte AS'
```

```
ERROR 1456 (HY000): Recursive CTE max_depth of 1000 exceeded for recursive CTE 'cte_name'
```

```
ERROR 1054 (42S22): Unknown column 'col_name' in 'CTE 'cte_name''
```

```
ERROR 3573 (HY000): Recursive query must contain one or more UNION ALL operators
```

## How to Fix It

### 1. Check MariaDB Version

```sql
SELECT VERSION();
-- CTEs require MariaDB 10.2+
```

### 2. Increase Recursive CTE Depth

```sql
SHOW VARIABLES LIKE 'cte_max_recursion_depth';
SET SESSION cte_max_recursion_depth = 5000;
```

### 3. Fix CTE Column References

```sql
WITH cte AS (
  SELECT id, name, email FROM users
)
SELECT id, name, email FROM cte;
```

### 4. Fix Recursive CTE Syntax

```sql
WITH RECURSIVE org_chart AS (
  SELECT id, name, parent_id, 1 AS depth
  FROM employees WHERE parent_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.parent_id, oc.depth + 1
  FROM employees e
  JOIN org_chart oc ON e.parent_id = oc.id
  WHERE oc.depth < 10
)
SELECT * FROM org_chart ORDER BY depth, name;
```

### 5. Optimize CTE Performance

```sql
CREATE TEMPORARY TABLE active_orders AS
SELECT id, name, status FROM orders WHERE status = 'active';

SELECT ao.name, t.total
FROM active_orders ao
JOIN (SELECT name, SUM(amount) AS total FROM active_orders GROUP BY name) t
ON ao.name = t.name;

DROP TEMPORARY TABLE active_orders;
```

## Common Scenarios

- **Hierarchy query hits recursion limit**: Increase limit or add depth safety.
- **CTE on MariaDB 10.1**: Rewrite using derived tables.
- **Performance degrades**: Materialize CTE into temporary table.

## Prevent It

- Add depth limits to recursive CTEs
- Use temporary tables for CTEs referenced multiple times
- Test recursive CTEs on staging with deep hierarchies

## Related Pages

- [MariaDB Query Error](/tools/mariadb/mariadb-query-error)
- [MariaDB Window Error](/tools/mariadb/mariadb-window-error)
- [MySQL CTE Error](/tools/mysql/mysql-cte-error)

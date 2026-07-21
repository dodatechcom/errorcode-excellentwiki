---
title: "[Solution] PostgreSQL Join Selectivity Estimation Error"
description: "Fix PostgreSQL join selectivity estimation errors. Resolve poor query plans caused by inaccurate statistics."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Join Selectivity Estimation Error

WARNING: statistics might be inaccurate / poor join performance

This error or warning occurs when the query planner misestimates the number of rows from a join, leading to very inefficient query plans such as nested loops on large datasets instead of hash joins.

## Common Causes

- Outdated table or column statistics after bulk data changes
- Correlated columns that are not captured by pg_statistic
- Data skew across partitioned or sharded tables

## How to Fix

1. Run ANALYZE on affected tables:

```sql
ANALYZE users;
ANALYZE orders;
```

2. Increase statistics target for columns involved in joins:

```sql
ALTER TABLE orders ALTER COLUMN user_id SET STATISTICS 1000;
ANALYZE orders;
```

3. Use extended statistics to capture column correlations:

```sql
CREATE STATISTICS user_order_correlation (dependencies)
ON user_id, created_at FROM orders;
ANALYZE orders;
```

## Examples

```sql
-- Check estimated vs actual rows in an explain plan
EXPLAIN (ANALYZE, BUFFERS)
SELECT u.name, COUNT(o.id)
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2025-01-01'
GROUP BY u.name;
```

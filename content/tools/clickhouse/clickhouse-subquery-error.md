---
title: "[Solution] ClickHouse Subquery Error — How to Fix"
description: "Fix ClickHouse subquery errors including IN subquery limits, correlated subquery issues, and performance problems with nested queries"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Subquery Error

Subquery errors in ClickHouse occur when using subqueries in WHERE, FROM, or SELECT clauses. ClickHouse has specific limitations on subqueries that differ from standard SQL.

## Why It Happens

- The IN subquery returns too many values exceeding `max_rows_in_set`
- A correlated subquery is not supported in ClickHouse
- The subquery result type does not match the comparison type
- The subquery returns NULL where a non-NULL value is expected
- The subquery is too complex for the query planner

## Common Error Messages

```
Code: 197. DB::Exception: Too many rows in the IN data set
```

```
Code: 53. DB::Exception: Type mismatch in IN expression
```

```
Code: 47. DB::Exception: Column 'xxx' in subquery is ambiguous
```

```
Code: 184. DB::Exception: Aggregate function found in WHERE clause in subquery
```

## How to Fix It

### 1. Fix Too Many Rows in IN Subquery

```sql
-- BAD: IN with millions of rows
SELECT * FROM t1 WHERE id IN (SELECT id FROM t2);

-- GOOD: use JOIN instead
SELECT t1.* FROM t1
INNER JOIN t2 ON t1.id = t2.id;

-- Or increase limit (use with caution)
SET max_rows_in_set = 10000000;
```

### 2. Replace Correlated Subqueries

```sql
-- BAD: correlated subquery (not supported in ClickHouse)
SELECT id, (SELECT count() FROM t2 WHERE t2.id = t1.id) FROM t1;

-- GOOD: use JOIN or window function
SELECT t1.id, count(t2.id)
FROM t1 LEFT JOIN t2 ON t1.id = t2.id
GROUP BY t1.id;
```

### 3. Fix Type Mismatch in Subquery

```sql
-- BAD: comparing String to UInt64
SELECT * FROM t1 WHERE id IN (SELECT CAST(id AS String) FROM t2);

-- GOOD: match types
SELECT * FROM t1 WHERE id IN (SELECT toUInt64(id) FROM t2);
```

### 4. Optimize Subquery Performance

```sql
-- Use temporary table instead of subquery
CREATE TEMPORARY TABLE tmp_ids AS SELECT id FROM t2 WHERE date > '2024-01-01';
SELECT * FROM t1 WHERE id IN (tmp_ids);
DROP TEMPORARY TABLE tmp_ids;

-- Or use pre-filtered subquery
SELECT * FROM t1
INNER JOIN (SELECT id FROM t2 WHERE status = 'active') t2
ON t1.id = t2.id;
```

## Common Scenarios

- **IN subquery too large**: Use JOIN instead for large datasets.
- **Correlated subquery does not work**: Rewrite using JOIN or window function.
- **Slow subquery performance**: Materialize into temporary table first.

## Prevent It

- Use JOIN instead of IN for subqueries returning more than 10,000 rows
- Pre-filter subquery data to reduce result set size
- Use `EXPLAIN` to verify subquery execution plan

## Related Pages

- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
- [ClickHouse Join Error](/tools/clickhouse/clickhouse-join-error)
- [ClickHouse Function Error](/tools/clickhouse/clickhouse-function-error)

---
title: "[Solution] YugabyteDB Subquery Error — How to Fix"
description: "Fix YugabyteDB subquery errors by resolving subquery execution failures, fixing correlated subquery issues, and handling subquery performance problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Subquery Error

YugabyteDB subquery errors occur when subqueries fail to execute due to optimization issues, unsupported patterns, or distributed execution limitations.

## Why It Happens

- Correlated subquery references a column that does not exist
- Subquery returns more than one row in an expression
- IN subquery with large result set causes memory issues
- Subquery cannot be pushed down to tablet servers
- EXISTS subquery with complex conditions fails optimization
- Subquery uses functions not supported in distributed mode

## Common Error Messages

```
ERROR: subquery returns more than one row
```

```
ERROR: correlated subquery not supported
```

```
ERROR: subquery execution failed
```

```
ERROR: could not push down subquery
```

## How to Fix It

### 1. Fix Single-Row Subquery Issues

```sql
-- Wrong: subquery might return multiple rows
SELECT * FROM sensor_data
WHERE device_id = (SELECT id FROM devices WHERE type = 'temp');

-- Correct: use IN or LIMIT
SELECT * FROM sensor_data
WHERE device_id IN (SELECT id FROM devices WHERE type = 'temp');

-- Or use aggregate
SELECT * FROM sensor_data
WHERE device_id = (SELECT MIN(id) FROM devices WHERE type = 'temp');
```

### 2. Convert Correlated Subqueries to JOINs

```sql
-- Slow correlated subquery
SELECT a.*, (SELECT AVG(b.value) FROM sensor_data b WHERE b.device_id = a.id)
FROM devices a;

-- Faster JOIN alternative
SELECT a.*, AVG(b.value) AS avg_value
FROM devices a
JOIN sensor_data b ON b.device_id = a.id
GROUP BY a.id;
```

### 3. Optimize IN Subqueries

```sql
-- Slow IN subquery
SELECT * FROM sensor_data
WHERE device_id IN (
  SELECT id FROM devices WHERE location = 'building1'
);

-- Use JOIN for better performance
SELECT s.*
FROM sensor_data s
JOIN devices d ON s.device_id = d.id
WHERE d.location = 'building1';
```

### 4. Use LATERAL JOIN for Complex Subqueries

```sql
-- LATERAL JOIN for row-by-row subquery
SELECT d.*, latest.value AS latest_value
FROM devices d,
LATERAL (
  SELECT value
  FROM sensor_data s
  WHERE s.device_id = d.id
  ORDER BY time DESC
  LIMIT 1
) latest;
```

## Common Scenarios

- **Subquery returns multiple rows**: Use IN, EXISTS, or aggregate functions.
- **Correlated subquery is slow**: Rewrite as a JOIN.
- **Subquery cannot be pushed down**: Use alternative query patterns.

## Prevent It

- Rewrite subqueries as JOINs when possible
- Test subquery performance with EXPLAIN ANALYZE
- Use LATERAL JOIN for row-by-row operations

## Related Pages

- [YugabyteDB Query Error](/tools/yugabyte/yugabyte-query-error)
- [YugabyteDB Join Error](/tools/yugabyte/yugabyte-join-error)
- [YugabyteDB DML Error](/tools/yugabyte/yugabyte-dml-error)

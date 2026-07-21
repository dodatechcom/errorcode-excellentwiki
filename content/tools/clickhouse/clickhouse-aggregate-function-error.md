---
title: "[Solution] ClickHouse Aggregate Function Error"
description: "Fix ClickHouse aggregate function errors when GROUP BY or aggregation operations fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Aggregate Function Error

Aggregate function errors occur when ClickHouse aggregation operations encounter type mismatches or invalid inputs.

## Common Causes

- Using aggregate function on wrong type
- GROUP BY on Nullable column producing unexpected nulls
- Aggregate function receiving too many arguments
- Nested aggregate functions not supported

## How to Fix

Check aggregate function compatibility:

```sql
SELECT name, is_aggregate FROM system.functions WHERE name = 'sum';
```

Use correct types:

```sql
SELECT user_id, sum(toFloat64(amount)) AS total FROM orders GROUP BY user_id;
```

Avoid nested aggregates:

```sql
-- BAD
SELECT count(max(id)) FROM t;
-- GOOD
SELECT count(*) FROM (SELECT max(id) AS id FROM t);
```

## Examples

```sql
SELECT department, avg(salary) AS avg_sal FROM employees GROUP BY department;
```

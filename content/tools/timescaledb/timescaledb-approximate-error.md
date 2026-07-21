---
title: "TimescaleDB Approximate Error"
description: "Approximate query result error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Approximate query functions returning incorrect results.

## Common Causes
- Approximate function misused
- Data not pre-aggregated
- Incorrect function parameters

## How to Fix
```sql
-- Use exact aggregation when needed
SELECT time_bucket('1 hour', time), AVG(value)
FROM mytable
WHERE time > NOW() - INTERVAL '1 day'
GROUP BY 1;

-- Use approximate only when appropriate
SELECT approx_count(*) FROM mytable;
```

## Examples
```sql
-- Compare exact vs approximate
SELECT EXACT_COUNT(*), approx_count(*) FROM mytable;
-- Use approximate for large datasets
SELECT approx_percentile(value, 0.95) FROM mytable;
```


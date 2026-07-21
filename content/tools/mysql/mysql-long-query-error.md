---
title: "[Solution] MySQL Long Query Error"
description: "Fix MySQL long query error when queries exceed the long_query_time threshold and fill slow query logs"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Long Query Error

Queries that exceed the `long_query_time` threshold are logged to the slow query log. Consistently slow queries degrade performance and consume resources.

## Common Causes

- Missing indexes on frequently queried columns
- Full table scans on large tables due to type conversions
- Complex JOINs with many tables
- Large result sets without pagination
- Queries using SELECT * instead of specific columns
- Subqueries that execute once per row (correlated)

## How to Fix

### Analyze Slow Query Log

```sql
-- Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;  -- log queries > 2 seconds
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';

-- Analyze with mysqldumpslow
-- $ mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
```

### Use EXPLAIN to Analyze Queries

```sql
EXPLAIN SELECT o.*, c.name
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.status = 'active'
  AND o.created_at > '2025-01-01';
```

### Add Missing Indexes

```sql
-- Check for queries without proper indexes
-- Look for "Using filesort" or "Using temporary" in EXPLAIN
CREATE INDEX idx_orders_status_created
  ON orders(status, created_at);
```

### Optimize JOIN Queries

```sql
-- Avoid joining unnecessary tables
-- Bad: joining customers when customer_id is enough
SELECT o.id, c.name, c.email
FROM orders o
JOIN customers c ON c.id = o.customer_id  -- only if you need customer data
WHERE o.status = 'active';

-- Good: only join when needed
SELECT o.id, o.customer_id
FROM orders o
WHERE o.status = 'active';
```

### Set Statement-Specific Timeout

```sql
-- Kill queries running longer than 30 seconds
SET SESSION max_execution_time = 30000;  -- milliseconds
```

## Examples

```
# Slow query log output:
# Time: 2025-01-15T10:30:00
# User@Host: admin[admin] @ localhost []
# Query_time: 45.123  Lock_time: 0.001  Rows_sent: 1000000
SELECT * FROM orders WHERE YEAR(created_at) = 2025;
```

## Related Errors

- [MySQL Explain Error]({{< relref "/tools/mysql/mysql-explain-error" >}}) -- explain issues
- [MySQL Lock Wait Timeout]({{< relref "/tools/mysql/mysql-lock-wait-timeout" >}}) -- lock timeouts
- [MySQL Net Read Timeout]({{< relref "/tools/mysql/mysql-net-read-timeout" >}}) -- network timeouts

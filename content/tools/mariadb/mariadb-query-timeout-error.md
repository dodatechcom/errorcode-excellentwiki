---
title: "[Solution] MariaDB Query Timeout Error"
description: "Fix MariaDB query timeout errors when long-running queries are terminated"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Query Timeout Error

Query timeout errors occur when MariaDB terminates queries exceeding the configured timeout limit.

## Common Causes

- Query scanning too many rows without index
- Complex JOIN on large tables
- Missing WHERE clause on SELECT
- Lock wait timeout during query execution

## Common Error Messages

```
ERROR 1836 (HY000): Locked read/write transaction was aborted due to dead lock
```

## How to Fix It

### 1. Check Timeout Settings

```sql
SHOW VARIABLES LIKE '%timeout%';
```

### 2. Increase Query Timeout

```sql
SET SESSION max_execution_time = 60000;
```

### 3. Optimize Query

```sql
EXPLAIN SELECT * FROM my_table WHERE status = 'active';
```

## Examples

```sql
SELECT query, time FROM information_schema.PROCESSLIST WHERE time > 10;
```

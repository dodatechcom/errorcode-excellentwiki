---
title: "[Solution] Vitess Tablet Pool Connection Error"
description: "Fix Vitess tablet connection pool errors when MySQL connection pool is exhausted"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Pool Connection Error

Connection pool errors occur when the vttablet connection pool has no available connections to serve new queries.

## Common Causes

- All connections held by slow queries
- Connection leak in application code
- MySQL max_connections too low
- Pool size not scaled with traffic

## How to Fix

Check pool status:

```sql
SHOW STATUS LIKE 'Threads_connected';
```

Kill idle connections:

```sql
SELECT CONCAT('KILL ', id, ';') FROM information_schema.processlist WHERE command = 'Sleep' AND time > 300;
```

Increase MySQL max connections:

```sql
SET GLOBAL max_connections = 500;
```

## Examples

```bash
vttablet -mysql_server_pool_static_connections=20 -mysql_server_timeout 30s
```

---
title: "[Solution] PostgreSQL Connection Pool Exhausted"
description: "Fix PostgreSQL connection pool exhaustion errors. Resolve too many clients already errors in high-traffic apps."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Connection Pool Exhausted

FATAL: too many client connections / connection pool exhausted

This error occurs when all available connections in the pool are in use and new connection requests are being rejected.

## Common Causes

- max_connections set too low for the application workload
- Connections not being properly returned to the pool after use
- Long-running queries holding connections idle
- Multiple application instances competing for the same connection pool

## How to Fix

1. Check current connection count:

```sql
SELECT count(*), state FROM pg_stat_activity
GROUP BY state;
```

2. Increase max_connections in postgresql.conf:

```
max_connections = 300
```

3. Implement connection pooling with PgBouncer:

```ini
[mydb]
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 50
```

4. Kill idle connections:

```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle'
  AND query_start < now() - interval '10 minutes';
```

## Examples

```bash
# Monitor connection usage
psql -c "SELECT count(*) as total_connections FROM pg_stat_activity;"

# Check connection limits
psql -c "SHOW max_connections;"
```

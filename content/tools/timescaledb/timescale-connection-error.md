---
title: "[Solution] TimescaleDB Connection Error — How to Fix"
description: "Fix TimescaleDB connection errors by tuning max_connections, resolving connection pool exhaustion, and fixing pgBouncer configuration"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Connection Error

TimescaleDB connection errors occur when clients cannot establish or maintain database connections. These are typical PostgreSQL connection issues in a TimescaleDB context.

## Why It Happens

- max_connections limit is reached
- Connection pool is exhausted
- pgBouncer is misconfigured
- Authentication fails (pg_hba.conf)
- Network timeout before connection completes
- Too many idle connections consume resources

## Common Error Messages

```
FATAL: too many connections for role
```

```
FATAL: connection limit exceeded for user
```

```
ERROR: connection timeout
```

```
FATAL: pg_hba.conf rejects connection
```

## How to Fix It

### 1. Check Connection Limits

```sql
-- Check current connections
SELECT count(*) as total_connections,
  state,
  usename
FROM pg_stat_activity
GROUP BY state, usename;

-- Check max connections
SHOW max_connections;

-- Check per-user limits
SELECT rolname, rolconnlimit
FROM pg_roles
WHERE rolname != 'postgres';
```

### 2. Configure Connection Pooling

```ini
# pgBouncer configuration (pgbouncer.ini)
[databases]
timescaledb = host=127.0.0.1 port=5432 dbname=tsdb

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 50
min_pool_size = 10
reserve_pool_size = 5
```

### 3. Increase Connection Limits

```sql
-- Increase max connections (requires restart)
ALTER SYSTEM SET max_connections = 200;
SELECT pg_reload_conf();

-- Or edit postgresql.conf directly
-- max_connections = 200
```

```bash
# Restart PostgreSQL
sudo systemctl restart postgresql
```

### 4. Fix Authentication

```bash
# Edit pg_hba.conf to allow connections
# Add line for your application subnet
# host  all  all  10.0.0.0/24  md5

# Reload configuration
SELECT pg_reload_conf();
```

## Common Scenarios

- **Too many idle connections**: Use pgBouncer with transaction pooling mode.
- **Connection timeout during peak**: Increase connection pool size in pgBouncer.
- **Application opens too many connections**: Implement connection pooling in the app.

## Prevent It

- Always use connection pooling (pgBouncer) in production
- Monitor connection count with `pg_stat_activity`
- Set per-user connection limits appropriately

## Related Pages

- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB OOM Error](/tools/timescaledb/timescale-oom-error)

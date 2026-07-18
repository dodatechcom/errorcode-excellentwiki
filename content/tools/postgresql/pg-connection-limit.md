---
title: "[Solution] PostgreSQL Too Many Connections Already - Fix Connection Limits"
description: "Fix PostgreSQL too many connections errors by configuring max_connections, using PgBouncer, and auditing connection usage patterns"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Too Many Connections Already

This error means the PostgreSQL server has reached its configured `max_connections` limit and is rejecting new connection attempts. Every connection consumes memory and system resources, so PostgreSQL enforces a hard cap.

## What This Error Means

PostgreSQL returns this error when a new connection is attempted:

```
FATAL: too many connections already
```

PostgreSQL processes are heavyweight compared to other databases -- each connection is a separate OS process, not a thread. This means each connection uses approximately 10MB of memory (for `shared_buffers` and process-local memory) plus whatever `work_mem` is allocated per operation.

The `max_connections` setting applies to the entire cluster. There is no per-database or per-user connection limit by default.

## Why It Happens

- Application opens connections without a connection pool
- Connection pool size is larger than `max_connections` allows
- Idle connections are not being closed by the application or pool
- A traffic spike causes more concurrent connections than usual
- Connection leak in the application (connections opened but never returned to the pool)
- Monitoring or admin tools open additional connections during busy periods
- `superuser_reserved_connections` reduces the effective limit for non-superusers

## How to Fix It

### 1. Check Current Connection Usage

```sql
-- Count connections by state
SELECT state, count(*)
FROM pg_stat_activity
GROUP BY state;

-- Count connections by database and user
SELECT datname, usename, count(*)
FROM pg_stat_activity
GROUP BY datname, usename
ORDER BY count DESC;
```

### 2. Kill Idle Connections

```sql
-- Find idle connections
SELECT pid, usename, datname, state, query_start
FROM pg_stat_activity
WHERE state = 'idle'
ORDER BY query_start;

-- Terminate idle connections older than 10 minutes
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle'
  AND query_start < now() - interval '10 minutes';
```

### 3. Set an Idle Connection Timeout

```sql
-- Disconnect idle sessions after 5 minutes
ALTER SYSTEM SET idle_in_transaction_session_timeout = '5min';
SELECT pg_reload_conf();
```

### 4. Deploy a Connection Pooler

```bash
# Install PgBouncer
sudo apt install pgbouncer

# Configure in /etc/pgbouncer/pgbouncer.ini
[databases]
mydb = host=localhost port=5432 dbname=mydb

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 25
```

### 5. Increase max_connections (With Caution)

```sql
-- In postgresql.conf
max_connections = 200
superuser_reserved_connections = 3

-- This requires a restart
sudo systemctl restart postgresql
```

### 6. Audit Connection Leaks

```sql
-- Monitor connection count over time
SELECT
    now() AS timestamp,
    count(*) AS total_connections,
    count(*) FILTER (WHERE state = 'active') AS active,
    count(*) FILTER (WHERE state = 'idle') AS idle,
    count(*) FILTER (WHERE state = 'idle in transaction') AS idle_in_transaction
FROM pg_stat_activity;
```

## Common Mistakes

- Setting `max_connections` to 1000+ without a connection pool -- this consumes excessive memory
- Not monitoring idle-in-transaction connections, which hold server resources
- Using per-database connection limits when the cluster-wide limit is the bottleneck
- Forgetting that `superuser_reserved_connections` reduces the effective limit for regular users
- Not restarting PostgreSQL after changing `max_connections` -- it requires a full restart

## Related Pages

- [PostgreSQL Connection Refused](/tools/postgresql/pg-connection-refused)
- [PostgreSQL OOM](/tools/postgresql/pg-oom)
- [PostgreSQL Config Error](/tools/postgresql/pg-config-error)
- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)

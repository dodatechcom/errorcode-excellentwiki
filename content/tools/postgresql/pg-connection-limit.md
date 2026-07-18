---
title: "[Solution] PostgreSQL Too Many Connections Error — How to Fix"
description: "Fix PostgreSQL too many connections by configuring max_connections, deploying PgBouncer, killing idle sessions, and monitoring connection usage"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 10
comments: true
---

# PostgreSQL Too Many Connections Error

This error means PostgreSQL has reached its `max_connections` limit and is refusing new connections. Each PostgreSQL connection is a separate OS process, consuming significant memory compared to thread-based databases.

## Why It Happens

- Application does not use a connection pool and opens new connections per request
- Connection pool size exceeds `max_connections` on the database
- Idle connections accumulate because the application does not close them
- Traffic spike increases concurrent connection demand
- Connection leak in application code (connections opened but never returned)
- Monitoring or admin tools open extra connections during busy periods
- `superuser_reserved_connections` reduces the limit for non-superusers
- Microservices each maintain their own connection pool, multiplying usage

## Common Error Messages

```
FATAL: too many connections already
```

```
FATAL: sorry, too many clients already
```

```
FATAL: number of connections (101) exceeds the limit (100)
```

## How to Fix It

### 1. Analyze Current Connection Usage

```sql
-- Count connections by state
SELECT state, count(*)
FROM pg_stat_activity
GROUP BY state;

-- Count by database and user
SELECT datname, usename, state, count(*)
FROM pg_stat_activity
GROUP BY datname, usename, state
ORDER BY count DESC;

-- Find long-running idle connections
SELECT pid, usename, datname, state, query_start,
       now() - query_start AS duration
FROM pg_stat_activity
WHERE state = 'idle'
ORDER BY query_start;
```

### 2. Terminate Idle Connections

```sql
-- Kill idle connections older than 10 minutes
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle'
  AND query_start < now() - interval '10 minutes';

-- Kill idle-in-transaction connections
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle in transaction'
  AND state_change < now() - interval '5 minutes';
```

### 3. Set Connection Timeouts

```sql
-- Disconnect idle sessions after 5 minutes
ALTER SYSTEM SET idle_in_transaction_session_timeout = '5min';

-- Set statement timeout to prevent long queries
ALTER SYSTEM SET statement_timeout = '60s';

SELECT pg_reload_conf();
```

### 4. Deploy PgBouncer as Connection Pooler

```bash
# Install PgBouncer
sudo apt install pgbouncer

# Configure /etc/pgbouncer/pgbouncer.ini
```

```ini
[databases]
mydb = host=localhost port=5432 dbname=mydb

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 25
min_pool_size = 5
reserve_pool_size = 5
```

### 5. Increase max_connections (With Caution)

```sql
-- In postgresql.conf
-- Each connection uses ~10MB, so 200 connections = ~2GB
max_connections = 200
superuser_reserved_connections = 3

-- Requires a restart
sudo systemctl restart postgresql
```

### 6. Application-Level Pool Configuration

```python
# Python with psycopg2 and a pool
from psycopg2 import pool

connection_pool = pool.ThreadedConnectionPool(
    minconn=5,
    maxconn=20,
    host='localhost',
    database='mydb',
    user='myuser',
    password='password'
)
```

## Common Scenarios

- **Microservices proliferation**: 10 microservices each with a pool of 20 connections = 200 connections. Deploy PgBouncer in front of PostgreSQL.
- **Lambda/serverless functions**: Each function invocation opens a new connection. Use RDS Proxy or a PgBouncer sidecar.
- **Debug connection left open**: A developer connects with pgAdmin and leaves it open. Set `idle_in_transaction_session_timeout` to catch these.

## Prevent It

- Always use a connection pooler (PgBouncer or application-level pool) in front of PostgreSQL
- Keep total pool size well below `max_connections` to leave room for admin connections
- Monitor `pg_stat_activity` and alert when active connections exceed 80% of the limit

## Related Pages

- [PostgreSQL Deadlock Detected](/tools/postgresql/pg-deadlock-detected)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)
- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)

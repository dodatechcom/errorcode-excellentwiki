---
title: "[Solution] MySQL Too Many Connections - Fix Connection Limit Errors"
description: "Fix MySQL too many connections errors by configuring max_connections, using connection pooling, and killing idle processes"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Too Many Connections

This error means MySQL has reached its `max_connections` limit and is rejecting new connection attempts. Unlike PostgreSQL, MySQL uses a thread-per-connection model, which is more lightweight but still has limits.

## What This Error Means

MySQL returns this error when the connection limit is reached:

```
ERROR 1040 (08004): Too many connections
```

The `max_connections` setting controls the maximum number of simultaneous client connections. The default in MySQL 5.7 is 151, and in MySQL 8.0 it is 151 as well. The actual usable limit is `max_connections - 1` because one connection is reserved for the `SUPER` user.

## Why It Happens

- Application does not use a connection pool and opens new connections for each request
- Connection pool size is larger than `max_connections`
- Idle connections are not being closed by the application or pool
- A traffic spike causes more concurrent connections than usual
- Connection leak in the application (connections opened but never closed)
- Long-running queries keep connections occupied longer than expected
- Monitoring or admin tools open additional connections

## How to Fix It

### 1. Check Current Connection Usage

```sql
-- Total connections
SHOW STATUS LIKE 'Threads_connected';

-- Maximum connections reached since startup
SHOW STATUS LIKE 'Max_used_connections';

-- Current max_connections setting
SHOW VARIABLES LIKE 'max_connections';
```

### 2. Kill Idle Connections

```sql
-- Find idle connections
SHOW PROCESSLIST;

-- Kill connections idle for more than 60 seconds
SELECT CONCAT('KILL ', id, ';')
FROM information_schema.PROCESSLIST
WHERE command = 'Sleep' AND time > 60;

-- Kill a specific connection
KILL <process_id>;
```

### 3. Increase max_connections

```sql
-- Increase the limit (requires restart)
SET GLOBAL max_connections = 500;

-- In my.cnf (persists across restarts)
[mysqld]
max_connections = 500
```

### 4. Set an Idle Timeout

```sql
-- Disconnect idle connections after 300 seconds
SET GLOBAL wait_timeout = 300;
SET GLOBAL interactive_timeout = 300;
```

### 5. Deploy a Connection Pooler

```bash
# Use ProxySQL or MySQL Router as a connection pooler
# In proxySQL config
mysql_variables =
{
    max_connections = 1000
}

mysql_servers =
(
    { address = "127.0.0.1", port = 3306, max_connections = 200 }
)
```

### 6. Monitor Connection Usage

```sql
-- Connections by user
SELECT user, count(*) AS connections
FROM information_schema.PROCESSLIST
GROUP BY user ORDER BY connections DESC;

-- Connections by state
SELECT command, count(*) AS cnt
FROM information_schema.PROCESSLIST
GROUP BY command;
```

## Common Mistakes

- Setting `max_connections` very high without considering memory usage -- each thread uses memory for sort buffers, join buffers, and other per-session allocations
- Not monitoring `Max_used_connections` -- if it approaches `max_connections`, you need to increase the limit or reduce usage
- Using `SHOW PROCESSLIST` output to manually kill connections instead of implementing proper connection pooling
- Forgetting that `wait_timeout` and `interactive_timeout` are separate settings
- Not accounting for replication connections when setting `max_connections`

## Related Pages

- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
- [MySQL User Limit](/tools/mysql/mysql-user-limit)
- [MySQL Lock Timeout](/tools/mysql/mysql-lock-timeout)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)

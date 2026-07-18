---
title: "[Solution] MySQL User Has Too Many Connections - Fix Per-User Limits"
description: "Fix MySQL user has too many connections errors by setting per-user limits, auditing connection usage, and configuring max_user_connections"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL User Has Too Many Connections

This error occurs when a specific user reaches their individual connection limit. MySQL supports both a global `max_connections` limit and per-user limits via `max_user_connections`.

## What This Error Means

MySQL returns this error when a user exceeds their per-user connection limit:

```
ERROR 1226 (42000): User 'root'@'localhost' has exceeded the 'max_user_connections' resource (current value: 10)
```

This is different from the global "Too many connections" error. The per-user limit is enforced before the global limit. MySQL checks both limits for every new connection.

## Why It Happens

- The application uses a specific user for all connections without a connection pool
- `max_user_connections` is set too low for the user's workload
- Connection leak: the application opens connections but never closes them
- A single application instance opens more connections than expected
- Monitoring or admin tools connect using the same user as the application
- The per-user limit was set without considering peak traffic

## How to Fix It

### 1. Check Current Per-User Limits

```sql
-- Show max_user_connections for all users
SELECT user, max_user_connections, max_connections
FROM mysql.user;

-- Check the global setting
SHOW VARIABLES LIKE 'max_user_connections';
```

### 2. Increase the Per-User Limit

```sql
-- Increase for a specific user
ALTER USER 'myuser'@'localhost' WITH MAX_USER_CONNECTIONS 50;

-- Remove the per-user limit (uses global limit instead)
ALTER USER 'myuser'@'localhost' WITH MAX_USER_CONNECTIONS 0;
```

### 3. Check Active Connections Per User

```sql
-- Current connections per user
SELECT user, count(*) AS connections
FROM information_schema.PROCESSLIST
GROUP BY user ORDER BY connections DESC;
```

### 4. Kill Idle Connections for the User

```sql
-- Find idle connections for a specific user
SELECT id, user, host, db, command, time
FROM information_schema.PROCESSLIST
WHERE user = 'myuser' AND command = 'Sleep';

-- Kill a specific connection
KILL <process_id>;
```

### 5. Set the Global Limit Appropriately

```sql
-- The global limit applies to all users combined
SET GLOBAL max_connections = 500;

-- In my.cnf
[mysqld]
max_connections = 500
max_user_connections = 0
```

### 6. Implement Connection Pooling

```bash
# Use a connection pooler to limit actual MySQL connections
# while allowing many application connections

# Example with ProxySQL
mysql_servers = (
    { address = "127.0.0.1", port = 3306, max_connections = 50 }
)
```

## Common Mistakes

- Setting `max_user_connections` to a very low value like 10 without considering peak usage
- Not monitoring per-user connection counts -- the error occurs only when the limit is hit
- Using the same MySQL user for the application and admin tools
- Forgetting that `max_user_connections = 0` means unlimited (uses only the global limit)
- Not distinguishing between the "Too many connections" (global) and "has exceeded max_user_connections" (per-user) errors

## Related Pages

- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)
- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)

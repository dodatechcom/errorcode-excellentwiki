---
title: "[Solution] MySQL Too Many Connections Error — How to Fix"
description: "Fix MySQL too many connections errors by tuning max_connections, using connection pools, killing idle threads, and monitoring connection usage"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MySQL Too Many Connections Error

This error means MySQL has reached its `max_connections` limit and is rejecting new connection attempts. Every connection to MySQL consumes memory and a thread, so there is a hard upper limit.

## Why It Happens

- Application opens new connections for every query instead of reusing a pool
- Connection pool size exceeds `max_connections`
- Idle connections are not being released by the application
- Traffic spike causes more concurrent users than usual
- Connection leak where connections are opened but never closed
- Monitoring tools or batch jobs open extra connections during peak hours
- Short-lived connections add overhead faster than they are cleaned up

## Common Error Messages

```
ERROR 1040 (08004): Too many connections
```

```
ERROR 1129 (HY000): Host '192.168.1.50' is blocked because too many connection errors
```

```
Can't connect to MySQL server on 'db.example.com' (111)
```

## How to Fix It

### 1. Check Current Connection Usage

```sql
-- Total connections
SHOW STATUS LIKE 'Threads_connected';

-- Max allowed
SHOW VARIABLES LIKE 'max_connections';

-- Connections by state
SELECT
    processlist_id,
    user,
    host,
    db,
    command,
    time,
    state
FROM information_schema.processlist
ORDER BY time DESC;
```

### 2. Kill Idle Connections

```sql
-- Find idle connections
SELECT id, user, host, db, command, time, state
FROM information_schema.processlist
WHERE command = 'Sleep' AND time > 300;

-- Kill specific connections
KILL <process_id>;
```

```bash
# Kill all idle connections from a specific host
mysql -e "SELECT CONCAT('KILL ', id, ';')
FROM information_schema.processlist
WHERE command = 'Sleep' AND host LIKE '192.168.1.%'" | mysql -u root -p
```

### 3. Increase max_connections

```sql
-- Check current value
SHOW VARIABLES LIKE 'max_connections';

-- Increase (requires RELOAD privilege, no restart needed)
SET GLOBAL max_connections = 500;
```

```ini
# In my.cnf — persistent setting
[mysqld]
max_connections = 500
```

### 4. Configure Connection Timeout

```sql
-- Close idle connections after 300 seconds
SET GLOBAL wait_timeout = 300;
SET GLOBAL interactive_timeout = 300;

-- Close connections in active transaction after 60 seconds
SET GLOBAL max_execution_time = 60000;
```

### 5. Use a Connection Pool in the Application

```python
# Python with SQLAlchemy
from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://user:pass@host/db',
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800
)
```

```javascript
// Node.js with mysql2
const pool = mysql.createPool({
  host: 'localhost',
  user: 'myuser',
  password: 'password',
  database: 'mydb',
  connectionLimit: 20,
  queueLimit: 0,
  connectTimeout: 10000
});
```

### 6. Unblock Hosts After Too Many Errors

```sql
-- Check blocked hosts
SELECT * FROM performance_schema.host_cache
WHERE COUNT_HANDSHAKE_ERROR > 0;

-- Flush the host cache
FLUSH HOSTS;
```

## Common Scenarios

- **Microservices without pooling**: Each service instance opens its own connections. Deploy PgBouncer or use a connection pool library.
- **Short-lived Lambda functions**: Each invocation opens and closes a connection. Use RDS Proxy or a connection pooler.
- **Debug session left open**: A developer connects with a GUI tool and leaves it open all weekend. Set `wait_timeout` aggressively.

## Prevent It

- Always use a connection pool in the application layer with a size smaller than `max_connections`
- Monitor `Threads_connected` and `Max_used_connections` as key metrics
- Set `wait_timeout` to close idle connections automatically within minutes

## Related Pages

- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
- [MySQL Gone Away](/tools/mysql/mysql-gone-away)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)

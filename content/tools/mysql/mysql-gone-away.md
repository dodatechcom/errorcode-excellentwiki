---
title: "[Solution] MySQL Server Has Gone Away Error — How to Fix"
description: "Fix MySQL server has gone away errors by adjusting packet sizes, checking server stability, reconnecting gracefully, and tuning timeout settings"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MySQL Server Has Gone Away Error

This error means the connection to the MySQL server was lost unexpectedly during a query or idle period. The server may have terminated the connection, crashed, or been unreachable due to a network issue.

## Why It Happens

- The client sent a query larger than `max_allowed_packet` bytes
- The server crashed or was restarted while the client was connected
- The connection was idle longer than `wait_timeout` or `interactive_timeout`
- The server was killed or OOM-killed by the operating system
- Network interruption between the client and server
- The client was reading data and the server timed out
- A DNS resolution failure on the server side
- The `net_read_timeout` or `net_write_timeout` was exceeded

## Common Error Messages

```
MySQL server has gone away
```

```
Lost connection to MySQL server during query
```

```
ERROR 2006 (HY000): MySQL server has gone away
```

## How to Fix It

### 1. Increase max_allowed_packet

```sql
-- Check current value
SHOW VARIABLES LIKE 'max_allowed_packet';

-- Increase to 64MB (session level for testing)
SET GLOBAL max_allowed_packet = 67108864;
```

```ini
# In my.cnf for persistence
[mysqld]
max_allowed_packet = 64M
```

### 2. Increase Timeout Values

```sql
-- Allow longer idle connections
SET GLOBAL wait_timeout = 28800;
SET GLOBAL interactive_timeout = 28800;

-- Allow more time for network reads
SET GLOBAL net_read_timeout = 120;
SET GLOBAL net_write_timeout = 120;
```

### 3. Check Server Stability

```bash
# Check if MySQL was OOM-killed
dmesg | grep -i mysql | grep -i oom

# Check MySQL error log
tail -100 /var/log/mysql/error.log

# Check server uptime
mysqladmin -u root -p status
```

### 4. Implement Reconnection in Application Code

```python
import mysql.connector
from mysql.connector import errorcode

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='myuser',
            password='password',
            database='mydb',
            autocommit=True,
            connection_timeout=10
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.CR_SERVER_GONE_ERROR:
            print("Server gone away, retrying...")
            return get_connection()
        raise

def execute_with_retry(query, params=None, retries=3):
    for attempt in range(retries):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except mysql.connector.Error as err:
            if err.errno == errorcode.CR_SERVER_GONE_ERROR and attempt < retries - 1:
                continue
            raise
```

### 5. Keep Connections Alive with Ping

```python
import mysql.connector
import time

def keep_alive(conn, interval=300):
    """Send a ping to keep the connection alive."""
    try:
        conn.ping(reconnect=True, attempts=3, delay=1)
    except mysql.connector.Error:
        conn = get_connection()
    return conn

# Periodically ping during long waits
last_ping = time.time()
```

## Common Scenarios

- **Large bulk inserts**: Inserting millions of rows in one statement exceeds `max_allowed_packet`. Batch the inserts into smaller chunks.
- **Overnight batch job**: A long-running job opens a connection at midnight but the server's `wait_timeout` kills it by 3 AM. Use ping to keep it alive.
- **Server restart during deployment**: The MySQL server is restarted during a deployment window but application servers still hold old connections. Add retry logic with exponential backoff.

## Prevent It

- Set `max_allowed_packet` to at least 64MB for most workloads
- Use connection pools with health checks and automatic reconnection
- Configure server OOM protection with `oom_score_adj` to reduce the chance of the MySQL process being killed

## Related Pages

- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)
- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
- [PostgreSQL Connection Reset](/tools/postgresql/pg-connection-reset)

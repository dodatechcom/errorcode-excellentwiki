---
title: "[Solution] TimescaleDB Connection Pool Error — How to Fix"
description: "Fix TimescaleDB connection pool errors by resolving PgBouncer issues, fixing connection exhaustion, and handling idle connection cleanup"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Connection Pool Error

TimescaleDB connection pool errors occur when PgBouncer or similar connection poolers fail to manage connections properly, causing exhaustion, timeouts, or stale connections.

## Why It Happens

- Pool size is too small for the workload
- Clients hold connections longer than expected
- Server-side connection limit is reached
- Idle connections are not cleaned up
- Transaction pooling mode causes prepared statement issues
- Health check interval is too long

## Common Error Messages

```
ERROR: no connections available
```

```
ERROR: server closed the connection unexpectedly
```

```
FATAL: too many connections
```

```
WARNING: connection timed out in pool
```

## How to Fix It

### 1. Check Pool Configuration

```ini
; pgbouncer.ini
[databases]
mydb = host=localhost port=5432 dbname=mydb

[pgbouncer]
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 50
min_pool_size = 10
reserve_pool_size = 5
server_idle_timeout = 600
```

### 2. Increase Pool Size

```ini
; Increase default pool size
[pgbouncer]
default_pool_size = 100
max_user_connections = 50
max_db_connections = 50
```

### 3. Fix Transaction Mode Issues

```bash
# PgBouncer in transaction mode does not support prepared statements
# Switch to session mode for applications that use them
[pgbouncer]
pool_mode = session

# Or use protocol-level prepared statement support
```

### 4. Monitor Pool Status

```bash
# Check PgBouncer stats
psql -h localhost -p 6432 -U pgbouncer pgbouncer -c "SHOW POOLS;"

# Check active connections
psql -h localhost -p 6432 -U pgbouncer pgbouncer -c "SHOW CLIENTS;"

# Check server connections
psql -h localhost -p 6432 -U pgbouncer pgbouncer -c "SHOW SERVERS;"
```

## Common Scenarios

- **Pool exhaustion under load**: Increase default_pool_size and max_client_conn.
- **Prepared statement errors**: Switch to session mode or use protocol-level support.
- **Idle connections accumulate**: Reduce server_idle_timeout to reclaim connections.

## Prevent It

- Monitor pool statistics regularly
- Set appropriate pool sizes based on workload
- Use health checks to detect stale connections

## Related Pages

- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
- [TimescaleDB Overload Error](/tools/timescaledb/timescale-overload-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)

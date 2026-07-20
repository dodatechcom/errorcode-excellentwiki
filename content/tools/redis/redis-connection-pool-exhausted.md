---
title: "[Solution] Redis Connection Pool Exhausted"
description: "How to fix Redis connection pool exhausted error when all connections in the pool are in use"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Application not returning connections to the pool
- Pool size too small for workload
- Slow queries holding connections longer than expected
- Connection leak in application code

## Fix

Increase pool size:

```python
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=50)
r = redis.Redis(connection_pool=pool)
```

Set connection timeout:

```python
pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=20, timeout=5)
```

Check active connections:

```bash
redis-cli CLIENT LIST
```

Use connection pool with context manager:

```python
with redis.Redis(connection_pool=pool) as r:
    r.get("key")
```

## Examples

```bash
# Monitor connection count
watch -n 1 'redis-cli INFO clients | grep connected_clients'

# Kill long-running client connections
redis-cli CLIENT KILL IDLE 300
```

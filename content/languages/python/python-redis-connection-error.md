---
title: "[Solution] Python Redis Connection Error — How to Fix"
description: "Fix Python Redis connection errors. Resolve connection, authentication, and timeout issues with Redis."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Redis Connection Error

A `redis.ConnectionError` occurs when The Redis client cannot connect to the server due to network issues, authentication failures, or pool exhaustion..

## Why It Happens

This happens when the Redis server is not running, the connection pool is exhausted, or authentication credentials are incorrect. Python enforces strict type and state checking.

## Common Error Messages

- `Error 111 connecting to localhost:6379`
- `invalid username-password pair`
- `Socket timed out`

## How to Fix It

### Fix 1: Configure connection pooling

```python
import redis

pool = redis.ConnectionPool(
    host='localhost', port=6379, db=0,
    max_connections=20, socket_timeout=5
)
r = redis.Redis(connection_pool=pool)
```

### Fix 2: Handle authentication

```python
import redis

r = redis.Redis(host='localhost', port=6379, password='secret')
r.ping()
```

### Fix 3: Use retry logic

```python
import redis
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3))
def get_redis():
    return redis.Redis(host='localhost', port=6379)
```

### Fix 4: Monitor connection health

```python
import redis

r = redis.Redis(host='localhost', port=6379)
try:
    info = r.info('memory')
    print(f'Used memory: {info["used_memory_human"]}')
except redis.ConnectionError:
    print('Redis is down')
```

## Common Scenarios

- **Connection pool exhaustion** — Too many concurrent connections exceed pool size.
- **Network partitions** — Firewall blocks Redis port 6379.
- **Memory limits** — Redis maxmemory policy evicts keys.

## Prevent It

- Always set socket_timeout to prevent hanging connections
- Use connection pooling for high-throughput apps
- Monitor Redis with INFO command regularly

## Related Errors

- - [ConnectionError](/languages/python/connectionerror/) — network connection failure
- - [TimeoutError](/languages/python/timeouterror/) — operation timed out
- - [AuthenticationError](/languages/python/authenticationerror/) — auth failed

---
title: "[Solution] Redis ConnectionError: Connection Refused Fix"
description: "Fix redis.ConnectionError connection refused. Verify Redis server is running, check host/port, and configure connection pooling."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["redis", "connection", "cache", "connectionerror", "server"]
weight: 5
---

# Redis ConnectionError: Connection Refused Fix

A `redis.ConnectionError: Error connecting to localhost:6379` is raised when the Python Redis client cannot establish a TCP connection to the Redis server.

## What This Error Means

Common messages:

- `redis.exceptions.ConnectionError: Error 111 connecting to localhost:6379. Connection refused.`
- `redis.exceptions.ConnectionError: Connection closed by server.`
- `redis.exceptions.TimeoutError: Timeout connecting to server`

The Redis client attempted to open a socket to the Redis server but the server is not running, not listening on the expected port, or a firewall is blocking the connection.

## Common Causes

```python
import redis

# Cause 1: Redis server not running
r = redis.Redis(host="localhost", port=6379)
r.ping()  # ConnectionError: Error 111 connecting to localhost:6379

# Cause 2: Wrong host or port
r = redis.Redis(host="localhost", port=6380)  # Wrong port

# Cause 3: Redis bound to different interface
r = redis.Redis(host="localhost", port=6379)  # Redis bound to 127.0.0.1 only

# Cause 4: Connection pool exhausted
pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=5)
r = redis.Redis(connection_pool=pool)
# 6th concurrent connection fails
```

## How to Fix

### Fix 1: Start Redis server

```bash
# Linux
sudo systemctl start redis

# macOS
brew services start redis

# Docker
docker run -d -p 6379:6379 redis:latest
```

### Fix 2: Verify connection parameters

```python
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    password=None,
    socket_timeout=5,
    decode_responses=True,
)
print(r.ping())  # True
```

### Fix 3: Configure connection pool properly

```python
import redis

pool = redis.ConnectionPool(
    host="localhost",
    port=6379,
    max_connections=20,
    socket_timeout=5,
    socket_connect_timeout=5,
    retry_on_timeout=True,
)
r = redis.Redis(connection_pool=pool)
```

### Fix 4: Handle reconnection with retry

```python
import redis
from redis.retry import Retry
from redis.backoff import ExponentialBackoff

retry = Retry(
    backoff=ExponentialBackoff(),
    retries=3,
)

r = redis.Redis(
    host="localhost",
    port=6379,
    retry=retry,
    retry_on_error=[redis.ConnectionError, redis.TimeoutError],
)
```

### Fix 5: Use Sentinel for high availability

```python
from redis.sentinel import Sentinel

sentinel = Sentinel(
    [("sentinel-1", 26379), ("sentinel-2", 26379)],
    socket_timeout=5,
)
master = sentinel.master_for("mymaster", socket_timeout=5)
master.ping()
```

## Related Errors

- {{< relref "connectionrefusederror" >}} — Python connection refused error.
- {{< relref "importerror-redis-py" >}} — Redis Python client import issue.

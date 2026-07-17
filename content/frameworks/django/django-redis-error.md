---
title: "[Solution] Django Redis Connection Error"
description: "Fix Django Redis connection errors. Resolve Redis cache and connection issues."
frameworks: ["django"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Django Redis connection error occurs when the application cannot connect to the Redis server used for caching, sessions, or Celery broker.

## Common Causes

- Redis server is not running
- Wrong Redis URL or port configuration
- Redis password is incorrect
- Maximum connections reached
- Redis server out of memory

## How to Fix

### Check Redis Settings

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Test Redis Connection

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.ping()
```

### Start Redis

```bash
sudo systemctl start redis
redis-cli ping
# PONG
```

### Check Redis Status

```bash
redis-cli info server
redis-cli info memory
```

### Use Connection Pool

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
            },
        }
    }
}
```

## Examples

```python
# Example 1: Redis not running
# ConnectionRefusedError: [Errno 111] Connection refused
# Fix: sudo systemctl start redis

# Example 2: Wrong password
# AuthenticationError: Client sent AUTH, but no password is set
# Fix: set REDIS_URL with correct password
```

## Related Errors

- [Django Database Error]({{< relref "/frameworks/django/django-db-connection" >}}) — DatabaseError connection failed
- [Django Celery Error]({{< relref "/frameworks/django/django-celery-error" >}}) — Celery task error

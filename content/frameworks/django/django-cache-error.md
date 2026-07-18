---
title: "[Solution] Django Cache Backend Connection Failed Error — How to Fix"
description: "Fix Django cache backend connection errors. Resolve Redis, Memcached, and database cache connection issues."
frameworks: ["django"]
error-types: ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A Django cache backend connection error occurs when Django cannot connect to the configured cache server (Redis, Memcached, database, or file-based cache). This can cause application slowdowns or failures when cache operations are attempted.

## Why It Happens

Django's cache framework supports multiple backends, each with its own connection requirements. The error occurs when the cache server is not running, the connection URL is incorrect, authentication credentials are wrong, network connectivity is lost, or the cache server has hit memory limits.

## Common Error Messages

```
ConnectionError: Error connecting to redis://localhost:6379/0
```

```
MemcacheStrategyError: Memcached is down or not responding
```

```
django.core.cache.backends.base.BaseCacheTimeoutError: Cache key timeout
```

```
redis.exceptions.ConnectionError: Error 111 connecting to localhost:6379. Connection refused.
```

## How to Fix It

### 1. Configure Cache Backend Correctly

Set up the cache backend in `settings.py` with proper connection parameters:

```python
# settings.py — Redis cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            ' db': 1,
        },
        'KEY_PREFIX': 'myproject',
        'TIMEOUT': 300,  # 5 minutes default
    }
}

# settings.py — Memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
        'OPTIONS': {
            'timeout': 300,
        }
    }
}

# settings.py — Database cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
```

### 2. Test Cache Connection

Verify the cache server is running and accessible:

```python
# In Django shell
from django.core.cache import cache

# Test set and get
cache.set('test_key', 'test_value', timeout=30)
value = cache.get('test_key')
print(f"Cache value: {value}")

# Test with specific cache
from django.core.cache import caches
redis_cache = caches['default']
redis_cache.set('key', 'value')
```

```bash
# Test Redis connection directly
redis-cli ping
# Should return: PONG

# Test Memcached connection
echo "stats" | nc localhost 11211
```

### 3. Add Cache Fallback Handling

Implement graceful degradation when cache is unavailable:

```python
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

def get_cached_data(key, compute_fn, timeout=300):
    try:
        value = cache.get(key)
        if value is not None:
            return value
    except Exception as e:
        logger.warning(f"Cache read failed for {key}: {e}")

    value = compute_fn()
    try:
        cache.set(key, value, timeout=timeout)
    except Exception as e:
        logger.warning(f"Cache write failed for {key}: {e}")

    return value

# Usage
articles = get_cached_data(
    'published_articles',
    lambda: list(Article.objects.filter(status='published')),
)
```

### 4. Use Connection Pooling for Production

Configure connection pooling for Redis in production:

```python
# settings.py
import redis

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_CLASS': 'redis.ConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'retry_on_timeout': True,
            },
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
        }
    }
}
```

## Common Scenarios

**Scenario 1: Cache works locally but fails in production.**
This is typically a network or configuration issue. Production environments may use different Redis/Memcached hosts, require authentication, or be behind firewalls. Verify the production cache URL and credentials.

**Scenario 2: Cache becomes stale after deployment.**
When deploying code changes, cached data may reference old code versions. Use cache versioning or clear the cache during deployment:

```python
# Clear entire cache
cache.clear()

# Or use versioned keys
cache.set('key', 'value', version=2)
```

**Scenario 3: High memory usage on cache server.**
Set appropriate TTLs and use `MAX_ENTRIES` to limit cache size:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'MAX_ENTRIES': 10000,
        },
        'TIMEOUT': 600,
    }
}
```

## Prevent It

1. **Always implement cache fallback logic.** The cache layer should be optional — if it fails, the application should still function correctly by computing values directly.

2. **Monitor cache hit rates.** Use `cache.get_many()` and Django debug toolbar to track cache efficiency. Low hit rates indicate misconfigured cache keys or timeouts.

3. **Set up cache server monitoring.** Use tools like Redis Monitor or `django-debug-toolbar` to track cache operations and identify bottlenecks.

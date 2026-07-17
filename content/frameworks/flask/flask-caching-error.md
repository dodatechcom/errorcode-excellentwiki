---
title: "Flask-Caching Error"
description: "Flask-Caching raises errors when cache operations fail due to backend issues, serialization problems, or configuration errors"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["caching", "cache", "redis", "memcached", "flask"]
weight: 5
---

## What This Error Means

Flask-Caching errors occur when the cache backend is unavailable, serialization of cached objects fails, or cache configuration is incorrect. These errors can affect application performance and cause unexpected behavior in cached views or functions.

## Common Causes

- Cache backend (Redis, Memcached) not running
- Cache key conflicts or invalidation issues
- Object not serializable for caching
- TTL configuration too aggressive
- Backend connection timeout

## How to Fix

Configure Flask-Caching properly:

```python
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)

# Redis backend
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300

cache = Cache(app)
```

Cache view functions:

```python
@app.route('/expensive-data')
@cache.cached(timeout=60)
def expensive_data():
    result = perform_complex_calculation()
    return jsonify(result)
```

Cache with dynamic keys:

```python
@app.route('/user/<int:user_id>')
@cache.cached(timeout=120, key_prefix=f'user_{user_id}')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())
```

Handle cache misses gracefully:

```python
def get_cached_data(key):
    data = cache.get(key)
    if data is None:
        data = expensive_computation()
        cache.set(key, data, timeout=300)
    return data
```

Use SimpleCache for development:

```python
app.config['CACHE_TYPE'] = 'SimpleCache'
```

## Examples

```python
@cache.cached(timeout=60)
def get_posts():
    return Post.query.all()
```

```text
ConnectionError: Error 111 connecting to localhost:6379. Connection refused.
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
- [SQLAlchemy error]({{< relref "/frameworks/flask/sqlalchemy-error" >}})

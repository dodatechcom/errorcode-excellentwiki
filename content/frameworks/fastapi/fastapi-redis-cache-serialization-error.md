---
title: "[Solution] FastAPI Redis Cache Serialization Error"
description: "Fix FastAPI Redis cache serialization errors when cached data cannot be deserialized back to Python objects."
frameworks: ["fastapi"]
error-types: ["cache-error"]
severities: ["error"]
---

When caching responses in Redis with FastAPI, serialization errors occur if the cached data format does not match what the deserializer expects.

## Common Causes

- Using `json.dumps` for serialization but `pickle.loads` for deserialization
- Complex Python objects (datetime, UUID) are not JSON-serializable
- Cached data corrupted by partial writes or network issues
- Redis connection pool returns connections in inconsistent state
- Cache key contains characters that Redis does not handle well

## How to Fix

### Use Consistent Serialization

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

async def cache_set(redis, key: str, value: dict, ttl: int = 300):
    data = json.dumps(value, cls=DateTimeEncoder)
    await redis.setex(key, ttl, data)

async def cache_get(redis, key: str):
    data = await redis.get(key)
    if data:
        return json.loads(data)
    return None
```

### Use a Cache Library

```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

@app.get("/data")
@cache(expire=60)
async def get_data():
    return {"data": "expensive computation"}
```

### Handle Cache Misses Gracefully

```python
async def get_cached_or_compute(redis, key: str):
    try:
        cached = await redis.get(key)
        if cached:
            return json.loads(cached)
    except (json.JSONDecodeError, redis.RedisError):
        pass
    result = await compute_data()
    await redis.setex(key, 300, json.dumps(result))
    return result
```

## Examples

```python
import json
import redis

r = redis.Redis()

# Bug -- mixing json and pickle
r.set("cache:key", json.dumps({"data": value}))
data = pickle.loads(r.get("cache:key"))  # Fails

# Fix -- use consistent format
r.set("cache:key", json.dumps({"data": value}))
data = json.loads(r.get("cache:key"))  # Works
```

Always use the same serialization format for both storing and retrieving cached data.

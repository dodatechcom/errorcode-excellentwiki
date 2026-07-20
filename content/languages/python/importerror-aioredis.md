---
title: "[Solution] Python ImportError: No module named 'aioredis' — Fix"
description: "Fix Python ImportError: No module named 'aioredis'. Install aioredis with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 312
---

# Python ImportError: No module named 'aioredis'

The `ModuleNotFoundError: No module named 'aioredis'` error occurs when Python cannot locate the aioredis package, which provides asynchronous Redis client support. Note that aioredis is deprecated — redis-py 4.2+ includes async support natively.

## Common Causes

```python
# Cause 1: aioredis not installed
import aioredis  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version or virtual environment
from aioredis import Redis  # ModuleNotFoundError

# Cause 3: Using aioredis v1 vs v2 API differences
# aioredis 1.x: aioredis.create_redis()
# aioredis 2.x: aioredis.from_url()
```

```python
# Cause 4: Deprecated package — recommend redis-py async instead
# aioredis merged into redis-py 4.2+

# Cause 5: Version conflict with redis package
# having both aioredis and redis can cause conflicts
```

## How to Fix

### Fix 1: Install aioredis with pip (legacy)

```bash
# Legacy approach (deprecated)
pip install aioredis

# For aioredis 2.x
pip install aioredis>=2.0
```

### Fix 2: Use redis-py async instead (recommended)

```bash
# aioredis is now built into redis-py
pip install redis>=4.2
```

```python
# Using redis-py async (replacement for aioredis)
import asyncio
from redis.asyncio import Redis

async def main():
    r = Redis(host="localhost", port=6379)
    await r.set("key", "value")
    value = await r.get("key")
    print(value)
    await r.aclose()

asyncio.run(main())
```

### Fix 3: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install redis>=4.2
python -c "from redis.asyncio import Redis; print('OK')"
```

## Examples

```python
# Legacy aioredis usage (deprecated)
import aioredis

async def legacy_example():
    redis = await aioredis.from_url("redis://localhost")
    await redis.set("my_key", "my_value")
    value = await redis.get("my_key")
    await redis.close()

# Modern redis-py async (recommended)
import redis.asyncio as aioredis

async def modern_example():
    redis = aioredis.from_url("redis://localhost")
    await redis.set("my_key", "my_value")
    value = await redis.get("my_key")
    await redis.aclose()
```

## Related Errors

- {{< relref "importerror-redis-py" >}} — ImportError: redis
- {{< relref "importerror-asyncpg" >}} — ImportError: asyncpg
- {{< relref "importerror-celery-redbeat" >}} — ImportError: redbeat

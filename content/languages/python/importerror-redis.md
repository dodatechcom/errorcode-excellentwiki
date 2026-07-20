---
title: "[Solution] Python ImportError: No module named 'redis' — Fix"
description: "Fix Python ImportError: No module named 'redis'. Install redis-py with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 321
---

# Python ImportError: No module named 'redis'

The `redis` package (redis-py) is the official Python client for Redis. This error occurs when the package is not installed in the current Python environment.

## Common Causes

```python
# Cause 1: redis-py not installed
import redis  # ImportError: No module named 'redis'

# Cause 2: Installed redis-server instead of redis-py
# apt install redis gives you the server, not the Python client

# Cause 3: Wrong virtual environment activated
# redis installed in project-A venv but you are in project-B

# Cause 4: Using aioredis (legacy) without redis installed
import redis.asyncio as redis  # ImportError if redis < 4.2

# Cause 5: Case sensitivity
import Redis  # ImportError — must be lowercase
```

## How to Fix

### Fix 1: Install redis-py with pip

```bash
pip install redis

# For a specific version
pip install redis==5.0.4

# With async support (included in redis >= 4.2)
pip install redis
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install redis
python -c "import redis; print(redis.__version__)"
```

### Fix 3: Install alongside common companions

```bash
pip install redis celery[redis] django-redis
```

## Examples

```python
import redis

r = redis.Redis(host="localhost", port=6379, db=0)
r.set("key", "value")
print(r.get("key"))
```

## Related Errors

- {{< relref "importerror-redis-py" >}} — ImportError: redis (variant)
- {{< relref "importerror-aioredis" >}} — ImportError: aioredis
- {{< relref "importerror-celery" >}} — ImportError: celery

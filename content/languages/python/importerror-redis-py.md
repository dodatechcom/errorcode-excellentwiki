---
title: "[Solution] Python ImportError: redis not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: redis not found or ModuleNotFoundError: No module named 'redis'. Install redis-py properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: redis not found — ModuleNotFoundError Fix

An `ImportError: redis not found` or `ModuleNotFoundError: No module named 'redis'` means Python cannot locate the redis package.

## What This Error Means

redis-py is the Python client for Redis. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: redis not installed
import redis  # ModuleNotFoundError: No module named 'redis'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install redis

# For a specific version
pip install redis==5.0.1
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install redis
python -c "import redis; print(redis.__version__)"
```

## Related Errors

- {{< relref "testcontainers-redis" >}} — Redis container startup failed
- {{< relref "spring-cache" >}} — CacheAccessException
- {{< relref "importerror-celery" >}} — ImportError: celery

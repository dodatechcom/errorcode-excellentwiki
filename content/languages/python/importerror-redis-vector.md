---
title: "[Solution] Python ImportError: redis with vector search — ModuleNotFoundError Fix"
description: "Fix Python ImportError: redis with vector search. Configure Redis Stack for vector search capabilities."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "redis", "vector-search", "module-not-found", "pip"]
weight: 5
---

# ImportError: redis with vector search — ModuleNotFoundError Fix

This error occurs when trying to use Redis vector search features but the required dependencies are not installed or Redis Stack is not running.

## What This Error Means

Redis vector search requires Redis Stack (with RediSearch module) and the redis-py package with vector search support.

## Common Causes

```python
# Cause 1: redis-py not installed
import redis  # ModuleNotFoundError

# Cause 2: Redis Stack not running (vector search module missing)

# Cause 3: Using standard Redis instead of Redis Stack
```

## How to Fix

### Fix 1: Install redis with vector search

```bash
pip install redis

# Verify vector search support
python -c "from redis.commands.search.field import VectorField; print('OK')"
```

### Fix 2: Use Redis Stack Docker image

```bash
docker run -d --name redis-stack -p 6379:6379 redis/redis-stack-server:latest
```

### Fix 3: Connect with proper configuration

```python
import redis
from redis.commands.search.field import VectorField
from redis.commands.search.commands import SearchCommands

r = redis.Redis(host='localhost', port=6379)
# Verify RediSearch module is loaded
print(r.info('modules'))
```

## Related Errors

- {{< relref "importerror-redis-py" >}} — ImportError: redis
- {{< relref "importerror-chromadb" >}} — ImportError: chromadb
- {{< relref "testcontainers-redis" >}} — Redis container startup failed (Java)

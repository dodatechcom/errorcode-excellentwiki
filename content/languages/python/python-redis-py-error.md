---
title: "[Solution] Python redis-py Error — Redis Client Failures"
description: "Fix Python redis-py errors like ConnectionError, TimeoutError, ResponseError, pipeline errors, and pub/sub issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 430
---

# Python redis-py Error — Redis Client Failures

redis-py errors occur when the client cannot connect to Redis, commands time out, data type mismatches occur, pipelines fail, or pub/sub connections drop. These are common in caching and real-time applications.

## Common Causes

```python
# ConnectionError: cannot connect to Redis
import redis
r = redis.Redis(host="localhost", port=6379, db=0, socket_connect_timeout=2)
r.ping()

# ResponseError: wrong data type for operation
r = redis.Redis()
r.set("key", "string_value")
r.incr("key")  # cannot increment a string

# TimeoutError: command timed out
r = redis.Redis(socket_timeout=0.001)
r.set("key", "value")

# ResponseError: index out of range
r.lindex("nonexistent-list", 0)

# PubSubError: pub/sub already subscribed
r_pubsub = r.pubsub()
r_pubsub.subscribe("channel")
r_pubsub.subscribe("channel")  # already subscribed
```

## How to Fix

### Fix 1: Use Connection Pools for Reliability
Always use a connection pool instead of a single connection.
```python
import redis

pool = redis.ConnectionPool(
    host="localhost",
    port=6379,
    db=0,
    max_connections=20,
    socket_connect_timeout=5,
    socket_timeout=5,
    decode_responses=True,
)
r = redis.Redis(connection_pool=pool)

try:
    r.ping()
    print("Connected to Redis")
except redis.ConnectionError:
    print("Cannot connect to Redis")
```

### Fix 2: Handle Data Type Mismatches
Check the type before performing type-specific operations.
```python
import redis

r = redis.Redis()
key = "counter"

if not r.exists(key):
    r.set(key, 0)
elif r.type(key).decode() != "string" or not r.get(key).isdigit():
    r.delete(key)
    r.set(key, 0)

r.incr(key)
```

### Fix 3: Use Pipelines Correctly
Use context managers to ensure pipelines are properly executed.
```python
import redis

r = redis.Redis()

# Correct pipeline usage
pipe = r.pipeline(transaction=True)
try:
    pipe.set("key1", "value1")
    pipe.set("key2", "value2")
    pipe.incr("counter")
    results = pipe.execute()
    print(results)
except redis.ResponseError as e:
    pipe.reset()
    print(f"Pipeline error: {e}")
```

### Fix 4: Handle Pub/Sub Reconnection
Implement reconnection logic for pub/sub subscriptions.
```python
import redis
import time

def subscribe_with_retry(channel, max_retries=5):
    r = redis.Redis()
    pubsub = r.pubsub()

    for attempt in range(max_retries):
        try:
            pubsub.subscribe(channel)
            for message in pubsub.listen():
                if message["type"] == "message":
                    yield message["data"]
        except (redis.ConnectionError, redis.TimeoutError) as e:
            print(f"Pub/Sub disconnected (attempt {attempt + 1}): {e}")
            time.sleep(2 ** attempt)
            pubsub.close()
            pubsub = r.pubsub()
```

### Fix 5: Set Appropriate Timeouts
Configure timeouts based on expected command latency.
```python
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    socket_connect_timeout=5,
    socket_timeout=5,
    retry_on_timeout=True,
)

r.set("key", "value")
value = r.get("key")
```

## Examples

```python
# Cache class with error handling
import redis
import json
import time

class Cache:
    def __init__(self, host="localhost", port=6379, db=0):
        pool = redis.ConnectionPool(host=host, port=port, db=db, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool)

    def get(self, key):
        try:
            data = self.r.get(key)
            if data:
                return json.loads(data)
            return None
        except redis.ConnectionError:
            return None

    def set(self, key, value, ttl=3600):
        try:
            self.r.setex(key, ttl, json.dumps(value))
            return True
        except redis.ConnectionError:
            return False

    def delete(self, key):
        try:
            return self.r.delete(key) > 0
        except redis.ConnectionError:
            return False
```

## Related Errors

- [Python PyMongo Error](/languages/python/python-pymongo-error/)
- [Python Elasticsearch Error](/languages/python/python-elasticsearch-error/)
- [Python kafka-python Error](/languages/python/python-kafka-python-error/)

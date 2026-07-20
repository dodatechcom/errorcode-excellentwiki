---
title: "[Solution] Redis Optimistic Lock Failure Error"
description: "How to fix Redis optimistic lock failure when concurrent modifications are detected"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- High contention on a single key
- Multiple clients trying to update same key simultaneously
- Long processing time between WATCH and EXEC

## Fix

Implement retry with backoff:

```python
import time
import redis

r = redis.Redis()

for attempt in range(5):
    try:
        with r.pipeline() as pipe:
            pipe.watch('balance')
            balance = int(pipe.get('balance'))
            pipe.multi()
            pipe.set('balance', balance - 100)
            pipe.execute()
            break
    except redis.exceptions.WatchError:
        time.sleep(0.1 * (attempt + 1))
```

Reduce contention window:

```bash
# Quick WATCH-MULTI-EXEC
redis-cli WATCH mykey
redis-cli MULTI
redis-cli SET mykey newvalue
redis-cli EXEC
```

## Examples

```bash
# Fast transaction to reduce contention
redis-cli WATCH account:balance
redis-cli MULTI
redis-cli DECRBY account:balance 100
redis-cli EXEC
```

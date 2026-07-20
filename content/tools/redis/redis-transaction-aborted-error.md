---
title: "[Solution] Redis Transaction Aborted Error"
description: "How to fix Redis transaction aborted errors due to WATCH failures"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- WATCHed key was modified between WATCH and EXEC
- Another client modified the watched key
- Optimistic lock conflict

## Fix

Retry the transaction:

```python
import redis
r = redis.Redis()

while True:
    try:
        pipe = r.pipeline()
        pipe.watch('mykey')
        val = pipe.get('mykey')
        pipe.multi()
        pipe.set('mykey', new_value)
        pipe.execute()
        break
    except redis.exceptions.WatchError:
        continue  # Retry
```

Check watched keys:

```bash
redis-cli WATCH mykey
redis-cli MULTI
redis-cli EXEC
# If WATCHed key changed: EXECABORT Transaction discarded
```

## Examples

```bash
# Transaction with retry logic
# Terminal 1:
redis-cli WATCH counter
redis-cli GET counter
redis-cli MULTI
redis-cli INCR counter
redis-cli EXEC
# May return: EXECABORT if counter changed

# Terminal 2 (during Terminal 1's WATCH):
redis-cli INCR counter  # This causes Terminal 1's EXEC to fail
```

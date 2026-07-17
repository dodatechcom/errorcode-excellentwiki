---
title: "Redis Transaction Error"
description: "Redis MULTI/EXEC transaction fails or encounters errors."
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["redis", "transaction", "multi", "exec", "watch"]
weight: 5
---

# Redis Transaction Error

A Redis transaction error occurs when a MULTI/EXEC transaction fails. Redis transactions provide atomic execution of multiple commands but have specific limitations.

## Common Causes

- Syntax error in transaction command
- WATCH key modified during transaction
- Command inside transaction is invalid
- EXEC discarded due to WATCH failure

## How to Fix

### Use MULTI/EXEC Correctly

```bash
MULTI
SET key1 value1
SET key2 value2
EXEC
```

### Handle WATCH Failures

```bash
WATCH mykey
val = GET mykey
MULTI
SET mykey newvalue
EXEC
# Returns nil if WATCH detected changes
```

### Use Pipeline Instead of Transaction

```python
import redis

r = redis.Redis()
pipe = r.pipeline()
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
pipe.execute()
```

### Check for Syntax Errors

```bash
MULTI
INVALID_COMMAND
EXEC
# ERR unknown command
```

### Use DISCARD to Abort

```bash
MULTI
SET key1 value1
DISCARD
```

### Handle Optimistic Locking

```python
import redis

r = redis.Redis()
with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch('mykey')
            val = pipe.get('mykey')
            pipe.multi()
            pipe.set('mykey', 'newvalue')
            pipe.execute()
            break
        except redis.WatchError:
            continue
```

## Examples

```bash
MULTI
SET key1 value1
EXEC
# OK

# WATCH failure
WATCH mykey
MULTI
SET mykey newvalue
EXEC
# (nil) - key was modified
```

## Related Errors

- [Transaction Error]({{< relref "/tools/redis/redis-transaction-error" >}}) — transaction failure
- [Lua Error]({{< relref "/tools/redis/redis-lua-error" >}}) — Lua script error

---
title: "Redis key expired during operation"
description: "A Redis key expires between the time it is read and the time it is written, causing inconsistent state"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["ttl", "expire", "race-condition", "consistency"]
weight: 5
---

This error occurs when a Redis key expires between the time your code reads it and the time it tries to write back to it. This creates a race condition where operations may be lost or duplicated.

## Common Causes

- Key TTL is too short for the operation duration
- Read-modify-write pattern without atomicity
- Distributed lock with TTL that expires mid-operation
- No retry logic for expired key scenarios

## How to Fix

1. Use atomic operations instead of read-modify-write:

```bash
# Instead of GET then SET:
INCR counter

# Or use Lua for atomic check-and-set:
```

```lua
-- Atomic read-modify-write in Lua
local val = redis.call("GET", KEYS[1])
if val then
  val = tonumber(val) + 1
  redis.call("SET", KEYS[1], val, "EX", 300)
  return val
end
return nil
```

2. Extend TTL before processing:

```bash
# Refresh the lock TTL before doing work
PEXPIRE lock:job 60000
```

3. Use Redis transactions for multi-step operations:

```bash
WATCH mykey
MULTI
SET mykey "new_value"
EXEC
```

## Examples

```python
import redis
r = redis.Redis()

# Key expires between get and set
val = r.get("session:abc")  # returns b"data"
# ... processing takes time, key expires ...
r.set("session:abc", "updated")  # creates a new key with no data
```

## Related Errors

- [OOM command not allowed](/tools/redis/max-memory)

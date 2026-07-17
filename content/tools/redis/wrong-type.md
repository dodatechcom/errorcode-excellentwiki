---
title: "WRONGTYPE Operation against a key"
description: "Redis command used on a key whose stored data type does not match the expected type"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when you execute a Redis command against a key that holds a different data type than the command expects. For example, using `LPUSH` on a key that stores a string.

## Common Causes

- Using a command meant for one data type on a key holding another type
- Application code overwriting keys with incompatible types
- Mixing data structures (e.g., using a key as both a string and a list)
- Key was written by a different client or service with a different structure

## How to Fix

1. Check the current type of the key:

```bash
redis-cli TYPE mykey
```

2. Delete the key and recreate it with the correct type:

```bash
redis-cli DEL mykey
redis-cli LPUSH mykey "value1" "value2"
```

3. Use key naming conventions to avoid collisions:

```bash
# Instead of using "session" for both types:
# Use "session:string:user123" and "session:list:user123"
```

4. In application code, always check the type before operating:

```python
import redis
r = redis.Redis()

key_type = r.type("mykey").decode()
if key_type != "list":
    r.delete("mykey")
r.lpush("mykey", "value1")
```

## Examples

```bash
# Key is a string
redis-cli SET mykey "hello"

# Trying to use a list command on it fails
redis-cli LPUSH mykey "world"
# WRONGTYPE Operation against a key holding the wrong kind of value
```

```python
# Python example
import redis
r = redis.Redis()
r.set("counter", 42)
r.lpush("counter", 1)
# redis.exceptions.ResponseError: WRONGTYPE Operation against a key holding the wrong kind of value
```

## Related Errors

- [Connection Refused](/tools/redis/connection-refused)

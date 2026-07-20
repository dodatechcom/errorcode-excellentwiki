---
title: "[Solution] Redis EVALSHA NOSCRIPT Error"
description: "How to fix Redis EVALSHA NOSCRIPT error when script is not in cache"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Script was evicted from cache after SCRIPT FLUSH
- Redis server restarted (script cache is in-memory only)
- SHA1 hash mismatch between EVALSHA and actual script

## Fix

Register script first with EVAL:

```bash
redis-cli EVAL "return redis.call('GET', KEYS[1])" 1 mykey
```

Then use EVALSHA with the returned SHA1:

```bash
# Get SHA1
echo -n "return redis.call('GET', KEYS[1])" | sha1sum

# Use EVALSHA
redis-cli EVALSHA <sha1> 1 mykey
```

Handle NOSCRIPT in application:

```python
try:
    r.evalsha(script_sha, 1, 'mykey')
except redis.exceptions.NoScriptError:
    r.eval(script, 1, 'mykey')
```

## Examples

```bash
# Register script
redis-cli EVAL "return redis.call('GET', KEYS[1])" 1 mykey

# Verify script is cached
redis-cli SCRIPT EXISTS <sha1>

# Flush script cache
redis-cli SCRIPT FLUSH
```

---
title: "[Solution] Redis Script Killed Error"
description: "How to fix Redis script killed error when Lua scripts are terminated by timeout"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Script exceeded `lua-time-limit`
- Script performed blocking operations
- NOSCRIPT after script was evicted from cache

## Fix

Increase timeout for long scripts:

```bash
redis-cli CONFIG SET lua-time-limit 5000
```

Optimize script to run faster:

```lua
-- Use KEYS and ARGV instead of redis.call inside loops
local val = redis.call('GET', KEYS[1])
return val
```

Cache script with EVALSHA:

```bash
redis-cli EVAL "return redis.call('PING')" 0
redis-cli EVALSHA <sha1> 0
```

## Examples

```bash
# Check script timeout
redis-cli CONFIG GET lua-time-limit

# Find scripts in cache
redis-cli SCRIPT EXISTS

# Clear script cache
redis-cli SCRIPT FLUSH
```

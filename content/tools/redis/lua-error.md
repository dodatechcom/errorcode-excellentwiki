---
title: "ERR Error in Lua script"
description: "Redis returns an error from an EVAL or EVALSHA script because the Lua code failed at runtime"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Lua script executed via `EVAL` or `EVALSHA` encounters a runtime error, such as accessing a nil value or calling a Redis command that is not allowed inside a script.

## Common Causes

- Lua script calls a command that is not allowed inside `EVAL` (e.g. `SELECT`)
- Accessing a variable that is nil inside the script
- Script tries to use `KEYS` or `ARGV` with out-of-bounds indices
- Script exceeds the time limit (`lua-time-limit`)

## How to Fix

1. Ensure only allowed Redis commands are used inside scripts:

```lua
-- Allowed: GET, SET, HGET, etc.
-- Not allowed: SELECT, AUTH, QUIT
local val = redis.call("GET", KEYS[1])
```

2. Add nil checks before accessing values:

```lua
local val = redis.call("GET", KEYS[1])
if not val then
  return nil
end
```

3. Verify `KEYS` and `ARGV` usage:

```lua
-- Always check argc before using ARGV
if #ARGV == 0 then
  return redis.error_reply("no arguments provided")
end
```

4. Increase the Lua script time limit if needed:

```bash
redis-cli CONFIG SET lua-time-limit 10000
```

## Examples

```lua
-- Script with error: accessing nil field
local val = redis.call("GET", KEYS[1])
return val.toUpperCase()  -- val may be nil
```

```text
(error) ERR Error in call to redis.eval(): ERR user_script:2: attempt to index a nil value
```

## Related Errors

- [WRONGTYPE Operation against a key](/tools/redis/wrong-type)

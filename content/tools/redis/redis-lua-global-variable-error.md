---
title: "[Solution] Redis Lua Global Variable Error"
description: "How to fix Redis Lua script global variable errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Using global variables in Lua scripts
- Missing `local` keyword
- Accidentally polluting global namespace

## Fix

Always use `local` for variables:

```lua
-- Wrong
x = redis.call('GET', KEYS[1])

-- Correct
local x = redis.call('GET', KEYS[1])
```

Check for globals:

```lua
-- Add at start of script
local function main()
    -- all logic here
end
return main()
```

## Examples

```bash
# Good script with local variables
redis-cli EVAL "
  local key = KEYS[1]
  local val = redis.call('GET', key)
  return val
" 1 mykey

# Bad script (global variable)
redis-cli EVAL "
  key = KEYS[1]
  val = redis.call('GET', key)
  return val
" 1 mykey
```

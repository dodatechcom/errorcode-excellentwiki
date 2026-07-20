---
title: "[Solution] Redis Lua Stack Overflow Error"
description: "How to fix Redis Lua script stack overflow errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Too many nested function calls in Lua script
- Deep recursion in Lua script
- Script processing too many nested elements

## Fix

Limit recursion depth:

```lua
local function safe_get(key, depth)
    if depth > 100 then return nil end
    return redis.call('GET', key)
end
```

Use iteration instead of recursion:

```lua
-- Instead of recursive traversal, use iterative approach
local stack = {root_key}
while #stack > 0 do
    local key = table.remove(stack)
    -- process key
end
```

Increase Lua stack size (compile-time change):

```bash
# Requires recompiling Redis with larger LUA_MAXCSTACK
```

## Examples

```bash
# Test recursive script (will fail with deep recursion)
redis-cli EVAL "
  local function f(n) if n == 0 then return 1 end return f(n-1) end
  return f(10000)
" 0

# Use iterative approach
redis-cli EVAL "
  local sum = 0
  for i = 1, 10000 do sum = sum + i end
  return sum
" 0
```

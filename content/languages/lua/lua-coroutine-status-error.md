---
title: "[Solution] Lua Coroutine Status Error"
description: "Fix Lua coroutine status errors when querying coroutine state incorrectly."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Coroutine status errors occur when coroutine.status is called with an invalid argument.

## Common Causes

- Passing non-coroutine to coroutine.status
- Using status on thread incorrectly
- Status check on garbage-collected coroutine
- Missing coroutine variable

## How to Fix

### 1. Verify coroutine exists before checking status

```lua
if co then
  local status = coroutine.status(co)
  print(status)
end
```

### 2. Proper coroutine lifecycle management

```lua
local co = coroutine.create(function() return 1 end)
print(coroutine.status(co))  -- "suspended"
coroutine.resume(co)          -- resume once
print(coroutine.status(co))  -- "dead"
```

## Examples

```lua
local function statusName(co)
  if not co then return "nil" end
  return coroutine.status(co)
end

local co = coroutine.create(function()
  coroutine.yield()
end)

print(statusName(co))  -- "suspended"
coroutine.resume(co)
print(statusName(co))  -- "dead"
```

## Related Errors

- [Coroutine resume error](/languages/lua/lua-coroutine-resume-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)

---
title: "[Solution] Lua Coroutine Status Error Fix"
description: "Fix Lua coroutine.status errors. Learn how to check and interpret coroutine states."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1104
---

## What This Error Means

A coroutine status error occurs when attempting to resume a coroutine that is in an invalid state, such as "dead" or "running" (self-resume).

## Common Causes

- Resuming a coroutine that has already finished (dead)
- Resuming a coroutine from within itself (running)
- Not checking coroutine.status before resuming
- Confusing "suspended" vs "normal" states

## How to Fix

```lua
-- WRONG: Resuming a dead coroutine
local co = coroutine.create(function() return "done" end)
coroutine.resume(co)  -- true, "done"
coroutine.resume(co)  -- false, "cannot resume dead coroutine"

-- CORRECT: Check status before resuming
if coroutine.status(co) ~= "dead" then
    coroutine.resume(co)
end
```

```lua
-- WRONG: Self-resume
local co = coroutine.create(function()
    coroutine.resume(co)  -- cannot resume running coroutine
end)
coroutine.resume(co)

-- CORRECT: Use a separate coroutine or restructure
local co = coroutine.create(function()
    coroutine.yield("yielded")
end)
local main = coroutine.create(function()
    coroutine.resume(co)
end)
```

```lua
-- WRONG: Assuming "suspended" is the only valid state
local co = coroutine.create(function()
    coroutine.yield()
end)
print(coroutine.status(co))  -- "suspended"
coroutine.resume(co)
print(coroutine.status(co))  -- "dead"

-- CORRECT: Handle all states
local function safe_resume(co)
    local status = coroutine.status(co)
    if status == "suspended" then
        return coroutine.resume(co)
    elseif status == "dead" then
        return false, "coroutine is dead"
    elseif status == "running" then
        return false, "cannot resume self"
    end
end
```

```lua
-- "normal" state explained
local co = coroutine.create(function()
    coroutine.yield()
end)
local co2 = coroutine.create(function()
    coroutine.resume(co)  -- co2 is "normal" while co runs
end)
coroutine.resume(co2)
```

## Examples

```lua
local co = coroutine.create(function()
    for i = 1, 3 do
        coroutine.yield(i)
    end
end)

while true do
    local status = coroutine.status(co)
    if status == "dead" then break end
    local ok, val = coroutine.resume(co)
    if ok then print(val) end
end
```

## Related Errors

- [Lua coroutine error](lua-coroutine-error) - coroutine issue
- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua stack overflow](lua-stack-overflow) - stack overflow

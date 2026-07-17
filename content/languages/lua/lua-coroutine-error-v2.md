---
title: "[Solution] Lua Cannot Resume Dead Coroutine"
description: "Fix Lua coroutine errors when trying to resume a dead or already-running coroutine. Manage coroutine lifecycle correctly."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["coroutine", "resume", "dead", "yield", "thread", "lua"]
weight: 5
---

## What This Error Means

The error `cannot resume dead coroutine` occurs when you try to resume a coroutine that has already finished execution or was never properly created. Coroutines can only be resumed when they are in the "suspended" state.

## Common Causes

- Resuming a coroutine that has finished (dead state)
- Creating coroutine without coroutine.create
- Resuming an already-running coroutine
- Coroutine returned an error
- Forgetting to check coroutine.status

## How to Fix

```lua
-- WRONG: Resuming dead coroutine
local co = coroutine.create(function()
    return "done"
end)
coroutine.resume(co)  -- Returns true, "done"
coroutine.resume(co)  -- Error: cannot resume dead coroutine

-- CORRECT: Check status before resuming
if coroutine.status(co) ~= "dead" then
    coroutine.resume(co)
end
```

```lua
-- WRONG: Not handling coroutine errors
local co = coroutine.create(function()
    error("something went wrong")
end)
coroutine.resume(co)  -- Returns false, error message

-- CORRECT: Check resume result
local success, result = coroutine.resume(co)
if not success then
    print("Coroutine error: " .. tostring(result))
end
```

```lua
-- WRONG: Creating new coroutine instead of reusing
while true do
    local co = coroutine.create(work)
    coroutine.resume(co)  -- Creates new one each time
end

-- CORRECT: Use coroutine.wrap for simple cases
local co = coroutine.wrap(function()
    while true do
        coroutine.yield("result")
    end
end)
print(co())  -- "result"
print(co())  -- "result"
```

## Examples

```lua
-- Example 1: Coroutine lifecycle management
local function create_worker()
    local co = coroutine.create(function()
        for i = 1, 5 do
            coroutine.yield(i)
        end
        return "done"
    end)
    return co
end

local worker = create_worker()
while coroutine.status(worker) ~= "dead" do
    local success, value = coroutine.resume(worker)
    if success then
        print("Got: " .. tostring(value))
    else
        print("Error: " .. tostring(value))
        break
    end
end

-- Example 2: Producer-consumer with coroutine
local producer = coroutine.create(function()
    for i = 1, 10 do
        coroutine.yield(i)
    end
end)

local consumer = coroutine.create(function()
    while true do
        local ok, value = coroutine.resume(producer)
        if not ok or coroutine.status(producer) == "dead" then
            break
        end
        print("Consumed: " .. value)
    end
end)

coroutine.resume(consumer)

-- Example 3: Safe resume wrapper
local function safe_resume(co, ...)
    if coroutine.status(co) == "dead" then
        return false, "coroutine is dead"
    end
    return coroutine.resume(co, ...)
end
```

## Related Errors

- [lua-runtime-error]({{< relref "/languages/lua/lua-runtime-error" >}}) — runtime error
- [lua-memory-error]({{< relref "/languages/lua/lua-memory-error" >}}) — memory error
- [lua-type-error]({{< relref "/languages/lua/lua-type-error" >}}) — type error

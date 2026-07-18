---
title: "[Solution] Lua Cannot Resume Dead Coroutine Error Fix"
description: "Fix Lua 'cannot resume dead coroutine' errors. Learn why coroutine resume fails and how to manage coroutine lifecycle."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The `cannot resume dead coroutine` error in Lua occurs when you attempt to resume a coroutine that has already finished executing. Once a coroutine function returns or throws an error, the coroutine enters the "dead" state and cannot be resumed again. Each coroutine can only be resumed a limited number of times determined by its execution.

## Why It Happens

- Resuming a coroutine after its function has already returned
- Attempting to resume a coroutine that hit an unhandled error
- Calling `coroutine.resume` without first checking `coroutine.status`
- Accidentally resuming a coroutine twice in the same event loop iteration
- A coroutine yields internally but the surrounding logic resumes it again after it finishes
- Reusing a coroutine object after its function completes

## How to Fix It

### Check coroutine status before resuming

```lua
-- WRONG: Resuming without checking status
local co = coroutine.create(function()
    return "done"
end)
coroutine.resume(co)  -- returns "done"
coroutine.resume(co)  -- error: cannot resume dead coroutine

-- CORRECT: Always check status first
local co = coroutine.create(function()
    return "done"
end)
while coroutine.status(co) ~= "dead" do
    local ok, result = coroutine.resume(co)
    if ok then
        print(result)
    end
end
```

### Use a safe wrapper for coroutine management

```lua
-- WRONG: Direct resume without safety
function runTask(task)
    local co = coroutine.create(task)
    coroutine.resume(co)
    coroutine.resume(co)  -- may be dead
end

-- CORRECT: Track coroutine state
function runTask(task)
    local co = coroutine.create(task)
    return function()
        if coroutine.status(co) ~= "dead" then
            return coroutine.resume(co)
        else
            return false, "coroutine already finished"
        end
    end
end
```

### Handle coroutine errors properly

```lua
-- WRONG: Error inside coroutine not checked
local co = coroutine.create(function()
    error("task failed")
end)
coroutine.resume(co)  -- returns false, error message
coroutine.resume(co)  -- dead now, crashes

-- CORRECT: Handle resume result
local co = coroutine.create(function()
    error("task failed")
end)
local ok, err = coroutine.resume(co)
if not ok then
    print("Coroutine error: " .. tostring(err))
end
-- Do not resume again after error
```

### Create new coroutines for repeated tasks

```lua
-- WRONG: Reusing dead coroutine
local co = coroutine.create(function() print("run") end)
coroutine.resume(co)
coroutine.resume(co)  -- dead

-- CORRECT: Create a new coroutine each time
local function createTask()
    return coroutine.create(function() print("run") end)
end
local co1 = createTask()
coroutine.resume(co1)
local co2 = createTask()
coroutine.resume(co2)
```

### Use coroutine.wrap for simpler iteration

```lua
-- WRONG: Managing coroutine lifecycle manually
local co = coroutine.create(function()
    for i = 1, 3 do coroutine.yield(i) end
end)

-- CORRECT: Use coroutine.wrap which raises error on dead coroutine
local nextVal = coroutine.wrap(function()
    for i = 1, 3 do coroutine.yield(i) end
end)
print(nextVal())  -- 1
print(nextVal())  -- 2
print(nextVal())  -- 3
-- nextVal()  -- would raise error
```

## Common Mistakes

- Assuming `coroutine.resume` returns `true` for a dead coroutine
- Not distinguishing between a coroutine that returned normally versus one that errored
- Storing a coroutine reference and resuming it from multiple call sites without coordination
- Forgetting that `coroutine.yield` with arguments passes them to the next `resume`, not the previous one
- Creating coroutines inside tight loops without ever letting them finish

## Related Pages

- [Lua Stack Overflow](lua-stack-overflow) - recursion too deep
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Runtime Error](lua-runtime-error) - general runtime issue

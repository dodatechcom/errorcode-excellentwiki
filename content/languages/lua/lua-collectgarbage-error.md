---
title: "[Solution] Lua collectgarbage Function Error Fix"
description: "Fix Lua collectgarbage errors when interacting with the garbage collector."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1119
---

## What This Error Means

A collectgarbage error occurs when calling collectgarbage with invalid options or when the garbage collector encounters an issue. The function accepts specific string arguments to control GC behavior.

## Common Causes

- Invalid option string passed to collectgarbage
- Calling collectgarbage with wrong argument type
- Calling collectgarbage("stop") and forgetting to restart
- Using collectgarbage("count") incorrectly
- Not understanding collectgarbage return values

## How to Fix

```lua
-- WRONG: Invalid option
local ok, err = pcall(collectgarbage, "invalid_option")
print(ok, err)  -- false, "bad argument #1 to 'collectgarbage' (invalid option 'invalid_option')"

-- CORRECT: Use valid options
local valid_options = {
    "stop", "restart", "collect", "count",
    "step", "setpause", "setstepmul", "isrunning"
}
```

```lua
-- WRONG: Collecting in a performance-critical section
collectgarbage("collect")  -- Triggers full GC cycle

-- CORRECT: Collect between tasks
-- During heavy processing:
collectgarbage("stop")  -- Pause GC
-- ... do work ...
collectgarbage("restart")  -- Resume GC
collectgarbage("step", 200)  -- Incremental collection
```

```lua
-- WRONG: Misinterpreting count return
local mem_kb = collectgarbage("count")
print("Memory:", mem_kb)  -- In kilobytes

-- CORRECT: Understand the return value
local mem_kb = collectgarbage("count")
local mem_bytes = mem_kb * 1024
print(string.format("Memory: %.2f KB (%.2f MB)", mem_kb, mem_kb / 1024))
```

```lua
-- WRONG: Using count after collect
-- collectgarbage("collect") doesn't return memory freed
collectgarbage("collect")
local mem_after = collectgarbage("count")

-- CORRECT: Measure before and after
local mem_before = collectgarbage("count")
-- allocate lots of memory...
local t = {}
for i = 1, 100000 do t[i] = { i } end
t = nil
-- collect
local mem_after_alloc = collectgarbage("count")
collectgarbage("collect")
local mem_after_collect = collectgarbage("count")
print("Freed:", mem_after_alloc - mem_after_collect, "KB")
```

```lua
-- Check if GC is running
if collectgarbage("isrunning") then
    print("GC is active")
else
    print("GC is paused")
    collectgarbage("restart")
end
```

## Examples

```lua
local function measure_memory(fn)
    collectgarbage("collect")
    local before = collectgarbage("count")
    fn()
    collectgarbage("collect")
    local after = collectgarbage("count")
    return after - before
end

local mem = measure_memory(function()
    local t = {}
    for i = 1, 10000 do
        t[i] = string.rep("x", 100)
    end
end)
print("Memory used:", mem, "KB")
```

## Related Errors

- [Lua GC error](lua-gc-error) - GC issue
- [Lua memory error](lua-memory-error) - memory issue
- [Lua runtime error](lua-runtime-error) - runtime issue

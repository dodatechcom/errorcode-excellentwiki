---
title: "[Solution] Lua Garbage Collector Pause Error Fix"
description: "Fix Lua garbage collector errors. Learn how to control GC pausing and step behavior."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1118
---

## What This Error Means

A garbage collector error occurs when Lua's GC pauses too frequently, doesn't run often enough, or causes performance issues. The GC can be tuned with collectgarbage parameters.

## Common Causes

- GC running too frequently causing lag spikes
- GC not running enough leading to high memory usage
- Calling collectgarbage("collect") too often
- Circular references preventing collection
- Weak references not configured for caching scenarios

## How to Fix

```lua
-- WRONG: Forcing GC too often
for i = 1, 1000 do
    local t = { data = i }
    collectgarbage("collect")  -- Slow!
end

-- CORRECT: Let GC run naturally
for i = 1, 1000 do
    local t = { data = i }
end
-- GC will collect when needed
```

```lua
-- WRONG: GC pauses too frequently (default pause=200, stepmul=200)
-- These settings cause frequent pauses

-- CORRECT: Tune GC parameters for throughput
collectgarbage("setpause", 200)    -- Default: wait until 200% growth
collectgarbage("setstepmul", 200)  -- Default: 200% of allocation rate

-- For batch processing, increase pause
collectgarbage("setpause", 400)    -- Allow 400% growth before GC
```

```lua
-- WRONG: Circular references causing memory leaks
function create_leak()
    local a = {}
    local b = {}
    a.other = b
    b.other = a  -- Circular!
end
for i = 1, 10000 do create_leak() end
-- Memory keeps growing until GC runs

-- CORRECT: Break cycles manually or use weak tables
function create_no_leak()
    local a = {}
    local b = {}
    a.other = b
    b.other = a
    a.other = nil  -- Break cycle when done
end
```

```lua
-- Monitoring GC
local function gc_stats()
    print("Memory (KB):", collectgarbage("count"))
    print("GC running:", collectgarbage("isrunning"))
end

gc_stats()
-- Do work...
collectgarbage()  -- Full GC cycle
gc_stats()
```

```lua
-- Weak references for caches
local cache = setmetatable({}, { __mode = "k" })  -- Weak keys

function cached_load(filename)
    local data = cache[filename]
    if not data then
        data = loadfile(filename)
        cache[filename] = data
        print("Cached:", filename)
    end
    return data
end
```

## Examples

```lua
-- Tuning GC for a game loop
local function game_loop()
    local frame_count = 0
    while running do
        update()
        render()
        frame_count = frame_count + 1
        if frame_count % 60 == 0 then
            collectgarbage("step", 100)  -- Incremental GC
        end
    end
end
```

## Related Errors

- [Lua GC error](lua-gc-error) - GC issue
- [Lua memory error](lua-memory-error) - memory issue
- [Lua nil error](lua-nil-error) - nil error

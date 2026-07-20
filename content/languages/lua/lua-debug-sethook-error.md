---
title: "[Solution] Lua debug.sethook Hook Error Fix"
description: "Fix Lua debug.sethook errors when setting debugging hooks for breakpoints and profiling."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1131
---

## What This Error Means

A debug.sethook error occurs when installing debug hooks for call/return/line events. Common issues include invalid hook masks, hook function errors cascading, or hook performance problems.

## Common Causes

- Invalid hook mask characters (only 'c', 'r', 'l' are valid)
- Hook function raising its own errors
- Not removing hooks after use (performance drain)
- Hook count parameter causing unexpected stops
- Recursive hook calls when hook itself triggers events

## How to Fix

```lua
-- WRONG: Invalid mask characters
debug.sethook(function() end, "xyz")  -- Invalid mask 'xyz'

-- CORRECT: Use valid masks
-- 'c' = call events, 'r' = return events, 'l' = line events
debug.sethook(function() end, "c")    -- Only function calls
debug.sethook(function() end, "cr")   -- Calls and returns
debug.sethook(function() end, "l")    -- Every line
```

```lua
-- WRONG: Hook function raising errors
debug.sethook(function()
    error("Hook failed")  -- Error cascades to main code!
end, "c")

function test() end
test()  -- Prints error from hook

-- CORRECT: Protect hook function
debug.sethook(function()
    local ok, err = pcall(function()
        -- Debugging logic
    end)
    if not ok then
        -- Log error silently
        debug.sethook()  -- Remove broken hook
    end
end, "c")
```

```lua
-- WRONG: Forgetting to remove hooks
debug.sethook(function() print("line"), "l")
-- ... Long running code ...
-- Hook still running, severely slowing things down

-- CORRECT: Remove hooks when done
debug.sethook(function() print("line"), "l")
-- ... Debug code ...
debug.sethook()  -- Remove all hooks

-- Or use count parameter
debug.sethook(function()
    print("Hit instruction limit")
    debug.sethook()  -- Self-removing hook
end, "", 1000)  -- After 1000 instructions
```

```lua
-- Profiling with hooks
local call_count = 0
local last_time = os.clock()

debug.sethook(function(event)
    if event == "call" then
        call_count = call_count + 1
    elseif event == "return" or event == "tail return" then
        call_count = call_count - 1
    end
end, "cr")

-- Code to profile
for i = 1, 1000 do math.sqrt(i) end

debug.sethook()
print("Max call depth:", call_count)
```

```lua
-- Line-by-line tracing
local function line_tracer(event, line)
    if event == "line" then
        local info = debug.getinfo(2, "nS")
        print(string.format("Line %d in %s (%s)",
            line,
            info.name or "main",
            info.short_src))
    end
end

debug.sethook(line_tracer, "l")
-- Code to trace
local x = 1
x = x + 2
debug.sethook()
```

## Examples

```lua
-- Simple instruction counter
local count = 0
debug.sethook(function()
    count = count + 1
    if count % 10000 == 0 then
        print("Instructions: " .. count)
    end
end, "", 100)  -- Check every 100 instructions

for i = 1, 100 do
    local _ = i * i
end

debug.sethook()
print("Total instructions: " .. count)
```

## Related Errors

- [Lua debug error](lua-debug-error) - debug issue
- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua nil call error](lua-nil-call-error) - nil call

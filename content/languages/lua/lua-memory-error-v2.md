---
title: "[Solution] Lua Not Enough Memory Error"
description: "Fix Lua out-of-memory errors. Handle memory allocation failures, optimize table usage, and manage memory in long-running scripts."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `not enough memory` occurs when Lua's memory allocator cannot allocate more memory. This happens when tables, strings, or other objects consume too much memory.

## Common Causes

- Very large table allocations
- String concatenation in loops creating many temporary strings
- Circular references preventing garbage collection
- Too many local variables or closures
- Memory leak in C extensions

## How to Fix

```lua
-- WRONG: String concatenation in loop (creates many temp strings)
local result = ""
for i = 1, 100000 do
    result = result .. i .. ","  -- Memory grows rapidly
end

-- CORRECT: Use table.concat
local parts = {}
for i = 1, 100000 do
    parts[i] = tostring(i)
end
local result = table.concat(parts, ",")
```

```lua
-- WRONG: Large pre-allocated table
local huge = {}
for i = 1, 10000000 do
    huge[i] = i  -- Allocates million entries
end

-- CORRECT: Process in chunks
local chunk_size = 1000
for i = 1, 10000000, chunk_size do
    local chunk = {}
    for j = i, math.min(i + chunk_size - 1, 10000000) do
        chunk[j - i + 1] = j
    end
    process(chunk)
    chunk = nil  -- Allow GC to collect
end
```

```lua
-- WRONG: Not triggering garbage collection
local large_data = {}
for i = 1, 1000000 do
    large_data[i] = string.rep("x", 100)
end
-- large_data still referenced, memory not freed

-- CORRECT: Set reference to nil and collect
large_data = nil
collectgarbage("collect")
```

## Examples

```lua
-- Example 1: Monitor memory usage
local function check_memory()
    local used = collectgarbage("count")
    print(string.format("Memory: %.2f KB", used))
    if used > 100000 then  -- 100MB
        collectgarbage("collect")
        print("After GC: " .. collectgarbage("count") .. " KB")
    end
end

-- Example 2: Memory-efficient iteration
function process_large_file(filename)
    local f = io.open(filename, "r")
    if not f then return end
    
    for line in f:lines() do
        process_line(line)
        -- Line is garbage collected after each iteration
    end
    f:close()
end

-- Example 3: Limit string allocations
local buffer = {}
for i = 1, 1000 do
    buffer[#buffer + 1] = tostring(i)
    if #buffer > 100 then
        io.write(table.concat(buffer, ","))
        buffer = {}
    end
end
```

## Related Errors

- [lua-runtime-error]({{< relref "/languages/lua/lua-runtime-error" >}}) — runtime error
- [lua-coroutine-error]({{< relref "/languages/lua/lua-coroutine-error" >}}) — coroutine error
- [lua-file-error]({{< relref "/languages/lua/lua-file-error" >}}) — file not found

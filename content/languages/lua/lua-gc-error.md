---
title: "[Solution] Lua Garbage Collection Error"
description: "Fix Lua garbage collection errors and memory management issues."
languages: ["lua"]
error-types: ["memory-error"]
severities: ["warning"]
---

Garbage collection errors occur when Lua memory management encounters issues.

## Common Causes

- Excessive memory usage
- Circular references
- GC pressure from many small objects
- Forcing GC too often

## How to Fix

### 1. Monitor memory usage

```lua
local function memUsage()
  local kb = collectgarbage("count")
  return string.format("%.2f MB", kb / 1024)
end
```

### 2. Control garbage collection

```lua
collectgarbage("stop")  -- Disable GC
-- ... critical code ...
collectgarbage("restart")  -- Re-enable GC
collectgarbage("collect")  -- Force collection
```

## Examples

```lua
-- Memory monitoring
local function withMemoryLimit(fn, limitMB)
  collectgarbage("collect")
  local before = collectgarbage("count")
  
  fn()
  
  collectgarbage("collect")
  local after = collectgarbage("count")
  local usedMB = (after - before) / 1024
  
  if usedMB > limitMB then
    print("Warning: Used " .. string.format("%.2f", usedMB) .. " MB")
  end
end
```

## Related Errors

- [Memory limit error](/languages/lua/lua-memory-limit)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Stack overflow error](/languages/lua/lua-stack-overflow)

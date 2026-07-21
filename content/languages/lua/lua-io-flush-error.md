---
title: "[Solution] Lua Io Flush Error"
description: "Fix Lua io.flush errors when flushing file buffers."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Io flush errors occur when io.flush is called incorrectly.

## Common Causes

- Flushing closed file
- Invalid file handle
- Flushing read-only file
- io.flush on output file

## How to Fix

### 1. Check file is open for writing

```lua
local f = io.open(path, "w")
if f then
  f:write(data)
  f:flush()
  f:close()
end
```

### 2. Use pcall for safety

```lua
local function safeFlush(f)
  if f then
    pcall(function() f:flush() end)
  end
end
```

## Examples

```lua
-- Write and flush immediately
local function writeAndFlush(path, data)
  local f, err = io.open(path, "w")
  if f == nil then
    return false, err
  end
  
  f:write(data)
  f:flush()  -- Ensure data is written
  f:close()
  
  return true
end
```

## Related Errors

- [Io write error](/languages/lua/lua-io-write-error)
- [Io open error](/languages/lua/lua-io-open-error)
- [Runtime error](/languages/lua/lua-runtime-error)

---
title: "[Solution] Lua Ltn12 Error"
description: "Fix Lua LTN12 source/sink/pump/filter errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

LTN12 errors occur when using the LTN12 module incorrectly.

## Common Causes

- Wrong source/sink pattern
- Filter not returning values
- Pump error
- Missing ltn12 module

## How to Fix

### 1. Use ltn12 correctly

```lua
local ltn12 = require("ltn12")
local source = ltn12.source.string("Hello")
local sink = ltn12.sink.table({})
```

### 2. Handle pump errors

```lua
local function safePump(source, sink, filter)
  local ok, err = pcall(ltn12.pump.all, source, sink, filter)
  if ok then
    return true
  else
    return false, err
  end
end
```

## Examples

```lua
-- Transform data with LTN12
local ltn12 = require("ltn12")

local source = ltn12.source.string("hello world")
local transformer = ltn12.transformer(function(chunk)
  return chunk:upper()
end)
local result = {}
local sink = ltn12.sink.table(result)

ltn12.pump.all(source, sink, transformer)
print(table.concat(result))  -- "HELLO WORLD"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)
- [Nil value error](/languages/lua/lua-nil-value)

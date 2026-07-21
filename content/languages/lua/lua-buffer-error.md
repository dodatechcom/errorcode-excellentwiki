---
title: "[Solution] Lua Buffer Error"
description: "Fix Lua buffer errors when using string buffers."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Buffer errors occur when string buffer operations fail.

## Common Causes

- Buffer overflow
- Invalid buffer position
- Not enough space
- Buffer too small

## How to Fix

### 1. Check buffer size

```lua
local function safeAppend(buf, data)
  if #buf + #data > MAX_SIZE then
    return false, "Buffer full"
  end
  buf[#buf + 1] = data
  return true
end
```

### 2. Use table as buffer

```lua
local function createBuffer()
  return {}
end

local function appendBuffer(buf, data)
  buf[#buf + 1] = data
end

local function getBuffer(buf)
  return table.concat(buf)
end
```

## Examples

```lua
-- Efficient string building
local buffer = {}
for i = 1, 1000 do
  buffer[#buffer + 1] = "item" .. i
end
local result = table.concat(buffer, ", ")
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Memory error](/languages/lua/lua-memory-limit)
- [Table index error](/languages/lua/lua-table-index-error)

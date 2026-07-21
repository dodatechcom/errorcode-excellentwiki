---
title: "[Solution] Lua Io Read Error"
description: "Fix Lua io.read errors when reading from files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Io read errors occur when reading from files incorrectly.

## Common Causes

- File not opened for reading
- At end of file
- Invalid read argument
- File handle invalid

## How to Fix

### 1. Check file mode

```lua
local f = io.open(path, "r")
if f then
  local content = f:read("*a")
  f:close()
end
```

### 2. Handle EOF gracefully

```lua
local function readLine(f)
  local line = f:read("*l")
  if line == nil then
    return nil  -- EOF
  end
  return line
end
```

## Examples

```lua
-- Read all lines
local function readAllLines(path)
  local lines = {}
  local f = io.open(path, "r")
  if f then
    for line in f:lines() do
      lines[#lines + 1] = line
    end
    f:close()
  end
  return lines
end
```

## Related Errors

- [Io open error](/languages/lua/lua-io-open-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)

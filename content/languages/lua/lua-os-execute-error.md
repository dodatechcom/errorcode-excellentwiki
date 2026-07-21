---
title: "[Solution] Lua Os Execute Error"
description: "Fix Lua os.execute errors when running shell commands."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Os execute errors occur when os.execute fails.

## Common Causes

- Command not found
- Permission denied
- Invalid syntax
- Command returns error

## How to Fix

### 1. Check return value

```lua
local ok, err, code = os.execute(command)
if not ok then
  print("Command failed:", err, code)
end
```

### 2. Use io.popen for output

```lua
local function getCommandOutput(cmd)
  local handle = io.popen(cmd)
  if handle then
    local result = handle:read("*a")
    handle:close()
    return result
  end
  return nil
end
```

## Examples

```lua
-- Safe command execution
local function safeExecute(command)
  local ok, err, code = os.execute(command)
  return {
    success = ok,
    error = err,
    code = code
  }
end

local result = safeExecute("ls -la")
if result.success then
  print("Command succeeded")
else
  print("Error:", result.error)
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Permission denied error](/languages/lua/lua-permission-denied-error)
- [File not found error](/languages/lua/lua-file-not-found-error)

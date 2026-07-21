---
title: "[Solution] Lua Argparse Error"
description: "Fix Lua command-line argument parsing errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Argparse errors occur when parsing command-line arguments incorrectly.

## Common Causes

- Missing required arguments
- Wrong argument type
- Invalid option format
- arg table not available

## How to Fix

### 1. Check arg table exists

```lua
if not arg then
  print("No command line arguments")
  os.exit(1)
end
```

### 2. Parse arguments carefully

```lua
local function parseArgs()
  local args = {}
  local i = 1
  while i <= #arg do
    if arg[i]:sub(1, 2) == "--" then
      local key, value = arg[i]:match("^%-%-(.+)=(.+)$")
      if key then
        args[key] = value
      else
        args[arg[i]:sub(3)] = true
      end
    else
      args[#args + 1] = arg[i]
    end
    i = i + 1
  end
  return args
end
```

## Examples

```lua
-- Simple argument parser
local function getArg(name, default)
  for i = 1, #arg - 1 do
    if arg[i] == name then
      return arg[i + 1]
    end
  end
  return default
end

local verbose = false
for _, a in ipairs(arg) do
  if a == "--verbose" then
    verbose = true
  end
end

print("Verbose:", verbose)
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)

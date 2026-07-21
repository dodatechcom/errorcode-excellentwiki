---
title: "[Solution] Lua Env Variable Error"
description: "Fix Lua environment variable access errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Environment variable errors occur when accessing environment variables incorrectly.

## Common Causes

- Variable not set
- Wrong case (Unix is case-sensitive)
- Using os.getenv incorrectly
- Missing fallback

## How to Fix

### 1. Use os.getenv with default

```lua
local path = os.getenv("PATH") or "/usr/bin"
```

### 2. Check if variable exists

```lua
local function getEnv(name, default)
  local value = os.getenv(name)
  return value or default
end
```

## Examples

```lua
-- Safe environment access
local function requireEnv(name)
  local value = os.getenv(name)
  if value == nil then
    error("Environment variable " .. name .. " not set")
  end
  return value
end

-- Configuration from environment
local config = {
  db_host = os.getenv("DB_HOST") or "localhost",
  db_port = tonumber(os.getenv("DB_PORT") or "5432"),
  debug = os.getenv("DEBUG") == "true"
}
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)
- [Nil value error](/languages/lua/lua-nil-value)

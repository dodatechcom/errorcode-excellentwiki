---
title: "[Solution] Lua Nginx Error"
description: "Fix Lua Nginx/OpenResty errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Nginx errors occur when Lua code runs in Nginx/OpenResty context.

## Common Causes

- API used outside context
- Missing module
- Phase error
- Yield in wrong phase

## How to Fix

### 1. Use correct API for phase

```lua
-- Access phase
ngx.say("Hello from access")

-- Content phase
ngx.say("Hello from content")
```

### 2. Handle errors

```lua
local function safeNginxFn(fn)
  local ok, err = pcall(fn)
  if not ok then
    ngx.log(ngx.ERR, err)
    ngx.exit(500)
  end
end
```

## Examples

```lua
-- OpenResty request handler
local function handleRequest()
  local args = ngx.req.get_uri_args()
  local name = args.name or "World"
  
  ngx.say("Hello, " .. name .. "!")
end

-- With error handling
local function safeHandler()
  local ok, err = pcall(handleRequest)
  if not ok then
    ngx.log(ngx.ERR, "Handler error: ", err)
    ngx.exit(500)
  end
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Yield error](/languages/lua/lua-coroutine-yield-error)
- [Type error](/languages/lua/lua-type-error)

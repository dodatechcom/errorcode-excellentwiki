---
title: "[Solution] Lua Lapis Error"
description: "Fix Lua Lapis web framework errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Lapis errors occur when using the Lapis web framework incorrectly.

## Common Causes

- Missing route
- Template error
- Session error
- Model error

## How to Fix

### 1. Handle route errors

```lua
local app = require("lapis.application")

app:get("/", function(self)
  return { render = "index" }
end)
```

### 2. Handle template errors

```lua
local function renderTemplate(self, template)
  local ok, result = pcall(function()
    return self:render(template)
  end)
  if ok then
    return result
  else
    return "Template error: " .. tostring(result)
  end
end
```

## Examples

```lua
-- Lapis route with error handling
local app = require("lapis.application")
local capture_errors = require("lapis.application").capture_errors

app:get("/user/:id", capture_errors(function(self)
  local user = Users:find(self.params.id)
  if not user then
    return { status = 404, render = "404" }
  end
  return { render = "user", user = user }
end))
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Template error](/languages/lua/lua-template-error)
- [Database error](/languages/lua/lua-database-error)

---
title: "[Solution] Lua Database Error"
description: "Fix Lua database connection errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Database errors occur when database operations fail.

## Common Causes

- Connection refused
- Authentication failed
- Query syntax error
- Table does not exist

## How to Fix

### 1. Handle database connection

```lua
local db = require("luasql.mysql")
local env = db.mysql()
local con = env:connect("database", "user", "password")
```

### 2. Handle query errors

```lua
local function safeQuery(con, sql)
  local cur, err = con:execute(sql)
  if not cur then
    return nil, err
  end
  return cur
end
```

## Examples

```lua
-- Safe database query
local function queryUsers(con)
  local cur, err = con:execute("SELECT * FROM users")
  if not cur then
    return nil, err
  end
  
  local rows = {}
  local row = cur:fetch({}, "a")
  while row do
    rows[#rows + 1] = row
    row = cur:fetch(row, "a")
  end
  
  cur:close()
  return rows
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Connection error](/languages/lua/lua-connection-error)
- [Type error](/languages/lua/lua-type-error)

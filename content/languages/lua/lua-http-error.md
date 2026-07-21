---
title: "[Solution] Lua Http Request Error"
description: "Fix Lua HTTP request errors when making web requests."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

HTTP request errors occur when HTTP operations fail.

## Common Causes

- Connection timeout
- DNS resolution failed
- SSL/TLS error
- Invalid URL

## How to Fix

### 1. Handle request errors

```lua
local http = require("socket.http")
local result, code, headers, status = http.request(url)
if code ~= 200 then
  print("HTTP Error:", code, status)
end
```

### 2. Use timeout

```lua
local ltn12 = require("ltn12")
local result = {}
local res, code = http.request{
  url = url,
  sink = ltn12.sink.table(result),
  timeout = 10
}
```

## Examples

```lua
-- Safe HTTP GET
local function httpGet(url)
  local http = require("socket.http")
  local ltn12 = require("ltn12")
  
  local response = {}
  local res, code, headers, status = http.request{
    url = url,
    sink = ltn12.sink.table(response),
    timeout = 10
  }
  
  if code == 200 then
    return table.concat(response)
  else
    return nil, code, status
  end
end

local body, err = httpGet("https://example.com")
```

## Related Errors

- [Socket error](/languages/lua/lua-socket-error)
- [Timeout error](/languages/lua/lua-timeout-error)
- [Runtime error](/languages/lua/lua-runtime-error)

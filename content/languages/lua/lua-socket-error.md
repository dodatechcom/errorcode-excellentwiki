---
title: "[Solution] Lua Socket Error"
description: "Fix Lua socket library connection errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Socket errors occur when socket operations fail.

## Common Causes

- Connection refused
- Host unreachable
- Timeout
- Invalid address

## How to Fix

### 1. Handle connection errors

```lua
local socket = require("socket")
local conn, err = socket.connect("example.com", 80)
if not conn then
  print("Connection failed:", err)
end
```

### 2. Set timeout

```lua
local sock = socket.tcp()
sock:settimeout(5)  -- 5 second timeout
local ok, err = sock:connect(host, port)
```

## Examples

```lua
-- Safe connection
local function safeConnect(host, port, timeout)
  local sock = socket.tcp()
  sock:settimeout(timeout or 5)
  
  local ok, err = sock:connect(host, port)
  if not ok then
    sock:close()
    return nil, err
  end
  
  return sock
end

local conn, err = safeConnect("example.com", 80)
if conn then
  conn:send("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
  local response = conn:receive("*a")
  conn:close()
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Timeout error](/languages/lua/lua-timeout-error)
- [Connection error](/languages/lua/lua-connection-error)

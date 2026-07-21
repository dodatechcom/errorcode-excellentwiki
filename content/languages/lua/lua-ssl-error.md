---
title: "[Solution] Lua Ssl Error"
description: "Fix Lua SSL/TLS connection errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

SSL errors occur when SSL/TLS connections fail.

## Common Causes

- Certificate verification failed
- Protocol mismatch
- Handshake error
- Missing SSL library

## How to Fix

### 1. Load ssl library

```lua
local ssl = require("ssl")
```

### 2. Handle SSL errors

```lua
local function safeConnect(host, port)
  local sock = socket.tcp()
  local ok, err = sock:connect(host, port)
  if not ok then
    return nil, err
  end
  
  local sslsock, err = ssl.wrap(sock, {
    mode = "client",
    protocol = "tlsv1_2",
    verify = "none"
  })
  
  if not sslsock then
    sock:close()
    return nil, err
  end
  
  return sslsock
end
```

## Examples

```lua
-- HTTPS request
local function httpsGet(host, path)
  local socket = require("socket")
  local ssl = require("ssl")
  
  local sock = socket.tcp()
  sock:connect(host, 443)
  
  local sslsock = ssl.wrap(sock, {
    mode = "client",
    protocol = "tlsv1_2",
    verify = "none"
  })
  
  sslsock:dohandshake()
  sslsock:send("GET " .. path .. " HTTP/1.1\r\nHost: " .. host .. "\r\n\r\n")
  
  local response = sslsock:receive("*a")
  sslsock:close()
  
  return response
end
```

## Related Errors

- [Socket error](/languages/lua/lua-socket-error)
- [Connection error](/languages/lua/lua-connection-error)
- [Runtime error](/languages/lua/lua-runtime-error)

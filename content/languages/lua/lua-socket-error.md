---
title: "[Solution] Lua Socket Connect Send Failed Error Fix"
description: "Fix Lua socket connection and send errors. Learn why luasocket operations fail and how to handle network errors properly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Lua socket error occurs when the luasocket library fails during network operations such as connecting to a remote host, sending data, or receiving responses. The error typically includes a system-level error message like "connection refused", "host unreachable", or "timeout".

## Why It Happens

- The remote host is unreachable or the port is not open
- DNS resolution fails for the hostname
- The connection times out before completing
- The remote server closes the connection unexpectedly
- Firewall rules block outgoing or incoming traffic
- The socket is used after being closed
- Network interface is down or disconnected
- Too many concurrent connections exhaust system resources

## How to Fix It

### Check connection return values

```lua
-- WRONG: Not checking connect result
local socket = require("socket")
local conn = socket.tcp()
conn:connect("example.com", 80)
conn:send("GET / HTTP/1.1\r\n")  -- may fail

-- CORRECT: Validate each step
local socket = require("socket")
local conn = socket.tcp()
conn:settimeout(5)
local ok, err = conn:connect("example.com", 80)
if not ok then
    print("Connection failed: " .. tostring(err))
    conn:close()
    return
end
```

### Set appropriate timeouts

```lua
-- WRONG: No timeout, may block forever
local conn = socket.tcp()
conn:connect("slow-server.com", 8080)  -- blocks indefinitely

-- CORRECT: Set connection and receive timeouts
local conn = socket.tcp()
conn:settimeout(10)  -- 10 second timeout
local ok, err = conn:connect("slow-server.com", 8080)
if not ok then
    if err == "timeout" then
        print("Connection timed out")
    else
        print("Connection error: " .. err)
    end
end
```

### Handle partial sends correctly

```lua
-- WRONG: Assuming send completes in one call
local sent = conn:send("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

-- CORRECT: Handle partial sends in a loop
local function sendAll(conn, data)
    local totalSent = 0
    while totalSent < #data do
        local sent, err, partial = conn:send(data, totalSent + 1)
        if not sent then
            return nil, err, partial
        end
        totalSent = totalSent + sent
    end
    return totalSent
end
```

### Use protected calls for network operations

```lua
-- WRONG: Network errors crash the program
local resp = conn:receive("*a")

-- CORRECT: Wrap in pcall
local ok, data, err = pcall(function()
    return conn:receive("*a")
end)
if not ok then
    print("Receive failed: " .. tostring(data))
end
```

### Close sockets properly with error handling

```lua
-- WRONG: No cleanup on error
local conn = socket.tcp()
conn:connect(host, port)
conn:send(data)  -- if this fails, socket leaks

-- CORRECT: Use pcall for cleanup
local conn = socket.tcp()
local ok, err = pcall(function()
    conn:settimeout(5)
    conn:connect(host, port)
    conn:send(data)
    local response = conn:receive("*a")
    conn:close()
    return response
end)
if not ok then
    conn:close()
    print("Socket error: " .. tostring(err))
end
```

## Common Mistakes

- Not setting a timeout, causing the script to hang on unreachable hosts
- Assuming `socket.select` returns immediately without checking readiness
- Using a closed socket without checking `conn:connect` status first
- Not handling DNS resolution failures separately from connection failures
- Forgetting that `send` may only send part of the data and must be retried

## Related Pages

- [Lua I/O Error](lua-io-error) - file I/O errors
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Runtime Error](lua-runtime-error) - general runtime issue

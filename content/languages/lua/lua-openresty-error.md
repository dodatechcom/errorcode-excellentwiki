---
title: "[Solution] OpenResty Lua Nginx Module Error Fix"
description: "Fix OpenResty and lua-nginx-module errors. Learn why OpenResty Lua code fails and how to debug nginx Lua integration issues."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An OpenResty error occurs when Lua code running inside the lua-nginx-module encounters a problem during request processing. OpenResty embeds LuaJIT into nginx, creating a unique execution environment with APIs like `ngx.say`, `ngx.req`, and shared dictionaries. Errors in this environment differ from standard Lua errors because they execute within nginx's event loop.

## Why It Happens

- Using Lua standard library functions that are not allowed in OpenResty contexts
- Yielding from a phase that does not support coroutines
- Accessing `ngx.*` APIs outside of a request context
- Shared dictionary (`ngx.shared`) operations fail due to memory limits or key issues
- DNS resolution fails in `ngx.socket` operations
- A timer created with `ngx.timer` fails to start
- Request body was already consumed before `ngx.req.read_body()`

## How to Fix It

### Respect phase restrictions for ngx APIs

```lua
-- WRONG: Using request-phase API in init_worker
init_worker_by_lua_block {
    ngx.say("hello")  -- error: not in request context
}

-- CORRECT: Use appropriate phase
init_worker_by_lua_block {
    -- Use timer for work outside request context
    local function do_work(premature)
        -- background work here
    end
    ngx.timer.at(0, do_work)
}

server_by_lua_block {
    ngx.say("hello")  -- correct in request phase
}
```

### Handle shared dictionary memory limits

```lua
-- WRONG: Assuming shared dict has unlimited space
local dict = ngx.shared.mydict
for i = 1, 1000000 do
    dict:set("key" .. i, "value")  -- may fail: memory limit
end

-- CORRECT: Check dict capacity and handle eviction
local dict = ngx.shared.mydict
local capacity = dict:capacity()
local free_space = capacity - dict:free_space()
if free_space < 1024 then
    ngx.log(ngx.WARN, "Shared dict nearly full")
end
dict:set("key", "value", 30)  -- set with TTL for auto-cleanup
```

### Read request body before accessing it

```lua
-- WRONG: Accessing body before reading
server_by_lua_block {
    local body = ngx.req.get_body_data()  -- nil
}

-- CORRECT: Read body first
server_by_lua_block {
    ngx.req.read_body()
    local body = ngx.req.get_body_data()
    if not body then
        local file = ngx.req.get_body_file()
        -- read from file instead
    end
}
```

### Use cosocket for non-blocking network I/O

```lua
-- WRONG: Blocking I/O in nginx worker
server_by_lua_block {
    local socket = require("socket")
    local conn = socket.connect("api.example.com", 80)  -- blocks!
}

-- CORRECT: Use OpenResty cosocket
server_by_lua_block {
    local sock = ngx.socket.tcp()
    sock:settimeout(5000)
    local ok, err = sock:connect("api.example.com", 80)
    if not ok then
        ngx.status = 502
        ngx.say("Backend unavailable")
        return ngx.exit(502)
    end
    sock:send("GET /api HTTP/1.1\r\nHost: api.example.com\r\n\r\n")
    local data = sock:receive("*a")
    sock:close()
    ngx.say(data)
}
```

### Handle errors in timer callbacks

```lua
-- WRONG: Timer callback crashes silently
init_worker_by_lua_block {
    ngx.timer.at(1, function(premature)
        error("something failed")  -- silent failure
    end)
}

-- CORRECT: Handle timer errors properly
init_worker_by_lua_block {
    ngx.timer.at(1, function(premature)
        if premature then return end
        local ok, err = pcall(function()
            error("something failed")
        end)
        if not ok then
            ngx.log(ngx.ERR, "Timer error: ", err)
        end
    end)
}
```

## Common Mistakes

- Using `require` for modules that access the filesystem in an unsafe way during nginx startup
- Not understanding that `ngx.exit` does not immediately stop Lua code execution in all phases
- Using `ngx.sleep` in phases that do not yield (like `init_worker_by_lua` for some operations)
- Forgetting that `ngx.location.capture` is not available with `rewrite_by_lua` subrequests
- Not setting `lua_package_path` correctly so OpenResty cannot find Lua modules

## Related Pages

- [Lua Socket Error](lua-socket-error) - network operation failures
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua GC Error](lua-gc-error) - memory limit issues
- [Lua Stack Overflow](lua-stack-overflow) - recursion too deep

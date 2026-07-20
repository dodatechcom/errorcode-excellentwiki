---
title: "[Solution] Lua Multiple Return Value Error Fix"
description: "Fix Lua multiple return value errors when functions return unexpected numbers of values."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1142
---

## What This Error Means

A multiple return value error occurs when a function returns more or fewer values than expected, or when return values are incorrectly captured or discarded.

## Common Causes

- Calling a function in scalar context when it returns multiple values
- Discarding additional return values unintentionally
- Calling a function in an expression captures only the first return

## How to Fix

```lua
function get_user()
    return "Alice", 30, "alice@example.com"
end

local name, age = get_user()  -- Missing third return
print(email)  -- nil

local name, age, email = get_user()  -- All captured
```

```lua
function test()
    return 1, 2, 3
end

local t = {test()}     -- {1, 2, 3}
local x = test()        -- 3 (last in scalar, first in Lua 5.0)
local x = (test())     -- 1 (expression captures first only)
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua nil error](lua-nil-error) - nil error
- [Lua type error](lua-type-error) - type issue

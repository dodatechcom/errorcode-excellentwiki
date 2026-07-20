---
title: "[Solution] Lua Upvalue Closure Error Fix"
description: "Fix Lua upvalue errors when closures capture outer local variables."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1143
---

## What This Error Means

An upvalue error occurs when closures capture local variables (upvalues) and the expected value differs from actual. Common issues include loop variable capture and shared mutable state.

## Common Causes

- Loop variable captured by reference (all closures share same variable)
- Upvalue modified after closure creation
- Closure outliving its defining scope

## How to Fix

```lua
local funcs = {}
for i = 1, 5 do
    funcs[i] = function() return i end
end
print(funcs[1]())  -- May be 6 in Lua 5.1/LuaJIT, 1 in Lua 5.2+

local funcs = {}
for i = 1, 5 do
    do
        local j = i
        funcs[i] = function() return j end
    end
end
print(funcs[1]())  -- 1
```

```lua
local counter = 0
local fn = function() counter = counter + 1 return counter end
print(fn())  -- 1
counter = 100
print(fn())  -- 101 (upvalue reflects external change)
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua global error](lua-global-error) - global issue
- [Lua nil error](lua-nil-error) - nil error

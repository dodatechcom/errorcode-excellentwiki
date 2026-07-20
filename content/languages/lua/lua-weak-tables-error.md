---
title: "[Solution] Lua Weak Table Reference Error Fix"
description: "Fix Lua weak table errors when using weak references for caches and object tracking."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1120
---

## What This Error Means

A weak table error occurs when using the __mode metatable field incorrectly. Weak tables allow keys, values, or both to be collected by the GC, but misconfiguration leads to unexpected data loss or memory leaks.

## Common Causes

- Setting __mode to "k" (weak keys) when "v" (weak values) is needed
- Forgetting to set __mode before populating the table
- Using weak keys with literal values (strings/numbers) which are never collected
- Expecting weak table entries to persist after the only strong reference is removed
- Confusing weak keys with weak values semantics

## How to Fix

```lua
-- WRONG: Using weak keys for literal strings
local cache = setmetatable({}, { __mode = "k" })
cache["key"] = "value"  -- Strings are never collected as keys!

-- CORRECT: Use weak keys with table keys
local cache = setmetatable({}, { __mode = "k" })
local key = {}
cache[key] = "expensive data"
-- When 'key' goes out of scope, the entry can be collected
```

```lua
-- WRONG: Setting __mode after populating the table
local cache = {}
cache[{}] = "data"
setmetatable(cache, { __mode = "k" })  -- Too late for existing entries

-- CORRECT: Set __mode before adding entries
local cache = setmetatable({}, { __mode = "k" })
cache[{}] = "data"
```

```lua
-- WRONG: Confusing weak keys vs weak values
-- Weak keys: entry removed when KEY is collected
-- Weak values: entry removed when VALUE is collected

-- Weak keys (for caches keyed by objects):
local obj_cache = setmetatable({}, { __mode = "k" })
local widget = {}
obj_cache[widget] = computed_value
-- Removed when 'widget' is collected

-- Weak values (for object registries):
local registry = setmetatable({}, { __mode = "v" })
registry["id1"] = create_object()
-- Removed when the object has no other references
```

```lua
-- Both weak keys and weak values
local weak_both = setmetatable({}, { __mode = "kv" })
```

```lua
-- Practical weak table example
local pending_tasks = setmetatable({}, { __mode = "k" })

function schedule_task(task_fn)
    local task = { fn = task_fn }
    pending_tasks[task] = true
    return task
end

function run_pending()
    for task in pairs(pending_tasks) do
        task.fn()
    end
end

local t = schedule_task(function() print("done") end)
t = nil  -- Task will be GC'd since only weak ref remains
collectgarbage()
print(next(pending_tasks) == nil)  -- true
```

## Examples

```lua
-- Object property cache with weak references
local prop_cache = setmetatable({}, { __mode = "k" })

function get_property(obj, prop)
    if not prop_cache[obj] then
        prop_cache[obj] = {}
    end
    if prop_cache[obj][prop] == nil then
        prop_cache[obj][prop] = compute_property(obj, prop)
    end
    return prop_cache[obj][prop]
end
```

## Related Errors

- [Lua GC error](lua-gc-error) - GC issue
- [Lua memory error](lua-memory-error) - memory issue
- [Lua metatable error](lua-metatable-error) - metatable issue

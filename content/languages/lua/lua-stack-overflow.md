---
title: "[Solution] Lua Stack Overflow Recursion Too Deep Fix"
description: "Fix Lua stack overflow errors from deep recursion. Learn why recursion overflows the stack and how to implement tail calls."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Lua stack overflow error occurs when a script exceeds the maximum call stack depth. This typically happens with infinite or very deep recursion. Lua has a limited call stack size (default around 200 levels, configurable with `luajit-lua53` or `luaL_checkstack`). Each function call adds a frame to the stack, and when it fills up, Lua raises a stack overflow error.

## Why It Happens

- Infinite recursion from a function calling itself without a proper base case
- Mutual recursion between two or more functions without termination
- Deep recursive traversal of nested data structures
- Event handlers or callbacks that trigger each other in a loop
- Metamethods (`__index`, `__newindex`) that trigger themselves recursively
- Missing base case in tree traversal algorithms

## How to Fix It

### Add proper base cases to recursive functions

```lua
-- WRONG: No base case causes infinite recursion
local function factorial(n)
    return n * factorial(n - 1)  -- stack overflow
end

-- CORRECT: Include a base case
local function factorial(n)
    if n <= 1 then return 1 end
    return n * factorial(n - 1)
end
```

### Convert recursion to iteration for deep structures

```lua
-- WRONG: Recursive traversal of deep tree
local function traverse(node)
    for _, child in ipairs(node.children or {}) do
        traverse(child)  -- deep trees overflow
    end
end

-- CORRECT: Use an explicit stack to avoid recursion
local function traverse(root)
    local stack = { root }
    while #stack > 0 do
        local node = table.remove(stack)
        for _, child in ipairs(node.children or {}) do
            stack[#stack + 1] = child
        end
    end
end
```

### Use tail calls for recursive algorithms

```lua
-- WRONG: Non-tail-recursive call consumes stack
local function sum(n, acc)
    if n == 0 then return acc end
    return sum(n - 1, acc + n)  -- not tail call if arithmetic follows
end

-- CORRECT: Tail-recursive form (optimized by Lua)
local function sum(n, acc)
    acc = acc or 0
    if n == 0 then return acc end
    return sum(n - 1, acc + n)  -- Lua optimizes this
end
```

### Use an explicit stack for DFS traversals

```lua
-- WRONG: Recursive DFS on a graph with cycles
local function dfs(node, visited)
    visited[node] = true
    for _, neighbor in ipairs(node.neighbors) do
        if not visited[neighbor] then
            dfs(neighbor, visited)  -- cycles or deep graphs overflow
        end
    end
end

-- CORRECT: Iterative DFS with explicit stack
local function dfs(start)
    local visited = {}
    local stack = { start }
    while #stack > 0 do
        local node = table.remove(stack)
        if not visited[node] then
            visited[node] = true
            for _, neighbor in ipairs(node.neighbors) do
                if not visited[neighbor] then
                    stack[#stack + 1] = neighbor
                end
            end
        end
    end
end
```

### Increase stack size if needed

```lua
-- For LuaJIT or custom builds, you can increase the limit
-- In C API: luaL_checkstack(L, n, "message")
-- In Lua: not directly configurable, but you can restructure code

-- Use coroutine to get a fresh stack
local co = coroutine.create(function()
    deepRecursion()
end)
coroutine.resume(co)
```

## Common Mistakes

- Forgetting that mutual recursion also consumes stack space
- Not realizing that Lua tail calls are optimized but only when they are truly in tail position
- Using `error()` inside deeply recursive functions, which adds extra stack frames during error propagation
- Assuming Lua's default stack size is sufficient for all use cases
- Not considering that anonymous functions in closures still consume stack frames

## Related Pages

- [Lua Coroutine Error](lua-coroutine-error) - coroutine resume failure
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Runtime Error](lua-runtime-error) - general runtime issue

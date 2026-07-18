---
title: "[Solution] Lua String Concatenate Nil Error Fix"
description: "Fix Lua 'attempt to concatenate nil value' errors. Learn why string concatenation fails with nil and how to prevent it."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The `attempt to concatenate nil value` error in Lua occurs when you use the `..` concatenation operator with a `nil` operand. Lua requires both sides of the concatenation operator to be strings or numbers. When a `nil` value appears on either side, the runtime raises this error.

## Why It Happens

- A variable used in string concatenation was never assigned a value
- A function returned `nil` instead of a string
- A table field accessed during concatenation contained `nil`
- An optional parameter was not provided and defaulted to `nil`
- A database query returned `nil` for a field that was later concatenated into a message
- A variable was accidentally set to `nil` through incorrect logic

## How to Fix It

### Convert nil to a safe string before concatenation

```lua
-- WRONG: Variable may be nil
local user = getUser(42)
local msg = "Hello, " .. user.name  -- nil concatenation

-- CORRECT: Provide a fallback for nil
local user = getUser(42)
local name = user and user.name or "Guest"
local msg = "Hello, " .. name
```

### Use tostring to handle nil safely

```lua
-- WRONG: Direct concatenation of potentially nil value
local value = config.get("timeout")
local info = "Timeout: " .. value  -- crashes if nil

-- CORRECT: Use tostring and nil guard
local value = config.get("timeout")
local info = "Timeout: " .. tostring(value or "N/A")
```

### Validate function return values

```lua
-- WRONG: Assuming function returns a string
local data = fetchData()
local output = "Result: " .. data  -- nil crash

-- CORRECT: Validate before concatenating
local data = fetchData()
if data ~= nil then
    local output = "Result: " .. tostring(data)
    print(output)
else
    print("Result: no data available")
end
```

### Use string.format for type-safe concatenation

```lua
-- WRONG: Concatenation chain with nil risk
local name = profile.name
local age = profile.age
local bio = name .. " is " .. age .. " years old"  -- nil risk

-- CORRECT: Use string.format with defaults
local name = profile.name or "Unknown"
local age = profile.age or 0
local bio = string.format("%s is %d years old", name, age)
```

### Protect table-driven string building

```lua
-- WRONG: Building a string from table fields
local parts = {}
for i = 1, #items do
    parts[i] = items[i].label  -- label may be nil
end
local result = table.concat(parts, ", ")  -- nil in parts

-- CORRECT: Filter nil values before concatenation
local parts = {}
for i = 1, #items do
    if items[i].label then
        parts[#parts + 1] = items[i].label
    end
end
local result = table.concat(parts, ", ")
```

## Common Mistakes

- Forgetting that `table.remove` does not shift indices, leaving gaps that produce `nil` during iteration
- Not checking whether `ipairs` has stopped early due to a `nil` hole in an array-like table
- Using `..` in a loop where one iteration produces `nil` and breaks the entire chain
- Assuming JSON-decoded data will always have all expected keys present
- Concatenating a boolean value, which Lua does not auto-coerce to string with `..`

## Related Pages

- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Argument Type Error](lua-argument-type-error) - wrong argument type
- [Lua I/O Error](lua-io-error) - file read/write failure

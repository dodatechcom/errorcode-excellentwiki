---
title: "[Solution] Lua string.format Format String Error Fix"
description: "Fix Lua string.format errors when using format specifiers for string formatting."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1138
---

## What This Error Means

A string.format error occurs when using printf-style format specifiers with mismatched argument types or invalid format strings. Lua's string.format follows C printf conventions.

## Common Causes

- Mismatched format specifiers and argument types (%d expects number, %s expects string)
- Missing or extra arguments for format specifiers
- Using %f for floating point when integer is expected
- Locale issues with %f formatting (comma vs period)
- Not enough precision specifiers for large numbers

## How to Fix

```lua
-- WRONG: Type mismatch
local name = "Alice"
print(string.format("Age: %d", name))  -- %d expects number, got string

-- CORRECT: Use matching specifiers
print(string.format("Name: %s, Age: %d", name, 30))
```

```lua
-- WRONG: Missing arguments
print(string.format("%s is %d years old", "Alice"))  -- Missing age

-- CORRECT: Match arguments to specifiers
print(string.format("%s is %d years old", "Alice", 30))
```

```lua
-- WRONG: Too many arguments
print(string.format("Hello %s", "world", "extra"))  -- Extra arg ignored

-- CORRECT: Exact number of arguments
print(string.format("Hello %s", "world"))
```

```lua
-- WRONG: Floating point precision issues
print(string.format("%f", math.pi))  -- 3.141593 (6 decimal places)

-- CORRECT: Control precision
print(string.format("%.2f", math.pi))  -- 3.14
print(string.format("%.10f", math.pi)) -- 3.1415926536
```

```lua
-- Format specifier flags
print(string.format("%10s", "hi"))     -- Right-aligned: "        hi"
print(string.format("%-10s", "hi"))    -- Left-aligned: "hi        "
print(string.format("%010d", 42))      -- Zero-padded: "0000000042"
print(string.format("%+d", 42))        -- With sign: "+42"
print(string.format("% d", 42))        -- Space before: " 42"
```

## Examples

```lua
local function pad_number(n, width)
    return string.format("%0" .. width .. "d", n)
end

print(pad_number(5, 3))   -- "005"
print(pad_number(123, 5)) -- "00123"

local function format_currency(amount)
    return string.format("$%.2f", amount)
end

print(format_currency(19.9))  -- "$19.90"
```

## Related Errors

- [Lua string error](lua-string-error) - string issue
- [Lua type error](lua-type-error) - type issue
- [Lua runtime error](lua-runtime-error) - runtime issue

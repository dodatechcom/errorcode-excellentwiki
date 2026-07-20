---
title: "[Solution] Lua io.read / io.write I/O Error Fix"
description: "Fix Lua io.read and io.write I/O errors for terminal input and output."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1126
---

## What This Error Means

An I/O error occurs when using io.read or io.write for standard input/output operations. Common issues include reading nil when input is exhausted, format string mismatches, or writing to closed files.

## Common Causes

- Calling io.read with wrong format specifiers
- Reading from stdin when no input is available (nil return)
- Using io.write instead of print for formatted output
- Forgetting to convert numbers to strings for io.write
- Mixing io.read with other I/O operations on the same handle

## How to Fix

```lua
-- WRONG: io.read format specifier error
local line = io.read("*line")  -- *l is correct, not *line
-- Correct format specifiers: "*l" (line), "*a" (all), "*n" (number)

-- CORRECT: Use correct format specifiers
local line = io.read("*l")    -- Read one line
local all  = io.read("*a")    -- Read entire stdin
local num  = io.read("*n")    -- Read a number
```

```lua
-- WRONG: Not checking for nil input
local name = io.read()
-- When stdin is closed, name is nil
print("Hello, " .. name)  -- Error if name is nil

-- CORRECT: Check return value
local name = io.read()
if name then
    name = name:gsub("\n", "")
    print("Hello, " .. name)
else
    print("No input provided")
end
```

```lua
-- WRONG: io.write requires explicit string conversion
local value = 42
io.write(value)        -- Error: bad argument #1 to 'write' (expected string)
io.write(value, "\n")  -- Still an error

-- CORRECT: Convert to string
io.write(tostring(value), "\n")
io.write("Value: " .. value .. "\n")
```

```lua
-- WRONG: Using io.write vs print
io.write("Hello\n")  -- No formatting, no tab conversion
print("Hello")       -- Adds newline automatically

-- io.write is useful for binary data
io.write(string.char(0x48, 0x65, 0x6C, 0x6C, 0x6F))
```

```lua
-- Safe interactive input
print("Enter your name:")
local name = io.read()
while not name or name == "" do
    print("Please enter a valid name:")
    name = io.read()
end
name = name:match("^%s*(.-)%s*$")  -- Trim whitespace
print("Hello, " .. name .. "!")
```

## Examples

```lua
-- Simple interactive calculator
print("Enter first number:")
local a = tonumber(io.read())
print("Enter second number:")
local b = tonumber(io.read())
if a and b then
    io.write(string.format("Sum: %d\n", a + b))
else
    io.write("Invalid input\n")
end
```

## Related Errors

- [Lua IO error](lua-io-error) - IO issue
- [Lua file error](lua-file-error) - file issue
- [Lua runtime error](lua-runtime-error) - runtime issue

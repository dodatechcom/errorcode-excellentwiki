---
title: "[Solution] Lua String Format Error"
description: "Fix Lua string.format errors when format specifiers are incorrect."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String format errors occur when format specifiers in string.format don't match arguments.

## Common Causes

- Mismatched format specifiers
- Wrong number of arguments
- Invalid format character
- Missing type conversion

## How to Fix

### 1. Match specifiers to arguments

```lua
local function safeFormat(fmt, ...)
  local args = {...}
  local count = 0
  for _ in fmt:gmatch("%%.") do
    count = count + 1
  end
  assert(count == #args, "Argument count mismatch")
  return string.format(fmt, ...)
end
```

### 2. Use correct format codes

```lua
local name = "Alice"
local age = 30
print(string.format("Name: %s, Age: %d", name, age))
```

## Examples

```lua
-- Correct format
print(string.format("Pi is %.2f", math.pi))

-- Padding
print(string.format("%10s", "hello"))

-- Number formatting
print(string.format("%05d", 42))
```

## Related Errors

- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)

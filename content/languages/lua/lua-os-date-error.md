---
title: "[Solution] Lua Os Date Error"
description: "Fix Lua os.date errors when formatting dates."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Os date errors occur when os.date format string is incorrect.

## Common Causes

- Invalid format specifier
- Wrong argument order
- Missing time argument
- Format string error

## How to Fix

### 1. Use correct format codes

```lua
local now = os.date("%Y-%m-%d %H:%M:%S")
print(now)
```

### 2. Use table format

```lua
local date = os.date("*t")
print(date.year, date.month, date.day)
```

## Examples

```lua
-- Common formats
local formats = {
  iso = os.date("%Y-%m-%dT%H:%M:%S"),
  us = os.date("%m/%d/%Y"),
  eu = os.date("%d/%m/%Y"),
  time = os.date("%H:%M:%S")
}

for name, fmt in pairs(formats) do
  print(name .. ":", fmt)
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [String format error](/languages/lua/lua-string-format-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)

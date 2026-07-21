---
title: "[Solution] Lua Os Time Error"
description: "Fix Lua os.time errors when working with timestamps."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Os time errors occur when os.time is used incorrectly.

## Common Causes

- Invalid date table
- Missing date argument
- os.time with wrong format
- Year/month out of range

## How to Fix

### 1. Use os.time correctly

```lua
local now = os.time()
print(now)  -- Unix timestamp
```

### 2. Convert timestamp to date

```lua
local dateTable = os.date("*t", now)
print(dateTable.year, dateTable.month, dateTable.day)
```

## Examples

```lua
-- Time difference
local startTime = os.time()
-- ... do work ...
local endTime = os.time()
local elapsed = difftime(endTime, startTime)
print("Elapsed:", elapsed, "seconds")

-- Custom date
local customDate = os.time({year=2024, month=12, day=25})
print(os.date("%Y-%m-%d", customDate))
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)

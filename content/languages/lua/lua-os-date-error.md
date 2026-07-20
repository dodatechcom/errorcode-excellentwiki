---
title: "[Solution] Lua os.date Format Error Fix"
description: "Fix Lua os.date formatting errors when working with dates and times."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1129
---

## What This Error Means

An os.date error occurs when formatting date/time strings or converting timestamps. Common issues include invalid format strings, wrong argument types, or confusion about os.date vs os.time.

## Common Causes

- Invalid format specifiers in the format string
- Passing a timestamp that is out of range
- Confusing os.date (formats) with os.time (creates timestamps)
- Not handling nil returns for non-existent dates
- Timezone and locale differences

## How to Fix

```lua
-- WRONG: Invalid format specifier
print(os.date("%x %Y-%m-%d %H:%M:%S"))  -- %x is a valid specifier
print(os.date("%Y-%m-%d %H:%M:%S"))     -- Full format

-- CORRECT: Use valid format specifiers
print(os.date("%Y-%m-%d"))               -- 2024-01-15
print(os.date("%H:%M:%S"))               -- 14:30:00
print(os.date("%a, %d %b %Y"))           -- Mon, 15 Jan 2024
```

```lua
-- WRONG: Passing a string instead of a number
local timestamp = os.time()
print(os.date("%Y", "now"))  -- Error: bad argument #2

-- CORRECT: Pass numeric timestamp or nothing
print(os.date("%Y"))              -- Current year
print(os.date("%Y", timestamp))   -- Same
print(os.date("%Y", os.time()))   -- Same
```

```lua
-- WRONG: os.time returns a table, not a formatted string
local t = os.time()
print(t)  -- Unix timestamp (number)

-- os.date returns a table when no format is given
local t = os.date("*t")
print(t.year)    -- 2024
print(t.month)   -- 1
print(t.day)     -- 15
```

```lua
-- WRONG: Non-existent date
local t = os.time({ year = 2024, month = 2, day = 30 })  -- Feb 30 doesn't exist
print(t)  -- nil

-- CORRECT: Check if date is valid
local function valid_date(year, month, day)
    local t = os.time({ year = year, month = month, day = day })
    return t ~= nil
end

print(valid_date(2024, 2, 29))  -- true (leap year)
print(valid_date(2023, 2, 29))  -- false
```

```lua
-- Date arithmetic
local function add_days(timestamp, days)
    return timestamp + (days * 86400)  -- 24 * 60 * 60
end

local today = os.time()
local tomorrow = add_days(today, 1)
print(os.date("%Y-%m-%d", today))     -- Today
print(os.date("%Y-%m-%d", tomorrow))  -- Tomorrow
```

## Examples

```lua
local function format_timestamp(ts)
    if not ts then ts = os.time() end
    return os.date("%Y-%m-%d %H:%M:%S", ts)
end

local function parse_date(str)
    local y, m, d = str:match("(%d+)-(%d+)-(%d+)")
    if y and m and d then
        return os.time({ year = y, month = m, day = d })
    end
    return nil
end

print("Now:", format_timestamp())
print("Parsed:", format_timestamp(parse_date("2024-12-25")))
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua type error](lua-type-error) - type issue
- [Lua nil error](lua-nil-error) - nil error

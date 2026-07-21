---
title: "[Solution] Lua String Reverse Error"
description: "Fix Lua string.reverse errors when reversing strings."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String reverse errors occur when string.reverse is called on non-strings.

## Common Causes

- Non-string input
- Empty string handling
- Multibyte character issues
- Missing argument

## How to Fix

### 1. Validate input

```lua
local function safeReverse(s)
  if type(s) ~= "string" then return "" end
  return string.reverse(s)
end
```

### 2. Use correctly

```lua
local s = "Hello"
print(string.reverse(s))  -- "olleH"
```

## Examples

```lua
-- Palindrome check
local function isPalindrome(s)
  local reversed = string.reverse(s)
  return s == reversed
end

print(isPalindrome("racecar"))  -- true
print(isPalindrome("hello"))    -- false
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)

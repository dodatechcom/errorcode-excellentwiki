---
title: "[Solution] Lua Random Error"
description: "Fix Lua random number generation errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Random errors occur when generating random numbers.

## Common Causes

- Wrong range
- Non-integer where integer expected
- Missing randomseed
- Distribution error

## How to Fix

### 1. Seed random properly

```lua
math.randomseed(os.time())
```

### 2. Generate correct range

```lua
-- Random integer in range [min, max]
local function randInt(min, max)
  return math.random(min, max)
end

-- Random float in range [0, 1)
local function randFloat()
  return math.random()
end
```

## Examples

```lua
-- Random number utilities
math.randomseed(os.time())

-- Random integer
local function randInt(min, max)
  return math.random(min, max)
end

-- Random element from table
local function randElement(t)
  return t[math.random(#t)]
end

-- Shuffle table
local function shuffle(t)
  for i = #t, 2, -1 do
    local j = math.random(i)
    t[i], t[j] = t[j], t[i]
  end
  return t
end

print(randInt(1, 100))
print(randElement({"a", "b", "c"}))
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)

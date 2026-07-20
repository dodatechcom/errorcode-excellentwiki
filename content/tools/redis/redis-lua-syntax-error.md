---
title: "[Solution] Redis Lua Syntax Error"
description: "How to fix Redis Lua script syntax errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Invalid Lua syntax in script
- Missing or extra parentheses/brackets
- Incorrect use of redis.call() or redis.pcall()

## Fix

Validate Lua syntax offline:

```bash
luac -p script.lua
```

Common Lua syntax issues:

```lua
-- Wrong: missing 'local' keyword for local variables
result = redis.call('GET', KEYS[1])  -- will pollute global scope

-- Correct:
local result = redis.call('GET', KEYS[1])
```

Use redis-cli to test script:

```bash
redis-cli EVAL "return 1+1" 0
```

## Examples

```bash
# Test simple script
redis-cli EVAL "return redis.call('PING')" 0

# Test syntax
redis-cli EVAL "
  local x = 1
  local y = 2
  return x + y
" 0

# Find syntax error in log
redis-cli CLIENT LOG GET
```

---
title: "[Solution] Redis Lua Script Wrong Number of Arguments"
description: "How to fix Redis Lua script errors when wrong number of arguments is provided"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Number of KEYS does not match declared count in EVAL
- ARGV count mismatch
- Script expects different argument count

## Fix

Check the EVAL call:

```bash
# KEYS count must match the number passed after script
redis-cli EVAL "return KEYS[1]" 1 mykey
# Correct: 1 KEYS argument

# Wrong: passing 2 keys when script expects 1
redis-cli EVAL "return KEYS[1]" 1 key1 key2  # Wrong!
redis-cli EVAL "return KEYS[1] .. KEYS[2]" 2 key1 key2  # Correct
```

Validate in script:

```lua
if #KEYS ~= 2 then
    return {err = "Expected 2 keys"}
end
```

## Examples

```bash
# Correct usage
redis-cli EVAL "return {KEYS[1], ARGV[1]}" 1 mykey myvalue

# Wrong usage (will error)
redis-cli EVAL "return {KEYS[1], KEYS[2]}" 1 key1 key2

# Fix: specify correct KEYS count
redis-cli EVAL "return {KEYS[1], KEYS[2]}" 2 key1 key2
```

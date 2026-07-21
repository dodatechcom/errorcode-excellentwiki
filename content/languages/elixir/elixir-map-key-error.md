---
title: "[Solution] Elixir Map Key Error -- Accessing Missing Map Keys"
description: "Fix Elixir map key errors when accessing map keys that do not exist using dot notation."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Map Key Error

This error occurs when you access a key in a map that does not exist using the `map.key` syntax.

## Common Causes

- Key was never set in the map
- Typo in key name (atom keys are case-sensitive)
- Using dot notation where `map[:key]` returns nil
- Passing a struct where a plain map was expected

## How to Fix

### Use Map.get for safe access

```elixir
# WRONG: crashes if key missing
value = map.nonexistent_key

# CORRECT: use Map.get with default
value = Map.get(map, :nonexistent_key, nil)
```

### Verify key exists first

```elixir
if Map.has_key?(map, :key) do
  map.key
else
  {:error, :missing_key}
end
```

## Examples

```elixir
def get_user_name(user_map) do
  Map.get(user_map, :name, "Unknown")
end
```

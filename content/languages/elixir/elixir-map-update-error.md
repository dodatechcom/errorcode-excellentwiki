---
title: "[Solution] Elixir Map Update Error -- Updating Non-Existing Keys"
description: "Fix Elixir map update errors when trying to update keys that do not exist in the map."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Map Update Error

This error occurs when you attempt to update a key in a map using the `%{map | key: value}` syntax but the key does not already exist.

## Common Causes

- Using struct update syntax on a plain map with missing keys
- Updating a nested key without first accessing the inner map
- Confusing map update syntax with Map.put
- Accessing map fields that were never set

## How to Fix

### Use Map.put for new keys

```elixir
# WRONG: key :new_key does not exist
map = %{a: 1, b: 2}
updated = %{map | new_key: 3}  # KeyError

# CORRECT: use Map.put for new keys
updated = Map.put(map, :new_key, 3)
```

### Use update for existing keys

```elixir
map = %{a: 1, b: 2}
updated = %{map | a: map.a + 10}
```

## Examples

```elixir
def add_user(users, name, age) do
  Map.put(users, name, %{age: age, active: true})
end

def update_age(users, name, new_age) do
  Map.update!(users, name, fn user -> %{user | age: new_age} end)
end
```

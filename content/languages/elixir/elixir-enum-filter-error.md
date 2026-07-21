---
title: "[Solution] Elixir Enum Filter Error -- Incorrect Predicate Usage"
description: "Fix Elixir enum filter errors when Enum.filter is used with functions that return wrong boolean values."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Enum Filter Error

This error occurs when `Enum.filter/2` receives a predicate function that does not return a boolean value.

## Common Causes

- Predicate function returning nil instead of false
- Using `Enum.filter` where `Enum.reject` would be clearer
- Side effects inside filter causing unexpected behavior
- Predicate function raising instead of returning false

## How to Fix

### Ensure boolean return values

```elixir
# WRONG: Map.get may return nil (truthy but not boolean)
Enum.filter(users, fn u -> Map.get(u, :active) end)

# CORRECT: explicit boolean comparison
Enum.filter(users, fn u -> Map.get(u, :active) == true end)

# Or use explicit true/false
Enum.filter(users, fn u ->
  case Map.get(u, :active) do
    true -> true
    _ -> false
  end
end)
```

### Use Enum.reject for negation

```elixir
# Instead of filter with negation
Enum.reject(items, fn item -> item.status == :inactive end)
```

## Examples

```elixir
def active_users(users) do
  users
  |> Enum.filter(fn user ->
    user.active == true and user.verified == true
  end)
end
```

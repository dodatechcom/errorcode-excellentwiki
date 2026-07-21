---
title: "[Solution] Elixir Enum Map Error -- Incorrect Collection Transformation"
description: "Fix Elixir enum map errors when Enum.map returns unexpected results due to side effects or nil values."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Enum Map Error

This error occurs when `Enum.map/2` returns unexpected results, such as nil values in the output list.

## Common Causes

- Mapping function returns nil instead of a value
- Side effects inside map causing unexpected state changes
- Mapping over a list that was modified during iteration
- Using `Enum.map` where `Enum.each` is intended for side effects

## How to Fix

### Ensure function returns a value

```elixir
# WRONG: function may return nil
Enum.map(users, fn user ->
  if user.active, do: user.name  # nil for inactive users
end)

# CORRECT: always return a value
Enum.map(users, fn user ->
  if user.active, do: user.name, else: "inactive"
end)
```

### Use each for side effects

```elixir
# WRONG: using map for side effects
Enum.map(items, &IO.inspect/1)

# CORRECT: use each
Enum.each(items, &IO.inspect/1)
```

## Examples

```elixir
def transform_users(users) do
  users
  |> Enum.filter(& &1.active)
  |> Enum.map(&%{name: &1.name, email: &1.email})
end
```

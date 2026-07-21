---
title: "[Solution] Elixir Enum Empty Error -- Reducing Empty Collections"
description: "Fix Elixir Enum empty error when calling reduce or Enum.at on empty enumerables without default values."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Enum Empty Error

This error occurs when you call functions like `Enum.at/2` or `Enum.reduce/2` on empty enumerables without providing a fallback value.

## Common Causes

- Calling `Enum.at(collection, index)` on an empty list
- Using `Enum.reduce/2` without an accumulator on an empty enumerable
- Accessing first or last element of an empty collection
- Pattern matching on non-empty list that is actually empty

## How to Fix

### Provide default values

```elixir
# WRONG: crashes on empty list
result = Enum.at([], 0)

# CORRECT: provide a default
result = Enum.at([], 0, nil)
result = Enum.at([], 0, :not_found)
```

### Use reduce with accumulator

```elixir
# WRONG: no accumulator
result = Enum.reduce([], fn x, acc -> acc + x end)

# CORRECT: provide initial accumulator
result = Enum.reduce([], 0, fn x, acc -> acc + x end)
```

## Examples

```elixir
def safe_head(list) do
  case list do
    [head | _] -> {:ok, head}
    [] -> {:error, :empty}
  end
end
```

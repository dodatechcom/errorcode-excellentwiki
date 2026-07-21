---
title: "[Solution] Elixir Enum Reduce Error -- Missing Initial Accumulator"
description: "Fix Elixir enum reduce errors when Enum.reduce is called without an initial accumulator value."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Enum Reduce Error

This error occurs when `Enum.reduce/2` is called on an empty enumerable without an initial accumulator value.

## Common Causes

- Using `Enum.reduce/2` which requires at least one element
- Empty list with no accumulator value
- Accumulator type mismatch across iterations
- Reducer function throwing on first iteration

## How to Fix

### Use Enum.reduce/3 with initial value

```elixir
# WRONG: crashes on empty list
result = Enum.reduce([], fn x, acc -> acc + x end)

# CORRECT: provide initial accumulator
result = Enum.reduce([], 0, fn x, acc -> acc + x end)
```

### Use Enum.map_reduce for map+reduce

```elixir
{mapped, final} = Enum.map_reduce([1, 2, 3], 0, fn x, acc ->
  {x * 2, acc + x}
end)
# mapped = [2, 4, 6], final = 6
```

## Examples

```elixir
def sum_squares(numbers) do
  numbers
  |> Enum.reduce(0, fn n, acc -> acc + n * n end)
end

def build_map(keys) do
  keys
  |> Enum.reduce(%{}, fn key, map ->
    Map.put(map, key, length(Map.keys(map)))
  end)
end
```

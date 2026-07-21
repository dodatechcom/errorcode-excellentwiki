---
title: "[Solution] Elixir List Append Error -- Incorrect List Concatenation"
description: "Fix Elixir list append errors when using ++ operator or List.append incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir List Append Error

This error occurs when the `++` operator or `List.append/2` is used with incorrect argument types.

## Common Causes

- Using `++` with non-list operands
- Appending a single element without wrapping in a list
- Performance issues from repeated left-side appending
- Mixing lists and non-lists

## How to Fix

### Use correct concatenation

```elixir
# WRONG: ++ expects lists on both sides
result = [1, 2, 3] ++ 4  # argument error

# CORRECT: wrap element in list
result = [1, 2, 3] ++ [4]

# Or use List.insert_at for single element
result = List.insert_at([1, 2, 3], -1, 4)
```

### Prefer Kernel.-- for subtraction

```elixir
# List difference
[1, 2, 3] -- [2]  # [1, 3]
```

## Examples

```elixir
def flatten_once(nested) do
  Enum.reduce(nested, [], fn list, acc ->
    acc ++ list
  end)
end
```

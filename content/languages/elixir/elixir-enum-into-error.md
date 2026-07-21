---
title: "[Solution] Elixir Enum Into Error -- Incorrect Collection Conversion"
description: "Fix Elixir enum into errors when using Enum.into to convert between collection types incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Enum Into Error

This error occurs when `Enum.into/2` or `Enum.into/3` is used to convert between incompatible collection types.

## Common Causes

- Using `Enum.into` with incompatible target types
- Not providing a transform function when needed
- Target collectable expecting specific element format
- Using `Enum.into` where simpler functions would work

## How to Fix

### Use correct target collectable

```elixir
# WRONG: into: "" needs iodata, not strings
Enum.into(["hello", "world"], "")

# CORRECT: use List.to_string or join
Enum.join(["hello", "world"], " ")
```

### Provide transform function

```elixir
# Transform while converting
map = Enum.into([{:a, 1}, {:b, 2}], %{}, fn {k, v} -> {k, v * 10} end)
```

## Examples

```elixir
# List to map
pairs = [{:a, 1}, {:b, 2}]
map = Enum.into(pairs, %{})

# Map to keyword list
map = %{a: 1, b: 2}
kw = Enum.into(map, [])
```

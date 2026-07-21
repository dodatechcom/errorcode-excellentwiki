---
title: "[Solution] Elixir Comprehension Error -- Incorrect for Loop Usage"
description: "Fix Elixir comprehension errors when for loops produce incorrect results or fail to compile."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Comprehension Error

This error occurs when `for` comprehensions are written incorrectly, producing unexpected results or failing to compile.

## Common Causes

- Using `for` where `Enum.map` is more appropriate
- Missing `do` block in comprehension
- Using `when` guard with non-guard-safe expressions
- Forgetting that `for` returns a list, not side effects

## How to Fix

### Write correct comprehensions

```elixir
# WRONG: using for without collectable
for x <- 1..5  # missing do block

# CORRECT: complete comprehension
for x <- 1..5, do: x * 2

# Multi-generator
for x <- 1..3, y <- 1..3, do: {x, y}
```

### Use into: for non-list targets

```elixir
# WRONG: for always returns list
result = for x <- 1..5, do: {x, x * x}  # returns list

# CORRECT: use into: for map
result = for x <- 1..5, into: %{}, do: {x, x * x}
```

## Examples

```elixir
def cartesian_product(list_a, list_b) do
  for a <- list_a, b <- list_b, do: {a, b}
end

def even_squares(limit) do
  for x <- 1..limit, rem(x, 2) == 0, into: %{}, do: {x, x * x}
end
```

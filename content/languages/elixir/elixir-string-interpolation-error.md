---
title: "[Solution] Elixir String Interpolation Error -- Incorrect Syntax"
description: "Fix Elixir string interpolation errors when using #{ } interpolation syntax incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir String Interpolation Error

This error occurs when string interpolation syntax `#{}` is used incorrectly or contains invalid expressions.

## Common Causes

- Using `#{}` inside charlists (single-quoted strings)
- Missing closing `}` in interpolation
- Using `#{}` with expressions that cannot be stringified
- Double quotes not used (only double-quoted strings support interpolation)

## How to Fix

### Use double-quoted strings for interpolation

```elixir
# WRONG: charlist does not support interpolation
name = 'Alice'
greeting = 'Hello #{name}'

# CORRECT: use double quotes
name = "Alice"
greeting = "Hello #{name}"
```

### Ensure valid expressions

```elixir
# WRONG: keyword list cannot be interpolated directly
opts = [timeout: 5000]
IO.puts("Options: #{opts}")

# CORRECT: use inspect or format
IO.puts("Options: #{inspect(opts)}")
```

## Examples

```elixir
name = "Alice"
age = 30
IO.puts("Name: #{name}, Age: #{age}")
IO.puts("1 + 1 = #{1 + 1}")
```

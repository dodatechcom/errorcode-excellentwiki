---
title: "[Solution] Elixir Pipe Operator Error -- Incorrect Pipe Chaining"
description: "Fix Elixir pipe operator errors when | > is used with functions that have unexpected argument positions."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Pipe Operator Error

This error occurs when the pipe operator `|>` is used with functions that do not accept the piped value as their first argument.

## Common Causes

- Piping into a function where the value is not the first argument
- Forgetting that `|>` pipes into the first argument position
- Piping into a macro that expects a specific syntax
- Using pipe with a function that needs keyword list as second arg

## How to Fix

### Understand pipe argument position

```elixir
# WRONG: String.trim takes a string as first arg, not list
result = [1, 2, 3] |> String.trim()

# CORRECT: pipe into functions expecting the value first
result = "  hello  " |> String.trim()
```

### Reorder arguments or use capture

```elixir
# WRONG: Enum.at takes collection first, then index
result = 0 |> Enum.at([1, 2, 3])

# CORRECT: either flip or use capture
result = [1, 2, 3] |> Enum.at(0)
# or
result = 0 |> then(&Enum.at([1, 2, 3], &1))
```

## Examples

```elixir
"hello world"
|> String.split(" ")
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")
```

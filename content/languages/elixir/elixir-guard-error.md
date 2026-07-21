---
title: "[Solution] Elixir Guard Error -- Invalid Guard Expressions"
description: "Fix Elixir guard errors when guard clauses use expressions not allowed in guards."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Guard Error

This error occurs when a guard clause uses a function or expression that is not allowed in Elixir guards.

## Common Causes

- Using custom functions inside guards (not allowed)
- Calling String functions in guards (too complex for BEAM)
- Using `not` instead of `not` macro correctly
- Nesting case or cond inside guard expressions

## How to Fix

### Use only allowed guard expressions

```elixir
# WRONG: String.contains? not allowed in guard
def process(s) when is_binary(s) and String.contains?(s, "error") do
  :error
end

# CORRECT: use case or matching
def process(s) when is_binary(s) do
  if String.contains?(s, "error"), do: :error, else: :ok
end
```

### Use permitted functions

```elixir
# Allowed in guards: is_*, +, -, *, /, rem, trunc,
# round, abs, elem, tuple_size, etc.
def classify(x) when is_integer(x) and x > 0, do: :positive
def classify(x) when is_integer(x) and x < 0, do: :negative
def classify(x) when is_integer(x), do: :zero
```

## Examples

```elixir
def divide(a, b) when b != 0, do: {:ok, a / b}
def divide(_, _), do: {:error, :division_by_zero}
```

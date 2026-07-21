---
title: "[Solution] Elixir Function Clause Error -- No Matching Function Head"
description: "Fix Elixir function clause error when no function head matches the given arguments."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Function Clause Error

This error occurs when a function is called with arguments that do not match any of its defined clauses.

## Common Causes

- No clause matches the given argument pattern
- Missing a catch-all clause with a wildcard `_` pattern
- Pattern matching is too restrictive for the input
- Calling a private function from outside its module

## How to Fix

### Add a catch-all clause

```elixir
# WRONG: only handles integers
def process(x) when is_integer(x) do
  x * 2
end

# CORRECT: add catch-all
def process(x) when is_integer(x) do
  x * 2
end

def process(x) do
  raise ArgumentError, "Unsupported type: #{inspect(x)}"
end
```

### Broaden pattern matching

```elixir
def describe(%{status: status, name: name}) do
  "#{name}: #{status}"
end

def describe(_) do
  "Unknown item"
end
```

## Examples

```elixir
def factorial(0), do: 1
def factorial(n) when is_integer(n) and n > 0, do: n * factorial(n - 1)
def factorial(n), do: raise(ArgumentError, "Expected non-negative integer, got: #{inspect(n)}")
```

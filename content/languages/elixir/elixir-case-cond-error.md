---
title: "[Solution] Elixir Case Cond Error -- Incorrect Case/Cond Usage"
description: "Fix Elixir case/cond errors when case clauses do not match or cond has no true branch."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Case Cond Error

This error occurs when `case` clauses do not match the given value, or `cond` has no clause evaluating to true.

## Common Causes

- case clauses missing a catch-all `_` pattern
- cond clauses evaluating to nil or false instead of true
- Pattern matching with wrong field names or structure
- cond with complex expressions that evaluate unexpectedly

## How to Fix

### Always handle all cases

```elixir
# WRONG: no catch-all
case value do
  :ok -> "good"
  :error -> "bad"
end

# CORRECT: add catch-all
case value do
  :ok -> "good"
  :error -> "bad"
  other -> "unknown: #{inspect(other)}"
end
```

### Use cond with explicit checks

```elixir
# WRONG: nil evaluates to false
cond do
  x > 10 -> "large"
  x > 5 -> "medium"   # if x is nil, this is false
end

# CORRECT: explicit nil check first
cond do
  is_nil(x) -> "missing"
  x > 10 -> "large"
  x > 5 -> "medium"
  true -> "small"
end
```

## Examples

```elixir
def describe_status(status) do
  case status do
    :active -> "User is active"
    :inactive -> "User is inactive"
    :banned -> "User is banned"
    other -> "Unknown status: #{inspect(other)}"
  end
end
```

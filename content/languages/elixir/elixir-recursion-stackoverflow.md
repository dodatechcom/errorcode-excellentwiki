---
title: "[Solution] Elixir RecursionStackOverflow - Brief Description"
description: "Fix Elixir stack overflow from infinite recursion."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1004
---

A recursion stack overflow occurs when a recursive function never reaches its base case.

## Common Causes

- Missing or unreachable base case in recursive function
- Recursive call does not progress toward the base case
- Mutual recursion without termination
- Incorrect guard condition that never terminates

## How to Fix

Always define a clear base case:

```elixir
# WRONG: No base case
def factorial(n), do: n * factorial(n - 1)

# CORRECT: Base case defined
def factorial(0), do: 1
def factorial(n) when n > 0, do: n * factorial(n - 1)
```

Convert to tail-recursive form:

```elixir
def sum_list(list), do: sum_list(list, 0)
def sum_list([h | t], acc), do: sum_list(t, acc + h)
def sum_list([], acc), do: acc
```

## Examples

```elixir
defmodule EvenOdd do
  def is_even?(0), do: true
  def is_even?(n), do: is_odd?(n - 1)
  defp is_odd?(0), do: false
  defp is_odd?(n), do: is_even?(n - 1)
end
```

## Related Errors

- [FunctionClauseError](/languages/elixir/elixir-function-clause)
- [ProcessDied](/languages/elixir/elixir-process-died)

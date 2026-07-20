---
title: "[Solution] Elixir TailCallOptimizationError - Brief Description"
description: "Fix non-tail-recursive Elixir functions."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1005
---

When a recursive function is not tail-recursive, each call adds a frame to the call stack.

## Common Causes

- Performing computation after the recursive call returns
- Building data structures on the way down instead of using an accumulator
- Using pipes that wrap the recursive call

## How to Fix

Move computation before the recursive call:

```elixir
# NOT tail-recursive
def factorial(0), do: 1
def factorial(n), do: n * factorial(n - 1)

# Tail-recursive with accumulator
def factorial(n), do: factorial(n, 1)
defp factorial(0, acc), do: acc
defp factorial(n, acc), do: factorial(n - 1, acc * n)
```

Use `:timer.tc` to measure performance:

```elixir
{time, result} = :timer.tc(fn ->
  Enum.reduce(1..100_000, 1, fn x, acc -> x * acc end)
end)
IO.puts("Took #{div(time, 1000)}ms")
```

## Examples

```elixir
def reverse(list), do: reverse(list, [])
defp reverse([], acc), do: acc
defp reverse([h | t], acc), do: reverse(t, [h | acc])
```

## Related Errors

- [RecursionStackOverflow](/languages/elixir/elixir-recursion-stackoverflow)
- [FunctionClauseError](/languages/elixir/elixir-function-clause)

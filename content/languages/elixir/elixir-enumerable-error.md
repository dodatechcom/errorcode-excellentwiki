---
title: "[Solution] Elixir EnumerableError - Brief Description"
description: "Fix Elixir Enumerable protocol errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1027
---

An Enumerable error occurs when calling `Enum` functions on a non-enumerable type.

## Common Causes

- Passing a struct to `Enum.map/2` without Enumerable
- Using Enum functions on a binary string
- Passing `nil` to an Enum function

## How to Fix

Implement Enumerable for custom types:

```elixir
defimpl Enumerable, for: Range do
  def count(%Range{start: s, end: e}), do: {:ok, e - s + 1}
  def member?(%Range{start: s, end: e}, value), do: {:ok, value in s..e}
  def reduce(%Range{start: s, end: e}, acc, fun) do
    reduce_range(s, e, acc, fun)
  end
  defp reduce_range(_, _, {:halt, acc}, _), do: {:halted, acc}
  defp reduce_range(s, e, {:suspend, acc}, fun), do: {:suspended, acc, &reduce_range(s, e, &1, fun)}
  defp reduce_range(s, e, {:cont, acc}, fun) when s > e, do: {:done, acc}
  defp reduce_range(s, e, {:cont, acc}, fun) do
    reduce_range(s + 1, e, fun.(s, acc), fun)
  end
end
```

## Examples

```elixir
%{a: 1, b: 2, c: 3} |> Enum.map(fn {k, v} -> {k, v * 2} end)
```

## Related Errors

- [CollectableError](/languages/elixir/elixir-collectable-error)
- [EnumEmptyError](/languages/elixir/elixir-enum-empty)

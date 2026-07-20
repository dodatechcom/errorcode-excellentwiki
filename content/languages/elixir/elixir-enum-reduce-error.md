---
title: "[Solution] Elixir EnumReduceError - Brief Description"
description: "Fix Elixir Enum.reduce errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1030
---

An `Enum.reduce` error occurs when accumulator types are incompatible or the enumerable is empty.

## Common Causes

- Empty enumerable with no default accumulator
- Reducer returning wrong type
- Reducer function raising an exception

## How to Fix

Always provide a default accumulator:

```elixir
Enum.reduce([], 0, fn x, acc -> acc + x end)
```

Use `Enum.reduce_while` for early termination:

```elixir
Enum.reduce_while(1..100, 0, fn x, acc ->
  if acc + x > 50, do: {:halt, acc}, else: {:cont, acc + x}
end)
```

## Examples

```elixir
words = ~w(apple banana apple cherry banana apple)
Enum.reduce(words, %{}, fn word, acc ->
  Map.update(acc, word, 1, &(&1 + 1))
end)
```

## Related Errors

- [EnumEmptyError](/languages/elixir/elixir-enum-empty)
- [EnumerableError](/languages/elixir/elixir-enumerable-error)

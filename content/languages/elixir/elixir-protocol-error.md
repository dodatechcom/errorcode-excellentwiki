---
title: "[Solution] Elixir Protocol Error -- Missing Protocol Implementation"
description: "Fix Elixir protocol errors when a struct does not implement a required protocol."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Protocol Error

This error occurs when a struct is used with a protocol that has not been implemented for its type.

## Common Causes

- Forgetting to derive or implement the Enumerable protocol
- Using a struct with Map functions that require protocol implementation
- Missing `@derive` annotation for derived protocol implementations
- Using protocols with non-struct types that lack implementations

## How to Fix

### Implement or derive the protocol

```elixir
# WRONG: no protocol implementation
defmodule Range do
  defstruct [:start, :end_]
end

Enum.each(%Range{start: 1, end_: 5}, &IO.inspect/1)  # error

# CORRECT: derive the protocol
defmodule Range do
  defstruct [:start, :end_]
  @derive [Enumerable]
end

# Or implement directly
defimpl Enumerable, for: Range do
  def count(%Range{start: s, end_: e}), do: {:ok, e - s + 1}
  def member?(%Range{start: s, end_: e}, value), do: {:ok, value in s..e}
  def slice(_), do: {:error, __MODULE__}
  def reduce(%Range{start: s, end_: e}, acc, fun) do
    Enum.reduce(s..e, acc, fun)
  end
end
```

## Examples

```elixir
defimpl Collectable, for: MyList do
  def into(%MyList{} = list), do: {list, fn list, _ -> list end}
end
```

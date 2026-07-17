---
title: "** (FunctionClauseError) No Matching Function Clause"
description: "Elixir raises FunctionClauseError when no function clause matches the given arguments"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `FunctionClauseError` is raised when a function is called with arguments that don't match any of its defined clauses. Elixir functions use pattern matching on arguments.

## Common Causes

- Missing function clause for specific argument type
- Function clauses ordered incorrectly
- Passing unexpected types or values
- Forgetting to handle nil or edge cases

## How to Fix

Add clause for nil or guard clauses:

```elixir
defmodule Divide do
  def divide(_a, 0), do: {:error, :division_by_zero}
  def divide(_a, nil), do: {:error, :nil_divisor}
  def divide(a, b), do: {:ok, a / b}
end
```

Order clauses correctly (specific first):

```elixir
defmodule Parser do
  def parse(x) when is_binary(x), do: {:string, x}
  def parse(x) when is_list(x), do: {:list, x}
  def parse(x), do: {:other, x}
end
```

Handle edge cases:

```elixir
defmodule Head do
  def head([h | _]), do: {:ok, h}
  def head([]), do: {:error, :empty_list}
end
```

## Examples

```elixir
defmodule Adder do
  def add(a, b) when is_number(a) and is_number(b), do: a + b
end

Adder.add("hello", 42)
# ** (FunctionClauseError) no function clause matching in Adder.add/2
```

## Related Errors

- [MatchError]({{< relref "/languages/elixir/match-error" >}})
- [ArgumentError]({{< relref "/languages/elixir/argument-error4" >}})

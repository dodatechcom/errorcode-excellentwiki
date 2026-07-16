---
title: "** (FunctionClauseError) no function clause matching"
description: "A FunctionClauseError occurs when no function clause matches the given arguments."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["function", "clause", "pattern-matching", "functionclauseerror"]
weight: 5
---

## What This Error Means

A `FunctionClauseError` is raised when a function is called with arguments that don't match any of its defined clauses. Elixir functions are defined with pattern matching on their arguments, and if none of the patterns match the provided arguments, this error occurs.

## Common Causes

- Missing a function clause for a specific argument type
- Function clauses ordered incorrectly (specific clauses after general ones)
- Passing unexpected types or values to a function
- Forgetting to handle nil or edge cases

## How to Fix

```elixir
# WRONG: Missing clause for nil
defmodule Divide do
  def divide(a, b) do
    a / b
  end
end

Divide.divide(10, nil)
# ** (FunctionClauseError) no function clause matching in Divide.divide/2

# CORRECT: Add clause for nil or guard clauses
defmodule Divide do
  def divide(_a, 0), do: {:error, :division_by_zero}
  def divide(_a, nil), do: {:error, :nil_divisor}
  def divide(a, b), do: {:ok, a / b}
end
```

```elixir
# WRONG: Clause ordering issue
defmodule Parser do
  def parse(x) when is_binary(x), do: {:string, x}
  def parse(x) when is_list(x), do: {:list, x}
  def parse(x), do: {:other, x}           # catches everything first!
end

# CORRECT: More specific clauses first
defmodule Parser do
  def parse(x) when is_binary(x), do: {:string, x}
  def parse(x) when is_list(x), do: {:list, x}
  def parse(x), do: {:other, x}
end
```

## Examples

```elixir
# Example 1: No clause for empty list
defmodule Head do
  def head([h | _]), do: h
end

Head.head([])
# ** (FunctionClauseError) no function clause matching in Head.head/1

# Example 2: Wrong argument types
defmodule Adder do
  def add(a, b) when is_number(a) and is_number(b), do: a + b
end

Adder.add("hello", 42)
# ** (FunctionClauseError) no function clause matching in Adder.add/2

# Example 3: Missing guard for float
defmodule Double do
  def double(x) when is_integer(x), do: x * 2
end

Double.double(3.14)
# ** (FunctionClauseError) no function clause matching in Double.double/1
```

## Related Errors

- [MatchError: no match of right hand side value](/languages/elixir/badmatch)

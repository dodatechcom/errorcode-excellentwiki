---
title: "[Solution] Elixir GuardClauseError — Guard Expression Failed"
description: "Fix Elixir guard clause errors. Learn guard constraints, boolean guards, and proper guard usage."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1001
---

A `FunctionClauseError` with a guard clause failure occurs when a function guard expression evaluates to false or raises during evaluation. Guards are Boolean expressions that must succeed for a function clause to match.

## Common Causes

- Using non-Boolean operators in guard expressions
- Calling functions in guards that may raise exceptions
- Using pattern matching syntax unsupported in guards
- Guard expressions that are always false for certain input types
- Using Elixir-only functions not allowed in Erlang guards

## How to Fix

Use only allowed guard expressions:

```elixir
# WRONG: String.length is not allowed in guards
def process(x) when String.length(x) > 0 do
  x
end

# CORRECT: Use byte_size or match patterns
def process(x) when is_binary(x) and byte_size(x) > 0 do
  x
end
```

Avoid functions that may raise in guards:

```elixir
# WRONG: List.first may raise on empty list
def head(xs) when List.first(xs) != nil do
  xs
end

# CORRECT: Use pattern matching
def head([x | _]), do: x
def head([]), do: nil
```

Use multiple guard clauses for complex conditions:

```elixir
def classify(x)
    when is_integer(x) and x > 0 do
  :positive
end

def classify(x)
    when is_integer(x) and x < 0 do
  :negative
end

def classify(0), do: :zero
def classify(_), do: :not_a_number
```

Create guard-safe helper functions using macros:

```elixir
defmodule GuardHelpers do
  defmacro is_positive(x) do
    quote do
      is_number(unquote(x)) and unquote(x) > 0
    end
  end

  def classify(x) when is_positive(x), do: :positive
  def classify(x) when is_number(x), do: :non_positive
  def classify(_), do: :not_a_number
end
```

## Examples

```elixir
# Guard with membership check
def status(x) when x in [:active, :inactive, :pending], do: :valid
def status(_), do: :invalid
```

## Related Errors

- [FunctionClauseError in Elixir](/languages/elixir/elixir-function-clause)
- [CaseClauseError in Elixir](/languages/elixir/elixir-caseclauseerror)
- [MatchError in Elixir](/languages/elixir/elixir-matcherror)

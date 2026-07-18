---
title: "[Solution] Fix no function clause matching in Elixir"
description: "Fix no function clause matching errors in Elixir by adding catch-all clauses, broadening function patterns, and properly handling all expected inputs."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 7
---

## What This Error Means

A `FunctionClauseError` is raised when no function clause matches the given arguments. This happens in Elixir when you call a function and none of its clauses or pattern-matched definitions can handle the provided input.

The error typically appears as:

```elixir
** (FunctionClauseError) no function clause matching in Anonymous fn/1
```

or for named functions:

```elixir
** (FunctionClauseError) no function clause matching in MyModule.process/1
```

## Why It Happens

This error occurs when function arguments do not match any defined clause:

- Passing an unexpected type to a pattern-matched function
- Calling an anonymous function with arguments that do not match its patterns
- Providing values outside guard constraints
- Forgetting to add a catch-all clause
- Mismatched argument counts between call site and function definition

## How to Fix It

Add a catch-all clause to handle unexpected inputs:

```elixir
# WRONG: Only handles integers
def double(x) when is_integer(x) do
  x * 2
end

double("hello")
# ** (FunctionClauseError)

# CORRECT: Add a catch-all clause
def double(x) when is_integer(x) do
  x * 2
end

def double(x) do
  raise ArgumentError, "Expected integer, got: #{inspect(x)}"
end
```

Use `@fallback` or `Any` implementations for protocols and behaviours:

```elixir
# Ensure your function handles nil and edge cases
def process(nil), do: {:ok, :empty}
def process([]), do: {:ok, :empty}
def process([head | tail]) when is_list(tail) do
  {:ok, [head | tail]}
end
def process(other), do: {:error, {:unexpected, other}}
```

Fix anonymous function clause mismatches by broadening patterns:

```elixir
# WRONG: Anonymous function with narrow pattern
handler = fn
  {:ok, value} -> value
end

handler.({:error, "bad"})
# ** (FunctionClauseError)

# CORRECT: Handle all expected patterns
handler = fn
  {:ok, value} -> value
  {:error, reason} -> {:handled_error, reason}
  other -> {:unexpected, other}
end
```

## Common Mistakes

- Not including a catch-all `_` or `other` clause in multi-clause functions
- Relying on guard expressions that silently exclude valid inputs
- Assuming pattern matching will automatically coerce types between clauses
- Forgetting that Elixir matches clauses in definition order
- Using `defp` private functions without considering all public entry points

## Related Pages

- [MatchError: no match of right hand side value](/languages/elixir/match-error)
- [CaseClauseError in Elixir](/languages/elixir/elixir-caseclauseerror)
- [ArgumentError in Elixir](/languages/elixir/argument-error4)

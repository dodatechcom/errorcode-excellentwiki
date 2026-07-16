---
title: "** (MatchError) no match of right hand side value"
description: "A MatchError occurs when the right-hand side of a match operator (=) does not match the pattern on the left-hand side."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["match", "pattern-matching", "matcherror"]
weight: 5
---

## What This Error Means

Elixir uses the `=` operator as a match operator, not just assignment. A `MatchError` is raised when the right-hand side value does not match the pattern specified on the left-hand side. This is a fundamental part of Elixir's pattern matching system and can occur in function heads, case statements, and direct matches.

## Common Causes

- Expecting a specific pattern that doesn't match the actual value
- Using a variable on the left-hand side when you meant to match a specific value
- Incorrect function clause ordering (more specific clauses should come first)
- Trying to match a struct with the wrong type

## How to Fix

```elixir
# WRONG: Pattern doesn't match
{a, b, c} = {1, 2}          # ** (MatchError) no match of right hand side value: {1, 2}

# CORRECT: Ensure pattern matches the structure
{a, b} = {1, 2}              # a=1, b=2
```

```elixir
# WRONG: Variable on left side always matches (pins for specific values)
x = 10
x = 20                       # This actually works (rebind), but:

# For matching against specific values, use pin operator
x = 10
^x = 20                      # ** (MatchError) no match of right hand side value

# CORRECT: Use pin when you need exact match
x = 10
^x = 10                      # matches
```

## Examples

```elixir
# Example 1: Function pattern mismatch
defmodule Greeter do
  def greet(:hello), do: "Hi!"
  def greet(:goodbye), do: "Bye!"
end

Greeter.greet(:unknown)
# ** (MatchError) no match of right hand side value: :unknown

# Example 2: Destructuring mismatch
%{name: name, age: age} = %{name: "Alice"}
# ** (MatchError) no match of right hand side value: %{name: "Alice"}

# Example 3: Numeric match
42 = "hello"
# ** (MatchError) no match of right hand side value: "hello"
```

## Related Errors

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)

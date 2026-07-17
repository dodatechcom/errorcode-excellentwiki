---
title: "** (Enum.EmptyError) empty error"
description: "An Enum.EmptyError occurs when calling a function that requires at least one element on an empty enumerable."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `Enum.EmptyError` is raised when you call a function on an empty enumerable that requires at least one element to work. Functions like `Enum.first/1` with the `raise` option or `Enum.min/1` raise this error on empty collections.

## Common Causes

- Calling `Enum.first/1` or similar on an empty list
- Using functions that require at least one element without checking
- Processing collections that may be empty
- Missing empty-check before reduction operations

## How to Fix

```elixir
# WRONG: Calling function that requires elements on empty list
Enum.min([])
# ** (Enum.EmptyError) empty error in Enum.min/1

# CORRECT: Check if empty first or use default
list = []
if list != [] do
  Enum.min(list)
else
  nil
end

# Or use Enum.min/2 with default
Enum.min([], fn -> nil end)
```

```elixir
# WRONG: Using first! on empty
Enum.first!([])
# ** (Enum.EmptyError)

# CORRECT: Use Enum.at/2 or Enum.take/2
Enum.at([], 0)        # nil
Enum.take([], 1)      # []
Enum.find([], fn _ -> true end)  # nil
```

## Examples

```elixir
# Example 1: Min of empty list
Enum.min([])   # ** (Enum.EmptyError) empty error

# Example 2: First of empty list
Enum.first!([])  # ** (Enum.EmptyError)

# Example 3: Max of empty enumerable
Enum.max(MapSet.new())  # ** (Enum.EmptyError)
```

## Related Errors

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [MatchError: no match of right hand side value](/languages/elixir/match-error)

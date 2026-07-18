---
title: "[Solution] Fix Enum.EmptyError empty error in Elixir"
description: "Learn how to fix Enum.EmptyError in Elixir by using safe defaults, guarding against empty collections, and choosing the correct enumeration functions."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 6
---

## What This Error Means

An `Enum.EmptyError` is raised when you call a function that requires at least one element on an empty enumerable. Elixir's `Enum` module provides several functions that raise this error when the collection is empty, including `Enum.min/1`, `Enum.max/1`, `Enum.first!/1`, and `Enum.reduce/2` without an explicit initial accumulator.

The error message looks like:

```elixir
** (Enum.EmptyError) empty error in Enum.min/1
```

## Why It Happens

This error occurs because certain enumeration operations are mathematically undefined on empty collections. Common triggers include:

- Calling `Enum.min/1` or `Enum.max/1` on an empty list
- Using `Enum.first!/1` on a list with no elements
- Running `Enum.join/1` on an empty enumerable
- Reducing with `Enum.reduce/2` without providing an initial accumulator on an empty list
- Processing collections that become empty after filtering

## How to Fix It

Use safe alternative functions that accept a default value or a fallback function:

```elixir
# WRONG: These raise Enum.EmptyError on empty lists
Enum.min([])
Enum.max([])
Enum.first!([])

# CORRECT: Use the arity-2 versions with a fallback
Enum.min([], fn -> nil end)
Enum.max([], fn -> nil end)
Enum.at([], 0)           # returns nil
Enum.take([], 1)         # returns []
```

Check emptiness before calling the function:

```elixir
list = fetch_items()

if list != [] do
  Enum.min(list)
else
  :default_value
end
```

Use `Enum.reduce/3` with an explicit accumulator instead of `Enum.reduce/2`:

```elixir
# WRONG: Raises on empty list
Enum.reduce([1, 2, 3], &+/2)

# CORRECT: Provide initial accumulator
Enum.reduce([], 0, &+/2)   # returns 0
Enum.reduce([1, 2, 3], 0, &+/2)  # returns 6
```

Use pattern matching with `case` for safe handling:

```elixir
case Enum.to_list(collection) do
  [] -> handle_empty()
  [head | _] -> process(head)
end
```

## Common Mistakes

- Assuming `Enum.min/1` returns `nil` on empty lists when it actually raises
- Forgetting that `Enum.reduce/2` without an accumulator fails on empty enumerables
- Not checking for empty collections after `Enum.filter/2` or `Enum.reject/2` operations
- Using `Enum.at!/2` instead of the safe `Enum.at/2` variant
- Not considering that `MapSet.new()` or `Range.new(1, 0)` produce empty enumerables

## Related Pages

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [MatchError: no match of right hand side value](/languages/elixir/match-error)
- [ArgumentError in Elixir](/languages/elixir/argument-error4)

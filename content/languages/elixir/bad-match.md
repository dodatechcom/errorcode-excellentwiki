---
title: "** (BadMapError) expected a map"
description: "A BadMapError occurs when attempting to use a value as a map when it is not a map."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["map", "badmap", "type-error", "badmaperror"]
weight: 5
---

## What This Error Means

A `BadMapError` is raised when you try to use map operations (like `Map.get`, `Map.put`, or the `%{}` pattern) on a value that isn't a map. This typically happens when a function expects a map but receives a different type.

## Common Causes

- Passing a non-map value to map functions
- Pattern matching with map syntax on non-map data
- Confusing keyword lists with maps
- Nil or other types where a map is expected

## How to Fix

```elixir
# WRONG: Using map functions on non-map
Map.get([1, 2, 3], :key)
# ** (BadMapError) expected a map, got: [1, 2, 3]

# CORRECT: Ensure value is a map first
data = %{key: "value"}
Map.get(data, :key)  # "value"
```

```elixir
# WRONG: Pattern matching with map on keyword list
{key, value} = [a: 1, b: 2]
%{a: x} = [a: 1, b: 2]
# ** (BadMapError) expected a map, got: [a: 1, b: 2]

# CORRECT: Use keyword list syntax
[a: x, b: y] = [a: 1, b: 2]  # works
```

## Examples

```elixir
# Example 1: Map function on string
Map.keys("hello")
# ** (BadMapError) expected a map, got: "hello"

# Example 2: Map pattern on list
%{name: n} = [name: "Alice"]
# ** (BadMapError) expected a map

# Example 3: Nil where map expected
config = nil
Map.get(config, :timeout)
# ** (BadMapError) expected a map, got: nil
```

## Related Errors

- [MatchError: no match of right hand side value](/languages/elixir/match-error)
- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)

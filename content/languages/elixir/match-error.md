---
title: "** (MatchError) no match of right hand side value"
description: "A MatchError occurs when a pattern match fails because the right-hand side value doesn't match the expected pattern."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MatchError` is raised when a pattern match operation fails because the value on the right-hand side doesn't match the pattern on the left-hand side. In Elixir, the `=` operator performs pattern matching, not just assignment.

## Common Causes

- Pattern doesn't match the actual structure of the data
- Trying to match on wrong types
- Using variables in patterns that bind instead of match
- Incorrect tuple or list structure in pattern

## How to Fix

```elixir
# WRONG: Pattern doesn't match
{a, b} = [1, 2]    # ** (MatchError) no match of right hand side value: [1, 2]

# CORRECT: Match with correct structure
{a, b} = {1, 2}    # a=1, b=2
```

```elixir
# WRONG: Variable binding instead of matching
x = 1
{x, y} = {1, 2}   # works (binds x=1, y=2)
{x, y} = {3, 4}   # ** (MatchError) - x already bound to 1

# CORRECT: Use pin operator for matching
x = 1
{^x, y} = {1, 2}  # works (x must be 1)
{^x, y} = {3, 4}  # ** (MatchError)
```

## Examples

```elixir
# Example 1: Wrong tuple size
{a, b, c} = {1, 2}  # ** (MatchError) no match of right hand side value

# Example 2: Wrong list pattern
[h | t] = []         # ** (MatchError) no match of right hand side value

# Example 3: Guard clause mismatch
case 10 do
  x when x > 20 -> "big"
  # no match for x=10
end
# ** (MatchError)
```

## Related Errors

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [BadMapError: expected a map](/languages/elixir/bad-match)

---
title: "[Solution] Elixir CondClauseError — No Matching Cond Clause"
description: "Fix Elixir CondClauseError when no cond clause matches. Learn about cond expressions, boolean logic, and truthiness in Elixir."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `CondClauseError` is raised when a `cond` expression evaluates all clauses and none of them return a truthy value. Unlike `case` or `cond`, the `cond` macro evaluates each clause as a boolean expression, and if all evaluate to `false` or `nil`, the error is raised.

## Why It Happens

The most common cause is a `cond` expression that does not have a `true` catch-all clause. If none of the conditions evaluate to a truthy value and there is no `true ->` clause, the error occurs.

Another frequent cause is conditions that unexpectedly evaluate to `nil` or `false`. For example, a function that returns `nil` instead of `true` when used in a `cond` clause.

Boolean logic errors in conditions can cause all clauses to fail. Using `&&` instead of `and`, or confusing truthiness with exact `true` values, leads to unexpected behavior.

Comparison operators that return `false` for expected matches (like comparing different types) can cause this error.

Finally, missing conditions for all possible states of a variable cause this error when an unexpected state is encountered.

## How to Fix It

### Always include a true catch-all clause

```elixir
cond do
  x > 10 -> "large"
  x > 5  -> "medium"
  x > 0  -> "small"
  true   -> "non-positive"
end
```

### Handle nil and false explicitly

```elixir
cond do
  is_nil(value)      -> "nil case"
  value == false      -> "false case"
  value == true       -> "true case"
  true                -> "other"
end
```

### Use if/else for simple boolean conditions

```elixir
if x > 10 do
  "large"
else
  "small"
end
```

### Check for truthiness correctly

```elixir
# Elixir treats false and nil as falsy, everything else is truthy
cond do
  value -> "truthy"
  true  -> "always matches"
end
```

### Use case for pattern matching instead of cond

```elixir
case status do
  :ok    -> "success"
  :error -> "failure"
  _      -> "other"
end
```

## Common Mistakes

- Forgetting the `true` catch-all clause in `cond`
- Confusing truthiness with exact boolean comparison
- Using `cond` when `case` or `if` would be more appropriate
- Not handling nil values in conditions
- Writing conditions that can never be true for the expected input

## Related Pages

- [Elixir CaseClauseError](/languages/elixir/elixir-caseclauseerror/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)

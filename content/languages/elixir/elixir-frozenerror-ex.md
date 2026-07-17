---
title: "RuntimeError: Cannot Invoke Inside Match"
description: "Elixir raises RuntimeError when attempting function calls inside pattern matches"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `RuntimeError` with "cannot invoke inside match" occurs when you try to call a function or perform side effects inside a pattern match. Pattern matching should be pure and side-effect free.

## Common Causes

- Calling function in pattern match head
- Assigning with function call in match position
- Using side effects in case/with clauses
- attempting to match with runtime function result

## How to Fix

Move function calls outside pattern matching:

```elixir
# Wrong
case get_value() do
  ^compute_expected() -> :match  # Error: cannot invoke inside match
  _ -> :no_match
end

# Correct
expected = compute_expected()
case get_value() do
  ^expected -> :match
  _ -> :no_match
end
```

Use guards for runtime checks:

```elixir
case value do
  x when x > 0 -> :positive
  x when x < 0 -> :negative
  _ -> :zero
end
```

Bind variables before matching:

```elixir
result = process_data()

case result do
  {:ok, data} -> handle_success(data)
  {:error, reason} -> handle_error(reason)
end
```

## Examples

```elixir
^length([1, 2, 3]) = [1, 2, 3]
# ** (RuntimeError) cannot invoke "Elixir.Enum".length/1 inside match
```

## Related Errors

- [MatchError]({{< relref "/languages/elixir/match-error" >}})
- [FunctionClauseError]({{< relref "/languages/elixir/function-clause" >}})

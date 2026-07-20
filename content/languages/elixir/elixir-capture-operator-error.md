---
title: "[Solution] Elixir CaptureOperatorError - Brief Description"
description: "Fix Elixir capture operator errors. Learn &capture syntax and arity matching."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1002
---

A capture operator error occurs when the `&` syntax is used incorrectly to create function references.

## Common Causes

- Mismatched arity between `&fun/arity` and actual function definition
- Using capture syntax with wrong number of placeholders
- Capturing private functions without proper module qualification
- Mixing capture syntax with piped arguments incorrectly

## How to Fix

Match capture arity with function definition:

```elixir
# WRONG: Function has 2 args but captured with 1
def add(a, b), do: a + b
Enum.map([1, 2, 3], &add/1)

# CORRECT: Capture with correct arity
Enum.map([1, 2, 3], &add(&1, 0))
```

Use placeholders correctly:

```elixir
add = &(&1 + &2)
add.(1, 2)

# WRONG: Too many placeholders
bad = &(&1 + &2 + &3)
```

Use capture in pipeline chains:

```elixir
[1, 2, 3]
|> Enum.map(&(&1 * 2))
|> Enum.filter(&(&1 > 3))
|> Enum.sum()
```

## Examples

```elixir
downcase = &String.downcase/1
Enum.map(["HELLO", "WORLD"], downcase)
```

## Related Errors

- [FunctionClauseError](/languages/elixir/elixir-function-clause)
- [UndefinedFunctionError](/languages/elixir/elixir-undefined-function)
- [ArgumentError](/languages/elixir/elixir-argumenterror-elixir)

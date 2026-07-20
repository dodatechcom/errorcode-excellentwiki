---
title: "[Solution] Elixir FnCaptureArityError - Brief Description"
description: "Fix Elixir function capture arity errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1040
---

A function capture arity error occurs when `/N` syntax references wrong arity.

## Common Causes

- Using `&Module.function/N` where N does not match
- Capturing a function that does not exist
- Placeholder count not matching expected arity

## How to Fix

Verify function arity:

```elixir
def add(a, b), do: a + b

# WRONG: add/1 does not exist
Enum.map([1, 2], &add/1)

# CORRECT: Use correct arity
Enum.map([1, 2], &add(&1, 10))
```

Check function exists:

```elixir
if function_exported?(MyModule, :my_func, 2) do
  func = &MyModule.my_func/2
  func.(arg1, arg2)
else
  {:error, :function_not_exported}
end
```

## Examples

```elixir
Enum.map([1, 2, 3], &(&1 * 2))
Enum.filter([1, 2, 3, 4, 5], &(&1 > 3))
```

## Related Errors

- [CaptureOperatorError](/languages/elixir/elixir-capture-operator-error)
- [FunctionClauseError](/languages/elixir/elixir-function-clause)

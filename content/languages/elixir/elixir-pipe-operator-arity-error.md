---
title: "[Solution] Elixir PipeOperatorArityError - Brief Description"
description: "Fix Elixir pipe operator arity errors. Learn pipe operator rules."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1003
---

A pipe operator arity error occurs when the piped value does not align with the expected argument position.

## Common Causes

- Piping into a function that does not expect the piped value as first argument
- Using `&capture` with pipes and mismatched arity
- Piping into functions with multiple required arguments

## How to Fix

Ensure the piped value matches the first argument:

```elixir
# WRONG: Syntax error with capture in pipe
"hello world"
|> String.split()
|> Enum.map(String.upcase(&1))

# CORRECT: Use pipe-friendly capture
"hello world"
|> String.split()
|> Enum.map(&String.upcase/1)
```

Break complex pipelines into steps:

```elixir
result =
  "hello world"
  |> String.split()
  |> Enum.map(&String.downcase/1)
  |> Enum.reject(&(&1 == ""))
  |> Enum.join("_")
```

## Examples

```elixir
"  Hello World  "
|> String.trim()
|> String.downcase()
|> String.replace(" ", "_")
```

## Related Errors

- [PipeOperatorError](/languages/elixir/elixir-pipe-error)
- [FunctionClauseError](/languages/elixir/elixir-function-clause)

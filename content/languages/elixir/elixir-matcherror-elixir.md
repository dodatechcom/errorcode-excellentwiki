---
title: "MatchError in Elixir"
description: "Elixir raises MatchError when a pattern match fails on the right-hand side of = operator"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MatchError` is raised when a pattern match fails on the right-hand side of the `=` operator. This occurs when the value does not match the expected pattern.

## Common Causes

- Value does not match expected pattern
- Incorrect pin operator usage
- Pattern expecting specific struct but receiving different type
- Variable binding fails in function head

## How to Fix

Use case expressions for multiple patterns:

```elixir
value = {:ok, "result"}

case value do
  {:ok, result} -> IO.puts("Success: #{result}")
  {:error, reason} -> IO.puts("Error: #{reason}")
  _ -> IO.puts("Unknown")
end
```

Use pin operator for comparison:

```elixir
expected = :ok
result = :ok

^expected = result  # Works
^expected = :error  # MatchError
```

Handle struct matching:

```elixir
defmodule User do
  defstruct name: "", age: 0
end

user = %User{name: "Alice", age: 30}

case user do
  %User{name: name, age: age} when age >= 18 ->
    IO.puts("#{name} is an adult")
  %User{name: name} ->
    IO.puts("#{name} is a minor")
end
```

## Examples

```elixir
{:ok, value} = {:error, "failed"}
# ** (MatchError) no match of right hand side value: {:error, "failed"}
```

## Related Errors

- [FunctionClauseError]({{< relref "/languages/elixir/function-clause" >}})
- [CaseClauseError]({{< relref "/languages/elixir/caseclauseerror" >}})

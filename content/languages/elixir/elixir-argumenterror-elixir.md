---
title: "ArgumentError in Elixir"
description: "Elixir raises ArgumentError when a function receives an invalid argument"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `ArgumentError` is raised when a function receives an argument that is invalid in value but valid in type. This commonly occurs with invalid argument combinations or missing required arguments.

## Common Causes

- Invalid argument value for function
- Wrong number of arguments
- Keyword list missing required keys
- Nil passed where value expected

## How to Fix

Validate arguments explicitly:

```elixir
def set_age(age) when is_integer(age) and age >= 0 and age <= 150 do
  {:ok, age}
end

def set_age(age) do
  raise ArgumentError, "Invalid age: #{inspect(age)}"
end
```

Use guard clauses:

```elixir
def divide(a, b) when b == 0, do: raise(ArgumentError, "Cannot divide by zero")
def divide(a, b), do: a / b
```

Handle keyword arguments:

```elixir
def connect(opts \\ []) do
  host = Keyword.get(opts, :host) || raise ArgumentError, "host is required"
  port = Keyword.get(opts, :port, 8080)
  {host, port}
end
```

## Examples

```elixir
Enum.join([1, 2, 3], 123)
# ** (ArgumentError) argument error
```

## Related Errors

- [FunctionClauseError]({{< relref "/languages/elixir/function-clause" >}})
- [KeyError]({{< relref "/languages/elixir/keyerror-elixir" >}})

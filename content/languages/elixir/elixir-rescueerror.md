---
title: "Rescue Error in Elixir"
description: "Elixir rescue blocks catch exceptions and handle errors from code that may raise"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["rescue", "exception", "try", "catch", "error-handling"]
weight: 5
---

## What This Error Means

Rescue errors in Elixir occur when `try/rescue` blocks fail to catch the expected exception type, or when rescue logic itself contains errors. Proper rescue handling is essential for robust error recovery.

## Common Causes

- Rescue block catches wrong exception type
- Rescue logic throws a new exception
- Missing after block for cleanup
- Re-raising unhandled exceptions
- Exception struct accessed incorrectly

## How to Fix

Use proper rescue structure:

```elixir
try do
  File.read!("data.txt")
rescue
  e in File.Error ->
    IO.puts("File error: #{e.reason}")
    create_default_file()
  e in ArgumentError ->
    IO.puts("Argument error: #{e.message}")
after
  IO.puts("Cleanup complete")
end
```

Catch specific exception types:

```elixir
try do
  String.to_integer(input)
rescue
  ArgumentError -> {:error, :invalid_format}
  OverflowError -> {:error, :too_large}
end
```

Use catch for throws and exits:

```elixir
try do
  receive do
    {:ok, value} -> value
    {:error, reason} -> throw({:error, reason})
  end
catch
  {:error, reason} -> {:caught, reason}
  :exit, reason -> {:exit, reason}
end
```

Create custom exceptions:

```elixir
defmodule MyApp.ValidationError do
  defexception [:message, :field]

  @impl true
  def exception(value) do
    %__MODULE__{message: "Validation failed: #{inspect(value)}", field: :unknown}
  end
end

try do
  raise MyApp.ValidationError, "invalid input"
rescue
  e in MyApp.ValidationError ->
    IO.puts("Validation: #{e.message}")
end
```

## Examples

```elixir
try do
  raise "Something went wrong"
rescue
  RuntimeError -> IO.puts("Caught runtime error")
end
```

## Related Errors

- [FunctionClauseError]({{< relref "/languages/elixir/function-clause" >}})
- [MatchError]({{< relref "/languages/elixir/match-error" >}})

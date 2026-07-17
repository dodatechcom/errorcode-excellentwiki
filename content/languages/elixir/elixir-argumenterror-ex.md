---
title: "ArgumentError in Elixir Functions"
description: "Elixir raises ArgumentError when function arguments are invalid or missing"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["argument", "function", "invalid", "argumenterror"]
weight: 5
---

## What This Error Means

An `ArgumentError` occurs when a function receives invalid arguments. This differs from `FunctionClauseError` in that the function has clauses but the argument itself is malformed.

## Common Causes

- Wrong number of arguments passed
- Nil value where non-nil expected
- Invalid option in keyword list
- Missing required parameter

## How to Fix

Use default values for optional arguments:

```elixir
def greet(name, greeting \\ "Hello") do
  "#{greeting}, #{name}!"
end
```

Validate with guards:

```elixir
def process(list) when is_list(list) and list != [] do
  Enum.map(list, &(&1 * 2))
end

def process([]), do: {:error, :empty_list}
def process(_), do: raise(ArgumentError, "Expected a non-empty list")
```

Handle keyword options:

```elixir
def connect(opts \\ []) do
  host = Keyword.fetch!(opts, :host)  # Raises KeyError if missing
  port = Keyword.get(opts, :port, 443)
  {host, port}
end
```

## Examples

```elixir
String.to_integer("abc")
# ** (ArgumentError) argument error
```

## Related Errors

- [FunctionClauseError]({{< relref "/languages/elixir/function-clause" >}})
- [KeyError]({{< relref "/languages/elixir/keyerror-elixir" >}})

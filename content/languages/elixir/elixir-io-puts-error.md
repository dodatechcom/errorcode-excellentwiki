---
title: "[Solution] Elixir IOPutsError - Brief Description"
description: "Fix Elixir IO.puts errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1022
---

An `IO.puts` error occurs when the argument cannot be converted to a character list.

## Common Causes

- Passing a struct without `String.Chars` implementation
- Using `IO.puts` with a map or keyword list directly
- Attempting to print a PID without `inspect`

## How to Fix

Convert with `inspect` or `to_string`:

```elixir
# WRONG: Tuple does not implement String.Chars
IO.puts({:ok, "hello"})

# CORRECT: Use inspect
IO.inspect({:ok, "hello"}, label: "result")
```

Implement `String.Chars` for custom structs:

```elixir
defmodule User do
  defstruct [:name, :email]
end

defimpl String.Chars, for: User do
  def to_string(%User{name: name, email: email}) do
    "#{name} <#{email}>"
  end
end
```

## Examples

```elixir
IO.puts("Hello, world!")
IO.puts(to_string(42))
```

## Related Errors

- [IOGetsError](/languages/elixir/elixir-io-gets-error)
- [StringCharsError](/languages/elixir/elixir-string-chars-error)

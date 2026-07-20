---
title: "[Solution] Elixir StringCharsError - Brief Description"
description: "Fix Elixir String.Chars protocol errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1024
---

A `String.Chars` error occurs when converting a value that lacks the protocol implementation.

## Common Causes

- String interpolation on a struct without `String.Chars`
- Calling `to_string/1` on a tuple or map
- Missing protocol implementation for custom types

## How to Fix

Implement `String.Chars` for custom structs:

```elixir
defmodule Money do
  defstruct [:amount, :currency]
end

defimpl String.Chars, for: Money do
  def to_string(%Money{amount: amount, currency: currency}) do
    "#{currency} #{amount}"
  end
end

IO.puts(%Money{amount: 100, currency: "USD"})
```

Use `inspect` for debugging:

```elixir
IO.puts(inspect(%{a: 1, b: 2}))
```

## Examples

```elixir
to_string(123)       # "123"
to_string(:atom)     # "atom"
to_string("binary")  # "binary"
```

## Related Errors

- [InspectProtocolError](/languages/elixir/elixir-inspect-protocol-error)
- [ProtocolImplementation](/languages/elixir/elixir-protocol-implementation)

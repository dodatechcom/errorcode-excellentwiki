---
title: "[Solution] Elixir ProtocolDeriveError - Brief Description"
description: "Fix Elixir @derive protocol errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1006
---

A `Protocol.UndefinedError` occurs when using a protocol on a struct without derived implementation.

## Common Causes

- Forgetting to add `@derive` for required protocols
- Using `@derive` with unsupported protocol
- `@fallback_to_any` not set

## How to Fix

Derive built-in protocols:

```elixir
defmodule User do
  @derive [Inspect, Enumerable]
  defstruct [:name, :age]
end
```

Implement protocols manually:

```elixir
defimpl String.Chars, for: User do
  def to_string(%User{name: name, age: age}) do
    "#{name} (#{age})"
  end
end
```

## Examples

```elixir
defmodule Money do
  @derive {Inspect, only: [:amount, :currency]}
  defstruct [:amount, :currency]
end
```

## Related Errors

- [ProtocolImplementation](/languages/elixir/elixir-protocol-implementation)
- [StructFieldError](/languages/elixir/elixir-struct-field-error)

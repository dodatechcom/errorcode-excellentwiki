---
title: "[Solution] Fix protocol not implemented for type in Elixir"
description: "Resolve Protocol.UndefinedError in Elixir by implementing protocols for custom types, using @derive annotations, and adding catch-all Any fallback clauses."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A `Protocol.UndefinedError` is raised when you call a protocol function on a type that does not implement that protocol. Elixir protocols provide polymorphism, and each data type must explicitly implement or derive the protocol before its functions can be called on that type.

The error appears as:

```elixir
** (Protocol.UndefinedError) protocol MyProtocol not implemented for %MyStruct{}
```

## Why It Happens

This error occurs when there is a missing or incomplete protocol implementation:

- Using a protocol on a custom struct without implementing it
- Forgetting to add `@derive` annotation to a struct module
- Implementing the protocol for the wrong module name
- Calling built-in protocols like `Enumerable` on non-enumerable types
- Not implementing protocol for `Any` as a fallback

## How to Fix It

Implement the protocol explicitly for your type:

```elixir
defprotocol Stringifiable do
  def to_string(data)
end

defimpl Stringifiable, for: User do
  def to_string(%User{name: name, age: age}) do
    "#{name} (#{age})"
  end
end
```

Use `@derive` for built-in protocols on custom structs:

```elixir
defmodule User do
  @derive [Enumerable]
  defstruct [:name, :email]

  defimpl Enumerable do
    def count(_user), do: {:error, __MODULE__}
    def member?(_user, _element), do: {:error, __MODULE__}
    def reduce(_user, acc, _fun), do: acc
  end
end
```

Implement the protocol for `Any` as a catch-all fallback:

```elixir
defimpl Stringifiable, for: Any do
  def to_string(data), do: inspect(data)
end

defmodule User do
  @derive [Stringifiable]
  defstruct [:name]
end
```

Check protocol implementation at compile time:

```elixir
if Stringifiable.impl_for?(User) do
  IO.puts("Protocol implemented")
else
  IO.puts("Protocol NOT implemented - add @derive")
end
```

## Common Mistakes

- Implementing the protocol for the wrong struct module name
- Forgetting that `@derive` must appear before `defstruct`
- Not implementing `Enumerable` functions completely (all callbacks required)
- Assuming protocols work across processes without explicit imports
- Using `@derive` without also providing the `defimpl` for custom protocols

## Related Pages

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [KeyError: key not found](/languages/elixir/elixir-keyerror-elixir)
- [BadMapError: expected a map](/languages/elixir/bad-match)

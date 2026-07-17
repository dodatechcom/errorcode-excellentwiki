---
title: "** (Protocol.UndefinedError) protocol not implemented"
description: "A Protocol.UndefinedError occurs when calling a protocol function on a type that doesn't implement the protocol."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `Protocol.UndefinedError` is raised when you call a protocol function on a data type that doesn't implement that protocol. Protocols in Elixir provide a way to achieve polymorphism, and each type must explicitly implement the protocol.

## Common Causes

- Using protocol function on unimplemented type
- Forgetting to derive or implement protocol for custom struct
- Using built-in protocol on incompatible type
- Missing `@derive` annotation for structs

## How to Fix

```elixir
# WRONG: Using protocol on non-implemented type
defprotocol Printable do
  def print(data)
end

Printable.print(42)
# ** (Protocol.UndefinedError) protocol Printable not implemented for 42

# CORRECT: Implement protocol for the type
defimpl Printable, for: Integer do
  def print(data), do: IO.puts("Number: #{data}")
end

Printable.print(42)  # "Number: 42"
```

```elixir
# WRONG: Struct not deriving protocol
defmodule User do
  defstruct [:name, :age]
end

defprotocol Stringifiable do
  def to_string(data)
end

Stringifiable.to_string(%User{name: "Alice", age: 30})
# ** (Protocol.UndefinedError)

# CORRECT: Derive protocol
defmodule User do
  @derive [Stringifiable]
  defstruct [:name, :age]
end

defimpl Stringifiable, for: User do
  def to_string(%User{name: name}), do: name
end
```

## Examples

```elixir
# Example 1: Enumerable on non-enumerable
Enum.each(42, &IO.puts/1)
# ** (Protocol.UndefinedError) protocol Enumerable not implemented for 42

# Example 2: Collectable on map
Collectable.into(%{})
# works, but:
Collectable.into(42)
# ** (Protocol.UndefinedError)

# Example 3: Custom protocol
defprotocol Describable, do: def describe(data)
Describable.describe(:atom)
# ** (Protocol.UndefinedError)
```

## Related Errors

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [BadMapError: expected a map](/languages/elixir/bad-match)

---
title: "[Solution] Elixir Protocol Implementation Clash — Already Implemented Error"
description: "Fix Elixir protocol.claim clash when a protocol is already implemented. Learn about protocol consolidation, derive, and multi-implementation rules."
languages: ["elixir"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A protocol implementation clash error occurs when you try to implement a protocol for a type that already has an implementation. In Elixir, a protocol can only be implemented once per type per consolidation scope. If two modules implement the same protocol for the same type, a compilation error occurs.

## Why It Happens

The most common cause is implementing a protocol for a built-in type that already has an implementation. For example, the `String.Chars` protocol is already implemented for atoms, and trying to implement it again causes this error.

Another frequent cause is consolidating protocols in a dependency that conflicts with your own implementation. If a library implements `MyProtocol` for `String` and you try to implement it again, the consolidation fails.

Protocol delegation to another protocol can cause conflicts. If you delegate `@fallback_to_any` and the `Any` implementation conflicts with a specific implementation, the error occurs.

Finally, implementing a protocol in both a dependency and the main application can cause consolidation conflicts.

## How to Fix It

### Check existing implementations

```elixir
# List all implementations of a protocol
String.Chars.__protocol__(:impls)
```

### Use @derive for struct protocol implementation

```elixir
defmodule User do
  @derive [String.Chars]
  defstruct [:name, :age]

  defimpl String.Chars do
    def to_string(%User{name: name}), do: name
  end
end
```

### Use defderive for macro-based implementation

```elixir
defmodule MyApp.MyProtocol do
  defmacro defderive(module, opts) do
    quote do
      @derive unquote(module)
      defstruct unquote(opts)
    end
  end
end
```

### Avoid implementing protocols for built-in types

```elixir
# Wrong — Atom already implements String.Chars
defimpl String.Chars, for: Atom do
  def to_string(atom), do: Atom.to_string(atom)
end

# Correct — use a custom protocol
defprotocol MyApp.CustomString do
  def to_custom_string(value)
end
```

### Use @fallback_to_any for default implementations

```elixir
defprotocol MyProtocol do
  @fallback_to_any true
  def to_string(value)
end

defimpl MyProtocol, for: Any do
  def to_string(value), do: inspect(value)
end
```

## Common Mistakes

- Not checking if a protocol is already implemented before implementing it
- Implementing protocols for built-in types that already have implementations
- Forgetting to consolidate protocols in production builds
- Using @derive without also defining the implementation
- Not understanding that protocol implementation is per-type, not per-module

## Related Pages

- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
- [Elixir UndefinedFunctionError](/languages/elixir/elixir-undefined-function/)

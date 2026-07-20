---
title: "[Solution] Elixir InspectProtocolError - Brief Description"
description: "Fix Elixir Inspect protocol errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1025
---

An `Inspect` protocol error occurs when calling `inspect/1` on an unsupported struct.

## Common Causes

- Struct without custom Inspect implementation
- Circular references causing infinite recursion
- Exposing sensitive data through inspect output

## How to Fix

Implement Inspect for custom structs:

```elixir
defmodule Password do
  defstruct [:hash]
end

defimpl Inspect, for: Password do
  def inspect(%Password{}, _opts) do
    "#Password<***>"
  end
end
```

Handle circular references:

```elixir
defmodule TreeNode do
  defstruct [:value, :parent]
end

defimpl Inspect, for: TreeNode do
  def inspect(%TreeNode{value: value, parent: nil}, _opts) do
    "#TreeNode<#{value}>"
  end

  def inspect(%TreeNode{value: value}, _opts) do
    "#TreeNode<#{value} (has parent)>"
  end
end
```

## Examples

```elixir
defmodule Config do
  defstruct [:debug, :verbose]

  defimpl Inspect do
    def inspect(%Config{debug: d, verbose: v}, _opts) do
      "#Config<debug=#{d}, verbose=#{v}>"
    end
  end
end
```

## Related Errors

- [StringCharsError](/languages/elixir/elixir-string-chars-error)
- [ProtocolImplementation](/languages/elixir/elixir-protocol-implementation)

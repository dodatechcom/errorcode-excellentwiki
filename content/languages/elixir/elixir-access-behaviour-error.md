---
title: "[Solution] Elixir AccessBehaviourError - Brief Description"
description: "Fix Elixir Access behaviour errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1026
---

An Access behaviour error occurs when using `[]` on a type without Access implementation.

## Common Causes

- Using bracket access on a tuple or binary
- Accessing nested keys through non-Access types
- Using Access on a plain list instead of keyword list

## How to Fix

Use Access-compatible data:

```elixir
data = %{key: "value"}
data[:key]
```

Implement Access for custom types:

```elixir
defmodule Config do
  defstruct [:host, :port]

  defimpl Access do
    def get(config, key), do: Map.get(config, key)
    def get_and_update(config, key, fun), do: Map.get_and_update(config, key, fun)
    def pop(config, key), do: Map.pop(config, key)
  end
end
```

## Examples

```elixir
config = %{db: %{host: "localhost", port: 5432}}
get_in(config, [:db, :host])
```

## Related Errors

- [KeyError](/languages/elixir/elixir-keyerror-elixir)
- [MapError](/languages/elixir/elixir-map-error)

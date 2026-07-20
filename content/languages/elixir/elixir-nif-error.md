---
title: "[Solution] Elixir NIFError - Brief Description"
description: "Fix Elixir NIF errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1035
---

A NIF error occurs when a Native Implemented Function fails to load or crashes.

## Common Causes

- Shared library not found or wrong architecture
- NIF function raising a segfault
- Loading NIF from wrong path

## How to Fix

Ensure the NIF shared library is in the right path:

```elixir
defmodule MyNIF do
  @on_load :load_nif

  def load_nif do
    path = :filename.join(:code.priv_dir(:my_app), "my_nif")
    case :erlang.load_nif(path, 0) do
      :ok -> :ok
      {:error, {:reload, _}} -> :ok
      {:error, reason} -> raise "Failed to load NIF: #{inspect(reason)}"
    end
  end

  def native_add(_a, _b), do: :erlang.nif_error(:nif_not_loaded)
end
```

## Examples

```elixir
MyNIF.native_add(2, 3)
# 5
```

## Related Errors

- [CNodeError](/languages/elixir/elixir-cnode-error)
- [PortError](/languages/elixir/elixir-port-error)

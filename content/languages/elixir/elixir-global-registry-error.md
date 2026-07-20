---
title: "[Solution] Elixir GlobalRegistryError - Brief Description"
description: "Fix Elixir :global module errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1033
---

A `:global` registration error occurs when registering a process name globally across a cluster.

## Common Causes

- Two processes trying to register the same name
- Global name server not available
- Process crashed but name not cleaned up

## How to Fix

Handle name conflicts:

```elixir
case :global.register_name({MyModule, :instance}, self()) do
  :yes -> Logger.info("Registered as global leader")
  :no -> Logger.info("Another process holds this name")
end
```

Use Registry instead:

```elixir
{Registry, keys: :unique, name: MyApp.Registry}
```

## Examples

```elixir
:global.register_name({:leader, MyCluster}, self())

case :global.whereis_name({:leader, MyCluster}) do
  :undefined -> nil
  pid -> pid
end
```

## Related Errors

- [RegistryError](/languages/elixir/elixir-registry-error)
- [NodeConnectError](/languages/elixir/elixir-node-connect-error)

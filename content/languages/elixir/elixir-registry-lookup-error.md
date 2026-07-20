---
title: "[Solution] Elixir RegistryLookupError - Brief Description"
description: "Fix Elixir Registry lookup errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1019
---

A Registry lookup error occurs when trying to find a process that is not registered.

## Common Causes

- Registry process not started
- Looking up a key that was never registered
- Process registered but has crashed

## How to Fix

Start Registry in the supervision tree:

```elixir
children = [
  {Registry, keys: :unique, name: MyApp.Registry},
  {MyWorker, []}
]
Supervisor.start_link(children, strategy: :one_for_one)
```

Look up processes safely:

```elixir
case Registry.lookup(MyApp.Registry, "my_key") do
  [{pid, _extra}] -> {:ok, pid}
  [] -> {:error, :not_found}
end
```

## Examples

```elixir
{:ok, _} = Registry.register(MyApp.Registry, "cache", self())

[{pid, _}] = Registry.lookup(MyApp.Registry, "cache")
send(pid, :refresh)
```

## Related Errors

- [RegistryError](/languages/elixir/elixir-registry-error)
- [ProcessDied](/languages/elixir/elixir-process-died)

---
title: "[Solution] Elixir Registry Lookup or Registration Error — How to Fix"
description: "Fix Elixir Registry lookup and registration errors. Learn how to use Registry for process naming, key lookup, and handle registration conflicts in distributed systems."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Elixir's Registry module provides a scalable and distributed way to register and look up processes. When a process tries to register a name that is already taken, or looks up a name that does not exist, the operation fails.

The most common cause is duplicate name registration. If two processes try to register the same name in the same Registry, the second one gets a conflict error. This is by design to prevent naming collisions.

Another frequent cause is looking up a name that has no registered process. `Registry.lookup(MyRegistry, name)` returns an empty list if no process is registered with that name, and code that expects a tuple will crash.

Race conditions between process registration and lookup are common. If a process crashes and restarts, there is a brief window where the name is not registered. Code that looks up the name during this window gets empty results.

Registry configuration errors cause startup failures. If the Registry is configured with `keys: :duplicate` but the code tries to register unique names, the behavior is different than expected.

Distributed Registry issues arise when nodes connect and disconnect. Names registered on one node may not be visible on another node depending on the Registry configuration.

## Common Error Messages

```
** (ArgumentError) argument error: Registry.register/2 called with already registered name
```

```
** (exit) exited in: Registry.lookup(MyRegistry, :missing_name)
```

```
** (MatchError) no match of right hand side: []
```

```
** (RuntimeError) Registry conflict: key :my_name already registered to #PID<...>
```

## How to Fix It

### Handle registration conflicts gracefully

```elixir
case Registry.register(MyRegistry, :my_name, %{pid: self()}) do
  {:ok, _owner} ->
    # Successfully registered
    :ok

  {:error, {:already_registered, pid}} ->
    # Name is taken — handle the conflict
    Logger.warning("Name already registered to #{inspect(pid)}")
    {:error, :already_registered}
end
```

### Look up names safely

```elixir
case Registry.lookup(MyRegistry, :my_name) do
  [{pid, _meta}] ->
    # Found — use the pid
    GenServer.call(pid, :get_state)

  [] ->
    # Not found — handle gracefully
    Logger.warning("Process not found in registry")
    {:error, :not_found}

  multiple when is_list(multiple) ->
    # Duplicate keys — multiple processes registered
    Logger.warning("Multiple registrations found: #{length(multiple)}")
    {:error, :multiple_found}
end
```

### Use Registry with dynamic supervisors

```elixir
# Start a Registry
{:ok, _} = Registry.start_link(keys: :unique, name: MyApp.Registry)

# Start a DynamicSupervisor
{:ok, _} = DynamicSupervisor.start_link(
  strategy: :one_for_one,
  name: MyApp.DynamicSupervisor
)

# Start a child and register it
def start_child(name, arg) do
  child_spec = %{
    id: MyApp.Worker,
    start: {MyApp.Worker, :start_link, [arg]},
    restart: :temporary
  }

  case DynamicSupervisor.start_child(MyApp.DynamicSupervisor, child_spec) do
    {:ok, pid} ->
      case Registry.register(MyApp.Registry, name, %{pid: pid}) do
        {:ok, _} -> {:ok, pid}
        {:error, {:already_registered, _}} -> {:error, :name_taken}
      end

    {:error, reason} ->
      {:error, reason}
  end
end
```

### Use keys: :duplicate for multiple registrations per key

```elixir
# Allow multiple processes to register with the same key
{:ok, _} = Registry.start_link(keys: :duplicate, name: MyApp.EventRegistry)

# Multiple processes can register for the same event
Registry.register(MyApp.EventRegistry, :user_created, %{handler: self()})
Registry.register(MyApp.EventRegistry, :user_created, %{handler: other_pid})

# Lookup returns all registrations
Registry.lookup(MyApp.EventRegistry, :user_created)
# => [{#PID<...>, %{handler: #PID<...>}}, {#PID<...>, %{handler: #PID<...>}}]
```

### Use via tuples for GenServer naming

```elixir
defmodule MyApp.Worker do
  use GenServer

  def child_spec(name) do
    %{
      id: name,
      start: {__MODULE__, :start_link, [name]},
      restart: :transient
    }
  end

  def start_link(name) do
    GenServer.start_link(__MODULE__, %{}, name: via_tuple(name))
  end

  defp via_tuple(name) do
    {:via, Registry, {MyApp.Registry, name, %{}}}
  end
end
```

## Common Scenarios

- Building a distributed system where processes need unique names across nodes
- Implementing a service registry where clients look up services by name
- Handling process crashes and ensuring names are cleaned up properly

## Prevent It

- Always handle `{:error, {:already_registered, pid}}` when registering names
- Use `Registry.lookup` with pattern matching to handle missing names gracefully
- Consider using `keys: :duplicate` when multiple processes need to register for the same event

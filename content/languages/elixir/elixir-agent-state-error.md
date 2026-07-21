---
title: "[Solution] Elixir Agent State Error -- Concurrent State Corruption"
description: "Fix Elixir agent state errors when Agent.get and Agent.update cause race conditions."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Agent State Error

This error occurs when Agent state is accessed and modified concurrently, leading to inconsistent or corrupted state.

## Common Causes

- Using Agent.get followed by Agent.update without atomicity
- High-concurrency scenarios overwhelming Agent
- Agent state growing unbounded over time
- Not monitoring Agent processes for crashes

## How to Fix

### Use Agent.update for atomic operations

```elixir
# WRONG: read then write race condition
value = Agent.get(:cache, & &1)
Agent.update(:cache, fn _ -> value + 1 end)

# CORRECT: use atomic update
Agent.update(:cache, fn current -> current + 1 end)
```

### Use GenServer for complex state management

```elixir
defmodule Cache do
  use GenServer

  def get(key), do: GenServer.call(__MODULE__, {:get, key})

  def handle_call({:get, key}, _from, state) do
    {:reply, Map.get(state, key), state}
  end
end
```

## Examples

```elixir
defmodule Counter do
  use Agent

  def start_link(initial), do: Agent.start_link(fn -> initial end, name: __MODULE__)
  def increment, do: Agent.update(__MODULE__, &(&1 + 1))
  def get, do: Agent.get(__MODULE__, & &1)
end
```

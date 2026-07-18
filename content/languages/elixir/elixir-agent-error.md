---
title: "[Solution] Elixir Agent Error — Agent Not Started or Timeout"
description: "Fix Elixir Agent errors when processes are not started or timeout occurs. Learn about Agent lifecycle, GenServer alternatives, and process management."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `Agent` error is raised when you try to interact with an Agent process that is not started or has been terminated. The error typically shows `{:error, :noproc}` or `{:error, :timeout}`. Agents are simple state wrappers around GenServer, and they share the same process lifecycle issues.

## Why It Happens

The most common cause is calling `Agent.get/3` or `Agent.update/3` on an Agent that was not started. If the Agent is not registered under the expected name, the call fails.

Another frequent cause is Agent timeout. By default, Agent operations have a 5000ms timeout. If the Agent's callback function takes longer than this, the call times out.

Agent crashes from exceptions in callback functions cause the process to terminate. Subsequent calls to the Agent fail because the process is no longer running.

Using `Agent.start_link` without proper supervision means the Agent is not restarted after a crash.

Finally, name conflicts where multiple Agents try to register under the same name cause the second Agent to fail to start.

## How to Fix It

### Ensure Agent is started before use

```elixir
case Agent.start_link(fn -> %{} end, name: MyApp.Agent) do
  {:ok, pid} -> pid
  {:error, {:already_started, pid}} -> pid
end
```

### Handle timeout errors

```elixir
case Agent.get(MyApp.Agent, & &1, timeout: 10_000) do
  {:error, :timeout} -> {:error, :agent_timeout}
  state -> {:ok, state}
end
```

### Use proper supervision

```elixir
defmodule MyApp.Supervisor do
  use Supervisor

  def start_link(_) do
    Supervisor.start_link(__MODULE__, [], name: __MODULE__)
  end

  def init(_) do
    children = [
      {Agent, name: MyApp.Agent, start: {Agent, :start_link, [fn -> %{} end]}}
    ]

    Supervisor.init(children, strategy: :one_for_one)
  end
end
```

### Use GenServer for complex state management

```elixir
defmodule MyApp.StateManager do
  use GenServer

  def start_link(_) do
    GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  end

  def get(key) do
    GenServer.call(__MODULE__, {:get, key})
  end

  def handle_call({:get, key}, _from, state) do
    {:reply, Map.get(state, key), state}
  end
end
```

### Handle process crashes gracefully

```elixir
def safe_get(agent_name, key) do
  case Agent.get(agent_name, &Map.get(&1, key)) do
    {:error, :noproc} -> {:error, :agent_not_running}
    {:error, :timeout} -> {:error, :agent_timeout}
    value -> {:ok, value}
  end
end
```

## Common Mistakes

- Not starting the Agent before trying to use it
- Not using supervision for Agent processes
- Setting timeout too low for complex operations
- Not handling {:error, :noproc} from dead Agent processes
- Using Agent for complex state that would be better with GenServer

## Related Pages

- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir RuntimeError](/languages/elixir/elixir-rescueerror/)

---
title: "[Solution] Elixir GenServer Call or Cast Error — How to Fix"
description: "Fix Elixir GenServer call and cast errors. Learn why GenServer processes crash on malformed messages and how to handle calls and casts safely."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

GenServer is a behavior module for building stateful processes in Elixir. When a GenServer receives a message it does not handle, or when the `handle_call`, `handle_cast`, or `handle_info` callbacks crash, the process terminates and raises an error.

The most common cause is missing a `handle_call` clause for a message that clients send. If you call `GenServer.call(pid, {:unexpected, data})` and there is no clause matching that tuple, the GenServer process crashes.

Another frequent cause is raising an exception inside a callback. If `handle_call` performs a division by zero, pattern match failure, or any other runtime error, the GenServer process exits and the caller receives an `EXIT` reason.

Timeouts are another source of errors. `GenServer.call` has a default 5-second timeout. If the server is busy processing other messages and does not respond in time, the caller gets a timeout error.

Linked process exits propagate through GenServer. If a process linked to the GenServer crashes, the GenServer also crashes unless it traps exits.

State corruption in long-running GenServer processes can cause pattern match failures in subsequent messages if the state structure changes unexpectedly.

## Common Error Messages

```
** (EXIT from #PID<...>) reason: {:badarg, ...}
```

```
** (FunctionClauseError) no function clause matching in MyApp.Server.handle_call/3
```

```
** (RuntimeError) raised at MyApp.Server.handle_info/2
```

```
** (exit) exited in: GenServer.call(#PID<...>, :timeout_example, 5000)
```

## How to Fix It

### Add catch-all clauses for unexpected messages

```elixir
defmodule MyApp.Server do
  use GenServer

  def handle_call({:get, key}, _from, state) do
    {:reply, Map.get(state, key), state}
  end

  def handle_call(msg, from, state) do
    require Logger
    Logger.warning("Unexpected call: #{inspect(msg)} from #{inspect(from)}")
    {:reply, {:error, :unexpected}, state}
  end

  def handle_cast({:set, key, value}, state) do
    {:noreply, Map.put(state, key, value)}
  end

  def handle_cast(msg, state) do
    require Logger
    Logger.warning("Unexpected cast: #{inspect(msg)}")
    {:noreply, state}
  end

  def handle_info(msg, state) do
    require Logger
    Logger.warning("Unexpected message: #{inspect(msg)}")
    {:noreply, state}
  end
end
```

### Handle timeouts properly

```elixir
# Increase timeout for slow operations
result = GenServer.call(pid, {:slow_operation, data}, 30_000)

# Or use async call with handle_info for non-blocking operations
def handle_call({:slow_operation, data}, from, state) do
  Task.async(fn -> expensive_computation(data) end)
  {:noreply, %{state | pending: Map.put(state.pending, from, data)}}
end

def handle_info({ref, result}, state) when is_reference(ref) do
  {{from, _data}, pending} = Map.pop(state.pending, ref)
  Process.demonitor(ref, [:flush])
  {:reply, result, state}
end
```

### Trap exits for supervised processes

```elixir
def init(_) do
  Process.flag(:trap_exit, true)
  {:ok, %{workers: []}}
end

def handle_info({:EXIT, pid, reason}, state) do
  Logger.warning("Worker #{inspect(pid)} exited: #{inspect(reason)}")
  {:noreply, %{state | workers: List.delete(state.workers, pid)}}
end
```

### Use GenServer.start_link with proper error handling

```elixir
case GenServer.start_link(MyApp.Server, initial_state, name: MyApp.Server) do
  {:ok, pid} ->
    {:ok, pid}

  {:error, {:already_started, pid}} ->
    Logger.info("Server already started at #{inspect(pid)}")
    {:ok, pid}

  {:error, reason} ->
    Logger.error("Failed to start server: #{inspect(reason)}")
    {:error, reason}
end
```

## Common Scenarios

- A GenServer that handles API calls receives an unexpected message format from a client
- A GenServer with linked workers crashes when a worker process terminates unexpectedly
- A GenServer call times out because the process is performing a slow database query

## Prevent It

- Always include catch-all clauses for `handle_call`, `handle_cast`, and `handle_info`
- Use `Task.async` for long-running operations instead of blocking the GenServer
- Set appropriate timeouts for `GenServer.call` based on expected operation duration

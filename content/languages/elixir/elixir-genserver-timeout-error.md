---
title: "[Solution] Elixir GenServer Timeout Error -- Call/Cast Overload"
description: "Fix Elixir GenServer timeout errors when handle_call or handle_cast takes too long to respond."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir GenServer Timeout Error

This error occurs when a GenServer call times out because `handle_call` takes longer than the default 5000ms timeout.

## Common Causes

- handle_call performing blocking I/O operations
- Database queries running inside handle_call without timeout
- Large data processing blocking the GenServer loop
- Too many concurrent calls overwhelming the GenServer

## How to Fix

### Increase timeout or use async patterns

```elixir
# WRONG: long operation inside handle_call
def handle_call(:process, _from, state) do
  result = HeavyJob.run()  # takes 30 seconds
  {:reply, result, state}
end

# CORRECT: return immediately with a task reference
def handle_call({:start_processing, ref}, _from, state) do
  Task.start(fn -> HeavyJob.run() end)
  {:reply, :processing, state}
end
```

### Pass custom timeout

```elixir
GenServer.call(worker, :process, 60_000)  # 60 second timeout
```

## Examples

```elixir
def handle_call({:compute, data}, _from, state) do
  Task.Supervisor.start_child(TaskSupervisor, fn ->
    result = expensive_computation(data)
    GenServer.cast(self(), {:result, result})
  end)
  {:reply, :started, state}
end
```

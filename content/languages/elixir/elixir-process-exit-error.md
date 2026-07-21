---
title: "[Solution] Elixir Process Exit Error -- Unhandled Process Exits"
description: "Fix Elixir process exit errors when processes exit without proper handling or monitoring."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Process Exit Error

This error occurs when a process exits due to an unhandled error or when `exit/1` is called without proper trapping.

## Common Causes

- Process crashes without linked supervisor to restart it
- Not trapping exits in a process that needs to survive linked crashes
- Using `exit/1` where `throw` or `raise` is more appropriate
- Linked process dying causes the parent to die too

## How to Fix

### Trap exits when needed

```elixir
defmodule ResilientWorker do
  use GenServer

  def init(_) do
    Process.flag(:trap_exit, true)
    {:ok, %{}}
  end

  def handle_info({:EXIT, pid, reason}, state) do
    IO.puts("Linked process #{inspect(pid)} exited: #{inspect(reason)}")
    {:noreply, state}
  end
end
```

### Use Process.monitor for non-linked monitoring

```elixir
pid = spawn(fn -> work() end)
ref = Process.monitor(pid)

receive do
  {:DOWN, ^ref, :process, ^pid, reason} ->
    IO.puts("Process exited: #{inspect(reason)}")
after
  5000 -> IO.puts("Timeout waiting for process")
end
```

## Examples

```elixir
defmodule GracefulServer do
  use GenServer

  def init(_) do
    Process.flag(:trap_exit, true)
    {:ok, %{workers: []}}
  end

  def handle_cast({:spawn_worker, func}, state) do
    pid = spawn_link(func)
    {:noreply, %{state | workers: [pid | state.workers]}}
  end

  def handle_info({:EXIT, pid, reason}, state) do
    IO.puts("Worker #{inspect(pid)} died: #{inspect(reason)}")
    {:noreply, %{state | workers: List.delete(state.workers, pid)}}
  end
end
```

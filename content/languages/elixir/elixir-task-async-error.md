---
title: "[Solution] Elixir TaskAsyncError - Brief Description"
description: "Fix Elixir Task.async and Task.await errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1014
---

A Task.async/await error occurs when the spawned task crashes or times out.

## Common Causes

- Task crashing without returning a value
- `Task.await` timeout exceeded
- Not linking tasks to a parent process

## How to Fix

Use `Task.Supervisor` for fault-tolerant tasks:

```elixir
{:ok, pid} = Task.Supervisor.start_child(MyApp.TaskSupervisor, fn ->
  risky_operation()
end)
```

Set appropriate timeouts:

```elixir
task = Task.async(fn -> long_running_job() end)
result = Task.await(task, 30_000)
```

Handle task failures:

```elixir
case Task.yield(task, 5000) || Task.shutdown(task) do
  {:ok, result} -> handle_result(result)
  nil -> handle_timeout()
end
```

## Examples

```elixir
defmodule Parallel do
  def map_with_supervisor(items, fun) do
    items
    |> Enum.map(fn item ->
      Task.Supervisor.async(MyApp.TaskSupervisor, fn -> fun.(item) end)
    end)
    |> Enum.map(&Task.await/1)
  end
end
```

## Related Errors

- [TaskError](/languages/elixir/elixir-task-error)
- [SupervisorError](/languages/elixir/elixir-supervisor-error)

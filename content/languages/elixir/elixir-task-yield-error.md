---
title: "[Solution] Elixir Task Yield Error -- Unhandled Task Results"
description: "Fix Elixir task yield errors when Task.yield returns nil for tasks that have not completed."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Task Yield Error

This error occurs when `Task.yield/2` returns `nil` because the task has not completed within the timeout period.

## Common Causes

- Default 5000ms timeout too short for long-running tasks
- Not handling nil return from Task.yield
- Using Task.yield without a fallback strategy
- Task crashed before yield was called

## How to Fix

### Handle nil return

```elixir
# WRONG: not handling nil
{:ok, result} = Task.yield(task)

# CORRECT: handle nil with timeout
case Task.yield(task, 10_000) do
  {:ok, result} -> result
  nil ->
    Task.shutdown(task, :brutal_kill)
    {:error, :timeout}
end
```

### Use Task.yield_many for multiple tasks

```elixir
tasks = Enum.map(urls, &Task.async(fn -> fetch(&1) end))
results = Task.yield_many(tasks, timeout: 30_000)

Enum.map(results, fn
  {task, {:ok, result}} -> result
  {task, nil} -> {:error, :timeout}
end)
```

## Examples

```elixir
def fetch_with_timeout(task, timeout \\ 5000) do
  case Task.yield(task, timeout) do
    {:ok, result} -> {:ok, result}
    nil ->
      Task.shutdown(task)
      {:error, :timeout}
  end
end
```

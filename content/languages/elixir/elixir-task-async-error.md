---
title: "[Solution] Elixir Task Async Error -- Unhandled Task Exceptions"
description: "Fix Elixir task async errors when tasks started with Task.async raise exceptions."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Task Async Error

This error occurs when tasks started with `Task.async/1` crash and the calling process does not handle the error.

## Common Causes

- Not calling Task.await to collect results
- Exceptions in async tasks not being caught
- Using Task.async for fire-and-forget instead of Task.start
- Multiple Task.async calls without awaiting all

## How to Fix

### Always await async tasks

```elixir
# WRONG: fire-and-forget with async
Task.async(fn -> risky_operation() end)

# CORRECT: await the result
task = Task.async(fn -> risky_operation() end)
result = Task.await(task)
```

### Use Task.Supervisor for fault tolerance

```elixir
def fetch_all(urls) do
  tasks = Enum.map(urls, fn url ->
    Task.Supervisor.async_nolink(MySupervisor, fn ->
      HTTPClient.get(url)
    end)
  end)

  Enum.map(tasks, fn task ->
    Task.yield(task) || Task.shutdown(task, :brutal_kill)
  end)
end
```

## Examples

```elixir
def process_concurrently(items) do
  items
  |> Task.async_stream(&process_item/1)
  |> Enum.to_list()
end
```

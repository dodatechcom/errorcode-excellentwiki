---
title: "[Solution] Elixir Task Async or Await Error — How to Fix"
description: "Fix Elixir Task.async and Task.await errors. Learn why tasks crash, how to handle timeouts, and how to manage concurrent computations safely."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Elixir Tasks provide a simple way to run functions concurrently. When a task process crashes or `Task.await` is called incorrectly, the caller receives an error that propagates the failure.

The most common cause is the task process crashing. If the function passed to `Task.async` raises an exception, `Task.await` re-raises that exception in the calling process.

Another frequent cause is timeout. `Task.await` has a default 5-second timeout. If the task takes longer, `Task.await` raises a timeout error. The task process continues running even after the timeout.

Calling `Task.await` multiple times on the same task reference causes the second call to hang indefinitely because the result has already been consumed.

Linked process exits propagate through tasks. If a task's parent process crashes, the task also crashes unless it traps exits. Conversely, a crashing task does not crash the parent unless the parent is awaiting the result.

Tasks started with `Task.async` are linked to the caller. If you do not need the result, use `Task.start` or `Task.Supervisor.start_nolink` to avoid linking.

Unstructured concurrency with many concurrent tasks can overwhelm the system. Elixir does not limit the number of processes, so creating thousands of tasks simultaneously can exhaust memory.

## Common Error Messages

```
** (RuntimeError) raised at Task.await/1
```

```
** (exit) exited in: Task.await(%Task{...}, 5000)
```

```
** (MatchError) no match of right hand side: {:EXIT, #PID<...>, ...}
```

```
** (ArgumentError) argument error: task already awaited
```

## How to Fix It

### Handle task crashes in Task.await

```elixir
task = Task.async(fn ->
  if something_wrong? do
    raise "Something went wrong"
  end
  :ok
end)

try do
  result = Task.await(task, 10_000)
  {:ok, result}
rescue
  e ->
    Task.shutdown(task, :brutal_kill)
    {:error, e.message}
end
```

### Use Task.Supervisor for supervised tasks

```elixir
# Start a Task.Supervisor
{:ok, _} = Task.Supervisor.start_link(name: MyApp.TaskSupervisor)

# Start supervised tasks that do not crash the caller
task = Task.Supervisor.async_nolink(MyApp.TaskSupervisor, fn ->
  risky_operation()
end)

# Await with timeout handling
result = case Task.yield(task, 15_000) || Task.shutdown(task) do
  {:ok, result} -> result
  nil -> :timeout
end
```

### Avoid awaiting the same task twice

```elixir
task = Task.async(fn -> expensive_computation() end)

# Correct — await once
result = Task.await(task, 30_000)

# Wrong — second await will hang
# result2 = Task.await(task)
```

### Use Task.async_stream for concurrent map operations

```elixir
# Process a list concurrently
items |> Task.async_stream(&process_item/1, timeout: 30_000)
|> Enum.to_list()

# With error handling
items
|> Task.async_stream(&process_item/1, timeout: 30_000, on_timeout: :kill_task)
|> Enum.each(fn
  {:ok, result} -> handle_result(result)
  {:exit, reason} -> Logger.error("Task failed: #{inspect(reason)}")
end)
```

### Monitor tasks for long-running operations

```elixir
task = Task.async(fn -> long_running_operation() end)

# Poll for completion instead of blocking
Stream.repeatedly(fn ->
  case Task.yield(task, 1000) do
    {:ok, result} -> {:done, result}
    nil -> {:running, nil}
  end
end)
|> Enum.find_value(fn
  {:done, result} -> result
  {:running, nil} -> nil
end)
```

## Common Scenarios

- Running multiple API calls concurrently and collecting results
- Processing a large batch of items with parallel computation
- Background tasks that should not crash the main process if they fail

## Prevent It

- Use `Task.Supervisor.async_nolink` for tasks that might crash to protect the caller
- Always set appropriate timeouts in `Task.await` and `Task.yield`
- Use `Task.async_stream` for concurrent processing of collections instead of manual task management

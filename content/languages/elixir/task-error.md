---
title: "** (Task) error in async task"
description: "A Task error occurs when a spawned task crashes or returns an error during execution."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Task error occurs when an asynchronous task crashes or encounters an error during execution. When using `Task.async/1`, if the task process crashes, calling `Task.await/1` will raise an error, typically wrapping the original crash reason.

## Common Causes

- Task function throws an exception
- Task process receives an unexpected message
- Task exceeds timeout limit
- Task function calls `raise` or `throw`

## How to Fix

```elixir
# WRONG: Not handling task errors
task = Task.async(fn -> raise "oops" end)
result = Task.await(task)
# ** (RuntimeError) oops

# CORRECT: Use Task.yield/2 or try-catch
task = Task.async(fn -> raise "oops" end)
case Task.yield(task, 5000) do
  {:ok, result} -> result
  nil ->
    Task.shutdown(task, :brutal_kill)
    {:error, :timeout}
end
```

```elixir
# WRONG: Not supervising tasks
Task.async(fn -> risky_operation() end)

# CORRECT: Use Task.Supervisor for fault tolerance
Task.Supervisor.start_child(MySupervisor, fn ->
  try do
    risky_operation()
  rescue
    e -> Logger.error("Task failed: #{inspect(e)}")
  end
end)
```

## Examples

```elixir
# Example 1: Task with raise
task = Task.async(fn -> raise "boom" end)
Task.await(task)
# ** (RuntimeError) boom

# Example 2: Task timeout
task = Task.async(fn ->
  :timer.sleep(10000)
  :ok
end)
Task.await(task, 1000)
# ** (ArgumentError) task timed out

# Example 3: Task with exit
task = Task.async(fn -> exit(:killed) end)
Task.await(task)
# ** (exit) :killed
```

## Related Errors

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [ArgumentError: wrong number of arguments](/languages/elixir/argument-error4)

---
title: "[Solution] Fix process died EXIT error in Elixir"
description: "Diagnose and fix process exit errors in Elixir by using Process.monitor, trapping exits with trap_exit, and configuring proper supervision strategies."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 9
---

## What This Error Means

A process exit error occurs when a linked process terminates unexpectedly, sending an EXIT signal to its parent. This is displayed as:

```elixir
** (EXIT from <0.123.0>) process died
```

or when caught:

```elixir
{:EXIT, #PID<0.123.0>, {:shutdown, :normal}}
```

Each Elixir process is isolated, and when one crashes, its exit signal propagates to linked processes unless the exit is trapped.

## Why It Happens

This error occurs when a linked process terminates abnormally:

- A child process crashes without trapping exits
- A GenServer or Task terminates due to an unhandled exception
- The parent process receives an untrapped EXIT signal
- A supervision tree is not properly configured for expected crashes
- Using `spawn_link` without handling the linked process's exit

## How to Fix It

Trap exits in processes that need to handle linked process terminations gracefully:

```elixir
defmodule Worker do
  use GenServer

  def init(_) do
    Process.flag(:trap_exit, true)
    {:ok, %{}}
  end

  def handle_info({:EXIT, _pid, reason}, state) do
    IO.puts("Linked process exited: #{inspect(reason)}")
    {:noreply, state}
  end
end
```

Use proper supervision strategies to handle process crashes:

```elixir
defmodule MySupervisor do
  use Supervisor

  def init(_) do
    children = [
      {Worker, []}
    ]

    Supervisor.init(children, strategy: :one_for_one)
  end
end
```

Use `Task.async` with proper error handling:

```elixir
# WRONG: Ignoring process exit
task = Task.async(fn -> raise "boom" end)
Task.await(task)  # Crashes caller

# CORRECT: Handle errors within the task
task = Task.async(fn ->
  try do
    do_work()
  rescue
    e -> {:error, e}
  end
end)

case Task.yield(task) do
  {:ok, {:error, reason}} -> handle_error(reason)
  {:ok, result} -> handle_result(result)
  nil -> Task.shutdown(task)
end
```

Use `Process.monitor/1` instead of linking for non-critical monitoring:

```elixir
pid = spawn(fn -> work() end)
ref = Process.monitor(pid)

receive do
  {:DOWN, ^ref, :process, ^pid, reason} ->
    IO.puts("Process #{inspect(pid)} down: #{inspect(reason)}")
end
```

## Common Mistakes

- Not setting `Process.flag(:trap_exit, true)` in processes that link to workers
- Using `spawn_link` in hot paths where process crashes are expected
- Choosing the wrong supervision strategy (e.g., `:one_for_one` vs `:rest_for_one`)
- Not implementing `terminate/2` callback in GenServers to clean up resources
- Assuming `Task.async` automatically handles linked process failures

## Related Pages

- [GenServer timeout in Elixir](/languages/elixir/task-error)
- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [BadMatchError in Elixir](/languages/elixir/bad-match)

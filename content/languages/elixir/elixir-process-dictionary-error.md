---
title: "[Solution] Elixir Process Dictionary Error -- Shared Mutable State"
description: "Fix Elixir process dictionary errors when using Process dictionary instead of proper state management."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["warning"]
---

# Elixir Process Dictionary Error

This error occurs when the process dictionary is misused as shared mutable state, leading to race conditions and bugs.

## Common Causes

- Using `Process.put/2` for state that should be in GenServer
- Process dictionary values lost on process crash and restart
- Not considering process dictionary isolation in testing
- Using process dictionary for inter-process communication

## How to Fix

### Use GenServer for persistent state

```elixir
# WRONG: using process dictionary for state
def increment_counter do
  count = Process.get(:counter, 0)
  Process.put(:counter, count + 1)
end

# CORRECT: use GenServer
defmodule Counter do
  use GenServer

  def init(_), do: {:ok, 0}

  def increment(pid), do: GenServer.call(pid, :increment)

  def handle_call(:increment, _from, count) do
    {:reply, count + 1, count + 1}
  end
end
```

## Examples

```elixir
# Process dictionary is OK for request-scoped data
def call_with_metadata(request_id) do
  Process.put(:request_id, request_id)
  do_work()
end

def do_work do
  request_id = Process.get(:request_id)
  Logger.metadata(request_id: request_id)
end
```

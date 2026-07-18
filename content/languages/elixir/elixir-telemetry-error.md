---
title: "[Solution] Fix telemetry handler function crashed error in Elixir"
description: "Resolve telemetry handler crashes in Elixir by wrapping handler logic in try-rescue, checking for nil values, and isolating handler failures properly."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 7
---

## What This Error Means

A telemetry error occurs when a handler function attached to a telemetry event crashes during execution. Telemetry events fire synchronously, so a crashing handler can disrupt the event caller.

The error appears as:

```elixir
telemetry handler function crashed
** (RuntimeError) handler failed
```

or in logs:

```elixir
[error] Telemetry event :my_event handler MyHandler crashed with reason: :badarg
```

## Why It Happens

This error occurs when handler functions fail to handle event data:

- Handler functions raise exceptions on unexpected data
- Missing keys in the metadata or measurements maps
- Not accounting for nil or missing values in telemetry events
- Handlers performing side effects that fail (e.g., network calls)
- Incorrect handler function arity or return type

## How to Fix It

Wrap handler logic in try-rescue blocks:

```elixir
defmodule SafeHandler do
  def handle_event(_event, measurements, metadata, _config) do
    try do
      process_measurements(measurements)
      process_metadata(metadata)
    rescue
      e ->
        IO.puts("Handler error: #{inspect(e)}")
    catch
      kind, reason ->
        IO.puts("Handler caught #{kind}: #{inspect(reason)}")
    end
  end
end
```

Check for expected keys before accessing them:

```elixir
def handle_event(event, measurements, metadata, _config) do
  duration = Map.get(measurements, :duration, 0)
  system_time = Map.get(measurements, :system_time, System.system_time())

  case event do
    [:my_app, :request, :stop] ->
      Logger.info("Request took #{duration}us")
    _ ->
      :ok
  end
end
```

Register handlers with proper error isolation:

```elixir
# WRONG: Handler that can crash on nil
:telemetry.attach("my-handler", [:my_app, :event], fn _event, measurements, _meta, _config ->
  1 / measurements[:value]  # crashes if :value is nil
end, %{})

# CORRECT: Guard against nil values
:telemetry.attach("my-handler", [:my_app, :event], fn _event, measurements, _meta, _config do
  case Map.get(measurements, :value) do
    nil -> :ok
    0 -> :ok
    value -> process(1 / value)
  end
end, %{})
```

Use `:telemetry.attach_many` for bulk registration with shared safety:

```elixir
events = [
  [:my_app, :request, :start],
  [:my_app, :request, :stop],
  [:my_app, :request, :exception]
]

:telemetry.attach_many("my-handler", events, &SafeHandler.handle_event/4, %{})
```

## Common Mistakes

- Not wrapping handler logic in try-rescue to isolate failures
- Assuming all telemetry events provide the same measurements and metadata
- Performing slow or blocking operations inside telemetry handlers
- Forgetting to detach handlers in tests, causing cross-test pollution
- Not using `:telemetry.span/3` for automatic timing and error measurement

## Related Pages

- [GenServer timeout in Elixir](/languages/elixir/task-error)
- [Process died EXIT error](/languages/elixir/elixir-process-died)
- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)

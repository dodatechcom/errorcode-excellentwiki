---
title: "[Solution] Elixir GenServerCastError - Brief Description"
description: "Fix Elixir GenServer.cast errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1016
---

A GenServer.cast error occurs when a cast message is not handled or the GenServer is not running.

## Common Causes

- `handle_cast` clause does not match the sent message
- Sending a cast to a stopped process
- Not returning `{:noreply, new_state}` from `handle_cast`

## How to Fix

Match all expected cast messages:

```elixir
defmodule Counter do
  use GenServer

  def handle_cast({:increment, amount}, state) do
    {:noreply, state + amount}
  end

  def handle_cast({:set, value}, _state) do
    {:noreply, value}
  end

  def handle_cast(msg, state) do
    IO.warn("Unhandled cast: #{inspect(msg)}")
    {:noreply, state}
  end
end
```

## Examples

```elixir
GenServer.cast(logger, {:log, "user signed in"})
GenServer.cast(cache, {:invalidate, :user_cache})
```

## Related Errors

- [GenServerCallTimeout](/languages/elixir/elixir-genserver-call-timeout)
- [GenServerError](/languages/elixir/elixir-genserver-error)

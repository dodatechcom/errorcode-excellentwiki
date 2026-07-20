---
title: "[Solution] Elixir PhoenixLiveViewError - Brief Description"
description: "Fix Elixir Phoenix LiveView errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1012
---

A Phoenix LiveView error occurs when the process crashes or encounters invalid state transitions.

## Common Causes

- Accessing socket assigns not set in `mount/3`
- Crash during render causing full page reload
- Not matching event names in `handle_event`

## How to Fix

Initialize all assigns in `mount/3`:

```elixir
defmodule MyAppWeb.CounterLive do
  use Phoenix.LiveView

  def mount(_params, _session, socket) do
    {:ok, assign(socket, count: 0, items: [])}
  end
end
```

Handle all event patterns:

```elixir
def handle_event("increment", _params, socket) do
  {:noreply, update(socket, :count, &(&1 + 1))}
end

def handle_event("unknown", _params, socket) do
  {:noreply, socket}
end
```

## Examples

```elixir
def handle_event("save", %{"name" => name}, socket) do
  case Accounts.create_user(%{name: name}) do
    {:ok, user} ->
      {:noreply, assign(socket, :user, user) |> put_flash(:info, "Saved!")}
    {:error, _changeset} ->
      {:noreply, put_flash(socket, :error, "Failed")}
  end
end
```

## Related Errors

- [PhoenixControllerError](/languages/elixir/elixir-phoenix-controller-error)
- [PhoenixChannelError](/languages/elixir/elixir-phoenix-channel-error)

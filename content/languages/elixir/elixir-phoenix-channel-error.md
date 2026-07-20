---
title: "[Solution] Elixir PhoenixChannelError - Brief Description"
description: "Fix Elixir Phoenix channel errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1013
---

A Phoenix channel error occurs when a client cannot join a topic or a message handler fails.

## Common Causes

- Client joining a topic not authorized in `join/3`
- Not returning `{:ok, socket}` from `join/3`
- PubSub not configured for the endpoint

## How to Fix

Authorize topics in `join/3`:

```elixir
defmodule MyAppWeb.RoomChannel do
  use Phoenix.Channel

  def join("room:" <> room_id, _params, socket) do
    if authorized?(socket, room_id) do
      {:ok, assign(socket, room_id: room_id)}
    else
      {:error, %{reason: "unauthorized"}}
    end
  end

  defp authorized?(_socket, _room_id), do: true
end
```

Handle incoming messages:

```elixir
def handle_in("new_message", %{"body" => body}, socket) do
  broadcast!(socket, "new_message", %{
    body: body,
    user: socket.assigns.user_id
  })
  {:noreply, socket}
end
```

## Examples

```elixir
def handle_in("typing", _params, socket) do
  broadcast_from!(socket, "user_typing", %{user_id: socket.assigns.user_id})
  {:noreply, socket}
end
```

## Related Errors

- [PhoenixLiveViewError](/languages/elixir/elixir-phoenix-liveview-error)
- [PubSubError](/languages/elixir/elixir-pubsub-error)

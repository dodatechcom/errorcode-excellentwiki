---
title: "[Solution] Elixir PubSub Broadcast Error — How to Fix"
description: "Fix Elixir PubSub broadcast errors. Learn how to use Phoenix PubSub for message distribution, handle delivery failures, and manage topic subscriptions."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

PubSub (Publish/Subscribe) in Elixir allows processes to broadcast messages to all subscribers of a topic. When broadcasting fails, it usually means the PubSub system is not started, the topic is invalid, or the message format is incorrect.

The most common cause is the PubSub process not being started. If `Phoenix.PubSub` or a custom PubSub module is not in the supervision tree, broadcast calls fail silently or raise errors.

Another frequent cause is topic format issues. Topics must be strings and cannot be atoms, numbers, or other types. Using `nil` or an empty string as a topic also causes problems.

Message serialization failures occur when broadcasting complex data structures. If the PubSub system uses a serializer that cannot handle certain types (like functions or references), the broadcast fails.

Subscribing to a topic after a broadcast has already occurred means missing messages. PubSub is real-time — there is no message queue for late subscribers.

Node connectivity issues in distributed systems cause broadcasts to not reach subscribers on other nodes. The nodes must be connected and the PubSub must be configured for distributed operation.

The PubSub adapter must be configured correctly. Using `Phoenix.PubSub.PG2` for local-only systems and `Phoenix.PubSub.Redis` for distributed systems requires different configurations.

## Common Error Messages

```
** (ArgumentError) argument error: PubSub.broadcast/3 requires a string topic
```

```
** (exit) exited in: Phoenix.PubSub.PG2.broadcast/3
```

```
** (RuntimeError) PubSub system not started — add Phoenix.PubSub to your supervision tree
```

```
** (MatchError) no match of right hand side: {:error, :serialization_failed}
```

## How to Fix It

### Add PubSub to your supervision tree

```elixir
defmodule MyApp.Application do
  use Application

  def start(_type, _args) do
    children = [
      {Phoenix.PubSub, name: MyApp.PubSub},
      MyApp.Repo,
      MyAppWeb.Endpoint
    ]

    Supervisor.start_link(children, strategy: :one_for_one, name: MyApp.Supervisor)
  end
end
```

### Broadcast messages correctly

```elixir
# Broadcast to all subscribers of a topic
Phoenix.PubSub.broadcast(MyApp.PubSub, "user:123", %{
  event: "user_updated",
  payload: %{name: "Alice"}
})

# Broadcast with a specific message format
Phoenix.PubSub.broadcast(MyApp.PubSub, "notifications", {:new_message, "Hello"})
```

### Subscribe to topics

```elixir
# Subscribe to a specific topic
Phoenix.PubSub.subscribe(MyApp.PubSub, "user:123")

# Subscribe with a wildcard
Phoenix.PubSub.subscribe(MyApp.PubSub, "user:*")

# In a GenServer
def init(_) do
  Phoenix.PubSub.subscribe(MyApp.PubSub, "events")
  {:ok, %{messages: []}}
end

def handle_info({:event, data}, state) do
  {:noreply, %{state | messages: [data | state.messages]}}
end
```

### Handle broadcast errors gracefully

```elixir
case Phoenix.PubSub.broadcast(MyApp.PubSub, topic, message) do
  :ok ->
    :success

  {:error, reason} ->
    Logger.error("Broadcast failed: #{inspect(reason)}")
    {:error, reason}
end
```

### Use distributed PubSub across nodes

```elixir
# In config/config.exs
config :my_app, MyApp.PubSub,
  adapter: Phoenix.PubSub.PG2,
  pool_size: 5

# On each node, ensure the same PubSub name is started
# Nodes must be connected via Erlang distribution
Node.connect(:"node2@hostname")
```

## Common Scenarios

- Broadcasting real-time updates to connected WebSocket clients
- Notifying multiple GenServer processes about system events
- Implementing a distributed notification system across multiple nodes

## Prevent It

- Always verify PubSub is started by adding it to your application's supervision tree
- Use string topics and handle subscription in process `init` functions
- Test broadcasts with `Phoenix.PubSub.subscribe` before broadcasting to verify subscribers receive messages

---
title: "[Solution] Elixir NodeConnectError - Brief Description"
description: "Fix Elixir distributed node connection errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1032
---

A `Node.connect` error occurs when a distributed Erlang node cannot connect to another node.

## Common Causes

- EPMD not running
- Nodes using different cookie values
- Network firewall blocking the port

## How to Fix

Set the same cookie:

```elixir
Node.set_cookie(:my_secret_cookie)
```

Handle connection failures:

```elixir
def connect_to_node(node_name) do
  if Node.connect(node_name) do
    Logger.info("Connected to #{node_name}")
    {:ok, node_name}
  else
    Logger.warning("Failed to connect to #{node_name}")
    {:error, :connect_failed}
  end
end
```

## Examples

```elixir
Node.connect(:"node1@host1.example.com")
Node.connect(:"node2@host2.example.com")
Node.list()
```

## Related Errors

- [GlobalRegistryError](/languages/elixir/elixir-global-registry-error)
- [ProcessDied](/languages/elixir/elixir-process-died)

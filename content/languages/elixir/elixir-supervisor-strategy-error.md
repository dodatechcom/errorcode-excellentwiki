---
title: "[Solution] Elixir SupervisorStrategyError - Brief Description"
description: "Fix Elixir supervisor strategy errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1018
---

A supervisor strategy error occurs when a child process crashes repeatedly beyond restart limits.

## Common Causes

- Child process crashing in a loop
- Wrong supervision strategy for dependencies
- `max_restarts` exceeded

## How to Fix

Choose the right strategy:

```elixir
children = [
  {Agent, fn -> {:ok, %{}} end},
  {Worker, []}
]
Supervisor.start_link(children, strategy: :one_for_one)
```

Increase restart tolerance:

```elixir
Supervisor.start_link(children,
  strategy: :one_for_one,
  max_restarts: 10,
  max_seconds: 60
)
```

## Examples

```elixir
defmodule Application.Supervisor do
  use Supervisor

  def init(_arg) do
    children = [
      {DynamicSupervisor, name: DynamicSupervisor, strategy: :one_for_one},
      {Cache, []}
    ]
    Supervisor.init(children, strategy: :rest_for_one)
  end
end
```

## Related Errors

- [SupervisorError](/languages/elixir/elixir-supervisor-error)
- [ProcessDied](/languages/elixir/elixir-process-died)

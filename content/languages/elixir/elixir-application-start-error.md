---
title: "[Solution] Elixir Application Start Error -- Incorrect Application Callback"
description: "Fix Elixir application start errors when the Application.start/2 callback is not implemented correctly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Application Start Error

This error occurs when the application callback module does not correctly implement the `start/2` function or supervision tree.

## Common Causes

- Missing `use Application` in the application module
- `start/2` not returning `{:ok, pid}` or `{:ok, pid, state}`
- Circular dependencies between applications
- Not starting a supervisor as the root of the tree

## How to Fix

### Implement correct start callback

```elixir
defmodule MyApp.Application do
  use Application

  def start(_type, _args) do
    children = [
      MyApp.Repo,
      MyAppWeb.Telemetry,
      {Phoenix.PubSub, name: MyApp.PubSub},
      MyAppWeb.Endpoint
    ]

    opts = [strategy: :one_for_one, name: MyApp.Supervisor]
    Supervisor.start_link(children, opts)
  end

  def config_change(changed, _new, removed) do
    MyAppWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
```

### Check mix.exs configuration

```elixir
def application do
  [
    extra_applications: [:logger, :runtime_tools],
    mod: {MyApp.Application, []}
  ]
end
```

## Examples

```elixir
defmodule MyApp.Application do
  use Application

  @impl true
  def start(_type, _args) do
    children = [
      {MyApp.Worker, []},
      {MyApp.Cache, []}
    ]

    Supervisor.start_link(children, strategy: :one_for_one)
  end
end
```

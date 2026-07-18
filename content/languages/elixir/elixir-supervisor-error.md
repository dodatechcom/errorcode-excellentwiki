---
title: "[Solution] Elixir Supervisor Tree or Child Spec Error — How to Fix"
description: "Fix Elixir supervisor tree and child spec errors. Learn how to define proper child specifications, handle supervisor restarts, and build fault-tolerant supervision trees."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Elixir supervisors monitor child processes and restart them when they crash. When the child specification is malformed or the supervisor tree is incorrectly configured, the supervisor either refuses to start or restarts children in unexpected ways.

The most common cause is an invalid `child_spec` function. If your module returns a map missing required keys like `:id`, `:start`, or `:restart`, the supervisor rejects the child.

Another frequent cause is incorrect restart strategies. Using `:one_for_one` when a child depends on another child can leave the system in an inconsistent state. The `:rest_for_one` and `:one_for_all` strategies exist for specific dependency patterns.

Circular dependencies in supervision trees cause deadlocks. If supervisor A monitors supervisor B and supervisor B monitors supervisor A, starting either one blocks indefinitely.

Dynamic supervisors require explicit child specifications. Unlike static supervisors that use the `children` list at compile time, dynamic supervisors need `Supervisor.start_child` with a complete child spec at runtime.

Missing OTP application dependencies can cause supervisor startup failures. If your application depends on another application that is not started, the supervisor tree cannot initialize.

## Common Error Messages

```
** (ArgumentError) argument error: expected child_spec/0 to return a map, got: ...
```

```
** (exit) {:bad_start, {:error, {:badarg, ...}}}
```

```
** (exit) {:shutdown, {:failed_to_start_child, MyApp.Worker, :already_started}}
```

```
** (exit) {:bad_start, {:error, {:not_started, :some_application}}}
```

## How to Fix It

### Define proper child_spec in your module

```elixir
defmodule MyApp.Worker do
  use GenServer

  def child_spec(init_arg) do
    %{
      id: __MODULE__,
      start: {__MODULE__, :start_link, [init_arg]},
      restart: :permanent,
      shutdown: 5000,
      type: :worker
    }
  end

  def start_link(arg), do: GenServer.start_link(__MODULE__, arg)
end
```

### Configure the correct restart strategy

```elixir
defmodule MyApp.Application do
  use Application

  def start(_type, _args) do
    children = [
      MyApp.Repo,
      {MyApp.Cache, []},
      {MyApp.Worker, []}
    ]

    Supervisor.start_link(children, strategy: :one_for_one, name: MyApp.Supervisor)
  end
end
```

### Use rest_for_one for dependent processes

```elixir
# If Worker B depends on Worker A, use rest_for_one
children = [
  {MyApp.WorkerA, []},  # Start first
  {MyApp.WorkerB, []},  # Depends on WorkerA
  {MyApp.WorkerC, []}   # Independent
]

# :rest_for_one — if WorkerA crashes, WorkerB and WorkerC restart
Supervisor.start_link(children, strategy: :rest_for_one)
```

### Start dynamic children correctly

```elixir
# Start a dynamic supervisor
{:ok, sup} = DynamicSupervisor.start_link(strategy: :one_for_one)

# Add a child dynamically
{:ok, child} = DynamicSupervisor.start_child(sup, %{
  id: MyApp.DynamicWorker,
  start: {MyApp.DynamicWorker, :start_link, [arg]},
  restart: :temporary
})

# Or use the module directly if it defines child_spec
{:ok, child} = DynamicSupervisor.start_child(sup, {MyApp.DynamicWorker, arg})
```

### Handle application dependencies

```elixir
# In mix.exs, declare dependencies
def application do
  [
    extra_applications: [:logger],
    applications: [:my_dependency],
    mod: {MyApp.Application, []}
  ]
end
```

## Common Scenarios

- Building a supervision tree for a web application with database, cache, and worker processes
- Starting supervised processes dynamically in response to user actions
- Designing fault-tolerant systems where process failures do not bring down the entire application

## Prevent It

- Always define `child_spec/0` or `child_spec/1` in modules that will be supervised
- Test that your supervision tree starts correctly with `mix test` and verify crash recovery
- Use `:temporary` restart for processes that should not be restarted automatically

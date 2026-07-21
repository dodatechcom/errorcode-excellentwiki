---
title: "[Solution] Elixir Supervision Tree Error -- Restart Loop Crash"
description: "Fix Elixir supervision tree errors when child processes crash repeatedly causing restart loops."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Supervision Tree Error

This error occurs when a supervised child process crashes repeatedly, exhausting the supervisor's restart intensity and causing the supervisor itself to crash.

## Common Causes

- `:one_for_one` strategy not suited for interdependent processes
- Restart intensity too high, allowing too many restarts
- Permanent bug in child process causing immediate re-crash
- Missing configuration that causes startup failure each time

## How to Fix

### Choose appropriate restart strategy

```elixir
# WRONG: one_for_one when all children depend on first
children = [
  {Database, []},
  {Cache, deps: [Database]},
  {Worker, deps: [Cache]}
]

# CORRECT: one_for_all for dependent children
Supervisor.start_link(children, strategy: :one_for_all)
```

### Increase restart intensity

```elixir
# Allow 5 restarts in 10 seconds instead of 3 in 5
%{
  id: Worker,
  start: {Worker, :start_link, []},
  restart: :permanent,
  max_restarts: 5,
  max_seconds: 10
}
```

## Examples

```elixir
defmodule MyApp.Application do
  use Application

  def start(_type, _args) do
    children = [
      {MyWorker, []},
      {MyCache, []}
    ]

    Supervisor.start_link(children, strategy: :rest_for_one)
  end
end
```

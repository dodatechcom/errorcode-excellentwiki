---
title: "[Solution] Elixir Application Config Error -- Missing Config Values"
description: "Fix Elixir application config errors when accessing configuration values that are not set."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Application Config Error

This error occurs when `Application.get_env/2` returns `nil` because a configuration value was never set.

## Common Causes

- Environment-specific config not loaded in mix.exs
- Using `Application.get_env!` without default value
- Forgetting to set config for production environment
- Config files not compiled before application start

## How to Fix

### Use defaults with get_env

```elixir
# WRONG: no default, may return nil
host = Application.get_env(:my_app, :host)

# CORRECT: provide a default
host = Application.get_env(:my_app, :host, "localhost")
```

### Use get_env! with prior validation

```elixir
def start(_type, _args) do
  config = Application.get_env(:my_app, :database_url) ||
    raise "DATABASE_URL not configured"

  # ... start children
end
```

## Examples

```elixir
# config/config.exs
config :my_app,
  port: 4000,
  host: "localhost"

# In application code
defmodule MyApp.Endpoint do
  @port Application.get_env(:my_app, :port, 4000)
end
```

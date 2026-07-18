---
title: "[Solution] Elixir Application Config or Environment Error — How to Fix"
description: "Fix Elixir application configuration and environment errors. Learn how to manage compile-time vs runtime config, environment variables, and application settings."
languages: ["elixir"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Elixir applications use a layered configuration system with compile-time and runtime configuration. When configuration values are missing, have incorrect types, or reference undefined environment variables, the application fails to start or behaves unexpectedly.

The most common cause is accessing configuration values at compile time that are only available at runtime. Using `Application.get_env` in a module attribute or during compilation will fail because `runtime.exs` has not been evaluated yet.

Another frequent cause is environment variable references in `config/config.exs`. This file is evaluated at compile time, so `System.get_env` calls here will read the build environment's variables, not the deployment environment's variables.

Configuration conflicts between `config/config.exs`, `config/dev.exs`, `config/test.exs`, and `config/prod.exs` cause unexpected behavior when the wrong environment file is loaded.

Missing configuration keys cause `nil` values. If your code expects `Application.get_env(:my_app, :api_key)` to return a string but it returns `nil`, downstream code fails.

Configuration overrides in `config/runtime.exs` must correctly reference the same application and key names. A typo in the application name or key name means the override does not apply.

Mix tasks that access configuration before the application starts can fail because the configuration tree is not fully loaded.

## Common Error Messages

```
** (RuntimeError) application :my_app is not loaded
```

```
** (MatchError) no match of right hand side: nil (in Application.get_env)
```

```
** (ArgumentError) argument error: System.get_env("MISSING_VAR") returned nil
```

```
** (exit) {:bad_config, {:undefined, :my_app, :api_key}}
```

## How to Fix It

### Separate compile-time and runtime configuration

```elixir
# config/config.exs — compile-time only
import Config

# This is OK at compile time
config :my_app, feature_flag: true

# This is WRONG — environment not available at compile time
# config :my_app, api_key: System.get_env("API_KEY")

import "#{config_env()}.exs"
```

### Use runtime.exs for environment-dependent configuration

```elixir
# config/runtime.exs
import Config

if config_env() == :prod do
  config :my_app, MyApp.Repo,
    url: System.get_env("DATABASE_URL"),
    pool_size: String.to_integer(System.get_env("POOL_SIZE") || "10")

  config :my_app, MyAppWeb.Endpoint,
    secret_key_base: System.get_env("SECRET_KEY_BASE")
end
```

### Access configuration safely with defaults

```elixir
# Use Application.get_env with fallback
api_key = Application.get_env(:my_app, :api_key, "default_key")

# Or use a helper function
defp config!(key) do
  case Application.get_env(:my_app, key) do
    nil -> raise "Missing configuration: #{key}"
    value -> value
  end
end
```

### Handle configuration in Mix tasks

```elixir
defmodule Mix.Tasks.MyApp.Setup do
  use Mix.Task

  def run(_) do
    # Ensure the application is loaded before accessing config
    Mix.Task.run("app.start")

    config_value = Application.get_env(:my_app, :setup_key)
    IO.puts("Config value: #{inspect(config_value)}")
  end
end
```

### Test configuration with different environments

```elixir
# config/test.exs
import Config

config :my_app, MyApp.Repo,
  pool: Ecto.Adapters.SQL.Sandbox,
  pool_size: 10

config :my_app, MyAppWeb.Endpoint,
  http: [port: 4002],
  server: false

# config/dev.exs
import Config

config :my_app, MyApp.Repo,
  pool_size: 5

config :my_app, MyAppWeb.Endpoint,
  http: [port: 4000],
  server: true
```

## Common Scenarios

- Moving a development application to production and discovering configuration is hardcoded
- Building a library that needs configuration from the host application
- Running Mix tasks that fail because configuration is not loaded in the task context

## Prevent It

- Use `config/config.exs` for compile-time settings and `config/runtime.exs` for environment-dependent values
- Always provide default values for optional configuration keys
- Test your application in all environments (dev, test, prod) to catch configuration issues early

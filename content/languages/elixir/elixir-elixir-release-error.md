---
title: "[Solution] Elixir Mix Release or Deployment Error — How to Fix"
description: "Fix Elixir Mix release and deployment errors. Learn how to build OTP releases, handle missing dependencies, and configure releases for production."
languages: ["elixir"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Mix releases package your Elixir application into a self-contained deployment artifact. When the release build fails or the deployed application crashes, the error is often related to missing configuration, incorrect dependencies, or runtime initialization issues.

The most common cause is missing runtime configuration. Unlike compile-time configuration, runtime configuration (in `config/runtime.exs`) is evaluated when the release starts. If it references system environment variables that are not set, the release fails to start.

Another frequent cause is missing optional dependencies. The release only includes applications that are explicitly listed as dependencies. If your code calls a function from an application not included in the release, it crashes at runtime.

Asset compilation failures in Phoenix applications block the release build. If `mix assets.deploy` or `mix phx.digest` fails, the release cannot include the compiled assets.

Database migration failures during release startup occur when `release: true` is set on the migration step and the database is not available at startup time.

Node.js dependencies for asset compilation are not included in the release. The release build environment must have Node.js installed if the application compiles assets.

Release configuration in `mix.exs` must correctly specify the applications to include and the steps to execute. Incorrect `releases` configuration causes the build to fail or the release to behave unexpectedly.

## Common Error Messages

```
** (RuntimeError) config/runtime.exs: environment variable DATABASE_URL not set
```

```
** (exit) {:bad_app, :missing_application}
```

```
** (File.Error) could not read file "priv/static/assets/app.js": no such file
```

```
** (Mix.Error) mix release failed with status: 1
```

## How to Fix It

### Set up runtime configuration correctly

```elixir
# config/runtime.exs
import Config

config :my_app, MyApp.Repo,
  url: System.get_env("DATABASE_URL"),
  pool_size: String.to_integer(System.get_env("POOL_SIZE") || "10")

config :my_app, MyAppWeb.Endpoint,
  http: [port: String.to_integer(System.get_env("PORT") || "4000")],
  secret_key_base: System.get_env("SECRET_KEY_BASE")
```

### Configure the release in mix.exs

```elixir
defmodule MyApp.MixProject do
  use Mix.Project

  def project do
    [
      app: :my_app,
      version: "1.0.0",
      releases: [
        my_app: [
          include_executables_for: [:unix],
          applications: [
            runtime_tools: :permanent,
            my_app: :permanent
          ],
          steps: [:assemble, :tar]
        ]
      ]
    ]
  end
end
```

### Build the release

```bash
# Build the release
mix release

# Or build for a specific environment
MIX_ENV=prod mix release

# Start the release
_build/prod/rel/my_app/bin/my_app start
```

### Handle asset compilation

```bash
# Compile assets before building the release
mix assets.deploy

# Or include asset compilation in the release steps
mix phx.digest
```

### Configure releases for Docker

```dockerfile
# In Dockerfile
FROM elixir:1.16 AS builder

WORKDIR /app
COPY mix.exs mix.lock ./
RUN mix deps.get --only prod

COPY config config
COPY lib lib
COPY priv priv

ENV MIX_ENV=prod
RUN mix release

FROM alpine:3.18

RUN apk add --no-cache libstdc++ openssl ncurses-libs

COPY --from=builder /app/_build/prod/rel/my_app ./

ENV PORT=4000
CMD ["bin/my_app", "start"]
```

### Handle missing environment variables gracefully

```elixir
# config/runtime.exs
import Config

database_url =
  case System.get_env("DATABASE_URL") do
    nil ->
      IO.warn("DATABASE_URL not set, using default")
      "postgres://localhost/my_app_dev"

    url ->
      url
  end

config :my_app, MyApp.Repo, url: database_url
```

## Common Scenarios

- Building a production release for the first time and encountering missing configuration
- Deploying to a server where system environment variables are not set
- Migrating from `mix run` to releases and discovering runtime dependencies are not included

## Prevent It

- Always test the release locally before deploying to production
- Set all required environment variables in your deployment environment
- Use `mix release.init` to generate a template release configuration

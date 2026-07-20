---
title: "[Solution] Elixir PhoenixRouterError - Brief Description"
description: "Fix Elixir Phoenix router errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1010
---

A Phoenix router error occurs when route definitions conflict or reference missing controllers.

## Common Causes

- Duplicate routes with same method and path
- Referencing a controller that does not exist
- Pipeline referencing undefined plug

## How to Fix

Avoid duplicate routes:

```elixir
# CORRECT: Use different paths
get "/users", UserController, :index
get "/users/list", UserController, :list
```

Use proper scope nesting:

```elixir
scope "/api/v1", MyAppWeb.API.V1 do
  pipe_through :api
  resources "/users", UserController
end
```

## Examples

```elixir
scope "/admin", MyAppWeb.Admin do
  pipe_through :admin_auth
  resources "/posts", PostController
end
```

## Related Errors

- [PhoenixControllerError](/languages/elixir/elixir-phoenix-controller-error)
- [PhoenixLiveViewError](/languages/elixir/elixir-phoenix-liveview-error)

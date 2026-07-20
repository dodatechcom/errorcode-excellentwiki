---
title: "[Solution] Elixir PhoenixControllerError - Brief Description"
description: "Fix Elixir Phoenix controller errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1011
---

A Phoenix controller error occurs when an action fails to render or raises during request processing.

## Common Causes

- Rendering a template that does not exist
- Missing `conn` assignment before rendering
- Not returning `conn` as last expression

## How to Fix

Handle missing params safely:

```elixir
def show(conn, %{"id" => id}) do
  case Repo.get(User, id) do
    nil ->
      conn |> put_status(:not_found) |> json(%{error: "not found"})
    user ->
      render(conn, :show, user: user)
  end
end
```

Use fallback controllers:

```elixir
defmodule MyAppWeb.FallbackController do
  use Phoenix.Controller

  def call(conn, {:error, :not_found}) do
    conn |> put_status(:not_found) |> render("404.html")
  end
end
```

## Examples

```elixir
def delete(conn, %{"id" => id}) do
  user = Repo.get!(User, id)
  Repo.delete!(user)
  send_resp(conn, :no_content, "")
end
```

## Related Errors

- [PhoenixRouterError](/languages/elixir/elixir-phoenix-router-error)
- [PhoenixLiveViewError](/languages/elixir/elixir-phoenix-liveview-error)

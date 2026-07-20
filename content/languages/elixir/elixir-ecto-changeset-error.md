---
title: "[Solution] Elixir EctoChangesetError - Brief Description"
description: "Fix Elixir Ecto changeset errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1008
---

An Ecto changeset error occurs when changeset validations fail.

## Common Causes

- Missing required fields in changeset params
- Using `change/2` instead of `cast/3`
- Database constraint violations not handled

## How to Fix

Use cast for allowed fields:

```elixir
defmodule User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :name, :string
    field :email, :string
  end

  def changeset(user, attrs) do
    user
    |> cast(attrs, [:name, :email])
    |> validate_required([:name, :email])
    |> validate_format(:email, ~r/@/)
  end
end
```

Use `apply_action` for form validation:

```elixir
changeset = User.changeset(%User{}, %{name: "", email: "bad"})

case Ecto.Changeset.apply_action(changeset, :validate) do
  {:ok, validated} -> IO.puts("Valid!")
  {:error, changeset} -> IO.inspect(changeset.errors)
end
```

## Examples

```elixir
%Post{}
|> Post.changeset(%{title: "Hello", body: "World"})
|> Repo.insert()
```

## Related Errors

- [EctoError](/languages/elixir/elixir-ecto-error)
- [EctoCastError](/languages/elixir/elixir-ecto-cast-error)

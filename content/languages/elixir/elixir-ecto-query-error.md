---
title: "[Solution] Elixir EctoQueryError - Brief Description"
description: "Fix Elixir Ecto query syntax errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1009
---

An Ecto query error occurs when a query expression is malformed or references nonexistent fields.

## Common Causes

- Referencing fields not in the schema
- Using `where` with invalid expressions
- SQL functions not supported by adapter

## How to Fix

Use schema module for field references:

```elixir
import Ecto.Query

from u in User, where: u.name == "test"
```

Compose dynamic queries:

```elixir
def search(query, params) do
  Enum.reduce(params, query, fn
    {:name, name}, q -> where(q, [u], u.name == ^name)
    {:age, age}, q -> where(q, [u], u.age == ^age)
  end)
end
```

## Examples

```elixir
query =
  from u in User,
    where: u.age >= 18,
    order_by: [desc: u.inserted_at],
    limit: 10

Repo.all(query)
```

## Related Errors

- [EctoChangesetError](/languages/elixir/elixir-ecto-changeset-error)
- [EctoError](/languages/elixir/elixir-ecto-error)

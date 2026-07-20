---
title: "[Solution] Elixir StructAccessError - Brief Description"
description: "Fix Elixir struct access errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1039
---

A struct access error occurs when using `[]` on a struct without Access implementation.

## Common Causes

- Using `struct[:field]` instead of `struct.field`
- Using `get_in` with structs lacking Access

## How to Fix

Use dot notation:

```elixir
defmodule User do
  defstruct [:name, :email]
end

user = %User{name: "Alice", email: "alice@example.com"}
user.name
```

## Examples

```elixir
opts = [host: "localhost", port: 8080]
opts[:host]

config = %{db: %{host: "localhost"}}
get_in(config, [:db, :host])
```

## Related Errors

- [AccessBehaviourError](/languages/elixir/elixir-access-behaviour-error)
- [StructFieldError](/languages/elixir/elixir-struct-field-error)

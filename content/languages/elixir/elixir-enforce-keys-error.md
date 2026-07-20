---
title: "[Solution] Elixir EnforceKeysError - Brief Description"
description: "Fix Elixir @enforce_keys errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1007
---

An `EnforceKeysError` is raised when constructing a struct without required keys.

## Common Causes

- Forgetting to provide a required key during struct creation
- Refactoring struct and adding `@enforce_keys` without updating call sites

## How to Fix

Always provide all enforced keys:

```elixir
defmodule Order do
  @enforce_keys [:id, :total]
  defstruct [:id, :total, :status, :note]
end

Order.new(id: 1, total: 100)
```

Use a builder function:

```elixir
defmodule User do
  @enforce_keys [:email]
  defstruct [:email, :name, :role]

  def new(email, opts \ []) do
    struct!(__MODULE__, [email: email] ++ opts)
  end
end
```

## Examples

```elixir
defmodule Event do
  @enforce_keys [:name, :date]
  defstruct [:name, :date, :location]
end

Event.new(name: "Meetup", date: ~D[2025-01-01])
```

## Related Errors

- [StructFieldError](/languages/elixir/elixir-struct-field-error)
- [StructUpdate](/languages/elixir/elixir-struct-update)

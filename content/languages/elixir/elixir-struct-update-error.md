---
title: "[Solution] Elixir Struct Update Error -- Using With on Structs"
description: "Fix Elixir struct update errors when using the with syntax to update struct fields."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Struct Update Error

This error occurs when attempting to update struct fields using incorrect syntax or updating fields that do not exist.

## Common Causes

- Using `%{struct | field: value}` on a map without that field
- Trying to update a field not defined in defstruct
- Forgetting the `|` separator in struct update syntax
- Using map update syntax instead of struct update

## How to Fix

### Use correct struct update syntax

```elixir
defmodule User do
  defstruct [:name, :email, :age]
end

# WRONG: field :role not in struct
user = %User{name: "Alice", email: "a@b.com"}
%{user | role: :admin}  # KeyError

# CORRECT: use Map.put for new fields or add to struct
updated = %{user | age: 31}
```

### Use Map.put for adding fields

```elixir
extended = Map.put(user, :role, :admin)
```

## Examples

```elixir
defmodule Config do
  defstruct host: "localhost", port: 4000, env: :dev

  def for_env(env) do
    %__MODULE__{env: env}
  end

  def with_port(%Config{} = config, port) do
    %{config | port: port}
  end
end
```

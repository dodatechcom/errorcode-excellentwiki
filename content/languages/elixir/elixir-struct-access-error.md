---
title: "[Solution] Elixir Struct Access Error -- Dot Notation on Structs"
description: "Fix Elixir struct access errors when using dot notation on structs that are actually maps."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Struct Access Error

This error occurs when you use dot notation on a value that is not a struct or when the struct does not have the requested field.

## Common Causes

- Accessing a struct field that does not exist in the struct definition
- Using dot notation on a plain map instead of a struct
- Confusing Access behavior with struct field access
- Missing struct definition for a module

## How to Fix

### Verify field exists in struct

```elixir
# WRONG: :age is not defined in the struct
defmodule User do
  defstruct [:name, :email]
end

user = %User{name: "Alice"}
user.age  # KeyError

# CORRECT: add field to struct or use Map.get
defmodule User do
  defstruct [:name, :email, :age]
end
```

### Use Map.get for optional access

```elixir
user = %User{name: "Alice", email: "a@b.com"}
age = Map.get(user, :age, 0)  # returns 0 if :age not set
```

## Examples

```elixir
defmodule Config do
  defstruct host: "localhost", port: 4000, ssl: false

  def from_env do
    %__MODULE__{
      host: System.get_env("HOST", "localhost"),
      port: System.get_env("PORT", "4000") |> String.to_integer()
    }
  end
end
```

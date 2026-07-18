---
title: "[Solution] Fix Ecto cast error invalid value for type"
description: "Resolve Ecto cast errors in Elixir by validating input types, using Ecto.Enum for restricted value sets, and configuring custom Ecto.Type implementations."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

An Ecto cast error occurs when you try to cast a value into a schema field but the value does not match the expected Ecto type. This happens during `Ecto.Changeset.cast/3` or `Ecto.Changeset.change/2` operations.

The error appears as:

```elixir
** (Ecto.CastError) cannot cast value of type String for field :age in schema User
```

or:

```elixir
** (Ecto.ChangeError) invalid value for :status in changeset
```

## Why It Happens

This error occurs due to type mismatches between input data and schema definitions:

- Passing a string where an integer is expected
- Sending a map where an embedded schema is defined
- Providing an enum value not included in the allowed list
- Using raw params instead of cast-compatible params
- Not handling nil values for required fields properly

## How to Fix It

Ensure input data types match schema field types:

```elixir
defmodule User do
  use Ecto.Schema

  schema "users" do
    field :name, :string
    field :age, :integer
    field :status, Ecto.Enum, values: [:active, :inactive]
  end
end

# WRONG: String where integer expected
Ecto.Changeset.cast(%User{}, %{age: "thirty"}, [:age])

# CORRECT: Use proper types
Ecto.Changeset.cast(%User{}, %{age: 30}, [:age])
```

Use `Ecto.Changeset.change/2` for simple updates with type-safe values:

```elixir
# WRONG: Type mismatch
Ecto.Changeset.change(%User{}, %{age: "invalid"})

# CORRECT: Valid integer value
Ecto.Changeset.change(%User{}, %{age: 25})
```

Validate enums before casting:

```elixir
# WRONG: Invalid enum value
Ecto.Changeset.cast(%User{}, %{status: :unknown}, [:status])

# CORRECT: Use only allowed enum values
Ecto.Changeset.cast(%User{}, %{status: :active}, [:status])
```

Handle custom types with `Ecto.Type`:

```elixir
defmodule MyApp.CustomDate do
  use Ecto.Type

  def type, do: :date

  def cast(value) when is_binary(value) do
    case Date.from_iso8601(value) do
      {:ok, date} -> {:ok, date}
      _ -> :error
    end
  end

  def cast(%Date{} = date), do: {:ok, date}
  def cast(_), do: :error

  def dump(value), do: {:ok, value}
  def load(value), do: {:ok, value}
end
```

## Common Mistakes

- Passing raw JSON string params without converting to proper types
- Not using `Ecto.Enum` for restricted value sets
- Assuming Ecto will auto-convert strings to integers or atoms
- Forgetting that `cast/3` returns `{:error, changeset}` on failure
- Not using `Ecto.Changeset.validate_number/3` for numeric constraints

## Related Pages

- [ArgumentError in Elixir](/languages/elixir/argument-error4)
- [KeyError: key not found](/languages/elixir/elixir-keyerror-elixir)
- [Struct field does not exist](/languages/elixir/elixir-struct-field-error)

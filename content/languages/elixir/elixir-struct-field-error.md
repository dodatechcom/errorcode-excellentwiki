---
title: "[Solution] Fix field does not exist in struct error in Elixir"
description: "Fix struct field errors in Elixir by verifying field names against defstruct, using Map.get for safe access, and understanding struct vs map differences."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 7
---

## What This Error Means

This error is raised when you try to access a field on a struct using the `.` operator, but that field does not exist in the struct definition. It typically appears as:

```elixir
** (KeyError) key :age not found in: %User{name: "Alice"}
```

or when using struct update syntax:

```elixir
** (KeyError) key :nonexistent not found in: %User{name: "Alice"}
```

Structs in Elixir are compiled to maps with a fixed set of defined fields plus a `__struct__` key.

## Why It Happens

This error occurs due to field name mismatches or type confusion:

- Accessing a field that was never defined in the `defstruct`
- Typo in the field name (e.g., `:user_name` vs `:name`)
- Treating a regular map as a struct or vice versa
- Accessing struct fields after a deep merge or update lost the struct key
- Receiving a map from an external source and trying to use struct access syntax

## How to Fix It

Verify the struct definition and use the correct field names:

```elixir
defmodule User do
  defstruct [:name, :email, :age]
end

# WRONG: :username is not a defined field
%User{}.username

# CORRECT: Use defined field names
%User{}.name
%User{}.email
```

Use `Map.get/3` for safe access with a default value:

```elixir
user = %User{name: "Alice", age: 30}

# WRONG: Crashes if field doesn't exist
user.role

# CORRECT: Safe access with default
Map.get(user, :role, :user)
```

Check if a field exists before accessing it:

```elixir
def get_field(struct, field) do
  if Map.has_key?(struct, field) do
    Map.get(struct, field)
  else
    {:error, :field_not_found}
  end
end
```

Use `put_in/3` for dynamic field access:

```elixir
user = %User{name: "Alice"}
put_in(user, [:name], "Bob")
```

Handle structs that have been converted to plain maps:

```elixir
data = %{__struct__: User, name: "Alice"}
# data.name works

data = %{name: "Alice"}  # plain map, not a struct
data.name  # works (maps support . access)
%User{} = data  # MatchError - not a struct
```

## Common Mistakes

- Confusing atom keys with string keys when working with JSON-decoded data
- Using struct access syntax on a plain map that lacks the `__struct__` key
- Not realizing that `Map.merge/2` does not preserve struct types
- Forgetting that struct field order does not matter but spelling does
- Accessing fields defined with default values without understanding their defaults

## Related Pages

- [KeyError: key not found](/languages/elixir/elixir-keyerror-elixir)
- [MatchError: no match of right hand side value](/languages/elixir/match-error)
- [BadMapError: expected a map](/languages/elixir/bad-match)

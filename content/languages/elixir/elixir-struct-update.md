---
title: "[Solution] Elixir Struct Update Syntax Failed — Unknown Key Error"
description: "Fix Elixir struct update syntax errors. Learn about struct field access, update syntax, and struct validation in Elixir."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A struct update syntax error occurs when you try to update a struct with a key that does not exist or use incorrect update syntax. Elixir structs are maps with a fixed set of keys defined by `defstruct`, and only those keys can be updated.

## Why It Happens

The most common cause is trying to update a struct field that is not defined in the struct. For example, if a struct has `[:name, :age]` and you try to update `:email`, the error is raised.

Another frequent cause is using wrong update syntax. The correct syntax is `%{struct | field: value}`, not `%{field: value}` or direct assignment.

Accessing struct fields before the struct is fully initialized can also cause errors. If a struct has default values that depend on other fields, updating before initialization fails.

Using struct update syntax on a plain map causes this error because maps do not have the `|` update syntax in the same way.

Finally, trying to add new keys to a struct (which is not allowed because structs are closed maps) causes this error.

## How to Fix It

### Use the correct struct update syntax

```elixir
defmodule User do
  defstruct [:name, :age, :email]
end

user = %User{name: "Alice", age: 30}

# Wrong — missing pipe
%{name: "Bob"}

# Correct — use pipe syntax
%{user | name: "Bob"}
```

### Only update fields that exist in the struct

```elixir
# Wrong — :phone is not a struct field
%{user | phone: "555-1234"}

# Correct — only update valid fields
%{user | email: "alice@example.com"}
```

### Use Map.merge for multiple updates

```elixir
updated = Map.merge(user, %{name: "Bob", age: 31})
```

### Add new fields to the struct definition

```elixir
defmodule User do
  defstruct [:name, :age, :email, :phone]
end
```

### Use functional update for complex changes

```elixir
def update_user(user, attrs) do
  struct!(user, attrs)
end
```

## Common Mistakes

- Trying to add fields to a struct that are not in defstruct
- Using wrong update syntax without the pipe operator
- Assuming structs are open like maps
- Not initializing all required struct fields
- Using struct update syntax on plain maps

## Related Pages

- [Elixir KeyError](/languages/elixir/elixir-keyerror-elixir/)
- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)

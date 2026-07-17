---
title: "KeyError - Key Not Found in Elixir"
description: "Elixir raises KeyError when accessing a key that does not exist in a map or keyword list"
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["key", "map", "keyword", "keyerror", "access"]
weight: 5
---

## What This Error Means

A `KeyError` is raised when you try to access a key in a map or keyword list that does not exist. This commonly occurs with `map.key` syntax when the key is missing.

## Common Causes

- Accessing non-existent key with dot notation
- Missing key in JSON/API response
- Incorrect key name (typo)
- Keyword list accessed as map

## How to Fix

Use `Map.get` for safe access:

```elixir
map = %{"name" => "Alice", "age" => 30}

# Wrong: KeyError if key missing
name = map["name"]
email = map["email"]  # nil, no error

# Wrong: dot notation raises KeyError
email = map.email  # KeyError

# Correct: use Map.get with default
email = Map.get(map, "email", "unknown")
```

Use pattern matching:

```elixir
case Map.fetch(map, "email") do
  {:ok, email} -> IO.puts("Email: #{email}")
  :error -> IO.puts("Email not found")
end
```

Handle nested maps:

```elixir
user = %{
  "name" => "Alice",
  "address" => %{"city" => "Portland"}
}

city = get_in(user, ["address", "city"]) || "Unknown"
```

## Examples

```elixir
map = %{name: "Bob"}
IO.puts(map.name)   # Works
IO.puts(map.email)  # ** (KeyError) key :email not found
```

## Related Errors

- [ArgumentError]({{< relref "/languages/elixir/argument-error4" >}})
- [MatchError]({{< relref "/languages/elixir/match-error" >}})

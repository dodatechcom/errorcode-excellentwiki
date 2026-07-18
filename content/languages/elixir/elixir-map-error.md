---
title: "[Solution] Elixir KeyError — Key Not Found in Map"
description: "Fix Elixir KeyError when accessing map keys. Learn about map access patterns, get/2, has_key?/2, and safe map operations."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `KeyError` is raised when you access a map with a key that does not exist. The error message shows the key that was not found. In Elixir, `map[key]` raises `KeyError` if the key is missing, while `Map.get(map, key)` returns `nil`.

## Why It Happens

The most common cause is using bracket access `map[key]` without first checking if the key exists. This is the most frequent source of this error in Elixir code.

Another frequent cause is keyword list access with string keys instead of atom keys. Elixir keyword lists require atom keys, and using string keys causes a key error.

Accessing nested map keys that do not exist at any level also causes this error. If you access `map[:a][:b][:c]` and `:a` exists but `:b` does not, the error occurs at the `:b` level.

Using `Access.get/3` with the wrong key type (atom vs string) can cause unexpected `nil` returns instead of the expected value.

Finally, updating a struct with a key that is not part of the struct definition causes this error.

## How to Fix It

### Use Map.get for safe access

```elixir
map = %{"name" => "Alice", "age" => 30}

# Wrong — KeyError if key missing
value = map["email"]

# Correct — returns nil if missing
value = Map.get(map, "email")
```

### Check has_key? before access

```elixir
if Map.has_key?(map, :key) do
  value = map[:key]
  process(value)
end
```

### Use pattern matching for expected keys

```elixir
case map do
  %{name: name, age: age} -> {:ok, {name, age}}
  %{name: name} -> {:ok, {name, nil}}
  _ -> {:error, :missing_keys}
end
```

### Use nested access safely

```elixir
# Wrong — may fail at any level
value = map[:a][:b][:c]

# Correct — use get_in for nested access
value = get_in(map, [:a, :b, :c])
```

### Use put_in for nested updates

```elixir
updated = put_in(map, [:a, :b, :c], "new_value")
```

## Common Mistakes

- Using `map[key]` instead of `Map.get(map, key)` for potentially missing keys
- Not checking if a key exists before accessing nested values
- Using string keys when atom keys are expected (or vice versa)
- Not handling the `nil` case from `Map.get`
- Assuming struct fields are accessible like map keys

## Related Pages

- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir CaseClauseError](/languages/elixir/elixir-caseclauseerror/)

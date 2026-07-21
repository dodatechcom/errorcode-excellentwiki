---
title: "[Solution] Elixir Keyword List Error -- Incorrect Keyword List Usage"
description: "Fix Elixir keyword list errors when using keyword lists with incorrect syntax or accessing options incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Keyword List Error

This error occurs when keyword lists are used incorrectly, such as mixing atom keys with non-atom keys or accessing them with map syntax.

## Common Causes

- Using map syntax `%{key: value}` instead of keyword list `[key: value]`
- Keyword lists must have atom keys at the front
- Mixing keyword list and map syntax
- Passing keyword list where a map is expected

## How to Fix

### Use correct keyword list syntax

```elixir
# WRONG: map syntax with atom keys (creates map, not keyword list)
opts = %{timeout: 5000, retries: 3}

# CORRECT: keyword list syntax
opts = [timeout: 5000, retries: 3]

# Access with keyword functions
timeout = Keyword.get(opts, :timeout, 3000)
```

### Ensure atom keys at the front

```elixir
# WRONG: non-atom key in middle
[timeout: 5000, "retries" => 3]  # error

# CORRECT: all atom keys
[timeout: 5000, retries: 3]
```

## Examples

```elixir
def start_link(opts) do
  timeout = Keyword.get(opts, :timeout, 5000)
  name = Keyword.get(opts, :name, __MODULE__)

  GenServer.start_link(__MODULE__, %{timeout: timeout}, name: name)
end
```

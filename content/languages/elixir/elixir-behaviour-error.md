---
title: "[Solution] Elixir Behaviour Error -- Missing Callback Implementation"
description: "Fix Elixir behaviour errors when a module using @behaviour does not implement all callbacks."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Behaviour Error

This error occurs when a module declares `@behaviour` but does not implement all required callbacks defined by that behaviour.

## Common Causes

- Forgetting to implement newly added callbacks
- Typo in callback function name
- Wrong arity for a callback implementation
- Not returning the correct type from a callback

## How to Fix

### Implement all required callbacks

```elixir
defmodule MyParser do
  @behaviour Parser

  # WRONG: missing parse/1 implementation
  @impl true
  def validate(input), do: String.valid?(input)
end

# CORRECT: implement all callbacks
defmodule MyParser do
  @behaviour Parser

  @impl true
  def parse(input), do: {:ok, input}

  @impl true
  def validate(input), do: String.valid?(input)
end
```

### Check callback specifications

```elixir
defmodule Parser do
  @callback parse(String.t()) :: {:ok, term()} | {:error, String.t()}
  @callback validate(String.t()) :: boolean()
end
```

## Examples

```elixir
defmodule JSONParser do
  @behaviour Parser

  @impl true
  def parse(json) do
    case Jason.decode(json) do
      {:ok, data} -> {:ok, data}
      {:error, _} -> {:error, "Invalid JSON"}
    end
  end

  @impl true
  def validate(json) do
    is_binary(json) and String.starts_with?(json, "{")
  end
end
```

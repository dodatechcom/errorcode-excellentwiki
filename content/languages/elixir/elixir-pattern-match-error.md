---
title: "[Solution] Elixir Pattern Match Error -- MatchFailed Exception"
description: "Fix Elixir pattern match errors when = operator fails to match against the given value."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Pattern Match Error

This error occurs when the `=` operator is used and the left side does not match the right side at runtime.

## Common Causes

- Matching a value against a struct that is actually a plain map
- Pattern matching with wrong tuple size
- Expecting a specific atom tag that is not present
- Matching on exact values that change between calls

## How to Fix

### Use struct matching correctly

```elixir
# WRONG: matching plain map against struct
%User{name: name} = %{name: "Alice"}

# CORRECT: match against actual structs
%User{name: name} = %User{name: "Alice", age: 30}
```

### Handle match failures

```elixir
case result do
  {:ok, value} -> process(value)
  {:error, reason} -> handle_error(reason)
  _ -> :unexpected
end
```

## Examples

```elixir
defmodule Point do
  defstruct [:x, :y]
end

def distance(%Point{x: x1, y: y1}, %Point{x: x2, y: y2}) do
  :math.sqrt(:math.pow(x2 - x1, 2) + :math.pow(y2 - y1, 2))
end
```

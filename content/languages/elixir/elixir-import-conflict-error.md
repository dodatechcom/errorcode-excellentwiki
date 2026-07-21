---
title: "[Solution] Elixir Import Conflict Error -- Ambiguous Function Imports"
description: "Fix Elixir import conflict errors when two modules export functions with the same name."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Import Conflict Error

This error occurs when two imported modules define functions with the same name and arity, causing ambiguity.

## Common Causes

- Importing two modules with overlapping function names
- Using `import` instead of qualified calls
- Conflicting imports from application and dependencies
- Not using `:only` to restrict imported functions

## How to Fix

### Use only: to restrict imports

```elixir
# WRONG: both modules have map/2
import Enum
import Map

# CORRECT: import only what you need
import Enum, only: [map: 2, filter: 2]
import Map, only: [get: 3, put: 3]
```

### Use fully qualified calls

```elixir
# Instead of importing, use module-qualified calls
Enum.map([1, 2, 3], &(&1 * 2))
Map.get(%{a: 1}, :b, 0)
```

## Examples

```elixir
defmodule MyModule do
  import String, only: [split: 2, trim: 1]
  import List, only: [first: 1, last: 1]

  def process(input) do
    input |> split(" ") |> first()
  end
end
```

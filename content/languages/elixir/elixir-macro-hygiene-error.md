---
title: "[Solution] Elixir Macro Hygiene Error -- Variable Capture Issues"
description: "Fix Elixir macro hygiene errors when macros unintentionally capture or shadow variables."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Macro Hygiene Error

This error occurs when macros accidentally capture variables from the calling scope, leading to unexpected behavior.

## Common Causes

- Macros defining variables that clash with caller variables
- Using `var!` to intentionally break hygiene when not needed
- Quoted expressions leaking bindings
- Missing `quote`/`unquote` for proper AST manipulation

## How to Fix

### Keep macro hygiene

```elixir
# WRONG: variable capture
defmacro set_value(value) do
  quote do
    x = unquote(value)  # captures or shadows x
  end
end

# CORRECT: use unique variable names
defmacro set_value(value) do
  quote do
    unquote(Macro.var(:value, __MODULE__)) = unquote(value)
  end
end
```

### Use unquote for values from caller

```elixir
defmacro unless(condition, do: block) do
  quote do
    if not unquote(condition) do
      unquote(block)
    end
  end
end
```

## Examples

```elixir
defmodule MyMacros do
  defmacro defadder(name, value) do
    quote do
      def unquote(name)(), do: unquote(value)
    end
  end
end
```

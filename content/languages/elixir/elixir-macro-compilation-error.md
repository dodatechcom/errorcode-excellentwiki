---
title: "[Solution] Elixir Macro Compilation Error -- Quote/Unquote Issues"
description: "Fix Elixir macro compilation errors when quote and unquote are used incorrectly in macro definitions."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Macro Compilation Error

This error occurs when the `quote`/`unquote` mechanism is used incorrectly in macro definitions.

## Common Causes

- Forgetting to unquote values inside quote blocks
- Unquoting in the wrong position (e.g., inside another quote)
- Not understanding that quote returns AST, not values
- Using unquote splice incorrectly for lists

## How to Fix

### Quote and unquote correctly

```elixir
# WRONG: not unquoting the value
defmacro say_hello(name) do
  quote do
    IO.puts("Hello " <> name)  # 'name' is not unquoted
  end
end

# CORRECT: unquote the value
defmacro say_hello(name) do
  quote do
    IO.puts("Hello " <> unquote(name))
  end
end
```

### Use unquote splice for lists

```elixir
defmacro def_list(name, items) do
  quote do
    def unquote(name)() do
      unquote(items)  # items must be unquoted as a list
    end
  end
end
```

## Examples

```elixir
defmodule MyMacros do
  defmacro defmodule_with_attr(module_name, attrs) do
    quote do
      defmodule unquote(module_name) do
        @moduledoc unquote(attrs[:doc])
        defstruct unquote(attrs[:fields])
      end
    end
  end
end
```

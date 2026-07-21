---
title: "[Solution] Elixir Module Attribute Error -- Incorrect @ Module Attribute Usage"
description: "Fix Elixir module attribute errors when @ attributes are defined, accumulated, or accessed incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Module Attribute Error

This error occurs when module attributes are used incorrectly, such as accessing an undefined attribute or misusing accumulation.

## Common Causes

- Accessing a module attribute that was never defined
- Using `@attr` before defining it with `@attr value`
- Not accumulating with `Module.register_attribute` for repeated definitions
- Using module attributes in functions that run at runtime

## How to Fix

### Define before use

```elixir
# WRONG: using @name before defining it
def greet, do: "Hello #{@name}"

# CORRECT: define first
@name "World"
def greet, do: "Hello #{@name}"
```

### Register attribute for accumulation

```elixir
defmodule MyModule do
  Module.register_attribute(__MODULE__, :routes, accumulate: true)

  @route [:get, "/users", :index]
  @route [:get, "/users/:id", :show]
  @route [:post, "/users", :create]

  def routes, do: @routes
end
```

## Examples

```elixir
defmodule Controller do
  @before_compile ControllerMacros

  @impl true
  def init(_), do: {:ok, %{}}
end
```

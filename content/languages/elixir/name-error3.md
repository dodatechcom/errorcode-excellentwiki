---
title: "** (NameError) undefined function"
description: "A NameError occurs when calling a function that is not defined or not imported."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NameError` is raised when you try to call a function that doesn't exist in the current scope. This can happen when the function is not defined, not imported, or you've made a typo in the function name.

## Common Causes

- Typo in function name
- Function not imported with `import` or `alias`
- Module not compiled or loaded
- Calling private function from outside its module

## How to Fix

```elixir
# WRONG: Typo in function name
IO.puttln("hello")
# ** (NameError) undefined function IO.puttln/1

# CORRECT: Use correct function name
IO.puts("hello")
```

```elixir
# WRONG: Not importing the function
defmodule Foo do
  def bar, do: :ok
end
bar()
# ** (NameError) undefined function bar/0

# CORRECT: Import or alias the module
defmodule MyModule do
  import Foo, only: [bar: 0]
  def test, do: bar()  # works
end
```

## Examples

```elixir
# Example 1: Undefined function
String.nonexistent("hello")
# ** (NameError) undefined function String.nonexistent/1

# Example 2: Module not loaded
Enum.reverse([1, 2, 3])  # works if Enum loaded
MyCustomModule.func()
# ** (NameError) undefined function

# Example 3: Private function
defmodule Secret do
  defp hidden, do: :private
end
Secret.hidden()
# ** (NameError) undefined function Secret.hidden/0
```

## Related Errors

- [ArgumentError: wrong number of arguments](/languages/elixir/argument-error4)
- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)

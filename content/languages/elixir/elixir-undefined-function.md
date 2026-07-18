---
title: "[Solution] Elixir UndefinedFunctionError — Function Not Defined"
description: "Fix Elixir UndefinedFunctionError when calling functions that don't exist. Learn about module imports, function visibility, and compilation errors."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `UndefinedFunctionError` is raised when you call a function that is not defined in the expected module or is not accessible. The error message shows the function name, arity, and the module where it was expected.

## Why It Happens

The most common cause is calling a function with the wrong arity. Elixir distinguishes between `def foo()` and `def foo(x)` as different functions, and calling with the wrong number of arguments triggers this error.

Another frequent cause is calling a private function from outside its module. Functions defined with `defp` are not accessible from other modules, and attempting to call them raises this error.

Importing or aliasing a module incorrectly can cause this error. If you `alias MyApp.Repo` but the function is defined in `MyApp.Repo.Query`, the alias does not make the function available.

Compilation order issues can cause this error. If a module depends on another module that has not been compiled yet, the function may appear undefined.

Finally, calling a function on a struct or protocol that has not been implemented for the given type causes this error.

## How to Fix It

### Verify the function exists and has the correct arity

```elixir
# Check if the function exists
function_exported?(MyModule, :my_function, 1)

# Or use iex
iex> MyModule.__info__(:functions)
```

### Import or alias the correct module

```elixir
# Wrong — function not in Repo
alias MyApp.Repo
Repo.query("SELECT ...")  # UndefinedFunctionError

# Correct — import the right module
import MyApp.Repo.Query
```

### Use public functions instead of private ones

```elixir
# Wrong — calling private function
defmodule A do
  defp helper, do: :ok
end
A.helper()  # UndefinedFunctionError

# Correct — make it public or restructure
defmodule A do
  def helper, do: :ok
end
```

### Check for compilation issues

```bash
# Recompile dependencies
mix deps.compile

# Clean and rebuild
mix clean && mix compile
```

### Use function_exported? for dynamic calls

```elixir
if function_exported?(module, :function_name, arity) do
  apply(module, :function_name, args)
else
  raise ArgumentError, "Function not found"
end
```

## Common Mistakes

- Calling a function with the wrong number of arguments
- Trying to access private functions defined with `defp`
- Not importing modules that define the functions you need
- Assuming a function is available before the module is compiled
- Not checking function_exported? before dynamic dispatch

## Related Pages

- [Elixir FunctionClauseError](/languages/elixir/elixir-function-clause/)
- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)

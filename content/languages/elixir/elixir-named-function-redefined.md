---
title: "[Solution] Fix variable unused warning and named function redefined in Elixir"
description: "Resolve Elixir unused variable warnings and function redefinition issues by using underscore prefixes, renaming shadowed variables, and removing dead code."
languages: ["elixir"]
error-types: ["compiler-warning"]
severities: ["warning"]
weight: 7
---

## What This Error Means

Elixir raises a compiler warning when a variable is defined but never used, or when a named function is redefined within the same module scope. The warning messages appear as:

```elixir
warning: variable "x" is unused (if you intended to use it, prefix it with an underscore)
  lib/my_module.ex:5

warning: this clause/head of def is unused
  lib/my_module.ex:12
```

## Why It Happens

This warning occurs due to variable shadowing or dead code:

- Defining a variable but not referencing it later in the function
- Rebinding a variable name that shadows a previous binding
- Defining two function heads with the same name and arity without a clear primary definition
- Using the same variable name in nested `case`, `cond`, or `with` blocks
- Copy-pasting code and forgetting to rename variables

## How to Fix It

Prefix unused variables with an underscore to signal intentional non-use:

```elixir
# WARNING: variable "x" is unused
def process(x) do
  :ok
end

# CORRECT: Prefix with underscore
def process(_x) do
  :ok
end
```

Rename shadowed variables to avoid confusion:

```elixir
# WARNING: variable "x" shadows previous binding
def process(x) do
  case validate(x) do
    {:ok, x} -> x  # shadows the parameter x
    {:error, reason} -> reason
  end
end

# CORRECT: Use a distinct name
def process(input) do
  case validate(input) do
    {:ok, validated} -> validated
    {:error, reason} -> reason
  end
end
```

Remove or properly scope unused clauses:

```elixir
# WARNING: clause is unused
def handle(:ok), do: :success
def handle(:ok), do: :also_success

# CORRECT: Use a single function head with guards
def handle(:ok), do: :success
```

Use `@compile {:no_warn_undefined, ...}` selectively when dealing with optional dependencies:

```elixir
@compile {:no_warn_undefined, OptionalModule}
```

## Common Mistakes

- Ignoring unused variable warnings instead of fixing them
- Using the same variable name across `with` chain steps, causing subtle bugs
- Assuming `^` pinning solves all shadowing issues without changing semantics
- Not understanding that `_x` is still bound even though it is not used
- Leaving dead code in production modules after refactoring

## Related Pages

- [MatchError: no match of right hand side value](/languages/elixir/match-error)
- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [CompileError in Elixir](/languages/elixir/elixir-mix-compile-error)

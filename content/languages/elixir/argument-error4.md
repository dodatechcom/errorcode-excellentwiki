---
title: "** (ArgumentError) wrong number of arguments"
description: "An ArgumentError occurs when calling a function with the wrong number of arguments."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["argument", "arity", "wrong-number", "argumenterror"]
weight: 5
---

## What This Error Means

An `ArgumentError` is raised when a function is called with a different number of arguments than it expects. Elixir functions have fixed arities, and calling with the wrong number of arguments results in this error.

## Common Causes

- Calling function with wrong number of arguments
- Missing required arguments
- Confusing function arities (e.g., `fun/1` vs `fun/2`)
- Incorrect function signature in call

## How to Fix

```elixir
# WRONG: Wrong number of arguments
String.split("hello world")
# works, but:
String.split("hello world", " ", "x")
# ** (ArgumentError) wrong number of arguments (given 3, expected 1..2)

# CORRECT: Check function arity
String.split("hello world", " ")
# ["hello", "world"]
```

```elixir
# WRONG: Missing arguments
def greet(name, greeting), do: "#{greeting}, #{name}!"
greet("Alice")
# ** (ArgumentError) wrong number of arguments (given 0, expected 2)

# CORRECT: Provide all required arguments
greet("Alice", "Hello")
# "Hello, Alice!"
```

## Examples

```elixir
# Example 1: Wrong arity
Enum.map([1, 2, 3])
# ** (ArgumentError) wrong number of arguments (given 0, expected 2)

# Example 2: Extra argument
IO.puts("hello", "extra")
# ** (ArgumentError) wrong number of arguments (given 2, expected 1)

# Example 3: Missing default argument (if not defined)
def add(a, b), do: a + b
add(1)
# ** (ArgumentError) wrong number of arguments (given 1, expected 2)
```

## Related Errors

- [FunctionClauseError: no function clause matching](/languages/elixir/function-clause)
- [NameError: undefined function](/languages/elixir/name-error3)

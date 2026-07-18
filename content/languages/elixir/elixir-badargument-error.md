---
title: "[Solution] Elixir BadArgument — Bad Argument in Function Call"
description: "Fix Elixir bad argument errors when calling functions. Learn about argument validation, type checking, and function contract enforcement."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `bad argument in call to` error is raised when a function receives an argument of the wrong type or an invalid value. The error message shows the function name and the problematic argument.

## Why It Happens

The most common cause is passing the wrong type to a function. For example, passing a string where an integer is expected, or passing a list where a map is required.

Another frequent cause is passing `nil` to a function that does not accept it. Elixir functions typically expect explicit types, and `nil` is not implicitly converted.

Using the wrong operator for a type causes this error. For example, using `Kernel.+` on strings instead of the `<>` concatenation operator.

Pattern matching failures in function heads can also cause argument errors. If a function is defined with specific patterns, passing values that do not match those patterns raises this error.

Finally, using ETS or Agent with invalid arguments (like non-existent table names) causes this error.

## How to Fix It

### Validate argument types before calling functions

```elixir
def process(value) when is_integer(value) do
  value * 2
end

def process(value) do
  raise ArgumentError, "Expected integer, got: #{inspect(value)}"
end
```

### Use guard clauses for type checking

```elixir
def add(a, b) when is_number(a) and is_number(b) do
  a + b
end
```

### Handle nil explicitly

```elixir
def process(nil), do: {:error, :nil_value}
def process(value) when is_binary(value), do: String.upcase(value)
```

### Use pattern matching for different types

```elixir
def concatenate(a, b) when is_binary(a) and is_binary(b) do
  a <> b
end

def concatenate(a, b) when is_list(a) and is_list(b) do
  a ++ b
end
```

### Check function documentation for expected types

```elixir
# Always read @doc and @spec for expected types
@spec process(String.t()) :: {:ok, String.t()} | {:error, atom()}
def process(input) do
  # ...
end
```

## Common Mistakes

- Not validating argument types before passing to functions
- Using `<>` operator with non-binary types
- Passing `nil` without explicit handling
- Not using guard clauses for type safety
- Assuming functions will implicitly convert types

## Related Pages

- [Elixir FunctionClauseError](/languages/elixir/elixir-function-clause/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
- [Elixir CaseClauseError](/languages/elixir/elixir-caseclauseerror/)

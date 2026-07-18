---
title: "[Solution] Elixir ArgumentError in String Module — Invalid String Operation"
description: "Fix ArgumentError when using Elixir String module functions. Learn about string validation, UTF-8 requirements, and String function signatures."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `ArgumentError` from the `String` module is raised when a string function receives an argument of the wrong type or an invalid value. The error message shows the function name and the problematic argument.

## Why It Happens

The most common cause is passing a non-binary value to a `String` function. `String` functions expect binaries (strings), and passing atoms, integers, or lists causes this error.

Another frequent cause is using `String` functions with invalid UTF-8 data. Functions like `String.length`, `String.downcase`, and `String.trim` require valid UTF-8 input.

Passing the wrong number of arguments to `String` functions causes this error. For example, `String.slice("hello", 1)` is missing the second argument.

Using `String` functions on non-string values in templates or interpolations can cause unexpected errors if the value is nil or not a string.

Finally, using string functions with special characters or escape sequences incorrectly can cause this error.

## How to Fix It

### Ensure arguments are strings

```elixir
def process(value) when is_binary(value) do
  String.trim(value)
end

def process(value) do
  raise ArgumentError, "Expected string, got: #{inspect(value)}"
end
```

### Validate UTF-8 before string operations

```elixir
def safe_length(data) do
  if is_binary(data) and String.valid?(data) do
    String.length(data)
  else
    byte_size(data)
  end
end
```

### Use correct argument counts

```elixir
# Wrong — missing second argument
String.slice("hello", 1)

# Correct — provide both start and length
String.slice("hello", 1, 3)  # "ell"
```

### Handle nil values explicitly

```elixir
def safe_upcase(nil), do: nil
def safe_upcase(s) when is_binary(s), do: String.upcase(s)
```

### Use String.to_integer with error handling

```elixir
case Integer.parse(string) do
  {num, ""} -> num
  _ -> raise ArgumentError, "Invalid integer: #{string}"
end
```

## Common Mistakes

- Passing atoms or integers to String functions
- Not checking UTF-8 validity before string operations
- Using String functions with wrong argument counts
- Not handling nil values in string processing pipelines
- Assuming String functions work on any data type

## Related Pages

- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir UnicodeConversionError](/languages/elixir/elixir-unicode-error/)

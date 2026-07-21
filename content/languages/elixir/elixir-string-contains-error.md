---
title: "[Solution] Elixir String Contains Error -- Incorrect Substring Checking"
description: "Fix Elixir string contains errors when checking for substrings with String.contains? incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir String Contains Error

This error occurs when `String.contains?/2` is called with invalid arguments or produces unexpected results.

## Common Causes

- Passing a list of strings when a single string is expected
- Case sensitivity issues when checking containment
- Using contains? where pattern matching would be better
- Checking for containment in empty strings

## How to Fix

### Check arguments and use correctly

```elixir
# WRONG: wrong argument type
String.contains?(123, "12")

# CORRECT: ensure binary input
String.contains?("hello world", "world")  # true
```

### Use multiple patterns

```elixir
# Check for any of multiple patterns
String.contains?("hello world", ["hello", "world"])  # true

# Check all patterns
["hello", "world"]
|> Enum.all?(&String.contains?("hello world", &1))
```

## Examples

```elixir
def contains_any?(string, patterns) do
  Enum.any?(patterns, &String.contains?(string, &1))
end

def redact_sensitive(text) do
  ["password", "secret", "token"]
  |> Enum.reduce(text, fn pattern, acc ->
    String.replace(acc, pattern, "[REDACTED]")
  end)
end
```

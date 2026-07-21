---
title: "[Solution] Elixir Regex Error -- Invalid Pattern Compilation"
description: "Fix Elixir regex errors when regular expression patterns fail to compile or match incorrectly."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir Regex Error

This error occurs when a regular expression pattern is invalid or fails to compile due to syntax errors.

## Common Causes

- Unclosed parentheses or brackets in regex pattern
- Invalid escape sequences in regex strings
- Using Elixir string escapes that conflict with regex escapes
- Pattern too complex causing catastrophic backtracking

## How to Fix

### Use raw sigil syntax

```elixir
# WRONG: double escaping
Regex.run(~r/^\\d+$/, "123")

# CORRECT: use raw sigil
Regex.run(~r/^\d+$/, "123")
```

### Test patterns before deployment

```elixir
pattern = ~r/(?<email>[^\s@]+@[^\s@]+\.[^\s@]+)/
case Regex.named_captures(pattern, "user@example.com") do
  %{"email" => email} -> IO.puts("Found: #{email}")
  nil -> IO.puts("No match")
end
```

## Examples

```elixir
defmodule Validator do
  @email_pattern ~r/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/

  def valid_email?(email) do
    Regex.match?(@email_pattern, email)
  end
end
```

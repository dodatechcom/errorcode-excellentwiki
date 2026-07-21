---
title: "[Solution] Elixir Sigil Error -- Incorrect Sigil Usage"
description: "Fix Elixir sigil errors when using custom or built-in sigils with wrong delimiters or modifiers."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Sigil Error

This error occurs when sigils are used with incorrect delimiters, missing modifiers, or invalid content.

## Common Causes

- Mismatched delimiters in sigil (opening `[` with closing `)`)
- Using modifiers that are not supported by the sigil
- Invalid content inside sigil (e.g., unescaped delimiters)
- Using sigils with wrong argument count

## How to Fix

### Match delimiters correctly

```elixir
# WRONG: mismatched delimiters
pattern = ~r/^test$/[  # error: mismatched bracket

# CORRECT: match opening and closing
pattern = ~r/^test$/

# Different delimiter pairs are valid
list = ~w[foo bar baz]
tuple = ~w(foo bar baz)
```

### Use correct modifiers

```elixir
# WRONG: 'i' modifier not valid for ~s
str = ~s(hello)i  # no effect for string sigil

# CORRECT: use ~r for regex with modifiers
pattern = ~r/hello/i
```

## Examples

```elixir
defmodule PathUtils do
  @path_regex ~r/^(?<dir>.+)\/(?<file>[^\/]+)$/

  def split_path(path) do
    Regex.named_captures(@path_regex, path)
  end
end
```

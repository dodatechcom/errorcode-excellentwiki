---
title: "[Solution] Elixir String Split Error -- Incorrect Delimiter Usage"
description: "Fix Elixir string split errors when String.split is used with incorrect delimiters or options."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir String Split Error

This error occurs when `String.split/2` or `String.split/3` is called with invalid delimiters or options.

## Common Causes

- Using regex delimiter when a string is expected
- Empty string as delimiter causing unexpected behavior
- Not using trim: true for empty trailing elements
- Splitting on multi-byte characters incorrectly

## How to Fix

### Use correct delimiter type

```elixir
# WRONG: using regex when string expected
String.split("hello world", "/ /")

# CORRECT: use correct delimiter
String.split("hello world", " ")  # ["hello", "world"]
```

### Use options correctly

```elixir
# Split with limit
String.split("a,b,c,d", ",", parts: 2)  # ["a", "b,c,d"]

# Trim empty parts
String.split("a,,b,,c", ",", trim: true)  # ["a", "b", "c"]
```

## Examples

```elixir
def parse_csv_line(line) do
  line
  |> String.split(",", trim: true)
  |> Enum.map(&String.trim/1)
end
```

---
title: "[Solution] Elixir String UTF-8 Error -- Invalid Byte Sequences"
description: "Fix Elixir string UTF-8 errors when strings contain invalid byte sequences or non-UTF-8 data."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Elixir String UTF-8 Error

This error occurs when Elixir encounters a binary that is not valid UTF-8 when performing string operations.

## Common Causes

- Reading binary data as a string without checking encoding
- Processing network responses with non-UTF-8 content
- Splitting or indexing into binaries with invalid byte sequences
- Concatenating binaries that form incomplete multi-byte characters

## How to Fix

### Validate encoding before string operations

```elixir
# WRONG: assuming binary is valid UTF-8
String.length(<<0xFF, 0xFE>>)

# CORRECT: validate encoding
binary = <<0xFF, 0xFE>>
if String.valid?(binary) do
  String.length(binary)
else
  {:error, :invalid_utf8}
end
```

### Use Binary pattern matching

```elixir
def safe_to_string(data) do
  if String.valid?(data) do
    {:ok, data}
  else
    {:error, :invalid_encoding}
  end
end
```

## Examples

```elixir
def process_raw_data(raw) do
  case String.valid?(raw) do
    true -> {:ok, String.trim(raw)}
    false -> {:error, :bad_encoding}
  end
end
```

---
title: "[Solution] Elixir Bitstring Syntax Error -- Binary Construction Issues"
description: "Fix Elixir bitstring syntax errors when constructing or pattern matching binaries incorrectly."
languages: ["elixir"]
error-types: ["compile-time"]
severities: ["error"]
---

# Elixir Bitstring Syntax Error

This error occurs when bitstring syntax is incorrect, such as invalid size modifiers or type mismatches.

## Common Causes

- Using `binary` size with non-binary data
- Incorrect bit-level size specification
- Mixing bit-level and byte-level constructs
- Pattern matching with invalid bitstring syntax

## How to Fix

### Use correct bitstring syntax

```elixir
# WRONG: invalid size specification
<<x::binary-size(3)>> = "hello"  # 3 bytes

# CORRECT: use valid size
<<x::binary-size(3), rest::binary>> = "hello"
# x = "hel", rest = "lo"
```

### Construct binaries correctly

```elixir
# WRONG: mixing bit-level constructs
<<1::4, "test">>  # error: cannot mix

# CORRECT: consistent construction
<<1::4, 2::4>>  # two nibbles
<<1::8, "test">>  # byte followed by binary
```

## Examples

```elixir
defmodule PacketParser do
  def parse(<<length::16, payload::binary-size(length), rest::binary>>) do
    {payload, rest}
  end

  def parse(<<>>), do: {<<>>, <<>>}
end
```

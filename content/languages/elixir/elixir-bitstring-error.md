---
title: "[Solution] Elixir Bitstring Construction Error — Invalid Binary Syntax"
description: "Fix Elixir bitstring construction errors. Learn about binary syntax, bitstring modifiers, and binary pattern matching in Elixir."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A bitstring construction error occurs when you try to create or match a bitstring with invalid syntax or incompatible modifiers. Elixir's bitstring syntax `<<...>>` is powerful but strict about type compatibility and modifier usage.

## Why It Happens

The most common cause is mixing incompatible types in a bitstring. For example, trying to put a string directly into a numeric bitstring without converting it first.

Another frequent cause is using wrong size modifiers. If you specify `size(8)` for a type that requires more bits, the construction fails.

Pattern matching on bitstrings with incorrect segment sizes causes this error. If the binary data does not match the expected segment sizes, the match fails.

Using `bitstring` instead of `binary` for types that require byte-aligned data causes issues. `bitstring` allows arbitrary bit lengths while `binary` requires full bytes.

Finally, concatenating bitstrings with different endianness or signedness modifiers can cause unexpected behavior.

## How to Fix It

### Use correct type modifiers

```elixir
# Wrong — string cannot go directly in numeric context
<<value::integer>> = "hello"

# Correct — use binary for strings
<<value::binary>> = "hello"
```

### Match bitstring segments correctly

```elixir
# Pattern match on specific byte sequences
<<header::binary-size(4), payload::binary>> = data

# Match on individual bytes
<<a::8, b::8, c::8>> = <<1, 2, 3>>
```

### Use appropriate size specifications

```elixir
# 16-bit integer
<<value::16>> = <<0, 255>>

# 32-bit float
<<value::float-size(32)>> = <<64, 72, 0, 0>>
```

### Concatenate bitstrings properly

```elixir
# Correct — compatible types
<<1, 2>> <> <<3, 4>>  # Returns <<1, 2, 3, 4>>

# With specific types
<<value::16, rest::binary>> = <<0, 1, 2, 3>>
```

### Use for comprehensions for binary processing

```elixir
for <<byte <- "hello">> do
  byte + 1
end
```

## Common Mistakes

- Not specifying size modifiers for numeric bitstrings
- Using `bitstring` when `binary` is required
- Assuming bitstring concatenation works like string concatenation
- Not matching on the exact number of bytes expected
- Forgetting that bitstrings are zero-indexed

## Related Pages

- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)

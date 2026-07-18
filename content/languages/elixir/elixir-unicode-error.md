---
title: "[Solution] Elixir UnicodeConversionError — Invalid Byte Sequence"
description: "Fix Elixir UnicodeConversionError with invalid byte sequences. Learn about UTF-8 validation, binary encoding, and string sanitization."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `UnicodeConversionError` is raised when Elixir encounters an invalid byte sequence during string operations. This error occurs when binary data that is not valid UTF-8 is used in string functions like `String.length`, `String.downcase`, or IO operations.

## Why It Happens

The most common cause is reading binary data from external sources (files, network, databases) that contains non-UTF-8 bytes. If the data was created with a different encoding (like Latin-1 or Windows-1252), the bytes may not be valid UTF-8.

Another frequent cause is concatenating binaries that are not properly encoded. If you combine a UTF-8 string with raw bytes, the result may be invalid.

String interpolation with raw binary data can produce invalid sequences. If a variable contains non-UTF-8 bytes and is interpolated into a string, the error occurs.

Protocol implementations that receive binary data may fail if the data is not valid UTF-8. For example, `String.Chars.to_string/1` requires valid UTF-8.

Finally, truncating a binary at an arbitrary byte position can split a multi-byte UTF-8 character, creating an invalid sequence.

## How to Fix It

### Validate UTF-8 before string operations

```elixir
def safe_string操作(data) do
  if String.valid?(data) do
    String.length(data)
  else
    # Handle invalid encoding
    byte_size(data)
  end
end
```

### Use String.replace to remove invalid bytes

```elixir
sanitized = String.replace(data, ~r/[^\x00-\x7F]/, "")
```

### Read files with explicit encoding

```elixir
{:ok, content} = File.read("file.txt")
if String.valid?(content) do
  process(content)
else
  # Try to convert from Latin-1
  content |> :unicode.characters_to_binary(:latin1) |> process()
end
```

### Use Codepages for encoding conversion

```elixir
# Convert from Latin-1 to UTF-8
latin1_binary = <<195, 169>>  # "é" in Latin-1
utf8_binary = :unicode.characters_to_binary(latin1_binary, :latin1)
```

### Truncate binaries safely

```julia
def safe_truncate(binary, max_bytes) do
  if byte_size(binary) <= max_bytes do
    binary
  else
    truncated = binary_part(binary, 0, max_bytes)
    # Find last valid UTF-8 character boundary
    find_valid_boundary(truncated)
  end
end
```

## Common Mistakes

- Assuming all binary data is valid UTF-8
- Not checking String.valid? before string operations
- Truncating binaries at arbitrary byte positions
- Mixing encodings without explicit conversion
- Not handling encoding errors from external data sources

## Related Pages

- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir File.Error](/languages/elixir/elixir-filenotfounderror/)

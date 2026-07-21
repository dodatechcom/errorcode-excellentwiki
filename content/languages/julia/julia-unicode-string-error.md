---
title: "Julia Unicode String Encoding Error"
description: "Fix Julia Unicode string errors when handling strings with non-ASCII characters and encoding conversions."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Unicode errors in Julia occur when strings contain invalid byte sequences for UTF-8 encoding, or when converting between string encodings incorrectly.

## Common Causes

- String contains invalid UTF-8 byte sequences
- Mixing byte arrays and strings incorrectly
- File read with wrong encoding
- String concatenation producing invalid Unicode
- Comparing strings with different normalization forms

## How to Fix

```julia
# WRONG: Invalid UTF-8 bytes
str = String([0x80, 0x81])  # invalid UTF-8
# may produce replacement characters

# CORRECT: Validate encoding
bytes = [0x48, 0x65, 0x6C, 0x6C, 0x6F]  # "Hello" in UTF-8
str = String(bytes)
isvalid(str)  # true
```

```julia
# WRONG: Treating string as raw bytes
str = "café"
bytes = Vector{UInt8}(str)  # gives UTF-8 bytes
length(bytes)  # 5, not 4!

# CORRECT: Use appropriate functions
str = "café"
ncodeunits(str)   # 5 (bytes)
length(str)       # 4 (characters)
thisind(str, 1)   # 1 (valid index)
nextind(str, 1)   # 2 (next valid index)
```

## Examples

```julia
# Example 1: Unicode string operations
str = "Hello 世界 🌍"
length(str)      # 10 characters
ncodeunits(str)  # 14 bytes
sizeof(str)      # 14

# Example 2: String normalization
using Unicode
str = "café"
nfc = normalize(str, :NFC)
nfd = normalize(str, :NFD)
nfc == nfd  # may differ in byte representation

# Example 3: Safe string from bytes
function safe_string(bytes::Vector{UInt8})
    io = IOBuffer()
    write(io, bytes)
    return String(take!(io))
end
```

## Related Errors

- [String error](julia-nsstring-error) -- string operations
- [IO error](julia-io-stream-error) -- file encoding issues

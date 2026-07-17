---
title: "[Solution] Swift Unicode Error Fix"
description: "Fix Swift Unicode errors. Learn why Unicode string operations fail and how to handle multi-byte characters."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

Unicode errors occur when string operations fail due to multi-byte characters, invalid encodings, or scalar value issues. Swift strings are Unicode-correct, but operations on characters can be surprising.

## Common Causes

- Accessing string by integer index
- Combining characters (e.g. accented letters)
- Invalid UTF-8 sequences
- Emoji and multi-scalar characters

## How to Fix

```swift
// WRONG: Integer string indexing
let str = "Hello"
// str[1]  // Compile error in Swift

// CORRECT: Use String.Index
let str = "Hello"
let index = str.index(str.startIndex, offsetBy: 1)
let char = str[index]  // "e"
```

```swift
// WRONG: Counting characters incorrectly
let emoji = " family "
// emoji.count may be unexpected with complex emoji

// CORRECT: Understand String.count
let emoji = " family "
print(emoji.count)  // 9 (family is a single grapheme cluster)

// Or use unicodeScalars
print(emoji.unicodeScalars.count)  // More than 9
```

```swift
// WRONG: Invalid UTF-8 data
let data = Data([0xFF, 0xFE])
let str = String(data: data, encoding: .utf8)  // nil

// CORRECT: Handle invalid encoding
if let str = String(data: data, encoding: .utf8) {
    print(str)
} else {
    print("Invalid UTF-8")
}
```

## Examples

```swift
// Example 1: String iteration
let str = "Hello"
for char in str {
    print(char)
}

// Example 2: Character count
let str = " family "
print(str.count)  // 9

// Example 3: Unicode scalar access
let str = " family "
let scalars = str.unicodeScalars
for scalar in scalars {
    print("\(scalar) (U+\(String(scalar.value, radix: 16)))")
}
```

## Related Errors

- [String interpolation error](string-interpolation-error) — string formatting
- [Floating point error](floating-point-error-swift) — precision issues
- [Encoding error](encoding-error-swift) — JSON encoding failed

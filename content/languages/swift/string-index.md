---
title: "[Solution] Swift Error — String Index Is Out of Bounds"
description: "Fix Swift string index out of bounds errors. Learn why string indexing differs from arrays and how to safely navigate string characters."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# String Index Is Out of Bounds

This error occurs when you access a `String.Index` that is not within the valid range of the string's characters. String indices in Swift are not integers, making this error more subtle than array index errors.

## Description

Swift strings store characters using UTF-8 encoding internally. A `String.Index` is an opaque type, not a simple integer. You cannot use integer subscripts directly on strings. Attempting to advance an index beyond the string's bounds, or using an index from a different string, causes this crash.

Common patterns:

- **Integer indexing** — using `str[i]` where `i` is an `Int`.
- **Advancing too far** — `str.index(str.startIndex, offsetBy: n)` where `n > str.count`.
- **Wrong string index** — using an index from one string on another.
- **Substring mismatch** — creating ranges between indices of different strings.

## Common Causes

```swift
// Cause 1: Advancing index beyond string end
let str = "Hi"
let idx = str.index(str.startIndex, offsetBy: 10)
let char = str[idx] // Fatal error

// Cause 2: Using integer subscript (won't compile, but common confusion)
// let char = str[0] // Compiler error — not Int subscript

// Cause 3: Index from different string
let str1 = "Hello, World!"
let str2 = "Hi"
let idx = str1.index(str1.startIndex, offsetBy: 5)
let char = str2[idx] // Fatal error

// Cause 4: Empty string access
let empty = ""
let char = empty[empty.startIndex] // Fatal error
```

## How to Fix

### Fix 1: Bounds-check before accessing

```swift
let str = "Hello"
let offset = 10

// Wrong
let idx = str.index(str.startIndex, offsetBy: offset)
let char = str[idx]

// Correct
if offset < str.count {
    let idx = str.index(str.startIndex, offsetBy: offset)
    let char = str[idx]
}
```

### Fix 2: Use safe index access

```swift
extension String {
    subscript(safe offset: Int) -> Character? {
        guard offset >= 0, offset < count else { return nil }
        return self[index(startIndex, offsetBy: offset)]
    }
}

let str = "Hello"
let char = str[safe: 10] // nil instead of crash
```

### Fix 3: Use enumerated() for character iteration

```swift
let str = "Hello"

// Wrong — manual index tracking
var idx = str.startIndex
for _ in 0..<10 {
    let char = str[idx] // May crash
    idx = str.index(after: idx)
}

// Correct
for (i, char) in str.enumerated() {
    print("\(i): \(char)")
}
```

### Fix 4: Always check before using substring ranges

```swift
let str = "Hello"
let start = str.index(str.startIndex, offsetBy: 3)
let end = str.index(str.startIndex, offsetBy: 7)

// Correct — check that end doesn't exceed string
if end <= str.endIndex {
    let sub = str[start..<end]
}
```

## Examples

```swift
// Example 1: Off-by-one in string offset
let name = "Swift"
let idx = name.index(name.startIndex, offsetBy: name.count)
let char = name[idx] // Fatal error: past endIndex

// Example 2: Using .utf16 index incorrectly
let emoji = "Hello 👋"
let idx16 = emoji.utf16.index(emoji.startIndex, offsetBy: 6)
// Character boundaries may not align with UTF-16 offsets

// Example 3: Empty string
let text = ""
let first = text[text.startIndex] // Fatal error
```

## Related Errors

- [Index Out of Range]({{< relref "/languages/swift/index-out-of-range" >}}) — general index out of range.
- [Array Index Out of Range]({{< relref "/languages/swift/array-index" >}}) — array subscript error.
- [Range Requires lowerBound <= upperBound]({{< relref "/languages/swift/out-of-bounds" >}}) — invalid range.

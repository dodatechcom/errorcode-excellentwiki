---
title: "[Solution] Swift Error — Range Requires lowerBound <= upperBound"
description: "Fix Swift range errors where the lower bound exceeds the upper bound. Learn why invalid ranges crash and how to construct safe ranges."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Range Requires lowerBound <= upperBound

This error occurs when you construct a `Range` or `ClosedRange` where the lower bound is greater than the upper bound. The runtime crashes because such a range is mathematically invalid.

## Description

Swift ranges represent sequences of consecutive values. A `Range` (`0..<n`) requires `lowerBound < upperBound`, and a `ClosedRange` (`0...n`) requires `lowerBound <= upperBound`. This error commonly occurs with calculated bounds from external data, negative offsets, or arithmetic that produces unexpected values.

Common patterns:

- **Calculated upper bound** — arithmetic producing a lower value than expected.
- **Negative counts** — using `count - 1` when count is 0.
- **String ranges** — mismatched string indices in substring operations.
- **Slice operations** — creating ranges from indices of different collections.

## Common Causes

```swift
// Cause 1: Calculated range with wrong math
let count = 0
let range = 0...(count - 1) // Fatal error: 0...-1

// Cause 2: Empty collection range
let items: [Int] = []
let slice = items[0..<items.count] // Valid, but...
let range = items.count..<0 // Fatal error

// Cause 3: String index range mismatch
let str = "Hello"
let start = str.index(str.startIndex, offsetBy: 5)
let end = str.index(str.startIndex, offsetBy: 2)
let sub = str[start..<end] // Fatal error

// Cause 4: Reversed bounds from variables
let low = 10
let low2 = 5
let r = low...low2 // Fatal error
```

## How to Fix

### Fix 1: Guard against empty collections

```swift
let items: [Int] = []

// Wrong
let range = 0...(items.count - 1)

// Correct
guard !items.isEmpty else { return }
let range = 0...(items.count - 1)
```

### Fix 2: Use clamped ranges

```swift
let count = 3

// Wrong — crashes if count is 0
let range = 0..<count

// Correct — safe with clamped
let safeCount = max(0, count)
let range = 0..<safeCount
```

### Fix 3: Use min/max for bounds

```swift
let a = 10
let b = 5

// Wrong
let range = a...b

// Correct
let range = min(a, b)...max(a, b)
```

### Fix 4: Validate string indices before use

```swift
let str = "Hello"
let startOffset = 5
let endOffset = 2

// Wrong
let start = str.index(str.startIndex, offsetBy: startOffset)
let end = str.index(str.startIndex, offsetBy: endOffset)
let sub = str[start..<end]

// Correct
let startIdx = str.index(str.startIndex, offsetBy: min(startOffset, endOffset))
let endIdx = str.index(str.startIndex, offsetBy: max(startOffset, endOffset))
let sub = str[startIdx..<endIdx]
```

## Examples

```swift
// Example 1: Negative upper bound
let n = 0
let r = 0...n-1 // Fatal error: Range requires lowerBound <= upperBound

// Example 2: Closed range with count
let arr = [1]
let range = 0...arr.count // Fatal error: 0...1 is fine but 0...arr.count overshoots

// Example 3: Substring with mismatched indices
let text = "AB"
let start = text.index(text.startIndex, offsetBy: 2)
let end = text.startIndex
let slice = text[start..<end] // Fatal error
```

## Related Errors

- [Index Out of Range]({{< relref "/languages/swift/index-out-of-range" >}}) — index access out of bounds.
- [String Index Is Out of Bounds]({{< relref "/languages/swift/string-index" >}}) — string index out of bounds.
- [Array Index Out of Range]({{< relref "/languages/swift/array-index" >}}) — array subscript out of bounds.

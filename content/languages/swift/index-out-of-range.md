---
title: "[Solution] Swift Error — Index Out of Range"
description: "Fix Swift index out of range errors. Learn why this error occurs when accessing arrays, strings, and collections by invalid indices."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Index Out of Range

An "Index out of range" error occurs when you try to access an element at a position that doesn't exist in a collection, string, or range. The index is either negative, too large, or the collection is empty.

## Description

Swift collections (arrays, dictionaries, strings) use zero-based indexing. An array of length `n` has valid indices from `0` to `n-1`. Accessing any index outside this range triggers a runtime error. This is common with off-by-one mistakes, empty collections, or using stale indices after mutations.

Common patterns:

- **Off-by-one error** — accessing `array[array.count]` instead of `array[array.count - 1]`.
- **Empty collection access** — accessing index 0 of an empty array.
- **Stale index after modification** — using an index after removing elements.
- **Hardcoded index** — assuming a collection always has a certain number of elements.

## Common Causes

```swift
// Cause 1: Off-by-one error
let items = [1, 2, 3]
let value = items[3] // Fatal error: Index out of range

// Cause 2: Empty collection access
let empty: [Int] = []
let value = empty[0] // Fatal error: Index out of range

// Cause 3: Stale index after modification
var data = [10, 20, 30, 40, 50]
for i in 0..<data.count {
    if data[i] == 20 {
        data.remove(at: i)
    }
}
print(data[3]) // Fatal error — count decreased

// Cause 4: Wrong range in loop
let items = [1, 2, 3]
for i in 0...items.count {
    print(items[i]) // Fatal error when i == 3
}
```

## How to Fix

### Fix 1: Check collection bounds before accessing

```swift
let items = [1, 2, 3]

// Wrong
let value = items[3]

// Correct
if items.count > 3 {
    let value = items[3]
}
```

### Fix 2: Use optional subscript

```swift
let items = [1, 2, 3]

// Wrong
let value = items[10]

// Correct — returns nil instead of crashing
if let value = items[safe: 10] {
    print(value)
}

// Safe subscript extension
extension Collection {
    subscript(safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}
```

### Fix 3: Use prefix or dropFirst for safe sub-ranges

```swift
let items = [1, 2, 3, 4, 5]

// Safe access via prefix
let firstThree = items.prefix(3)

// Safe access via dropFirst
let withoutFirst = items.dropFirst()
```

### Fix 4: Avoid index-based iteration when possible

```swift
let items = [1, 2, 3]

// Wrong
for i in 0..<items.count {
    print(items[i])
}

// Correct — iterate directly
for item in items {
    print(item)
}

// Or use enumerated() if you need the index
for (i, item) in items.enumerated() {
    print("\(i): \(item)")
}
```

## Examples

```swift
// Example 1: Accessing empty array
let numbers: [Int] = []
let first = numbers[0] // Fatal error: Index out of range

// Example 2: Wrong loop range
let names = ["Alice", "Bob"]
for i in 0...names.count {
    print(names[i]) // Crashes at i == 2
}

// Example 3: String index out of range
let greeting = "Hello"
let char = greeting[greeting.startIndex.advanced(by: 10)]
// Fatal error: String index is out of bounds
```

## Related Errors

- [Array Index Out of Range]({{< relref "/languages/swift/array-index" >}}) — specific array subscript error.
- [String Index Is Out of Bounds]({{< relref "/languages/swift/string-index" >}}) — string-specific index error.
- [Range Requires lowerBound <= upperBound]({{< relref "/languages/swift/out-of-bounds" >}}) — invalid range construction.

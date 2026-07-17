---
title: "[Solution] Swift Index Out of Range Fix"
description: "Fix Swift index out of range errors. Learn why array and string indexing fails and how to access elements safely."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["index-out-of-range", "array", "string", "swift"]
weight: 5
---

## What This Error Means

An index out of range error occurs when you try to access an element at an index that doesn't exist in the collection. This is one of the most common Swift runtime errors.

## Common Causes

- Accessing array with index >= count
- Empty array access
- String character indexing issues
- Off-by-one errors in loops

## How to Fix

```swift
// WRONG: Index beyond bounds
let numbers = [1, 2, 3]
let value = numbers[5]  // Fatal error: index out of range

// CORRECT: Check bounds first
if numbers.indices.contains(5) {
    let value = numbers[5]
}

// Or use safe subscript
let value = numbers[safe: 5]  // nil
```

```swift
// WRONG: Accessing first/last on empty array
let empty: [Int] = []
let first = empty[0]  // Fatal error

// CORRECT: Use optional properties
let first = empty.first  // nil
let last = empty.last    // nil
```

```swift
// WRONG: Off-by-one in loop
let items = ["a", "b", "c"]
for i in 0...items.count {  // Count is 3, but indices are 0,1,2
    print(items[i])  // Crashes at i=3
}

// CORRECT: Use proper range
for i in 0..<items.count {
    print(items[i])
}
// Or better:
for item in items {
    print(item)
}
```

## Examples

```swift
// Example 1: Safe array access
extension Array {
    subscript(safe index: Int) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}

let arr = [1, 2, 3]
arr[safe: 0]  // Optional(1)
arr[safe: 5]  // nil

// Example 2: String indexing
let str = "Hello"
let index = str.startIndex
str[index]  // "H"

// Example 3: Enumerate
for (index, item) in items.enumerated() {
    print("\(index): \(item)")
}
```

## Related Errors

- [Nil unwrap error](nil-unwrap-error) — force unwrapping nil
- [Type cast error](type-cast-error) — type casting failed
- [Key not found](key-not-found-swift) — dictionary key missing

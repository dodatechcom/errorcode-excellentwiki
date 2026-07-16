---
title: "[Solution] Swift Array Index — Index Out of Range Fix"
description: "Fix Swift array index out of range crashes. Learn how to safely access array elements with bounds checking."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["array-index", "index-out-of-range", "collection", "swift"]
weight: 5
---

# Array Index — Index Out of Range

An index out of range crash occurs when you access an array element at an index that doesn't exist.

## Description

Swift arrays are zero-indexed. Accessing an index beyond `count - 1` or a negative index causes a fatal error. This is a common crash, especially with dynamic indices.

Common causes:

- **Off-by-one error** — accessing index equal to array count
- **Empty array access** — trying to access elements in empty array
- **Dynamic index** — computed index exceeds bounds
- **String index confusion** — using Int index on String characters

## Common Causes

```swift
// Cause 1: Off-by-one error
let arr = [1, 2, 3]
print(arr[3])  // Fatal error: Index out of range

// Cause 2: Empty array
let empty: [Int] = []
print(empty[0])  // Fatal error: Index out of range

// Cause 3: Dynamic index
let items = ["a", "b", "c"]
let index = items.count
print(items[index])  // Fatal error

// Cause 4: String index
let str = "Hello"
let char = str[str.startIndex]  // Works, but str[1] doesn't compile
```

## How to Fix

### Fix 1: Check bounds before access

```swift
// Wrong
let arr = [1, 2, 3]
print(arr[5])  // Crash

// Correct
if index < arr.count {
    print(arr[index])
}
```

### Fix 2: Use optional subscript

```swift
// Wrong
let arr = [1, 2, 3]
print(arr[5])  // Crash

// Correct
if let value = arr[safe: 5] {
    print(value)
}

// Or extend Array
extension Array {
    subscript(safe index: Int) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}
```

### Fix 3: Use first/last safely

```swift
// Wrong
let arr = [1, 2, 3]
print(arr[arr.count - 1])  // Crash if empty

// Correct
if let last = arr.last {
    print(last)
}
```

### Fix 4: Use prefix/suffix

```swift
// Wrong
let arr = [1, 2, 3]
print(arr[0..<5])  // Works but may be unexpected

// Correct
let slice = arr.prefix(2)  // [1, 2]
```

## Examples

```swift
// Example 1: Safe array access
let numbers = [10, 20, 30]
extension Array {
    subscript(safe index: Int) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}
print(numbers[safe: 1] ?? "nil")  // 20
print(numbers[safe: 10] ?? "nil")  // nil

// Example 2: Iterating safely
let items = ["a", "b", "c"]
for index in 0..<items.count {
    print(items[index])
}
```

## Related Errors

- [String Index Out of Range]({{< relref "/languages/swift/string-index" >}}) — invalid string character index
- [Nil Unwrap]({{< relref "/languages/swift/nil-unwrap" >}}) — force unwrapping nil
- [Out of Bounds]({{< relref "/languages/swift/out-of-bounds" >}}) — collection access beyond bounds

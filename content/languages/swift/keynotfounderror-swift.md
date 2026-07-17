---
title: "[Solution] Swift KeyNotFoundError Fix"
description: "Fix Swift KeyNotFoundError in dictionaries. Learn why dictionary key lookups fail and how to handle missing keys properly."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["keynotfound", "dictionary", "key", "swift"]
weight: 5
---

## What This Error Means

A `KeyNotFoundError` occurs when you access a dictionary with a key that doesn't exist and no default value is provided. In Swift, dictionary subscript returns an optional, but force-unwrapping nil causes a crash.

## Common Causes

- Accessing non-existent key with force unwrap
- Typo in key name
- Data structure changed but code wasn't updated
- Missing initialization of dictionary values

## How to Fix

```swift
// WRONG: Force unwrapping non-existent key
let dict = ["name": "Alice"]
let age = dict["age"]!  // Fatal error

// CORRECT: Use optional binding
if let age = dict["age"] {
    print(age)
} else {
    print("Key not found")
}
```

```swift
// WRONG: Not providing default value
var scores = ["math": 95]
let science = scores["science"]  // nil

// CORRECT: Provide default value
let science = scores["science"] ?? 0
```

```swift
// WRONG: Typo in key
let config = ["host": "localhost"]
let port = config["prot"]  // nil (typo)

// CORRECT: Verify key exists
let port = config["port"] ?? "3000"
```

## Examples

```swift
// Example 1: Safe dictionary access
let dict = ["a": 1, "b": 2, "c": 3]
if let value = dict["b"] {
    print(value)  // 2
}

// Example 2: Default values
let defaults = ["color": "blue", "size": "medium"]
let font = defaults["font"] ?? "Arial"

// Example 3: Dictionary with default
var counts: [String: Int] = [:]
counts["apple", default: 0] += 1
counts["apple", default: 0] += 1
print(counts["apple"]!)  // 2
```

## Related Errors

- [Index out of range](index-out-of-range-swift) — array index beyond bounds
- [Nil unwrap error](nil-unwrap-error) — force unwrapping nil
- [Decoding error](decoding-error-swift) — JSON decoding failed

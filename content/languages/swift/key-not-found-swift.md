---
title: "[Solution] Swift Key Not Found — Dictionary Key Not Found Fix"
description: "Fix Swift dictionary key not found errors. Learn how to safely access dictionary keys with optional binding and default values."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["key-not-found", "dictionary", "hashmap", "swift"]
weight: 5
---

# Key Not Found — Dictionary Key Not Found

A key not found error occurs when you access a dictionary key that doesn't exist without a default value.

## Description

Swift dictionaries return optionals when accessing keys with subscript. However, if you force-unwrap the result of a missing key, or if your code expects a key to exist, you'll get a runtime error.

Common causes:

- **Missing key assumption** — assuming key exists without checking
- **Typo in key name** — misspelling dictionary key
- **Config data** — missing configuration values
- **API response** — unexpected keys in JSON data

## Common Causes

```swift
// Cause 1: Force unwrapping missing key
let dict: [String: Int] = ["a": 1]
let value = dict["b"]!  // Fatal error: Unexpectedly found nil

// Cause 2: Typo in key name
let config: [String: String] = ["userName": "Alice"]
let name = config["username"]  // nil (case sensitive)

// Cause 3: Missing nested key
let data: [String: [String: Int]] = ["scores": ["math": 95]]
let science = data["grades"]!["science"]!  // Fatal error

// Cause 4: Wrong key type
let dict: [String: Int] = ["1": 100]
let value = dict[1]  // nil (Int vs String key)
```

## How to Fix

### Fix 1: Use optional binding

```swift
// Wrong
let dict: [String: Int] = ["a": 1]
let value = dict["b"]!  // Crash

// Correct
if let value = dict["b"] {
    print(value)
} else {
    print("Key not found")
}
```

### Fix 2: Use nil coalescing

```swift
// Wrong
let dict: [String: Int] = ["a": 1]
let value = dict["b"]!  // Crash

// Correct
let value = dict["b"] ?? 0
```

### Fix 3: Use default values

```swift
// Wrong
let dict: [String: Int] = ["a": 1]
let value = dict["b"]!  // Crash

// Correct
let value = dict["b", default: 0]
```

### Fix 4: Use safe subscript

```swift
// Wrong
let data: [String: [String: Int]] = ["scores": ["math": 95]]
let science = data["grades"]!["science"]!  // Crash

// Correct
let science = data["grades"]?["science"]  // nil, no crash
```

## Examples

```swift
// Example 1: Safe dictionary access
let config: [String: Any] = ["theme": "dark", "fontSize": 14]
let theme = config["theme"] as? String ?? "light"
let fontSize = config["fontSize"] as? Int ?? 12

// Example 2: Dictionary with defaults
var wordCount: [String: Int] = ["hello": 5]
wordCount["world", default: 0] += 1
wordCount["hello", default: 0] += 1
// ["hello": 6, "world": 1]
```

## Related Errors

- [Nil Unwrap]({{< relref "/languages/swift/nil-unwrap" >}}) — force unwrapping nil
- [Force Unwrap]({{< relref "/languages/swift/force-unwrap" >}}) — bang operator crash
- [Array Index Out of Range]({{< relref "/languages/swift/array-index" >}}) — index beyond bounds

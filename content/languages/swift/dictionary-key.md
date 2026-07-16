---
title: "[Solution] Swift Error — Key Not Found in Dictionary"
description: "Fix Swift dictionary key not found errors. Learn why accessing a missing dictionary key crashes and how to handle optional values safely."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["dictionary", "key", "keynotfound", "optional", "subscript"]
weight: 5
---

# Key Not Found in Dictionary

This error occurs when you force-unwrap a dictionary subscript for a key that doesn't exist, or when iterating over keys that have been removed.

## Description

Dictionaries in Swift return optionals when accessed by subscript. If you force-unwrap (`!`) the result and the key doesn't exist, the runtime crashes. This is common with misspelled keys, keys from external data, or assumptions about dictionary contents.

Common patterns:

- **Force-unwrapping missing key** — `dict["missing"]!`.
- **Misspelled key** — using `"userName"` when the key is `"username"`.
- **External data** — JSON with unexpected structure.
- **Concurrent modification** — key removed by another thread during access.

## Common Causes

```swift
// Cause 1: Force-unwrapping missing key
let dict = ["name": "Alice", "age": 30]
let email = dict["email"]! // Fatal error: nil

// Cause 2: Misspelled key
let config = ["backgroundColor": "blue"]
let bg = config["backgroundcolor"] // nil

// Cause 3: Assuming key exists
let userData: [String: Any] = fetchFromAPI()
let name = userData["name"]! // May not exist

// Cause 4: Concurrent access
var cache: [String: String] = [:]
// Thread A removes key while Thread B force-unwraps it
```

## How to Fix

### Fix 1: Use optional binding

```swift
let dict = ["name": "Alice", "age": 30]

// Wrong
let email = dict["email"]!

// Correct
if let email = dict["email"] {
    print(email)
} else {
    print("Email not found")
}
```

### Fix 2: Use nil coalescing for defaults

```swift
let dict = ["name": "Alice"]

// Wrong
let email = dict["email"]!

// Correct
let email = dict["email"] ?? "unknown@example.com"
```

### Fix 3: Use default value subscript

```swift
var counts: [String: Int] = [:]

// Wrong — crashes if key missing
let count = counts["apples"]!

// Correct — returns 0 if key missing
let count = counts["apples", default: 0]
```

### Fix 4: Validate keys from external data

```swift
let json: [String: Any] = ["name": "Alice", "age": 30]

// Wrong
let name = json["name"]! as! String

// Correct
if let name = json["name"] as? String {
    print(name)
}
```

## Examples

```swift
// Example 1: Force-unwrapping a nil dictionary value
let settings = ["theme": "dark", "lang": "en"]
let fontSize = settings["fontSize"]! // Fatal error

// Example 2: Wrong key casing
let headers = ["Content-Type": "application/json"]
let ct = headers["content-type"]! // Fatal error — wrong case
```

## Related Errors

- [Unexpectedly Found Nil While Unwrapping]({{< relref "/languages/swift/nil-unwrapping" >}}) — nil unwrap crash.
- [Key Not Found]({{< relref "/languages/swift/json-key-not-found" >}}) — JSON key missing during decoding.
- [DecodingError]({{< relref "/languages/swift/json-decoding" >}}) — JSON decoding failures.

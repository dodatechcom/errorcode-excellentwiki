---
title: "[Solution] Swift Nil Unwrap — Unexpectedly Found Nil Fix"
description: "Fix Swift nil unwrap crashes. Learn why force unwrapping optionals causes crashes and how to use safe alternatives like guard and if-let."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Nil Unwrap — Unexpectedly Found Nil

A nil unwrap crash occurs when you force-unwrap (`!`) an optional that holds `nil`.

## Description

Swift optionals represent values that may be absent. Force unwrapping with `!` tells the compiler the value is guaranteed non-nil. If that guarantee is wrong, Swift crashes immediately.

Common causes:

- **Force unwrapping nil optionals** — using `!` on nil value
- **Force try on throwing function** — `try!` when function throws
- **Implicitly unwrapped optionals** — accessing IUO before initialization
- **API data** — force unwrapping optional response data

## Common Causes

```swift
// Cause 1: Force unwrapping nil
let name: String? = nil
print(name!)  // Fatal error: Unexpectedly found nil

// Cause 2: Force try
let data = try! JSONDecoder().decode(MyType.self, from: badData)  // Fatal error

// Cause 3: Implicitly unwrapped optional
var view: UIView!
view.addSubview(UIButton())  // Fatal error before load

// Cause 4: Force unwrapping optional chain
let dict: [String: [Int]] = ["a": [1, 2]]
let value = dict["b"]![0]  // Fatal error
```

## How to Fix

### Fix 1: Use optional binding

```swift
// Wrong
let name: String? = nil
print(name!)  // Crash

// Correct
if let name = name {
    print(name)
} else {
    print("Name is nil")
}
```

### Fix 2: Use guard statement

```swift
// Wrong
let url = URL(string: input)!

// Correct
guard let url = URL(string: input) else {
    print("Invalid URL")
    return
}
```

### Fix 3: Use nil coalescing

```swift
// Wrong
let name: String? = nil
print(name!)  // Crash

// Correct
let name: String? = nil
print(name ?? "Unknown")
```

### Fix 4: Use optional chaining

```swift
// Wrong
let dict: [String: [Int]] = [:]
let value = dict["a"]![0]  // Crash

// Correct
let value = dict["a"]?.first  // nil, no crash
```

## Examples

```swift
// Example 1: Safe URL parsing
let input = "not a url"
if let url = URL(string: input) {
    print(url)
} else {
    print("Invalid URL")
}

// Example 2: Safe dictionary access
let scores: [String: Int] = ["math": 95]
let mathScore = scores["math"] ?? 0
let scienceScore = scores["science"] ?? 0
```

## Related Errors

- [Force Unwrap Crash]({{< relref "/languages/swift/force-unwrap" >}}) — bang operator on nil
- [Unexpectedly Found Nil]({{< relref "/languages/swift/unexpected-nil" >}}) — nil in unexpected context
- [Array Index Out of Range]({{< relref "/languages/swift/array-index" >}}) — index beyond bounds

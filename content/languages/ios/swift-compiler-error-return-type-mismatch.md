---
title: "[Solution] Swift Compiler Error: Return Type Mismatch"
description: "Fix return type mismatch errors in Swift functions."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Return Type Mismatch

Function return types must match exactly. Returning a value of a different type than declared triggers this compiler error.

## Common Causes
- Function declares Int but returns String
- Optional returned where non-optional is expected
- Different tuple element types returned
- Void function returns a value accidentally

## How to Fix
1. Ensure the return value matches the declared type
2. Use type conversion if the types are compatible
3. Update the return type declaration to match actual returns
4. Use optional return type if the function may return nil

```swift
// WRONG: Return type mismatch
func getCount() -> Int {
    return "42"  // Error - returning String
}

// RIGHT: Return correct type
func getCount() -> Int {
    return 42
}

// WRONG: Optional returned where non-optional expected
func findItem() -> String {
    let dict: [String: String] = [:]
    return dict["key"]  // Error - returns Optional<String>
}

// RIGHT: Use nil coalescing
func findItem() -> String {
    let dict: [String: String] = [:]
    return dict["key"] ?? "default"
}
```

## Examples
```swift
// Example: Matching return types
// Function declares String, returns Int:
func getLength(of text: String) -> Int {
    return text.count  // OK - returns Int
}

// Function declares optional:
func getItem(from list: [String]) -> String? {
    return list.first  // OK - returns Optional<String>
}

// Void function should not return:
func logMessage(_ message: String) {
    print(message)
    // return  // Error - void function
}
```

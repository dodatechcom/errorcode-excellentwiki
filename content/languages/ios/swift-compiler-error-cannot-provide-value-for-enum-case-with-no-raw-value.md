---
title: "[Solution] Swift Compiler Error: Cannot Provide Value for Enum Case with No Raw Value"
description: "Fix enum raw value assignment errors in Swift."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Cannot Provide Value for Enum Case with No Raw Value

Enums without raw values cannot be initialized with a raw value. You must use the case name directly or provide raw values in the enum definition.

## Common Causes
- Enum does not declare a raw value type
- Trying to initialize enum from raw value without raw type
- Using init(rawValue:) on non-raw-value enum
- String/Int raw value not matching case names

## How to Fix
1. Add a raw value type to the enum definition
2. Use the enum case name directly for assignment
3. Use init(rawValue:) with raw value types
4. Use associated values instead of raw values if needed

```swift
// WRONG: No raw value type
enum Status {
    case active, inactive
}

// let status = Status(rawValue: "active")  // Error - no raw value

// RIGHT: Add raw value type
enum Status: String {
    case active, inactive
}

let status = Status(rawValue: "active")  // OK
```

## Examples
```swift
// Example: Enum with raw values
enum HTTPMethod: String {
    case get = "GET"
    case post = "POST"
    case put = "PUT"
    case delete = "DELETE"
}

// Initialize from raw value:
let method = HTTPMethod(rawValue: "POST")  // .post

// Access raw value:
print(method?.rawValue)  // "POST"

// Initialize directly:
let getMethod = HTTPMethod.get
print(getMethod.rawValue)  // "GET"
```

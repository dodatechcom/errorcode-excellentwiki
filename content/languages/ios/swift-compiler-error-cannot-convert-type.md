---
title: "[Solution] Swift Compiler Error: Cannot Convert Type"
description: "Fix Swift type conversion errors in Xcode projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Cannot Convert Type

Type conversion errors occur when Swift cannot automatically convert between incompatible types. Explicit conversion or casting is required.

## Common Causes
- Passing Int where String is expected
- Optional type used where non-optional is required
- Array type mismatch without explicit conversion
- Protocol type cannot be implicitly converted to concrete type

## How to Fix
1. Use explicit type conversion functions (String(), Int(), etc.)
2. Force unwrap optionals only when safe
3. Map arrays to convert element types
4. Use as? or as! for protocol to concrete type conversion

```swift
// WRONG: Cannot convert type
let number: Int = 42
let text: String = number  // Error

// RIGHT: Explicit conversion
let text: String = String(number)

// WRONG: Optional to non-optional
let name: String? = "Hello"
let count: Int = name.count  // Error

// RIGHT: Unwrap first
let count: Int = name?.count ?? 0
```

## Examples
```swift
// Example: Converting between common types
let intVal = 42
let doubleVal = Double(intVal)  // 42.0
let stringVal = String(intVal)  // "42"
let boolVal = Bool(intVal)      // Error - no implicit conversion

// For arrays:
let ints = [1, 2, 3]
let strings = ints.map { String($0) }  // ["1", "2", "3"]
```

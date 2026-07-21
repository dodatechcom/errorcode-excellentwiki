---
title: "[Solution] Swift Compiler Error: Type of Expression Is Ambiguous"
description: "Fix ambiguous expression type errors in Swift code."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Type of Expression Is Ambiguous

The compiler cannot determine the type of an expression because multiple types are possible. This commonly occurs with numeric literals and collections.

## Common Causes
- Numeric literal could be multiple types (Int, Double, Float)
- Empty array or dictionary has no type information
- Closure return type too complex for inference
- Nil literal without context type

## How to Fix
1. Add explicit type annotations
2. Use type suffixes on literals (42.0, 42 as Double)
3. Provide type information to empty collections
4. Simplify complex expressions

```swift
// WRONG: Ambiguous type
let value = 42  // Could be Int, Double, UInt, etc.
// Use as:
let intVal = 42 as Int
let doubleVal = 42.0  // Literal with . makes it Double

// WRONG: Empty collection type
let items = []  // Error - type unknown

// RIGHT: Explicit type
let items: [String] = []
let dict: [String: Int] = [:]
```

## Examples
```swift
// Example: Resolving ambiguous types
// Numeric literals:
let a = 42        // Int
let b = 42.0      // Double
let c: Float = 42 // Float

// Empty collections:
let names: [String] = []
let scores: [String: Int] = [:]

// Nil:
let nothing: String? = nil  // Must specify Optional<String>
```

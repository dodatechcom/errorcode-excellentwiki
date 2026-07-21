---
title: "[Solution] Swift Compiler Error: Ambiguous Overload Resolution"
description: "Fix ambiguous overload resolution errors in Swift code."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Ambiguous Overload Resolution

When multiple overloaded functions match a call site, Swift cannot determine which one to use. This causes an ambiguous overload error.

## Common Causes
- Multiple overloads accept similar parameter types
- Default parameter values creating ambiguity
- Generic overloads matching multiple specializations
- Protocol extensions providing competing implementations

## How to Fix
1. Rename overloaded functions to reduce ambiguity
2. Provide explicit type annotations at the call site
3. Remove unnecessary overloads
4. Use specific type casting to resolve the ambiguity

```swift
// WRONG: Ambiguous overloads
func process(_ value: Int) { }
func process(_ value: Double) { }
process(42)  // Ambiguous - could be Int or Double

// RIGHT: Explicit type
let intVal: Int = 42
process(intVal)

// Or:
process(42 as Int)
```

## Examples
```swift
// Example: Resolving overload ambiguity
func configure(_ size: Int) { }
func configure(_ size: CGSize) { }

// Ambiguous:
// configure(CGSize(width: 100, height: 100))  // OK - clear
// configure(100)  // Ambiguous if Int and CGSize both match

// Fix by being explicit:
let width: Int = 100
configure(width)  // Now resolves to Int version

// Or use type annotation:
configure(100 as Int)
```

---
title: "[Solution] Swift Compiler Error: Cannot Assign to Property of Immutable Type"
description: "Fix immutable property assignment errors in Swift."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Cannot Assign to Property of Immutable Type

You cannot assign a new value to a property declared as let or to a property of an immutable struct/enum. The value must be declared as var.

## Common Causes
- Struct property accessed on let constant
- Enum case value modification attempt
- Function return value assigned to
- Property declared with let instead of var

## How to Fix
1. Use var for properties that need to change
2. Create a new instance instead of modifying immutable one
3. Use mutating functions on var instances
4. Consider if immutability is the intended behavior

```swift
// WRONG: Cannot assign to let
struct Point {
    let x: Int
    let y: Int
}

var point = Point(x: 0, y: 0)
point.x = 5  // Error - x is let

// RIGHT: Use var for mutable properties
struct Point {
    var x: Int
    var y: Int
}

var point = Point(x: 0, y: 0)
point.x = 5  // OK

// WRONG: Modifying let struct
let fixed = Point(x: 0, y: 0)
fixed.x = 5  // Error - fixed is let

// RIGHT: Create new instance
var mutable = fixed
mutable.x = 5  // OK - mutable is var
```

## Examples
```swift
// Example: Struct value semantics with let vs var
struct Settings {
    var theme: String
    var fontSize: Int
}

let fixedSettings = Settings(theme: "dark", fontSize: 14)
// fixedSettings.theme = "light"  // Error

var mutableSettings = Settings(theme: "dark", fontSize: 14)
mutableSettings.theme = "light"  // OK
```

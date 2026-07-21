---
title: "[Solution] Swift Compiler Error: Variable Used Before Being Initialized"
description: "Fix uninitialized variable errors in Swift code."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Variable Used Before Being Initialized

Swift requires variables to be initialized before use. Using a variable before it has been assigned a value triggers this compiler error.

## Common Causes
- Variable declared but not assigned a value
- Variable assigned in conditional branch but used outside
- Stored property not initialized in initializer
- Variable declared in one scope, used in another

## How to Fix
1. Initialize variables at declaration
2. Use default values for optional properties
3. Ensure all code paths initialize the variable
4. Use lazy initialization where appropriate

```swift
// WRONG: Variable not initialized
var name: String
print(name)  // Error

// RIGHT: Initialize at declaration
var name: String = ""
print(name)

// For stored properties:
class MyClass {
    var count: Int  // Error - no initial value

    init(count: Int) {
        self.count = count  // Initialize in init
    }
}

// Or use default value:
class MyClass {
    var count: Int = 0  // Default value
}
```

## Examples
```swift
// Example: Proper variable initialization
func processValues(_ values: [Int]) {
    var sum: Int = 0  // Initialize
    for value in values {
        sum += value
    }
    print("Sum: \(sum)")
}

// For optional properties:
class User {
    var name: String  // Non-optional
    var email: String?  // Optional - auto-initialized to nil

    init(name: String) {
        self.name = name
    }
}
```

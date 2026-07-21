---
title: "[Solution] Swift Compiler Error: Class Does Not Implement Required Initializer"
description: "Fix missing required initializer errors in Swift subclasses."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Class Does Not Implement Required Initializer

Subclasses must implement all required initializers from their superclass. Missing initializers cause this compiler error.

## Common Causes
- Subclass does not implement superclass required init
- Convenience initializer not marked with required
- Subclass designated initializer does not call super.init
- Init override missing required keyword

## How to Fix
1. Add the required initializer to the subclass
2. Call super.init from the required initializer
3. Mark convenience initializers as required in superclass
4. Use required convenience init for protocol conformance

```swift
// WRONG: Missing required initializer
class BaseClass {
    required init(value: Int) { }
}

class SubClass: BaseClass {
    // Error - must implement init(value: Int)
}

// RIGHT: Implement required init
class SubClass: BaseClass {
    required init(value: Int) {
        super.init(value: value)
    }
}
```

## Examples
```swift
// Example: Required initializers in hierarchy
class Animal {
    required init(name: String) {
        self.name = name
    }
    var name: String
}

class Dog: Animal {
    var breed: String

    init(name: String, breed: String) {
        self.breed = breed
        super.init(name: name)
    }

    required init(name: String) {
        self.breed = "Unknown"
        super.init(name: name)
    }
}

let dog = Dog(name: "Rex", breed: "Labrador")
let dog2 = Dog(name: "Buddy")  // Uses required init
```

---
title: "[Solution] Swift Compiler Error: Stored Property Not Initialized"
description: "Fix uninitialized stored property errors in Swift class initializers."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Stored Property Not Initialized

All non-optional stored properties must be initialized before super.init is called in a class initializer. Missing initialization causes this error.

## Common Causes
- Stored property not assigned before super.init
- Designated initializer does not initialize all properties
- Convenience initializer missing required parameters
- Optional property used where non-optional expected

## How to Fix
1. Initialize all stored properties before super.init
2. Use default values for properties
3. Ensure convenience initializers eventually call designated init
4. Make properties optional if they do not always have values

```swift
// WRONG: Missing initialization
class Animal {
    var name: String
    var age: Int

    init(name: String) {
        // age not initialized
        super.init()  // Error
    }
}

// RIGHT: Initialize all properties
class Animal {
    var name: String
    var age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
        super.init()
    }
}
```

## Examples
```swift
// Example: Proper initialization pattern
class Vehicle {
    var make: String
    var model: String
    var year: Int

    init(make: String, model: String, year: Int = 2024) {
        self.make = make
        self.model = model
        self.year = year
        super.init()
    }
}

class Car: Vehicle {
    var doors: Int

    init(make: String, model: String, doors: Int) {
        self.doors = doors
        super.init(make: make, model: model)
    }
}
```

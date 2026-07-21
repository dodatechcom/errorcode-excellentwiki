---
title: "[Solution] Swift Compiler Error: Inaccessible Due to Private Protection Level"
description: "Fix private access level errors in Swift code."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Inaccessible Due to Private Protection Level

Private members are only accessible within the same file or enclosing type. Trying to access them from outside their scope causes this error.

## Common Causes
- Accessing private property from another file
- Private method called from extension in different file
- Private type used in public API
- Nested type private member accessed from outside

## How to Fix
1. Use fileprivate instead of private for cross-file access
2. Use internal or public for shared access
3. Move extensions to the same file as the declaration
4. Restructure code to reduce access level needs

```swift
// WRONG: Accessing private member from another file
// File1.swift
class MyClass {
    private var secret = "hidden"
}

// File2.swift
let obj = MyClass()
// print(obj.secret)  // Error - private

// RIGHT: Use fileprivate or make internal
class MyClass {
    internal var secret = "hidden"  // Accessible in module
}
```

## Examples
```swift
// Example: Access levels in Swift
public class MyClass {
    public var publicProp = 1       // Everywhere
    internal var internalProp = 2   // Within module
    fileprivate var fileProp = 3    // Within file
    private var privateProp = 4     // Within type

    func test() {
        // All accessible here
        print(publicProp, internalProp, fileProp, privateProp)
    }
}

extension MyClass {
    func test2() {
        // Cannot access privateProp if extension is in different file
        print(publicProp, internalProp, fileProp)
    }
}
```

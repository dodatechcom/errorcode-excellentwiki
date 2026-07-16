---
title: "[Solution] Swift Type Cast Failed — Force Cast Crash Fix"
description: "Fix Swift force cast failures. Learn why as! operator crashes and how to use conditional casting with as? instead."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["type-cast", "force-cast", "as", "downcast", "swift"]
weight: 5
---

# Type Cast Failed — Force Cast Crash

A type cast failure occurs when you force-cast (`as!`) an object to a type it doesn't belong to.

## Description

Swift uses `as!` to force a type cast. If the object isn't of the target type, the cast fails with a fatal error. This commonly happens with protocol existentials, JSON parsing, and Core Data objects.

Common causes:

- **Wrong type assumption** — casting to incorrect type
- **Protocol existential** — casting protocol to concrete type
- **JSON parsing** — type mismatch in decoded data
- **Core Data objects** — casting managed objects incorrectly

## Common Causes

```swift
// Cause 1: Wrong type assumption
let value: Any = "Hello"
let number = value as! Int  // Fatal error: Could not cast

// Cause 2: Protocol existential
protocol Drawable { func draw() }
class Circle: Drawable { func draw() {} }
let drawable: Drawable = Circle()
let rectangle = drawable as! Rectangle  // Fatal error

// Cause 3: JSON type mismatch
let json: [String: Any] = ["count": "five"]
let count = json["count"] as! Int  // Fatal error

// Cause 4: Core Data cast
let object = entityManager.find(id)
let user = object as! UserEntity  // Fatal error if wrong type
```

## How to Fix

### Fix 1: Use conditional cast

```swift
// Wrong
let value: Any = "Hello"
let number = value as! Int  // Crash

// Correct
if let number = value as? Int {
    print(number)
} else {
    print("Not an Int")
}
```

### Fix 2: Use guard cast

```swift
// Wrong
let value: Any = "Hello"
let number = value as! Int  // Crash

// Correct
guard let number = value as? Int else {
    print("Not an Int")
    return
}
```

### Fix 3: Use switch for multiple types

```swift
// Wrong
let value: Any = "Hello"
let str = value as! String  // Works, but fragile

// Correct
switch value {
case let str as String:
    print("String: \(str)")
case let num as Int:
    print("Int: \(num)")
default:
    print("Unknown type")
}
```

### Fix 4: Validate before casting

```swift
// Wrong
let dict: [String: Any] = ["count": "five"]
let count = dict["count"] as! Int  // Crash

// Correct
if let count = dict["count"] as? Int {
    print(count)
}
```

## Examples

```swift
// Example 1: Safe protocol casting
protocol Animal { var name: String { get } }
class Dog: Animal { let name: String; init(name: String) { self.name = name } }

let animal: Animal = Dog(name: "Rex")
if let dog = animal as? Dog {
    print(dog.name)  // "Rex"
}

// Example 2: JSON parsing
let json: [String: Any] = ["name": "Alice", "age": 30]
let name = json["name"] as? String ?? "Unknown"
let age = json["age"] as? Int ?? 0
```

## Related Errors

- [Nil Unwrap]({{< relref "/languages/swift/nil-unwrap" >}}) — force unwrapping nil
- [Force Unwrap]({{< relref "/languages/swift/force-unwrap" >}}) — bang operator crash
- [Decoding Error]({{< relref "/languages/swift/decodable-error" >}}) — JSONDecoder failure

---
title: "[Solution] Swift Type Cast Error Fix"
description: "Fix Swift type cast errors. Learn why type casting fails and how to use safe casting operators properly."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A type cast error occurs when you try to cast a value to a type it doesn't match. Swift provides safe (`as?`) and forced (`as!`) casting operators, and using the wrong one can cause runtime crashes.

## Common Causes

- Using forced cast `as!` on wrong type
- Casting between unrelated types
- Downcasting inheritance hierarchy incorrectly
- Platform type casting issues

## How to Fix

```swift
// WRONG: Forced cast on wrong type
let value: Any = "hello"
let number = value as! Int  // Fatal error: cannot cast

// CORRECT: Use optional casting
if let number = value as? Int {
    print(number)
} else {
    print("Not an Int")
}
```

```swift
// WRONG: Unsafe downcast
class Animal {}
class Dog: Animal {}
class Cat: Animal {}

let animals: [Animal] = [Dog(), Cat()]
let dog = animals[0] as! Cat  // Fatal error

// CORRECT: Safe downcast
if let dog = animals[0] as? Dog {
    print("It's a dog")
}
```

```swift
// WRONG: Casting protocol types
protocol Drawable {}
struct Circle: Drawable {}

let shape: Drawable = Circle()
let circle = shape as! Rectangle  // Fatal error

// CORRECT: Check type first
if shape is Circle {
    let circle = shape as? Circle
}
```

## Examples

```swift
// Example 1: Basic type casting
let value: Any = 42
if let intVal = value as? Int {
    print(intVal)  // 42
}

// Example 2: Array type casting
let mixed: [Any] = [1, "hello", 3.14]
let ints = mixed.compactMap { $0 as? Int }

// Example 3: Enum casting
enum Result {
    case success(String)
    case failure(Error)
}
let result: Result = .success("ok")
if case .success(let msg) = result {
    print(msg)
}
```

## Related Errors

- [Nil unwrap error](nil-unwrap-error) — force unwrapping nil
- [Index out of range](index-out-of-range-swift) — array index beyond bounds
- [Key not found](key-not-found-swift) — dictionary key missing

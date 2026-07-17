---
title: "[Solution] Swift some Protocol Error Fix"
description: "Fix Swift some Protocol errors. Learn why some Protocol fails and how to use opaque return types properly."
languages: ["swift"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

## What This Error Means

A `some Protocol` error occurs when using opaque return types incorrectly. The `some` keyword tells the compiler to hide the concrete type while ensuring it's the same type every time the function is called.

## Common Causes

- Returning different types from function
- Missing protocol conformance
- Using `some` where existential type is needed
- Generic constraint violations

## How to Fix

```swift
// WRONG: Different return types
func makeShape() -> some Shape {
    if condition {
        return Circle()  // Circle
    } else {
        return Square()  // Square - different type!
    }
}

// CORRECT: Same return type
func makeShape() -> some Shape {
    if condition {
        return Circle()
    } else {
        return Circle()  // Same type
    }
}
```

```swift
// WRONG: Protocol not conformed
func makeAnimal() -> some Animal {
    return Rock()  // Rock doesn't conform to Animal
}

// CORRECT: Ensure conformance
protocol Animal {}
struct Dog: Animal {}

func makeAnimal() -> some Animal {
    return Dog()
}
```

```swift
// WRONG: Using some when you need existential
func makeValue() -> some Any {
    // May need different types
}

// CORRECT: Use Any or AnyProtocol
func makeValue() -> Any {
    return "Hello"
}
```

## Examples

```swift
// Example 1: Basic some Protocol
protocol Drawable {
    func draw() -> String
}

struct Line: Drawable {
    func draw() -> String { "Line" }
}

func makeDrawable() -> some Drawable {
    return Line()
}

// Example 2: some with generics
func first<T: Comparable>(_ a: T, _ b: T) -> some Comparable {
    return a < b ? a : b
}

// Example 3: some in SwiftUI
var body: some View {
    VStack {
        Text("Hello")
        Image(systemName: "star")
    }
}
```

## Related Errors

- [Opaque return type error](opaque-return-type) — opaque type issue
- [Result type error](result-type-error) — Result type issue
- [Throws error](throws-error) — error throwing issue

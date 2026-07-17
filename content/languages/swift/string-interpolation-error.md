---
title: "[Solution] Swift String Interpolation Error Fix"
description: "Fix Swift string interpolation errors. Learn why string interpolation fails and how to format strings properly."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

String interpolation errors occur when inserting values into strings fails. This can happen with types that do not have a String representation, escaping issues, or format specifier mismatches.

## Common Causes

- Interpolating non-StringConvertible types
- Escaping special characters
- Wrong format specifiers
- Optional values without unwrapping

## How to Fix

```swift
// WRONG: Interpolating optional directly
let name: String? = nil
let greeting = "Hello, \(name!)"  // Crash: force unwrap nil

// CORRECT: Unwrap safely
let greeting = "Hello, \(name ?? "stranger")"
```

```swift
// WRONG: Wrong format specifier
let pi = 3.14159
let str = String(format: "Pi is %d", pi)  // Wrong specifier

// CORRECT: Use correct specifier
let str = String(format: "Pi is %.2f", pi)  // "Pi is 3.14"
```

```swift
// WRONG: Special characters not escaped
let path = "C:\newfolder"  // \n is newline

// CORRECT: Use raw strings
let path = #"C:\newfolder"#
// Or escape the backslash
let path = "C:\\newfolder"
```

## Examples

```swift
// Example 1: Basic interpolation
let name = "Alice"
let age = 30
let msg = "I am \(name) and I am \(age) years old"

// Example 2: Expression interpolation
let a = 5, b = 3
let msg = "\(a) + \(b) = \(a + b)"

// Example 3: Custom StringConvertible
struct Person: CustomStringConvertible {
    let name: String
    var description: String { name }
}
let person = Person(name: "Bob")
let msg = "Hello, \(person)"
```

## Related Errors

- [Unicode error](unicode-error-swift) — Unicode issues
- [Floating point error](floating-point-error-swift) — precision issues
- [Nil unwrap error](nil-unwrap-error) — force unwrapping nil

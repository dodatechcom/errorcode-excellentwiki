---
title: "[Solution] Xcode Error: Swift Compiler Error Ambiguous Use"
description: "Resolve Swift ambiguous use errors in Xcode projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Swift Compiler Error Ambiguous Use

Ambiguous use errors occur when Swift cannot determine which overloaded function or method to call. The compiler finds multiple candidates that match the call site.

## Common Causes
- Multiple overloads with similar parameter types
- Protocol extensions providing default implementations
- Extensions on different protocols with same method names
- Type inference unable to disambiguate between options

## How to Fix
1. Add explicit type annotations to clarify the intended type
2. Use a more specific overload or cast parameters
3. Rename methods to reduce ambiguity
4. Use explicit type casting at the call site

```swift
// WRONG: Ambiguous use of 'init'
let view = UIView(frame: .zero)  // This works

// Ambiguous case:
protocol A { func doSomething() }
protocol B { func doSomething() }
extension A where Self: B {
    func doSomething() { print("A+B") }
}

// Fix: Use explicit protocol conformance
class MyClass: A, B {
    func doSomething() { print("explicit") }
}
```

## Examples
```swift
// Example: Resolving ambiguous function calls
// Before (ambiguous):
func process(_ value: Int) { }
func process(_ value: String) { }
process(42)  // Ambiguous because 42 could be Int or String

// After (explicit):
let number: Int = 42
process(number)  // Now unambiguous

// Or use explicit type annotation:
process(42 as Int)
```

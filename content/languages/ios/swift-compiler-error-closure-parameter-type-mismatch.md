---
title: "[Solution] Swift Compiler Error: Closure Parameter Type Mismatch"
description: "Fix closure parameter type mismatch errors in Swift."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Closure Parameter Type Mismatch

Closure parameters must match the expected signature. Mismatched types between the closure definition and expected parameters cause this error.

## Common Causes
- Closure parameter types do not match function signature
- Wrong number of parameters in closure
- Return type mismatch in closure
- Trailing closure syntax with wrong parameter binding

## How to Fix
1. Verify closure parameter types match the expected signature
2. Use explicit types in the closure if needed
3. Check the function's closure parameter signature
4. Use underscore to ignore unused parameters

```swift
// WRONG: Parameter type mismatch
let numbers = [1, 2, 3]
let strings = numbers.map { "\($0)" }  // OK
// But this fails:
// let doubled = numbers.map { $0 * 2.0 }  // Int vs Double

// RIGHT: Explicit type
let doubled = numbers.map { Double($0) * 2.0 }

// WRONG: Wrong parameter count
let pairs = [(1, "a"), (2, "b")]
let result = pairs.map { (a, b) -> String in
    return "\(a)-\(b)"
}
// If map expects single parameter:
// let wrong = pairs.map { a, b -> String in ... }  // Error
```

## Examples
```swift
// Example: Closure type matching
func perform(_ action: (Int, Int) -> Int) -> Int {
    return action(1, 2)
}

// Correct closure:
let result = perform { a, b in a + b }  // OK

// Wrong closure:
// let wrong = perform { a in a }  // Error - wrong parameter count
// let wrong = perform { a, b, c in a + b }  // Error - too many params
```

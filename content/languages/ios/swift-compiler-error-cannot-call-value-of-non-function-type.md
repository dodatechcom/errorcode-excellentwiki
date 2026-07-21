---
title: "[Solution] Swift Compiler Error: Cannot Call Value of Non-Function Type"
description: "Fix calling non-function type errors in Swift code."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Cannot Call Value of Non-Function Type

This error occurs when you try to call a value as if it were a function. The value is not callable.

## Common Causes
- Variable name conflicts with function name
- Forgetting to instantiate a type before calling a method
- Subscript syntax used where method is needed
- Closure stored in variable not invoked properly

## How to Fix
1. Verify the value is actually a function or closure
2. Check for naming conflicts between variables and functions
3. Use correct syntax for calling methods on types
4. Ensure closures are invoked with parentheses

```swift
// WRONG: Calling non-function
let x = 42
x()  // Error - Int is not callable

// WRONG: Missing parentheses on closure call
let greet = { print("Hello") }
greet  // Error - not calling the closure

// RIGHT:
greet()  // Call with parentheses

// WRONG: Forgetting to instantiate
struct MyClass {
    func doSomething() { }
}
// MyClass.doSomething()  // Error - need instance

// RIGHT:
let obj = MyClass()
obj.doSomething()
```

## Examples
```swift
// Example: Closure invocation
let add = { (a: Int, b: Int) -> Int in a + b }

// WRONG:
// add  // Not calling

// RIGHT:
let sum = add(3, 4)  // Returns 7

// With stored closure property:
class Handler {
    var action: (() -> Void)?
}

let handler = Handler()
handler.action?()  // Call with optional chaining
```

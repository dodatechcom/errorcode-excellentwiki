---
title: "[Solution] Swift Compiler Error: Cannot Apply Binary Operator to Operands of Type"
description: "Fix binary operator type errors in Swift code."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Cannot Apply Binary Operator to Operands of Type

Binary operators require specific operand types. Applying an operator to incompatible types causes this compiler error.

## Common Causes
- Adding Int and String
- Comparing different types without conversion
- Using operators on custom types without defining them
- Applying arithmetic operators to non-numeric types

## How to Fix
1. Convert operands to compatible types before the operation
2. Define custom operators for your types
3. Use type conversion functions (String(), Int(), etc.)
4. Implement Equatable or Comparable for custom types

```swift
// WRONG: Incompatible types
let num = 42
let str = "hello"
// let result = num + str  // Error

// RIGHT: Convert types
let result = String(num) + str

// WRONG: Comparing different types
let a: Int = 42
let b: Double = 42.0
// if a == b { }  // Error - different types

// RIGHT: Convert one type
if Double(a) == b { }  // OK
```

## Examples
```swift
// Example: Custom operator for your types
struct Money {
    var amount: Double
    var currency: String
}

func + (lhs: Money, rhs: Money) -> Money {
    // Only add if currencies match
    precondition(lhs.currency == rhs.currency)
    return Money(amount: lhs.amount + rhs.amount, currency: lhs.currency)
}

let price1 = Money(amount: 10.0, currency: "USD")
let price2 = Money(amount: 20.0, currency: "USD")
let total = price1 + price2  // Money(amount: 30.0, currency: "USD")
```

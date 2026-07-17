---
title: "[Solution] Swift Floating Point Error Fix"
description: "Fix Swift floating point precision errors. Learn why floating point arithmetic is imprecise and how to handle decimal calculations."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

Floating point errors occur when decimal arithmetic produces imprecise results due to how floating point numbers are represented in binary. For example, 0.1 + 0.2 does not equal exactly 0.3.

## Common Causes

- Comparing floating point values for equality
- Currency calculations using Double
- Accumulated rounding errors
- NaN or Infinity values

## How to Fix

```swift
// WRONG: Comparing floating point values
let a = 0.1 + 0.2
let b = 0.3
if a == b {  // false!
    print("Equal")
}

// CORRECT: Use epsilon comparison
func approximatelyEqual(_ a: Double, _ b: Double, epsilon: Double = 0.0001) -> Bool {
    return abs(a - b) < epsilon
}
if approximatelyEqual(a, b) {
    print("Equal")
}
```

```swift
// WRONG: Using Double for currency
var total: Double = 0.0
for _ in 0..<10 {
    total += 0.1
}
print(total)  // 0.9999999999999999

// CORRECT: Use Decimal for currency
var total = Decimal(0)
for _ in 0..<10 {
    total += Decimal(0.1)
}
print(total)  // 1.0
```

## Examples

```swift
// Example 1: Decimal arithmetic
let a = Decimal(0.1)
let b = Decimal(0.2)
let sum = a + b
print(sum == Decimal(0.3))  // true

// Example 2: Formatting floating point
let value = 3.14159
let formatted = String(format: "%.2f", value)  // "3.14"

// Example 3: NaN check
let nan = Double.nan
print(nan.isNaN)  // true
print(nan.isFinite)  // false
```

## Related Errors

- [Integer overflow](integer-overflow-swift) — integer overflow
- [Unicode error](unicode-error-swift) — encoding issues
- [String interpolation error](string-interpolation-error) — string formatting

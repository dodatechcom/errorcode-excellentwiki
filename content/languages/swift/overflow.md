---
title: "[Solution] Swift Error — Arithmetic Overflow"
description: "Fix Swift arithmetic overflow errors. Learn why integer overflow crashes and how to use overflow-safe operators."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["overflow", "arithmetic", "integer", "bitwise", "max", "min"]
weight: 5
---

# Arithmetic Overflow

This error occurs when an arithmetic operation produces a value that exceeds the storage capacity of the integer type. Swift traps on overflow by default to prevent silent data corruption.

## Description

Swift integers (`Int8`, `Int16`, `Int32`, `Int64`, `Int`) have fixed ranges. For example, `Int8` can hold -128 to 127. When an operation would produce a value outside this range, the runtime traps. This is a deliberate safety feature, unlike C which silently wraps around.

Common patterns:

- **Unbounded accumulation** — adding values without checking for max.
- **Downcasting** — converting `Int` to `Int8` without range checking.
- **User input** — parsing large numbers into small integer types.
- **Time calculations** — multiplying large intervals.

## Common Causes

```swift
// Cause 1: Exceeding Int8 range
let a: Int8 = 120
let b: Int8 = 10
let sum = a + b // Fatal error: 130 > 127

// Cause 2: Multiplication overflow
let big = Int32.max
let result = big * 2 // Fatal error

// Cause 3: Downcast overflow
let largeNumber: Int = 1000
let small = Int8(largeNumber) // Fatal error: 1000 > 127

// Cause 4: Negation overflow
let min = Int8.min // -128
let negated = -min // Fatal error: 128 > 127
```

## How to Fix

### Fix 1: Check bounds before operations

```swift
let a: Int8 = 120
let b: Int8 = 10

// Wrong
let sum = a + b

// Correct
if a <= Int8.max - b {
    let sum = a + b
} else {
    print("Would overflow")
}
```

### Fix 2: Use overflow operators for intentional wrapping

```swift
let a: Int8 = 120
let b: Int8 = 10

// Uses &+ to allow wrapping (no crash)
let sum = a &+ b // -126 (wraps around)
```

### Fix 3: Use safe downcasting

```swift
let largeNumber: Int = 1000

// Wrong
let small = Int8(largeNumber)

// Correct
if let small = Int8(exactly: largeNumber) {
    print(small)
} else {
    print("Number too large for Int8")
}
```

### Fix 4: Use wider types for intermediate calculations

```swift
let a: Int32 = Int32.max
let b: Int32 = 2

// Wrong
let product = a * b

// Correct — use wider type for intermediate
let product = Int64(a) * Int64(b)
if product <= Int64(Int32.max) {
    let result = Int32(product)
}
```

## Examples

```swift
// Example 1: Counter overflow
var count: UInt8 = 255
count += 1 // Fatal error: 256 > 255

// Example 2: Bit shift overflow
let bits: UInt8 = 1
let shifted = bits << 8 // Fatal error: shift >= bit width

// Example 3: Floating-point conversion
let huge: Double = Double(Int64.max) + 1
let asInt = Int(huge) // Fatal error: not representable
```

## Related Errors

- [Division by Zero]({{< relref "/languages/swift/division-by-zero" >}}) — zero denominator crash.
- [Index Out of Range]({{< relref "/languages/swift/index-out-of-range" >}}) — can result from overflow in index calculations.
- [EXC_BAD_ACCESS]({{< relref "/languages/swift/memory-access" >}}) — memory access issues.

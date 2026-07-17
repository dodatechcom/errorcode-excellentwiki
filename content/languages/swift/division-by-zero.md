---
title: "[Solution] Swift Error — Division by Zero"
description: "Fix Swift division by zero errors. Learn why dividing by zero crashes at runtime and how to guard against zero denominators."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Division by Zero

This error occurs when you divide an integer by zero. Unlike floating-point division (which produces `inf` or `nan`), integer division by zero crashes at runtime.

## Description

Swift handles integer and floating-point division differently. Integer division by zero (`a / 0`) is a fatal error. Floating-point division by zero produces `inf` or `nan` without crashing, but can cause downstream issues. This error is common with user-provided denominators, calculated divisors, or unvalidated input.

Common patterns:

- **User input** — dividing by a value from a text field without validation.
- **Calculated divisor** — subtraction producing zero before division.
- **Array count** — using `count` as a divisor without checking for empty.
- **Percentage calculations** — dividing by total that may be zero.

## Common Causes

```swift
// Cause 1: Integer division by zero
let a = 10
let b = 0
let result = a / b // Fatal error

// Cause 2: Calculated divisor becoming zero
let items = [1, 2, 3]
let removed = 3
let remaining = items.count - removed // 0
let avg = items.count / remaining // Fatal error

// Cause 3: User input without validation
let input = Int(userTextField.text ?? "0")! // 0
let share = 100 / input // Fatal error if 0

// Cause 4: Modulo by zero
let remainder = 10 % 0 // Fatal error
```

## How to Fix

### Fix 1: Guard against zero before division

```swift
let numerator = 10
let denominator = 0

// Wrong
let result = numerator / denominator

// Correct
guard denominator != 0 else {
    print("Cannot divide by zero")
    return
}
let result = numerator / denominator
```

### Fix 2: Use guard in functions

```swift
func divide(_ a: Int, by b: Int) -> Int? {
    // Wrong: return a / b
    // Correct
    guard b != 0 else { return nil }
    return a / b
}
```

### Fix 3: Use floating-point division with checks

```swift
let a = 10.0
let b = 0.0

// This won't crash but produces inf
let result = a / b

// Better — check first
let result = b != 0 ? a / b : 0
```

### Fix 4: Safe percentage calculation

```swift
func percentage(_ part: Int, of total: Int) -> Double {
    // Wrong: return Double(part) / Double(total) * 100
    // Correct
    guard total != 0 else { return 0 }
    return Double(part) / Double(total) * 100
}
```

## Examples

```swift
// Example 1: Average of empty array
let numbers: [Int] = []
let average = numbers.reduce(0, +) / numbers.count // Fatal error

// Example 2: Countdown division
let total = 5
let done = 5
let remaining = total - done
let perTask = total / remaining // Fatal error: 5 / 0

// Example 3: Modulo by zero
let value = 42
let mod = value % 0 // Fatal error
```

## Related Errors

- [Arithmetic Overflow]({{< relref "/languages/swift/overflow" >}}) — arithmetic overflow error.
- [Index Out of Range]({{< relref "/languages/swift/index-out-of-range" >}}) — can result from zero-based calculations.
- [EXC_BAD_ACCESS]({{< relref "/languages/swift/memory-access" >}}) — memory access crash.

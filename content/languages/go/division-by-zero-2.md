---
title: "[Solution] Go Integer Divide by Zero — Runtime Error Fix"
description: "Fix Go integer divide by zero panic. Check divisor values before division and handle edge cases in arithmetic operations."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Integer Divide by Zero — Runtime Error Fix

A divide by zero panic occurs when an integer division or modulo operation uses zero as the divisor.

## Description

Go panics when dividing an integer by zero or computing a modulo with zero. This applies to all integer types: `int`, `int8`, `int16`, `int32`, `int64`, `uint`, etc. Floating-point division by zero produces `+Inf` or `NaN` instead of panicking.

Common scenarios:

- **User input not validated** — dividing by a value from user input or network.
- **Empty collection statistics** — computing average with zero count.
- **Algorithm edge case** — divisor computed dynamically and happens to be zero.
- **Modulo in hash or bucketing** — modulo with dynamic bucket count.

## Common Causes

```go
// Cause 1: Unvalidated user input
func divide(a, b int) int {
    return a / b
}

func main() {
    fmt.Println(divide(10, 0)) // panic: integer divide by zero
}

// Cause 2: Average of empty slice
func average(nums []int) int {
    sum := 0
    for _, n := range nums {
        sum += n
    }
    return sum / len(nums) // panic if nums is empty
}

// Cause 3: Dynamic divisor
func mod(a, b int) int {
    return a % b
}

func main() {
    x := 10
    y := x - x // y is 0
    fmt.Println(mod(100, y)) // panic
}

// Cause 4: Bit shift by computed value
func main() {
    bits := 0
    _ = 1 << bits // This is fine, but division is the issue
    n := 10 / bits // panic
}
```

## How to Fix

### Fix 1: Check divisor before dividing

```go
// Wrong
func divide(a, b int) int {
    return a / b
}

// Correct
func divide(a, b int) (int, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Fix 2: Check collection length before computing statistics

```go
// Wrong
func average(nums []int) float64 {
    sum := 0
    for _, n := range nums {
        sum += n
    }
    return float64(sum) / float64(len(nums))
}

// Correct
func average(nums []int) (float64, error) {
    if len(nums) == 0 {
        return 0, fmt.Errorf("empty slice")
    }
    sum := 0
    for _, n := range nums {
        sum += n
    }
    return float64(sum) / float64(len(nums)), nil
}
```

### Fix 3: Guard modulo operations

```go
func bucket(key, numBuckets int) int {
    if numBuckets <= 0 {
        return 0
    }
    if key < 0 {
        key = -key
    }
    return key % numBuckets
}
```

### Fix 4: Use safe division helper

```go
func safeDiv(a, b int) int {
    if b == 0 {
        return 0
    }
    return a / b
}

func safeMod(a, b int) int {
    if b == 0 {
        return 0
    }
    return a % b
}
```

## Examples

```go
// This triggers: runtime error: integer divide by zero
package main

import "fmt"

func main() {
    x := 10
    y := 0
    fmt.Println(x / y)
}
```

## Related Errors

- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — another common runtime panic.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — excessive allocation before arithmetic.
- [stack-overflow]({{< relref "/languages/go/stack-overflow" >}}) — recursive division logic.

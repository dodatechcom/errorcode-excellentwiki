---
title: "[Solution] Go Integer Divide by Zero — Runtime Error Fix"
description: "Fix Go integer divide by zero panic. Check denominators before division, handle edge cases, and validate mathematical operations."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["division", "zero", "integer", "math", "panic"]
weight: 5
---

# Integer Divide by Zero — Runtime Error Fix

An integer divide by zero panic occurs when you divide an integer by zero at runtime.

## Description

In Go, integer division by zero causes a runtime panic. Float division by zero produces `+Inf` or `NaN` without panicking. Since Go does not allow implicit conversions, only integer division by zero triggers this panic.

Common scenarios:

- **User input not validated** — parsing an integer from user input and dividing without checking for zero.
- **Computed denominator** — the divisor is calculated and happens to be zero.
- **Slice index used as divisor** — length from a data source used in division.

## Common Causes

```go
// Cause 1: Direct division by zero
func divide(a, b int) int {
    return a / b // panic if b == 0
}

// Cause 2: Parsed user input
input := "0"
n, _ := strconv.Atoi(input)
result := 100 / n // panic if n == 0

// Cause 3: Computed denominator
nums := []int{10, 20, 0, 30}
for _, n := range nums {
    result := 100 / n // panic when n == 0
    _ = result
}

// Cause 4: Modulo by zero
result := 10 % 0 // panic: integer divide by zero
```

## How to Fix

### Fix 1: Check divisor before dividing

```go
// Wrong
func divide(a, b int) (int, error) {
    return a / b, nil
}

// Correct
func divide(a, b int) (int, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}
```

### Fix 2: Validate input before parsing and dividing

```go
// Wrong
func divideByInput(a int, input string) (int, error) {
    n, err := strconv.Atoi(input)
    if err != nil {
        return 0, err
    }
    return a / n, nil
}

// Correct
func divideByInput(a int, input string) (int, error) {
    n, err := strconv.Atoi(input)
    if err != nil {
        return 0, err
    }
    if n == 0 {
        return 0, errors.New("cannot divide by zero")
    }
    return a / n, nil
}
```

### Fix 3: Guard against zero in loops

```go
// Wrong
for _, n := range nums {
    result := 100 / n
    _ = result
}

// Correct
for _, n := range nums {
    if n == 0 {
        fmt.Printf("Skipping zero divisor\n")
        continue
    }
    result := 100 / n
    _ = result
}
```

### Fix 4: Use safe division wrapper

```go
func safeDiv(a, b int) (int, bool) {
    if b == 0 {
        return 0, false
    }
    return a / b, true
}

func safeMod(a, b int) (int, bool) {
    if b == 0 {
        return 0, false
    }
    return a % b, true
}
```

### Fix 5: Use float for potentially-zero denominators

```go
// Wrong — integer division by zero panics
func divideInt(a, b int) float64 {
    return float64(a / b)
}

// Correct — float division returns Inf/NaN
func divideFloat(a, b int) float64 {
    return float64(a) / float64(b)
}
```

## Examples

```go
// This triggers: runtime error: integer divide by zero
package main

import "fmt"

func main() {
    a := 10
    b := 0
    fmt.Println(a / b)
}
```

## Related Errors

- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer.
- [index-out-of-range]({{< relref "/languages/go/index-out-of-range" >}}) — accessing beyond slice bounds.
- [strconv-parse]({{< relref "/languages/go/strconv-parse" >}}) — parsing invalid strings to numbers.

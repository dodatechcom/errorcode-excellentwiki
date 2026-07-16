---
title: "[Solution] Go Slice Bounds Out of Range — Runtime Error Fix"
description: "Fix Go slice bounds out of range panic when using slice expressions with invalid low or high bounds. Validate indices before slicing."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["slice", "bounds", "range", "panic", "runtime"]
weight: 5
---

# Slice Bounds Out of Range — Runtime Error Fix

A slice bounds out of range panic occurs when a slice expression uses indices that are outside the valid range of the underlying array or slice.

## Description

Go slices have a length and capacity. Slice expressions `s[low:high]` require that `0 <= low <= high <= cap(s)`. Violating any of these constraints panics with `runtime error: slice bounds out of range [N] with length M`.

Common scenarios:

- **High exceeds length** — using an end index greater than `len(s)`.
- **Negative low index** — starting a slice at a negative position.
- **Low exceeds high** — start index is greater than end index.
- **Slicing nil slice** — slicing a nil slice without initializing it first.

## Common Causes

```go
// Cause 1: High index exceeds slice length
func main() {
    s := []int{1, 2, 3}
    sub := s[1:5] // panic: slice bounds out of range [1:5] with length 3
    _ = sub
}

// Cause 2: Negative low index
func main() {
    s := []int{1, 2, 3}
    sub := s[-1:2] // panic
    _ = sub
}

// Cause 3: Low exceeds high
func main() {
    s := []int{1, 2, 3}
    sub := s[2:1] // panic
    _ = sub
}

// Cause 4: Slicing a nil slice
func main() {
    var s []int
    sub := s[0:1] // panic
    _ = sub
}
```

## How to Fix

### Fix 1: Clamp the high index to the slice length

```go
// Wrong
sub := s[1:5]

// Correct
high := 5
if high > len(s) {
    high = len(s)
}
sub := s[1:high]
```

### Fix 2: Validate low index

```go
// Wrong
func subSlice(s []int, low, high int) []int {
    return s[low:high]
}

// Correct
func subSlice(s []int, low, high int) []int {
    if low < 0 || high < low || high > len(s) {
        return nil
    }
    return s[low:high]
}
```

### Fix 3: Initialize before slicing

```go
// Wrong
var s []int
sub := s[0:1]

// Correct
s := make([]int, 3)
sub := s[0:1]
```

### Fix 4: Use full slice expressions to limit capacity

```go
// Correct — full slice expression s[low:high:max]
s := make([]int, 10, 20)
sub := s[2:5:8] // length 3, capacity 6
// This prevents accidental grows via append
```

## Examples

```go
// This triggers: runtime error: slice bounds out of range [2:1] with length 3
package main

import "fmt"

func main() {
    data := []byte("hello")
    // Reversed bounds — low > high
    fmt.Println(data[4:1])
}
```

## Related Errors

- [index-out-of-range]({{< relref "/languages/go/index-out-of-range" >}}) — accessing a single index beyond slice length.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — creating slices with excessively large capacity.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil slice pointer.

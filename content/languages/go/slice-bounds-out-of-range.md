---
title: "[Solution] Go Slice Bounds Out of Range — Runtime Error Fix"
description: "Fix Go slice bounds out of range panic. Validate slice capacity before slicing, and check append results carefully."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["slice", "bounds", "out-of-range", "capacity", "panic"]
weight: 5
---

# Slice Bounds Out of Range — Runtime Error Fix

A slice bounds out of range panic occurs when a slice expression uses bounds that exceed the slice's length or capacity.

## Description

In Go, slice expressions `s[low:high]` require `0 <= low <= high <= cap(s)`. If `high` exceeds the capacity or `low` exceeds `high`, the runtime panics with `runtime error: slice bounds out of range`.

Common scenarios:

- **Slicing beyond capacity** — `s[:100]` when `cap(s)` is 50.
- **Slicing with reversed bounds** — `s[5:2]` where low > high.
- **Slicing a nil slice** — `var s []int; s[0:5]` panics.
- **Using `append` result without checking** — `append` may return a new slice with different capacity.

## Common Causes

```go
// Cause 1: Slicing beyond capacity
s := make([]int, 3, 5)
sub := s[2:10] // panic: slice bounds out of range [2:10] with capacity 5

// Cause 2: Reversed bounds
s := []int{1, 2, 3}
sub := s[2:1] // panic: slice bounds out of range [2:1]

// Cause 3: Nil slice slicing
var s []int
sub := s[0:5] // panic: slice bounds out of range [0:5] with length 0

// Cause 4: Slicing after append that grows the backing array
s := make([]int, 2, 4)
s = append(s, 3, 4) // capacity used up
// Original capacity reference is stale
sub := s[:10] // panic
```

## How to Fix

### Fix 1: Check capacity before slicing beyond length

```go
// Wrong
sub := s[:100]

// Correct
if cap(s) >= 100 {
    sub = s[:100]
} else {
    sub = s[:cap(s)]
}
```

### Fix 2: Ensure low <= high in slice expressions

```go
// Wrong
func sliceRange(s []int, low, high int) []int {
    return s[low:high]
}

// Correct
func sliceRange(s []int, low, high int) []int {
    if low < 0 || high < low || high > len(s) {
        return nil
    }
    return s[low:high]
}
```

### Fix 3: Initialize slices before slicing

```go
// Wrong
var s []int
sub := s[0:5]

// Correct
s := make([]int, 5)
sub := s[0:5]
```

### Fix 4: Use the three-index slice to limit capacity

```go
// Wrong — may accidentally share backing array
sub := s[:len(s)]

// Correct — explicitly control capacity
sub := s[:len(s):len(s)]
```

### Fix 5: Check length before slicing

```go
// Wrong
func firstN(s []int, n int) []int {
    return s[:n] // panics if n > len(s)
}

// Correct
func firstN(s []int, n int) []int {
    if n > len(s) {
        n = len(s)
    }
    return s[:n]
}
```

## Examples

```go
// This triggers: runtime error: slice bounds out of range [5:3] with length 4
package main

import "fmt"

func main() {
    s := []int{1, 2, 3, 4}
    fmt.Println(s[5:3])
}
```

## Related Errors

- [index-out-of-range]({{< relref "/languages/go/index-out-of-range" >}}) — accessing a single index beyond the slice length.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — allocating too much memory with large slices.

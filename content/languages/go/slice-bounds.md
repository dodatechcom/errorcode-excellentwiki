---
title: "[Solution] Go Slice Bounds Out of Range — Runtime Error Fix"
description: "Fix Go runtime error slice bounds out of range. Understand slice expressions, reslicing rules, and safe boundary checks."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Slice Bounds Out of Range — Runtime Error

The error `runtime error: slice bounds out of range` occurs when you use a slice expression (`s[low:high]`) where `low` or `high` exceeds the slice's length or capacity, or where `low > high`.

## Description

When reslicing in Go, the bounds must satisfy: `0 <= low <= high <= cap(s)`. If `high` exceeds the capacity or `low` is greater than `high`, Go panics at runtime. This differs from index-out-of-range errors because it involves slice expressions rather than single-element access.

Common scenarios include incorrect reslicing after appending, using `len()` instead of `cap()` for upper bounds, and constructing sub-slices without accounting for the original slice's capacity.

## Common Causes

- **Using `len()` instead of `cap()`** — reslicing beyond length but within capacity requires `cap()`
- **Incorrect reslice after append** — appending may reallocate, invalidating old capacity assumptions
- **Negative or reversed bounds** — `low > high` in a slice expression
- **Hardcoded slice expressions** — not accounting for dynamic slice lengths

## How to Fix

### Fix 1: Check length before reslicing

```go
func safeSlice(s []int, low, high int) []int {
    if low < 0 || high < low || high > len(s) {
        return nil
    }
    return s[low:high]
}
```

### Fix 2: Use `cap()` for capacity-aware reslicing

```go
s := make([]int, 5, 10)
// s has len=5, cap=10
sub := s[2:8] // OK — within capacity
```

### Fix 3: Validate before reslicing user input

```go
func subSlice(s []int, start, end int) ([]int, error) {
    if start < 0 || end < start || end > len(s) {
        return nil, fmt.Errorf("invalid bounds [%d:%d] for slice of length %d", start, end, len(s))
    }
    return s[start:end], nil
}
```

### Fix 4: Use three-index slicing to limit capacity

```go
s := make([]int, 5, 10)
// Restrict capacity to length
sub := s[:5:5]
sub = append(sub, 100) // does not affect original s
```

## Examples

```go
package main

import "fmt"

func main() {
    s := []int{1, 2, 3}
    fmt.Println(s[1:5]) // panic: slice bounds out of range [1:5] with length 3
}
```

Output:
```
panic: runtime error: slice bounds out of range [1:5] with length 3
```

## Related Errors

- [index-out-of-range]({{< relref "/languages/go/index-out-of-range" >}}) — single-element access beyond bounds.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — excessive memory allocation.
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — unexpected end of data when reading.

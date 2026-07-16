---
title: "[Solution] Go Index Out of Range — Runtime Error Fix"
description: "Fix Go runtime error index out of range. Understand slice and array bounds and how to safely access elements."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "out-of-range", "slice", "array", "bounds", "runtime"]
weight: 5
---

# Index Out of Range — Runtime Error

The error `runtime error: index out of range` occurs when you access a slice or array element using an index that is negative or greater than or equal to the length of the collection.

## Description

Go slices and arrays are zero-indexed. An index of `len(s)` or higher is out of bounds. Negative indices also cause this panic. Unlike languages with automatic bounds checking that return sentinel values, Go terminates the program immediately.

Common scenarios include off-by-one errors in loops, using user-supplied indices without validation, and accessing elements of an empty slice.

## Common Causes

- **Off-by-one error** — using `<=` instead of `<` in loop bounds
- **Empty slice access** — accessing index `0` on a slice with length `0`
- **Unvalidated external input** — using a user-supplied index without checking bounds
- **Incorrect slice length assumption** — assuming a slice has more elements than it does

## How to Fix

### Fix 1: Check bounds before accessing

```go
if i >= 0 && i < len(s) {
    fmt.Println(s[i])
} else {
    fmt.Println("index out of bounds")
}
```

### Fix 2: Fix off-by-one in loops

```go
// Wrong
for i := 0; i <= len(s); i++ {
    fmt.Println(s[i]) // panics when i == len(s)
}

// Correct
for i := 0; i < len(s); i++ {
    fmt.Println(s[i])
}
```

### Fix 3: Use range for iteration

```go
for i, v := range s {
    fmt.Println(i, v)
}
```

### Fix 4: Validate external input

```go
func getElement(s []string, idx int) (string, error) {
    if idx < 0 || idx >= len(s) {
        return "", fmt.Errorf("index %d out of range [0:%d]", idx, len(s))
    }
    return s[idx], nil
}
```

## Examples

```go
package main

import "fmt"

func main() {
    s := []int{10, 20, 30}
    fmt.Println(s[5]) // panic: index out of range
}
```

Output:
```
panic: runtime error: index out of range [5] with length 3
```

## Related Errors

- [slice-bounds-out-of-range]({{< relref "/languages/go/slice-bounds-out-of-range" >}}) — slice expression with invalid bounds.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil pointer.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — allocating excessive memory.

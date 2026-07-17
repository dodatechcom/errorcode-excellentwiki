---
title: "[Solution] Go Index Out of Range — Runtime Error Fix"
description: "Fix Go index out of range panic when accessing slices, arrays, or strings beyond their length. Bounds-check safely before indexing."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Index Out of Range — Runtime Error Fix

An index out of range panic occurs when you try to access a slice, array, or string at a position that doesn't exist.

## Description

Go performs bounds checking on slice, array, and string access. If the index is negative or greater than or equal to the length, the runtime panics with `runtime error: index out of range [N] with length M`.

Common scenarios:

- **Off-by-one error** — using `<=` instead of `<` in a loop condition.
- **Empty slice access** — indexing into a slice with no elements.
- **Wrong loop variable** — using the wrong counter variable as the index.
- **Stale length variable** — caching the length before an append that grows the slice.

## Common Causes

```go
// Cause 1: Off-by-one in loop
func main() {
    nums := []int{10, 20, 30}
    for i := 0; i <= len(nums); i++ {
        fmt.Println(nums[i]) // panic at i == 3
    }
}

// Cause 2: Indexing into empty slice
func main() {
    var s []int
    fmt.Println(s[0]) // panic: index out of range [0] with length 0
}

// Cause 3: Using wrong loop variable
func main() {
    data := [][]int{{1, 2}, {3, 4}}
    for i := range data {
        for j := range data {
            fmt.Println(data[i][j]) // uses i instead of j for inner index
        }
    }
}

// Cause 4: Stale length after append
func main() {
    s := make([]int, 2, 4)
    l := len(s)
    s = append(s, 3, 4, 5)
    fmt.Println(s[l]) // works, but s[l+2] panics if length grew unexpectedly
}
```

## How to Fix

### Fix 1: Use `<` not `<=` in loop conditions

```go
// Wrong
for i := 0; i <= len(nums); i++ {
    fmt.Println(nums[i])
}

// Correct
for i := 0; i < len(nums); i++ {
    fmt.Println(nums[i])
}
```

### Fix 2: Check slice length before indexing

```go
// Wrong
func getFirst(s []int) int {
    return s[0]
}

// Correct
func getFirst(s []int) (int, bool) {
    if len(s) == 0 {
        return 0, false
    }
    return s[0], true
}
```

### Fix 3: Use range correctly for multi-dimensional slices

```go
// Wrong
for i := range data {
    for j := range data {
        fmt.Println(data[i][j]) // j iterates over outer length
    }
}

// Correct
for i := range data {
    for j := range data[i] {
        fmt.Println(data[i][j])
    }
}
```

### Fix 4: Re-read length after mutations

```go
// Wrong
l := len(s)
s = append(s, more...)
fmt.Println(s[l+1]) // may panic

// Correct
s = append(s, more...)
if len(s) > l+1 {
    fmt.Println(s[l+1])
}
```

## Examples

```go
// This triggers: runtime error: index out of range [3] with length 3
package main

import "fmt"

func main() {
    colors := []string{"red", "green", "blue"}
    fmt.Println(colors[3]) // only indices 0-2 are valid
}
```

## Related Errors

- [slice-bounds-out-of-range]({{< relref "/languages/go/slice-bounds-out-of-range" >}}) — slice expression uses invalid start/end indices.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing a nil slice or pointer.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — allocating excessively large slices.

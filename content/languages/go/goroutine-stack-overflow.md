---
title: "[Solution] Go goroutine stack overflow — Runtime Error Fix"
description: "Fix Go goroutine stack overflow."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# goroutine stack overflow

The error `runtime: goroutine stack overflow` occurs when a goroutine's stack grows beyond the maximum allowed size.

## Common Causes

- **Infinite recursion** — function calling itself without a base case
- **Circular callbacks** — two functions calling each other

## How to Fix

### Fix 1: Add base case to recursive functions

```go
func factorial(n int) int {
    if n <= 1 { return 1 }
    return n * factorial(n-1)
}
```

### Fix 2: Convert to iterative approach

```go
func factorial(n int) int {
    result := 1
    for i := 2; i <= n; i++ {
        result *= i
    }
    return result
}
```

## Examples

```go
package main

func recurse() {
    recurse()
}

func main() {
    recurse()
}
```

Output:
```
runtime: goroutine stack overflow
```

## Related Errors

- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck forever.

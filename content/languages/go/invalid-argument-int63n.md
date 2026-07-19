---
title: "[Solution] Go invalid argument to Int63n — Runtime Error Fix"
description: "Fix Go invalid argument to Int63n. Ensure arguments are positive."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# invalid argument to Int63n

The error `invalid argument to Int63n` occurs when you pass a non-positive value to `rand.Int63n()`.

## Common Causes

- **Empty slice length** — using `len(s)` when slice is empty
- **Zero-value variable** — uninitialized size variable

## How to Fix

### Fix 1: Check n before calling

```go
func randomIndex(n int) int {
    if n <= 0 { return 0 }
    return rand.Intn(n)
}
```

## Examples

```go
package main

import (
    "fmt"
    "math/rand"
)

func main() {
    n := rand.Int63n(0)
    fmt.Println(n)
}
```

Output:
```
panic: invalid argument to Int63n
```

## Related Errors

- [divide-by-zero-runtime]({{< relref "/languages/go/divide-by-zero-runtime" >}}) — divide by zero.
- [overflow-conversion]({{< relref "/languages/go/overflow-conversion" >}}) — conversion overflow.

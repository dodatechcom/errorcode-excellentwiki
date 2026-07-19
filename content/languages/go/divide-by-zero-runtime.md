---
title: "[Solution] Go runtime error: integer divide by zero — Runtime Error Fix"
description: "Fix Go integer divide by zero panic."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# runtime error: integer divide by zero

The error `runtime error: integer divide by zero` occurs when you divide an integer by zero at runtime.

## Common Causes

- **User input** — dividing by a parsed integer without checking for zero
- **Counter-based division** — denominator could be zero

## How to Fix

### Fix 1: Check denominator before division

```go
func safeDiv(a, b int) (int, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

## Examples

```go
package main

import "fmt"

func main() {
    a, b := 10, 0
    fmt.Println(a / b)
}
```

Output:
```
panic: runtime error: integer divide by zero
```

## Related Errors

- [integer-overflow]({{< relref "/languages/go/integer-overflow" >}}) — integer overflow.
- [invalid-argument-int63n]({{< relref "/languages/go/invalid-argument-int63n" >}}) — invalid math argument.

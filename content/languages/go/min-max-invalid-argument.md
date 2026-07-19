---
title: "[Solution] Go min/max invalid argument — Runtime Error Fix"
description: "Fix Go invalid argument to min/max."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# invalid argument to min/max

The error `invalid argument to min` or `invalid argument to max` occurs when called with no arguments or NaN values.

## Common Causes

- **Empty argument list** — `min()` with no arguments
- **NaN values** — `0.0 / 0.0` produces NaN

## How to Fix

### Fix 1: Ensure at least one argument

```go
func safeMin(nums ...int) (int, bool) {
    if len(nums) == 0 { return 0, false }
    return min(nums...), true
}
```

## Examples

```go
package main

import "fmt"

func main() {
    result := min()
    fmt.Println(result)
}
```

Output:
```
panic: invalid argument to min
```

## Related Errors

- [divide-by-zero-runtime]({{< relref "/languages/go/divide-by-zero-runtime" >}}) — divide by zero.
- [integer-overflow]({{< relref "/languages/go/integer-overflow" >}}) — integer overflow.

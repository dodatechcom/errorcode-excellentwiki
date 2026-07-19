---
title: "[Solution] Go overflow during type conversion — Runtime Error Fix"
description: "Fix Go integer overflow during type conversion."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# overflow during type conversion

The error `runtime error: overflow during int64 conversion` occurs when converting a value that exceeds the target type's range.

## Common Causes

- **uint64 to int64** — large unsigned values exceeding signed range
- **Timestamp parsing** — Unix nanosecond timestamps overflowing int64

## How to Fix

### Fix 1: Validate range before conversion

```go
func toInt64(v uint64) (int64, error) {
    if v > math.MaxInt64 {
        return 0, fmt.Errorf("value %d overflows int64", v)
    }
    return int64(v), nil
}
```

## Examples

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    v := uint64(math.MaxUint64)
    n := int64(v)
    fmt.Println(n)
}
```

Output:
```
panic: runtime error: overflow during int64 conversion
```

## Related Errors

- [integer-overflow]({{< relref "/languages/go/integer-overflow" >}}) — integer overflow.
- [invalid-argument-int63n]({{< relref "/languages/go/invalid-argument-int63n" >}}) — invalid math argument.

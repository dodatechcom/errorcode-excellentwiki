---
title: "[Solution] Go conv overflow / conv t-string — Runtime Error Fix"
description: "Fix Go string conversion panic."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# conv overflow

The error `runtime error: conv overflow` occurs when converting a value too large for the target type.

## How to Fix

### Fix 1: Validate before conversion

```go
func intToByte(n int) (byte, error) {
    if n < 0 || n > 255 {
        return 0, fmt.Errorf("%d out of byte range", n)
    }
    return byte(n), nil
}
```

## Examples

```go
package main

import "fmt"

func main() {
    n := int64(1 << 40)
    b := byte(n)
    fmt.Println(b)
}
```

Output:
```
panic: runtime error: overflow
```

## Related Errors

- [overflow-conversion]({{< relref "/languages/go/overflow-conversion" >}}) — conversion overflow.
- [integer-overflow]({{< relref "/languages/go/integer-overflow" >}}) — integer overflow.

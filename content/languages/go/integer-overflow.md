---
title: "[Solution] Go integer overflow — Runtime Error Fix"
description: "Fix Go integer overflow panic."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# integer overflow

The error `runtime error: integer overflow` occurs when integer arithmetic overflows.

## Common Causes

- **Shift overflow** — shifting by more than the bit width
- **Multiplication overflow** — large numbers multiplied together

## How to Fix

### Fix 1: Check before shifting

```go
func safeShift(n, shift int) (int, error) {
    if shift < 0 || shift >= strconv.IntSize {
        return 0, fmt.Errorf("shift amount %d out of range", shift)
    }
    return n << uint(shift), nil
}
```

### Fix 2: Use big.Int for large numbers

```go
import "math/big"

a := big.NewInt(1)
b := big.NewInt(1)
b.Lsh(a, 1000)
```

## Examples

```go
package main

import "fmt"

func main() {
    var a int = 1 << 63
    fmt.Println(a)
}
```

Output:
```
panic: runtime error: shift out of range
```

## Related Errors

- [divide-by-zero-runtime]({{< relref "/languages/go/divide-by-zero-runtime" >}}) — divide by zero.
- [overflow-conversion]({{< relref "/languages/go/overflow-conversion" >}}) — conversion overflow.

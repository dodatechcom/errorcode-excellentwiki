---
title: "[Solution] Go makeslice: len out of range — Runtime Error Fix"
description: "Fix Go makeslice len out of range panic."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# makeslice: len out of range

The error `runtime error: makeslice: len out of range` occurs when creating a slice with an excessively large length.

## How to Fix

### Fix 1: Validate length before creating

```go
func safeMake(n int) ([]byte, error) {
    const maxLen = 1 << 30
    if n < 0 || n > maxLen {
        return nil, fmt.Errorf("invalid length: %d", n)
    }
    return make([]byte, n), nil
}
```

## Examples

```go
package main

func main() {
    n := int(^uint(0) >> 1)
    s := make([]byte, n)
    _ = s
}
```

Output:
```
panic: runtime error: makeslice: len out of range
```

## Related Errors

- [slice-bounds]({{< relref "/languages/go/slice-bounds" >}}) — slice bounds.
- [integer-overflow]({{< relref "/languages/go/integer-overflow" >}}) — integer overflow.

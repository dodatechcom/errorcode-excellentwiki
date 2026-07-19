---
title: "[Solution] Go invalid slice index / invalid slice expression — Compile Error Fix"
description: "Fix Go invalid slice index error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# invalid slice index / invalid slice expression

The error `invalid slice index` occurs when slice indices are not valid integer expressions.

## Common Causes

- **Float index** — `s[1.5:3]`
- **Reversed bounds** — `s[3:1]`

## How to Fix

### Fix 1: Use integer indices

```go
s := []int{1, 2, 3, 4}
sub := s[1:3]
```

## Examples

```go
package main

func main() {
    s := []int{1, 2, 3}
    _ = s[1.0:2]
}
```

Output:
```
invalid slice index 1.0 (float64)
```

## Related Errors

- [slice-bounds]({{< relref "/languages/go/slice-bounds" >}}) — slice bounds.
- [cannot-slice]({{< relref "/languages/go/cannot-slice" >}}) — cannot slice.

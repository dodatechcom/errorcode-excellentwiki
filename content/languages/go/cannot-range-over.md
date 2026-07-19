---
title: "[Solution] Go cannot range over / cannot iterate — Compile Error Fix"
description: "Fix Go cannot range over error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# cannot range over / cannot iterate

The error `cannot range over X` occurs when you use `range` on a non-iterable type.

## Common Causes

- **Ranging over integer** — `for i := range 10` (Go < 1.23)
- **Ranging over struct** — structs are not iterable

## How to Fix

### Fix 1: Use traditional for loop

```go
for i := 0; i < 10; i++ {
    fmt.Println(i)
}
```

## Examples

```go
package main

func main() {
    for i := range 5 {
        _ = i
    }
}
```

Output (Go < 1.23):
```
cannot range over 5 (untyped int)
```

## Related Errors

- [slice-bounds]({{< relref "/languages/go/slice-bounds" >}}) — slice bounds.
- [cannot-use-type]({{< relref "/languages/go/cannot-use-type" >}}) — type mismatch.

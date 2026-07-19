---
title: "[Solution] Go cannot take address of — Type Error Fix"
description: "Fix Go cannot take address of error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# cannot take address of

The error `cannot take address of x` occurs when you try to get the memory address of a non-addressable value.

## Common Causes

- **Taking address of literal** — `&123`
- **Taking address of map value** — `&m[key]`

## How to Fix

### Fix 1: Use a variable instead of literal

```go
x := 123
p := &x
```

## Examples

```go
package main

func main() {
    p := &42
    _ = p
}
```

Output:
```
cannot take address of 42
```

## Related Errors

- [cannot-assign]({{< relref "/languages/go/cannot-assign" >}}) — cannot assign.
- [cannot-use-type]({{< relref "/languages/go/cannot-use-type" >}}) — type mismatch.

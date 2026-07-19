---
title: "[Solution] Go cannot use X as type Y — Type Error Fix"
description: "Fix Go cannot use as type error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# cannot use X as type Y

The error `cannot use x (type A) as type B` occurs when you pass a value of one type where a different type is expected.

## Common Causes

- **Wrong argument type** — passing int where string is expected
- **Named type mismatch** — `type ID int` is not the same as `int`

## How to Fix

### Fix 1: Explicit type conversion

```go
var x int = 42
var y float64 = float64(x)
```

### Fix 2: Use type alias or conversion function

```go
type ID int
func toID(n int) ID { return ID(n) }
```

## Examples

```go
package main

func add(a, b int) int { return a + b }

func main() {
    result := add(1, 2.5)
    _ = result
}
```

Output:
```
cannot use 2.5 (type float64) as type int
```

## Related Errors

- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion failed.
- [interface-nil]({{< relref "/languages/go/interface-nil" >}}) — nil interface.

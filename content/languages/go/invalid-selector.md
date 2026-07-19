---
title: "[Solution] Go invalid selector / unknown field in struct literal — Type Error Fix"
description: "Fix Go invalid selector or unknown field error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# invalid selector / unknown field in struct literal

The error `invalid selector X` or `unknown field X in struct literal` occurs when referencing a field that does not exist.

## How to Fix

### Fix 1: Use correct field name

```go
type User struct {
    Name string
    Age  int
}

u := User{Name: "Alice", Age: 30}
fmt.Println(u.Name)
```

## Examples

```go
package main

type Point struct {
    X int
    Y int
}

func main() {
    p := Point{X: 1, Y: 2}
    _ = p.Z
}
```

Output:
```
p.Z undefined (type Point has no field or method Z)
```

## Related Errors

- [undefined-name]({{< relref "/languages/go/undefined-name" >}}) — undefined name.
- [cannot-use-type]({{< relref "/languages/go/cannot-use-type" >}}) — type mismatch.

---
title: "[Solution] Go interface conversion: interface {} is nil — Type Error Fix"
description: "Fix Go interface nil error. Understand nil interface values."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# interface conversion: interface {} is nil

The error `interface conversion: interface {} is nil` occurs when you attempt to type-assert a nil interface value.

## Common Causes

- **Returning nil from untyped function** — `func f() interface{} { return nil }`
- **Map lookup returning zero value** — zero value for interface type is nil
- **Unchecked type assertion** — not using comma-ok pattern

## How to Fix

### Fix 1: Use comma-ok type assertion

```go
val, ok := iface.(string)
if !ok {
    fmt.Println("not a string")
    return
}
```

### Fix 2: Use type switch

```go
switch v := iface.(type) {
case string:
    fmt.Println("string:", v)
case nil:
    fmt.Println("nil interface")
default:
    fmt.Println("unknown type")
}
```

## Examples

```go
package main

import "fmt"

func main() {
    var iface interface{} = nil
    val := iface.(string)
    fmt.Println(val)
}
```

Output:
```
panic: interface conversion: interface {} is nil, not string
```

## Related Errors

- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion failed.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — nil pointer dereference.

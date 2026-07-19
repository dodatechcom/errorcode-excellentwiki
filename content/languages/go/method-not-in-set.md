---
title: "[Solution] Go method X is not in method set of type — Type Error Fix"
description: "Fix Go method not in method set error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# method X is not in method set of type

The error `X does not implement Y (missing Z method)` occurs when a type doesn't satisfy an interface.

## Common Causes

- **Pointer vs value receiver** — interface needs methods with pointer receivers

## How to Fix

### Fix 1: Use pointer to type

```go
type MyType struct{}
func (m *MyType) Do() {}
var iface Interface = &MyType{} // must be pointer
```

## Examples

```go
package main

type Doer interface {
    Do()
}

type MyStruct struct{}
func (m *MyStruct) Do() {}

func main() {
    var d Doer = MyStruct{}
    _ = d
}
```

Output:
```
cannot use MyStruct{} as type Doer:
    MyStruct does not implement Doer (Do method has pointer receiver)
```

## Related Errors

- [cannot-use-interface]({{< relref "/languages/go/cannot-use-interface" >}}) — interface error.
- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion failed.

---
title: "[Solution] Go cannot use as interface in assignment — Type Error Fix"
description: "Fix Go cannot use as interface in assignment error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# cannot use X as interface in assignment

The error `cannot use x as type Y in assignment` occurs when a value does not implement the required interface.

## How to Fix

### Fix 1: Implement all required methods

```go
type Writer interface {
    Write([]byte) (int, error)
}

type MyWriter struct{}

func (w *MyWriter) Write(p []byte) (int, error) {
    return os.Stdout.Write(p)
}

var _ Writer = &MyWriter{}
```

## Examples

```go
package main

type Adder interface {
    Add(a, b int) int
}

type Math struct{}

func main() {
    var a Adder = Math{}
    _ = a
}
```

Output:
```
cannot use Math{} (type Math) as type Adder in assignment:
    Math does not implement Adder (missing Add method)
```

## Related Errors

- [type-assertion]({{< relref "/languages/go/type-assertion" >}}) — type assertion failed.
- [cannot-use-type]({{< relref "/languages/go/cannot-use-type" >}}) — type mismatch.

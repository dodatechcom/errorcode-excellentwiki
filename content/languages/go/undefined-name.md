---
title: "[Solution] Go undefined: X / undeclared name — Compile Error Fix"
description: "Fix Go undefined name error."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# undefined: X / undeclared name

The error `undefined: X` occurs when you reference a name that has not been declared.

## Common Causes

- **Typo** — misspelling a name
- **Missing import** — using a package without importing it
- **Wrong scope** — variable used outside its block

## How to Fix

### Fix 1: Add missing import

```go
import "fmt"
fmt.Println("hello")
```

## Examples

```go
package main

func main() {
    fmt.Println(x)
}
```

Output:
```
undefined: fmt
undefined: x
```

## Related Errors

- [syntax-error-unexpected]({{< relref "/languages/go/syntax-error-unexpected" >}}) — syntax errors.
- [import-cycle]({{< relref "/languages/go/import-cycle" >}}) — import cycle.

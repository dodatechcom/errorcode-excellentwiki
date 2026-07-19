---
title: "[Solution] Go syntax error: unexpected — Compile Error Fix"
description: "Fix Go syntax error unexpected token."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# syntax error: unexpected

The error `syntax error: unexpected X` occurs when the Go parser encounters a token it does not expect.

## Common Causes

- **Missing closing bracket** — `{` without matching `}`
- **Missing comma** — in function arguments
- **Misplaced keyword** — `return` outside a function

## How to Fix

### Fix 1: Check bracket matching

```go
func main() {
    if true {
        fmt.Println("hello")
    }
}
```

### Fix 2: Use gofmt to auto-fix formatting

```bash
gofmt -w file.go
```

## Examples

```go
package main

func main() {
    fmt.Println("hello"
}
```

Output:
```
syntax error: unexpected newline, expecting )
```

## Related Errors

- [undefined-name]({{< relref "/languages/go/undefined-name" >}}) — undefined name.
- [import-cycle]({{< relref "/languages/go/import-cycle" >}}) — import cycle.

---
title: "[Solution] Go Panic and Recover — Runtime Error Handling Guide"
description: "Understand Go panics and recover. Learn when panics occur, how to use recover() to handle them, and when to use error returns instead."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Panic and Recover — Runtime Error Handling

A Go panic is a runtime error that immediately stops normal execution and begins unwinding the stack, running any deferred functions. If not recovered, the program terminates. The `recover` function lets you catch panics inside deferred functions.

## Description

Panics occur for critical errors like nil pointer dereference, index out of range, and map access on nil maps. While Go prefers returning errors, panics are used for truly unrecoverable situations. The `recover` built-in function only works inside a `defer` function and returns the value passed to `panic()`.

Understanding the panic/recover mechanism is essential for writing resilient Go servers, especially HTTP handlers that should not crash on individual request errors.

## Common Causes

- **Runtime errors** — nil dereference, index out of range, slice bounds exceeded
- **Explicit panic calls** — `panic("something impossible happened")`
- **Unrecovered panic in goroutine** — panics in goroutines crash the entire program
- **Missing defer/recover in HTTP handlers** — a panic in a handler crashes the server

## How to Fix

### Fix 1: Use recover in HTTP middleware

```go
func recoveryMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                log.Printf("panic recovered: %v\n%s", err, debug.Stack())
                http.Error(w, "Internal Server Error", 500)
            }
        }()
        next.ServeHTTP(w, r)
    })
}
```

### Fix 2: Recover panics in goroutines

```go
func safeGoroutine(fn func()) {
    defer func() {
        if err := recover(); err != nil {
            log.Printf("goroutine panic recovered: %v", err)
        }
    }()
    fn()
}

go safeGoroutine(func() {
    riskyOperation()
})
```

### Fix 3: Don't use panic for normal error handling

```go
// Wrong — use error returns instead
func divide(a, b int) int {
    if b == 0 {
        panic("division by zero")
    }
    return a / b
}

// Correct
func divide(a, b int) (int, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Fix 4: Use defer to clean up resources even on panic

```go
func processFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close() // runs even if panic occurs
    // process file...
    return nil
}
```

## Examples

```go
package main

import (
    "fmt"
    "runtime/debug"
)

func main() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Printf("recovered: %v\n", r)
            debug.PrintStack()
        }
    }()

    panic("something went wrong")
}
```

Output:
```
recovered: something went wrong
goroutine 1 [running]:
main.main()
    /tmp/main.go:13 +0x45
```

## Related Errors

- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — most common cause of unexpected panics.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — unrecovered panics in goroutines crash the program.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — related runtime error that terminates the program.

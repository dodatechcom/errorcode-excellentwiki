---
title: "[Solution] Go Context Deadline Exceeded Fix"
description: "Fix Go context deadline exceeded error. Use appropriate timeouts, handle deadline errors gracefully, and avoid premature context expiration."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["context", "deadline", "timeout", "cancel", "runtime"]
weight: 5
---

# Context Deadline Exceeded Fix

A context deadline exceeded error occurs when an operation exceeds the timeout set on its context.

## Description

`context.WithTimeout` and `context.WithDeadline` create contexts that expire after a set duration. When the deadline passes before the operation completes, the context's `Done()` channel closes and `Err()` returns `context deadline exceeded`. This is Go's standard mechanism for enforcing timeouts.

Common scenarios:

- **HTTP request timeout too short** — context expires before server responds.
- **Database query timeout** — slow query exceeds context deadline.
- **Chained timeouts too tight** — parent timeout is shorter than child operation.
- **Clock skew** — system clock changes affecting deadline calculations.

## Common Causes

```go
// Cause 1: Timeout too short for operation
func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
    defer cancel()

    resp, err := http.Get("https://slow-api.example.com")
    // context deadline exceeded if API takes > 100ms
    _ = resp
    _ = err
}

// Cause 2: Parent timeout tighter than child needs
func handleRequest(w http.ResponseWriter, r *http.Request) {
    ctx, cancel := context.WithTimeout(r.Context(), 1*time.Second)
    defer cancel()

    result := slowDatabaseQuery(ctx) // needs 2 seconds
    _ = result
}

// Cause 3: Accumulated timeout across chained calls
func callChain(ctx context.Context) {
    ctx1, cancel1 := context.WithTimeout(ctx, 500*time.Millisecond)
    defer cancel1()

    callService1(ctx1)     // takes 400ms
    callService2(ctx1)     // only 100ms left
}

// Cause 4: Deadline set on already-expired context
func main() {
    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    cancel()

    child, cancel2 := context.WithTimeout(ctx, 5*time.Second)
    defer cancel2()
    // child is already expired because parent was canceled
}
```

## How to Fix

### Fix 1: Use appropriate timeouts for your operations

```go
// Wrong — too short
ctx, cancel := context.WithTimeout(context.Background(), 10*time.Millisecond)

// Correct — reasonable timeout for HTTP calls
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
```

### Fix 2: Check and handle deadline exceeded specifically

```go
func query(ctx context.Context) (Result, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    result, err := db.QueryContext(ctx, "SELECT ...")
    if err != nil {
        if ctx.Err() == context.DeadlineExceeded {
            return Result{}, fmt.Errorf("query timed out")
        }
        return Result{}, err
    }
    return result, nil
}
```

### Fix 3: Propagate deadlines correctly

```go
func handleRequest(w http.ResponseWriter, r *http.Request) {
    // Use request context which already has a deadline
    ctx := r.Context()

    // Add additional timeout relative to request deadline
    ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    defer cancel()

    doWork(ctx)
}
```

### Fix 4: Use context.WithDeadline for absolute times

```go
// Correct — absolute deadline
deadline := time.Now().Add(30 * time.Second)
ctx, cancel := context.WithDeadline(context.Background(), deadline)
defer cancel()
```

## Examples

```go
// This triggers: context deadline exceeded
package main

import (
    "context"
    "fmt"
    "time"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 1*time.Millisecond)
    defer cancel()

    select {
    case <-time.After(1 * time.Second):
        fmt.Println("done")
    case <-ctx.Done():
        fmt.Println(ctx.Err()) // context deadline exceeded
    }
}
```

## Related Errors

- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context explicitly canceled.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP request timeout.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.

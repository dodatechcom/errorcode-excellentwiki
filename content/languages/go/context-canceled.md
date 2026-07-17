---
title: "[Solution] Go Context Canceled / Deadline Exceeded — Runtime Error Fix"
description: "Fix Go context canceled and context deadline exceeded errors. Handle context propagation, timeouts, and cancellation properly."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Context Canceled / Deadline Exceeded

The error `context canceled` or `context deadline exceeded` occurs when an operation is performed on a context that has been cancelled or has passed its deadline. This is a normal part of Go's context lifecycle but becomes an error when not handled properly.

## Description

Go's `context.Context` carries deadlines, cancellation signals, and request-scoped values across API boundaries. When a context is canceled (via `cancel()`) or its deadline expires, all operations using that context should stop. Failing to check `ctx.Err()` or ignoring context cancellation leads to wasted work and confusing error messages.

Common scenarios include HTTP handlers where the client disconnects, background tasks that outlive their parent context, and database queries that should respect timeouts.

## Common Causes

- **Client disconnected** — HTTP request canceled before server finished processing
- **Timeout expired** — `context.WithTimeout` deadline reached before operation completed
- **Parent context canceled** — a parent context was canceled, propagating to children
- **Not checking ctx.Err()** — continuing work after context cancellation

## How to Fix

### Fix 1: Check context cancellation before expensive operations

```go
func processRequest(ctx context.Context, data []byte) error {
    if err := ctx.Err(); err != nil {
        return fmt.Errorf("context canceled: %w", err)
    }
    // proceed with work
    return nil
}
```

### Fix 2: Use select for non-blocking context checks

```go
func worker(ctx context.Context, jobs <-chan Job) {
    for {
        select {
        case <-ctx.Done():
            fmt.Println("worker stopped:", ctx.Err())
            return
        case job := <-jobs:
            process(job)
        }
    }
}
```

### Fix 3: Propagate context through function calls

```go
func handleRequest(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    result, err := queryDatabase(ctx, r.URL.Query().Get("id"))
    if err != nil {
        if errors.Is(err, context.Canceled) {
            // Client disconnected — no need to write response
            return
        }
        http.Error(w, err.Error(), 500)
    }
}
```

### Fix 4: Set appropriate timeouts

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

result, err := doSlowOperation(ctx)
if err != nil {
    if errors.Is(err, context.DeadlineExceeded) {
        log.Println("operation timed out")
    }
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "time"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
    defer cancel()

    time.Sleep(200 * time.Second) // simulate slow work

    fmt.Println(ctx.Err())
}
```

Output:
```
context deadline exceeded
```

## Related Errors

- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP request or response timeouts.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection failures and timeouts.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck waiting on canceled contexts.

---
title: "[Solution] Go Context Deadline Exceeded Error Fix"
description: "Fix Go context deadline exceeded error. Set appropriate timeouts, use context.WithTimeout properly, and handle deadline errors gracefully."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["context", "deadline", "timeout", "context-deadline-exceeded"]
weight: 5
---

# Context Deadline Exceeded — Error Fix

A context deadline exceeded error occurs when an operation takes longer than the timeout specified via `context.WithTimeout` or `context.WithDeadline`.

## Description

Go's `context.WithTimeout` creates a context that automatically cancels after a specified duration. When the timeout expires, all operations using that context receive `context deadline exceeded`. This is a safety mechanism to prevent operations from running indefinitely.

Common scenarios:

- **HTTP request timeout** — server doesn't respond within the timeout.
- **Database query timeout** — query takes too long.
- **RPC call timeout** — remote service is slow.
- **File I/O timeout** — disk is slow or unresponsive.
- **Too short timeout** — timeout value is smaller than the operation requires.

## Common Causes

```go
// Cause 1: HTTP request with short timeout
ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
defer cancel()

req, _ := http.NewRequestWithContext(ctx, "GET", "http://slow-server.com", nil)
resp, err := http.DefaultClient.Do(req) // context deadline exceeded

// Cause 2: Database query without context timeout
ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
defer cancel()

row := db.QueryRowContext(ctx, "SELECT * FROM large_table")
// May timeout if query is slow

// Cause 3: Timeout too short for the operation
ctx, cancel := context.WithTimeout(context.Background(), 10*time.Millisecond)
defer cancel()

result := doComplexComputation(ctx) // Takes 100ms, always times out

// Cause 4: Forgetting to cancel context (leaks timeout goroutine)
func bad() {
    ctx, _ := context.WithTimeout(context.Background(), 5*time.Second)
    doWork(ctx) // Context goroutine leaks
}
```

## How to Fix

### Fix 1: Set appropriate timeouts

```go
// Wrong — 1 second is too short for network call
ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
defer cancel()

// Correct — match the timeout to the expected operation time
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()

req, _ := http.NewRequestWithContext(ctx, "GET", "http://api.example.com/data", nil)
resp, err := http.DefaultClient.Do(req)
```

### Fix 2: Always defer cancel()

```go
// Wrong — context goroutine leaks
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
doWork(ctx)
// cancel() never called

// Correct
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
doWork(ctx)
```

### Fix 3: Handle deadline exceeded with retry

```go
func fetchWithRetry(ctx context.Context, url string) (*http.Response, error) {
    for attempt := 0; attempt < 3; attempt++ {
        req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
        resp, err := http.DefaultClient.Do(req)
        if err == nil {
            return resp, nil
        }
        if ctx.Err() == context.DeadlineExceeded {
            log.Printf("attempt %d: deadline exceeded, retrying...", attempt+1)
            continue
        }
        return nil, err
    }
    return nil, ctx.Err()
}
```

### Fix 4: Use per-operation timeouts

```go
// Wrong — single timeout for entire chain
ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
defer cancel()

fetchUser(ctx)     // May take 1s
fetchOrders(ctx)   // May take 5s
fetchReviews(ctx)  // May take 5s — total 11s > 10s

// Correct — per-operation timeouts
func handler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()

    userCtx, cancel := context.WithTimeout(ctx, 2*time.Second)
    defer cancel()
    user, err := fetchUser(userCtx)

    ordersCtx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()
    orders, err := fetchOrders(ordersCtx)
}
```

### Fix 5: Check for deadline exceeded before retrying

```go
// Wrong — retries even when context is done
for i := 0; i < 3; i++ {
    result, err := doWork(ctx)
    if err != nil {
        continue // May retry after context is already expired
    }
    return result, nil
}

// Correct — check context first
for i := 0; i < 3; i++ {
    if ctx.Err() != nil {
        return nil, ctx.Err()
    }
    result, err := doWork(ctx)
    if err != nil {
        continue
    }
    return result, nil
}
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
    ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
    defer cancel()

    // Simulate slow operation
    select {
    case <-time.After(3 * time.Second):
        fmt.Println("done")
    case <-ctx.Done():
        fmt.Println(ctx.Err()) // context deadline exceeded
    }
}
```

## Related Errors

- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context was manually canceled.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP client timeout.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines not exiting after deadline.

---
title: "[Solution] Go Context Canceled Error Fix"
description: "Fix Go context canceled error. Handle context cancellation in goroutines, avoid using canceled contexts, and properly propagate cancellation."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Context Canceled Error Fix

A context canceled error occurs when an operation is attempted using a context that has already been canceled by its parent or caller.

## Description

In Go, `context.Context` carries cancellation signals and deadlines through call chains. When a context is canceled (via its `cancel` function or parent cancellation), all operations using that context should stop. If code continues to use the canceled context, operations fail with `context canceled`.

Common scenarios:

- **HTTP handler after client disconnect** — the request context is canceled.
- **Explicit cancel called too early** — parent calls cancel before child finishes.
- **Deferred cancel in wrong scope** — cancel runs immediately after function returns.
- **Goroutine ignoring context** — goroutine continues work after context is done.

## Common Causes

```go
// Cause 1: Using context after explicit cancel
func main() {
    ctx, cancel := context.WithCancel(context.Background())
    cancel() // cancel immediately

    req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.example.com", nil)
    resp, err := http.DefaultClient.Do(req) // context canceled
    _ = resp
    _ = err
}

// Cause 2: Deferred cancel runs before context is used
func handle(w http.ResponseWriter, r *http.Request) {
    ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
    defer cancel() // runs when handle returns

    go func() {
        time.Sleep(10 * time.Second)
        doWork(ctx) // ctx already canceled
    }()
}

// Cause 3: Parent context canceled before child completes
func main() {
    parent, cancel := context.WithCancel(context.Background())
    child, _ := context.WithCancel(parent)

    go func() {
        time.Sleep(time.Second)
        cancel() // cancels parent AND child
    }()

    doWork(child) // fails with context canceled
}

// Cause 4: Channel close cancels context prematurely
func worker(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            return
        default:
            doWork(ctx)
        }
    }
}
```

## How to Fix

### Fix 1: Check context before using it

```go
func doWork(ctx context.Context) error {
    if ctx.Err() != nil {
        return ctx.Err() // don't start work on canceled context
    }
    // proceed with work
    return nil
}
```

### Fix 2: Don't defer cancel in goroutines that outlive the function

```go
// Wrong
func handle(ctx context.Context) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel() // runs when handle returns, canceling background work

    go backgroundWork(ctx)
}

// Correct
func handle(ctx context.Context) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)

    go func() {
        defer cancel() // cancel when work is done
        backgroundWork(ctx)
    }()
}
```

### Fix 3: Handle context cancellation gracefully

```go
func fetchData(ctx context.Context) ([]byte, error) {
    req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.example.com", nil)
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        if ctx.Err() == context.Canceled {
            return nil, fmt.Errorf("request canceled")
        }
        return nil, err
    }
    defer resp.Body.Close()
    return io.ReadAll(resp.Body)
}
```

### Fix 4: Create independent context for background tasks

```go
func handleRequest(w http.ResponseWriter, r *http.Request) {
    // Background task uses its own context, not request context
    bgCtx := context.Background()
    go doBackgroundWork(bgCtx)
}
```

## Examples

```go
// This triggers: Get "https://api.example.com": context canceled
package main

import (
    "context"
    "fmt"
    "net/http"
)

func main() {
    ctx, cancel := context.WithCancel(context.Background())
    cancel()

    req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.example.com", nil)
    _, err := http.DefaultClient.Do(req)
    fmt.Println(err) // context canceled
}
```

## Related Errors

- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline exceeded (timeout).
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP request timeout.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.

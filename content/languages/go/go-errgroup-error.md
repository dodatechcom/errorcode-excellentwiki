---
title: "[Solution] Go errgroup Error — How to Fix"
description: "Fix Go errgroup errors. Handle goroutine error propagation, context cancellation, concurrency limits, and error collection."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go errgroup Error

Fix Go errgroup errors. Handle goroutine error propagation, context cancellation, concurrency limits, and error collection.

## Why It Happens

- errgroup cancels the context on first error but goroutines do not check ctx.Done
- The errgroup limit is set too low causing goroutines to block indefinitely
- Errors from errgroup.Wait are not handled causing silent failures
- A goroutine spawned by errgroup.Go panics without recovery crashing the program

## Common Error Messages

```
errgroup: concurrent map writes
```
```
context canceled
```
```
errgroup: limit exceeded
```
```
panic: runtime error: index out of range
```

## How to Fix It

### Solution 1: Handle errgroup errors and context cancellation

```go
g, ctx := errgroup.WithContext(ctx)
for _, item := range items {
    item := item
    g.Go(func() error {
        select {
        case <-ctx.Done():
            return ctx.Err()
        default:
        }
        return processItem(ctx, item)
    })
}
if err := g.Wait(); err != nil {
    log.Printf("processing failed: %v", err)
}
```

### Solution 2: Use SetLimit to control concurrency

```go
g, ctx := errgroup.WithContext(ctx)
g.SetLimit(10)
for _, url := range urls {
    url := url
    g.Go(func() error {
        return download(ctx, url)
    })
}
return g.Wait()
```

### Solution 3: Collect all errors instead of just the first

```go
var mu sync.Mutex
var errs []error
g, ctx := errgroup.WithContext(ctx)
g.SetLimit(5)
for _, item := range items {
    item := item
    g.Go(func() error {
        if err := processItem(ctx, item); err != nil {
            mu.Lock()
            errs = append(errs, err)
            mu.Unlock()
        }
        return nil
    })
}
_ = g.Wait()
```

### Solution 4: Add panic recovery to errgroup goroutines

```go
g.Go(func() (retErr error) {
    defer func() {
        if r := recover(); r != nil {
            retErr = fmt.Errorf("panic: %v", r)
        }
    }()
    return executeTask(ctx, task)
})
```

## Common Scenarios

- A data pipeline uses errgroup but goroutines ignore context after cancellation
- Thousands of tasks overwhelm the system because errgroup has no concurrency limit
- One failing task cancels context and all other tasks fail even though they could succeed independently

## Prevent It

- Always check ctx.Done() at the start of errgroup goroutines
- Set g.SetLimit() to control maximum concurrency
- Collect errors in a thread-safe manner when all errors are needed

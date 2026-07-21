---
title: "[Solution] Deprecated Function Migration: context.Background to context.WithCancel"
description: "Migrate from deprecated context.Background usage to proper context propagation."
deprecated_function: "context.Background()"
replacement_function: "context.WithCancel(ctx)"
languages: ["go"]
deprecated_since: "Go 1.7+"
---

# [Solution] Deprecated Function Migration: context.Background to context.WithCancel

The `context.Background()` has been deprecated in favor of `context.WithCancel(ctx)`.

## Migration Guide

Context should be propagated, not created fresh

Using context.Background() in request handlers loses cancellation support. Pass context from caller.

## Before (Deprecated)

```go
func handler() {
    // Lost context -- no cancellation
    result := fetchData(context.Background())
}
```

## After (Modern)

```go
func handler(ctx context.Context) {
    // Proper context propagation
    result := fetchData(ctx)

    // Or with timeout
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()
    result := fetchData(ctx)
}
```

## Key Differences

- Pass context from caller
- context.WithCancel for cancellation
- context.WithTimeout for timeouts
- context.WithValue for request-scoped data

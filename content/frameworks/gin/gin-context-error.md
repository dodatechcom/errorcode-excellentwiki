---
title: "[Solution] Gin Context Error — How to Fix"
description: "Fix Gin context errors. Resolve context handling, goroutine context passing, and request lifecycle issues."
frameworks: ["gin"]
error-types: ["context-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin context error occurs when the request context is used incorrectly, especially in goroutines or async operations.

## Why It Happens

Context errors happen when using gin.Context outside request scope, accessing context in goroutines after request ends, or missing context propagation.

## Common Error Messages

```
context canceled
```

```
context deadline exceeded
```

```
use of closed connection
```

```
http: superfluous response WriteHeader
```

## How to Fix It

### 1. Don't Store Context

Don't store gin.Context in structs.

```go
// Wrong
type MyService struct {
    ctx *gin.Context
}

// Right
func MyHandler(c *gin.Context) {
    ctx := c.Request.Context()
    result := doWork(ctx)
}
```

### 2. Pass Context to Goroutines

Use request context in goroutines.

```go
func handler(c *gin.Context) {
    ctx := c.Request.Context()
    go func() {
        result, err := doAsyncWork(ctx)
        if err != nil {
            log.Printf("error: %v", err)
        }
    }()
}
```

### 3. Check Context Cancellation

Handle context cancellation.

```go
func handler(c *gin.Context) {
    ctx := c.Request.Context()
    select {
    case <-ctx.Done():
        c.JSON(408, gin.H{"error": "request timeout"})
        return
    case result := <-doWork(ctx):
        c.JSON(200, gin.H{"data": result})
    }
}
```

### 4. Copy Context for Background Tasks

Clone context for long-running tasks.

```go
func handler(c *gin.Context) {
    taskCtx := context.Background()
    go processAsync(taskCtx)
}
```

## Common Scenarios

**Scenario 1: Goroutine uses expired context.**
Don't use gin.Context in goroutines.

**Scenario 2: Request times out unexpectedly.**
Check context deadlines.

## Prevent It

1. **Always use request context, not gin.Context, in goroutines.**


2. **Set appropriate timeouts.**


3. **Handle context cancellation gracefully.**



---
title: "[Solution] Go Context Error — How to Fix"
description: "Fix Go context errors. Handle context cancellation, timeouts, values, and propagation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Context Error

Fix Go context errors. Handle context cancellation, timeouts, values, and propagation.

## Why It Happens

- Context is not properly cancelled causing goroutine leaks
- Context values are accessed using wrong keys
- Context deadline is too short causing premature cancellation
- Background context is used instead of request context

## Common Error Messages

```
context: deadline exceeded
```
```
context: canceled
```
```
context: value not found
```
```
context: missing context in function signature
```

## How to Fix It

### Solution 1: Use context with cancellation

```go
ctx, cancel := context.WithCancel(parentCtx)
defer cancel()
go func() {
    select {
    case <-ctx.Done():
        return
    case <-time.After(time.Second):
        doWork(ctx)
    }
}()
```

### Solution 2: Use context with timeout

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
result, err := db.QueryContext(ctx, "SELECT ...")
```

### Solution 3: Pass context values correctly

```go
type contextKey string
const userKey contextKey = "user"
ctx = context.WithValue(ctx, userKey, &User{})
user := ctx.Value(userKey).(*User)
```

### Solution 4: Use request context in handlers

```go
func handler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    result, err := service.DoWork(ctx)
}
```

## Common Scenarios

- Goroutine leaks because context is not cancelled
- Context value retrieval returns nil because of wrong key type
- Function uses context.Background instead of the request context

## Prevent It

- Always cancel context with defer after WithCancel/WithTimeout
- Define context keys as unexported types to avoid collisions
- Pass request context to downstream calls

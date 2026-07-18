---
title: "[Solution] Go singleflight Error — How to Fix"
description: "Fix Go sync singleflight errors. Handle deduplication, shared result errors, timeout propagation, and goroutine leak issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go singleflight Error

Fix Go sync singleflight errors. Handle deduplication, shared result errors, timeout propagation, and goroutine leak issues.

## Why It Happens

- singleflight.Do returns an error shared by all callers hiding the original context
- Multiple goroutines waiting on the same key block indefinitely without timeout
- The function passed to singleflight.Do panics causing all waiting callers to fail
- Results from singleflight are cached incorrectly leading to stale data serving

## Common Error Messages

```
singleflight: <function> returned error
```
```
context deadline exceeded during singleflight.Do
```
```
singleflight: panic in flight function
```
```
singleflight: too many goroutines waiting on key
```

## How to Fix It

### Solution 1: Use singleflight with context support

```go
var group singleflight.Group
func GetUser(ctx context.Context, id string) (*User, error) {
    result, err, _ := group.Do("user:"+id, func() (interface{}, error) {
        return fetchUserFromDB(ctx, id)
    })
    if err != nil { return nil, err }
    return result.(*User), nil
}
```

### Solution 2: Handle panics in the flight function

```go
group.Do(key, func() (val interface{}, err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("panic in flight: %v", r)
        }
    }()
    return fn()
})
```

### Solution 3: Forget keys after errors to allow retries

```go
result, err, _ := group.Do(key, fn)
if err != nil {
    group.Forget(key)
    return nil, err
}
return result, nil
```

### Solution 4: Add TTL-based deduplication

```go
type TTLFlight struct {
    mu      sync.Mutex
    group   singleflight.Group
    results map[string]time.Time
    ttl     time.Duration
}
```

## Common Scenarios

- A cache stampede causes thousands of simultaneous DB queries for the same key
- A shared singleflight call fails and all waiters receive the same stale error
- An API deduplicates requests but a panic causes all waiters to fail

## Prevent It

- Use group.Do only for idempotent operations where sharing results is safe
- Call group.Forget(key) after errors to allow subsequent callers to retry
- Wrap the flight function with panic recovery to prevent cascading failures

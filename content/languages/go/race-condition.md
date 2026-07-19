---
title: "[Solution] Go race condition detected — Concurrency Error Fix"
description: "Fix Go race condition detected by -race."
languages: ["go"]
error-types: ["concurrency-error"]
severities: ["error"]
weight: 5
---

# race condition detected

Running with `-race` flag detects data races: concurrent unsynchronized access to shared data.

## How to Fix

### Fix 1: Use sync.Mutex

```go
type SafeCounter struct {
    mu sync.Mutex
    v  map[string]int
}

func (c *SafeCounter) Inc(key string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.v[key]++
}
```

### Fix 2: Use channels

```go
type command struct {
    op    string
    key   string
    reply chan int
}
```

## Related Errors

- [concurrent-map]({{< relref "/languages/go/concurrent-map" >}}) — concurrent map access.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — deadlock.

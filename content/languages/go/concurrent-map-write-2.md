---
title: "[Solution] Go Concurrent Map Writes — Runtime Error Fix"
description: "Fix Go concurrent map writes fatal error. Use sync.Mutex, sync.RWMutex, or sync.Map for safe concurrent map access."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Concurrent Map Writes — Runtime Error Fix

Concurrent map writes cause a fatal error. Go maps are not safe for concurrent use — multiple goroutines writing simultaneously triggers `fatal error: concurrent map writes`.

## Description

Go's map implementation is not thread-safe. When two or more goroutines write to the same map concurrently (or one writes while another reads), the runtime detects the data race and terminates the program. This is a fatal error, not a recoverable panic.

Common scenarios:

- **Shared cache map** — multiple HTTP handlers writing to a shared map.
- **Fan-out pattern** — multiple workers updating the same result map.
- **Read during write** — one goroutine reads while another writes.
- **Map in struct used across goroutines** — struct fields shared without locking.

## Common Causes

```go
// Cause 1: Multiple goroutines writing to shared map
func main() {
    m := make(map[int]int)
    for i := 0; i < 10; i++ {
        go func(n int) {
            m[n] = n * n // fatal: concurrent map writes
        }(i)
    }
    time.Sleep(time.Second)
}

// Cause 2: Read during write
func main() {
    m := make(map[string]int)
    go func() {
        for {
            _ = m["key"] // concurrent read
        }
    }()
    for {
        m["key"] = 1 // concurrent write — fatal
    }
}

// Cause 3: Shared map in HTTP handlers
var cache = make(map[string]string)

func handler(w http.ResponseWriter, r *http.Request) {
    cache[r.URL.Path] = r.Method // concurrent map write
}

// Cause 4: Map passed to goroutine without copy
func main() {
    m := map[string]int{"a": 1}
    go func(m map[string]int) {
        m["b"] = 2 // fatal if main also writes
    }(m)
}
```

## How to Fix

### Fix 1: Protect with sync.Mutex

```go
// Wrong
var cache = make(map[string]string)

// Correct
type SafeCache struct {
    mu    sync.Mutex
    items map[string]string
}

func (c *SafeCache) Set(key, val string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.items[key] = val
}

func (c *SafeCache) Get(key string) (string, bool) {
    c.mu.Lock()
    defer c.mu.Unlock()
    v, ok := c.items[key]
    return v, ok
}
```

### Fix 2: Use sync.RWMutex for read-heavy workloads

```go
type RWCache struct {
    mu    sync.RWMutex
    items map[string]string
}

func (c *RWCache) Get(key string) (string, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    v, ok := c.items[key]
    return v, ok
}

func (c *RWCache) Set(key, val string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.items[key] = val
}
```

### Fix 3: Use sync.Map for simple key-value cases

```go
var m sync.Map

m.Store("key", "value")
v, ok := m.Load("key")
if ok {
    fmt.Println(v)
}
```

### Fix 4: Partition the map by goroutine

```go
// Each goroutine writes to its own map, merge afterward
func merge(maps []map[string]int) map[string]int {
    result := make(map[string]int)
    for _, m := range maps {
        for k, v := range m {
            result[k] = v
        }
    }
    return result
}
```

## Examples

```go
// This triggers: fatal error: concurrent map writes
package main

import "time"

func main() {
    m := make(map[int]int)
    for i := 0; i < 100; i++ {
        go func(n int) {
            m[n] = n
        }(i)
    }
    time.Sleep(time.Second)
}
```

## Related Errors

- [map-not-init]({{< relref "/languages/go/map-not-init" >}}) — writing to a nil map.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.
- [sync-mutex]({{< relref "/languages/go/sync-mutex" >}}) — RWMutex used incorrectly.

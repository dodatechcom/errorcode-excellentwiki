---
title: "[Solution] Go Concurrent Map Writes — Runtime Error Fix"
description: "Fix Go concurrent map writes panic. Use sync.Map, sync.RWMutex, or channels to protect map access from multiple goroutines."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Concurrent Map Writes — Runtime Error Fix

A concurrent map writes panic occurs when multiple goroutines write to the same map simultaneously without synchronization.

## Description

Go maps are not safe for concurrent use. When two or more goroutines write to the same map — or one reads while another writes — the runtime detects the race and panics with `fatal error: concurrent map writes` or `concurrent map reads and map writes`.

Common scenarios:

- **Web handler writes shared map** — multiple HTTP requests write to a global map.
- **Goroutine fan-out writes** — multiple worker goroutines write results to one map.
- **Reading during write** — one goroutine reads while another writes, triggering the panic.

## Common Causes

```go
// Cause 1: Multiple goroutines writing to shared map
m := make(map[string]int)
for i := 0; i < 10; i++ {
    go func(n int) {
        m[fmt.Sprintf("key%d", n)] = n // fatal: concurrent map writes
    }(i)
}

// Cause 2: HTTP handler writing to global map
var cache = make(map[string]string)

func handler(w http.ResponseWriter, r *http.Request) {
    cache[r.URL.Path] = "data" // Race with other requests
}

// Cause 3: Read and write from different goroutines
m := make(map[string]int)
go func() {
    _ = m["key"] // Read
}()
go func() {
    m["key"] = 1 // Write — races with read
}()
```

## How to Fix

### Fix 1: Use sync.RWMutex to protect map access

```go
// Wrong
var m = make(map[string]int)

func Set(key string, val int) {
    m[key] = val
}

// Correct
var (
    m  = make(map[string]int)
    mu sync.RWMutex
)

func Set(key string, val int) {
    mu.Lock()
    defer mu.Unlock()
    m[key] = val
}

func Get(key string) (int, bool) {
    mu.RLock()
    defer mu.RUnlock()
    v, ok := m[key]
    return v, ok
}
```

### Fix 2: Use sync.Map for high-concurrency read-heavy workloads

```go
// Wrong
var m = make(map[string]int)

// Correct
var m sync.Map

func Set(key string, val int) {
    m.Store(key, val)
}

func Get(key string) (int, bool) {
    v, ok := m.Load(key)
    if !ok {
        return 0, false
    }
    return v.(int), true
}
```

### Fix 3: Use channels to serialize map access

```go
// Wrong — concurrent writes
m := make(map[string]int)
for i := 0; i < 10; i++ {
    go func(n int) {
        m[fmt.Sprintf("key%d", n)] = n
    }(i)
}

// Correct — single goroutine owns the map
m := make(map[string]int)
ch := make(chan func(), 100)

go func() {
    for fn := range ch {
        fn()
    }
}()

for i := 0; i < 10; i++ {
    n := i
    ch <- func() {
        m[fmt.Sprintf("key%d", n)] = n
    }
}
```

### Fix 4: Run with race detector to find data races

```bash
go run -race main.go
go build -race -o myapp
go test -race ./...
```

### Fix 5: Create a concurrent map wrapper

```go
type SafeMap struct {
    mu sync.RWMutex
    m  map[string]interface{}
}

func NewSafeMap() *SafeMap {
    return &SafeMap{m: make(map[string]interface{})}
}

func (s *SafeMap) Set(key string, val interface{}) {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.m[key] = val
}

func (s *SafeMap) Get(key string) (interface{}, bool) {
    s.mu.RLock()
    defer s.mu.RUnlock()
    v, ok := s.m[key]
    return v, ok
}
```

## Examples

```go
// This triggers: fatal error: concurrent map writes
package main

import "fmt"

func main() {
    m := make(map[int]int)
    for i := 0; i < 100; i++ {
        go func(n int) {
            m[n] = n * n
        }(i)
    }
    fmt.Scanln()
}
```

## Related Errors

- [channel-closed]({{< relref "/languages/go/channel-closed" >}}) — sending on a closed channel.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck due to blocked channel operations.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines asleep.

---
title: "[Solution] Go Concurrent Map Read and Map Write — Runtime Error Fix"
description: "Fix Go fatal error concurrent map read and map write. Use sync.Mutex or sync.Map for safe concurrent map access."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["concurrent", "map", "race-condition", "sync-mutex", "sync-map", "goroutine", "runtime"]
weight: 5
---

# Concurrent Map Read and Map Write — Runtime Error

The error `fatal error: concurrent map read and map write` (or `concurrent map writes`) occurs when multiple goroutines access a Go map simultaneously, with at least one goroutine performing a write. Go maps are not safe for concurrent use.

## Description

Go's built-in map type is not thread-safe. When one goroutine reads from a map while another writes to it, the runtime detects the race and crashes the program with a fatal error. Unlike a regular panic, a fatal error cannot be recovered with `recover()`.

This is a common issue when transitioning from single-threaded to concurrent code, or when sharing a map between HTTP handlers without synchronization.

## Common Causes

- **Unprotected map in goroutines** — sharing a map between goroutines without a mutex
- **Map in HTTP handler** — multiple requests writing to a shared map concurrently
- **Forgot to use sync.Map** — using a plain map where `sync.Map` is needed
- **Nested goroutine map access** — spawning goroutines that all read/write the same map

## How to Fix

### Fix 1: Use sync.Mutex to protect the map

```go
type SafeMap struct {
    mu sync.RWMutex
    m  map[string]int
}

func (sm *SafeMap) Get(key string) (int, bool) {
    sm.mu.RLock()
    defer sm.mu.RUnlock()
    v, ok := sm.m[key]
    return v, ok
}

func (sm *SafeMap) Set(key string, value int) {
    sm.mu.Lock()
    defer sm.mu.Unlock()
    sm.m[key] = value
}
```

### Fix 2: Use sync.Map for read-heavy workloads

```go
var m sync.Map

m.Store("key", "value")

if v, ok := m.Load("key"); ok {
    fmt.Println(v.(string))
}
```

### Fix 3: Use channels to serialize access

```go
type command struct {
    key   string
    value int
    reply chan int
}

func worker(cmds <-chan command) {
    m := make(map[string]int)
    for cmd := range cmds {
        m[cmd.key] = cmd.value
        cmd.reply <- m[cmd.key]
    }
}
```

### Fix 4: Use atomic operations for simple counters

```go
var counter sync.Map

// For simple counters, use atomic
counter.Store("hits", int64(0))

if v, ok := counter.Load("hits"); ok {
    counter.Store("hits", v.(int64)+1)
}
```

## Examples

```go
package main

import "fmt"

func main() {
    m := make(map[string]int)

    go func() {
        for i := 0; i < 100; i++ {
            m[fmt.Sprintf("key%d", i)] = i
        }
    }()

    for i := 0; i < 100; i++ {
        _ = m[fmt.Sprintf("key%d", i)]
    }
}
```

Output:
```
fatal error: concurrent map read and map write
```

## Related Errors

- [sync-mutex]({{< relref "/languages/go/sync-mutex" >}}) — mutex-related deadlocks and panics.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines that never terminate.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked, program cannot proceed.

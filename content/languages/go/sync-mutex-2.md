---
title: "[Solution] Go RWMutex Not Locked Error Fix"
description: "Fix Go sync RWMutex is not locked error. Use correct Lock/Unlock pairing, match RLock with RUnlock, and avoid double-unlocking."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sync", "mutex", "rwmutex", "lock", "concurrency", "runtime"]
weight: 5
---

# RWMutex Not Locked Error Fix

The `sync: RWMutex is not locked` error occurs when trying to unlock a mutex that isn't currently locked, or when calling `RUnlock` without a matching `RLock`.

## Description

Go's `sync.RWMutex` allows multiple concurrent readers OR a single writer. The runtime panics if you call `Unlock` on a mutex that isn't locked, or `RUnlock` without a corresponding `RLock`. This is a programming error that indicates incorrect synchronization logic.

Common scenarios:

- **Double unlock** — calling `Unlock` twice on the same mutex.
- **Mismatched Lock/Unlock** — one goroutine locks, another unlocks.
- **RLock/RUnlock mismatch** — calling `RUnlock` when no reader lock is held.
- **Unlock in wrong goroutine** — mutex locked in one goroutine, unlocked in another.

## Common Causes

```go
// Cause 1: Double unlock
func main() {
    var mu sync.RWMutex
    mu.Lock()
    mu.Unlock()
    mu.Unlock() // panic: sync: RWMutex is not locked
}

// Cause 2: RUnlock without RLock
func main() {
    var mu sync.RWMutex
    mu.RUnlock() // panic: sync: RWMutex is not locked
}

// Cause 3: Wrong goroutine unlocking
func main() {
    var mu sync.RWMutex
    mu.Lock()
    go func() {
        mu.Unlock() // panics — locked in main goroutine
    }()
}

// Cause 4: Conditional lock without matching unlock
func process(mu *sync.RWMutex, readOnly bool) {
    if readOnly {
        mu.RLock()
    }
    // If readOnly is false, RLock was not called
    // but RUnlock may still be called
    defer mu.RUnlock() // panic if not readOnly
}
```

## How to Fix

### Fix 1: Use defer for unlock

```go
func readData(mu *sync.RWMutex, data map[string]string) string {
    mu.RLock()
    defer mu.RUnlock() // always unlocks exactly once
    return data["key"]
}

func writeData(mu *sync.RWMutex, data map[string]string, key, val string) {
    mu.Lock()
    defer mu.Unlock() // always unlocks exactly once
    data[key] = val
}
```

### Fix 2: Match Lock with Unlock in same scope

```go
func process(mu *sync.RWMutex, data map[string]string) {
    mu.Lock()
    data["key"] = "value"
    mu.Unlock() // matches the Lock above
}
```

### Fix 3: Don't cross goroutine boundaries with locks

```go
// Wrong
func main() {
    var mu sync.Mutex
    mu.Lock()
    go func() {
        mu.Unlock() // wrong goroutine
    }()
}

// Correct
func main() {
    var mu sync.Mutex
    mu.Lock()
    // Unlock in same goroutine
    mu.Unlock()
}
```

### Fix 4: Track lock state explicitly

```go
type SafeMap struct {
    mu      sync.RWMutex
    items   map[string]string
    readLocked bool
}

func (m *SafeMap) Read(key string) string {
    m.mu.RLock()
    defer m.mu.RUnlock()
    return m.items[key]
}

func (m *SafeMap) Write(key, val string) {
    m.mu.Lock()
    defer m.mu.Unlock()
    m.items[key] = val
}
```

## Examples

```go
// This triggers: sync: RWMutex is not locked
package main

import "sync"

func main() {
    var mu sync.RWMutex
    mu.RUnlock() // no RLock was called
}
```

## Related Errors

- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked on locks/channels.
- [concurrent-map-write]({{< relref "/languages/go/concurrent-map-write" >}}) — concurrent map writes without locking.
- [channel-closed]({{< relref "/languages/go/channel-closed" >}}) — sending on closed channel.

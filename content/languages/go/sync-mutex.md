---
title: "[Solution] Go Sync RWMutex Not Locked Error Fix"
description: "Fix Go sync RWMutex is not locked error. Lock mutexes before accessing shared data, use defer for unlocking, and avoid double-unlock."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sync", "mutex", "rwmutex", "lock", "concurrency"]
weight: 5
---

# Sync: RWMutex Is Not Locked — Fix

A "sync: RWMutex is not locked" error occurs when you call `RUnlock()` on an `RWMutex` that isn't currently held for reading, or `Unlock()` on a mutex that isn't locked.

## Description

Go's `sync.RWMutex` enforces locking discipline. Calling `RUnlock()` when no read lock is held, or `Unlock()` when no write lock is held, causes a runtime panic. This is a safeguard against misusing the mutex.

Common scenarios:

- **Double unlock** — calling `Unlock()` twice on the same mutex.
- **Unlock without lock** — forgetting to acquire the lock before releasing.
- **Wrong mutex** — unlocking a different mutex than the one locked.
- **Deferred unlock in wrong scope** — defer runs after function returns, but lock was acquired in a different function.

## Common Causes

```go
// Cause 1: Double unlock
var mu sync.RWMutex
mu.Lock()
mu.Unlock()
mu.Unlock() // panic: sync: RWMutex is not locked

// Cause 2: Unlock without lock
var mu sync.RWMutex
mu.Unlock() // panic: sync: RWMutex is not locked

// Cause 3: RUnlock without RLock
var mu sync.RWMutex
mu.RUnlock() // panic: sync: RWMutex is not locked for reading

// Cause 4: Wrong mutex in struct
type Cache struct {
    mu   sync.RWMutex
    data map[string]string
}

func (c *Cache) Get(key string) string {
    c.mu.RLock()
    defer c.mu.RUnlock() // Correct
    return c.data[key]
}

func (c *Cache) Set(key, value string) {
    c.mu.Lock()
    c.mu.Unlock() // Correct
    c.mu.Unlock() // Double unlock — panic
}
```

## How to Fix

### Fix 1: Use defer to ensure unlock happens exactly once

```go
// Wrong — manual unlock may skip on error paths
var mu sync.RWMutex
mu.Lock()
if err := doWork(); err != nil {
    mu.Unlock()
    return err
}
doMore()
mu.Unlock()

// Correct — defer guarantees unlock
var mu sync.RWMutex
mu.Lock()
defer mu.Unlock()
if err := doWork(); err != nil {
    return err
}
doMore()
```

### Fix 2: Never unlock what you didn't lock

```go
// Wrong — different goroutine unlocks
var mu sync.RWMutex

go func() {
    mu.Lock()
}()

go func() {
    mu.Unlock() // May run before Lock — panic
}()

// Correct — same goroutine that locks should unlock
var mu sync.RWMutex
mu.Lock()
defer mu.Unlock()
```

### Fix 3: Check lock state before unlocking (for complex patterns)

```go
// Use atomic operations for lock state tracking
type SafeStruct struct {
    mu     sync.RWMutex
    locked atomic.Bool
}

func (s *SafeStruct) SafeUnlock() {
    if s.locked.CompareAndSwap(true, false) {
        s.mu.Unlock()
    }
}
```

### Fix 4: Use channels instead of mutexes when possible

```go
// Wrong — mutex complexity
var mu sync.RWMutex
var data map[string]string

func Set(key, value string) {
    mu.Lock()
    data[key] = value
    mu.Unlock()
}

// Correct — channel-based access (single goroutine owns data)
type Cache struct {
    data  map[string]string
    setCh chan setCmd
    getCh chan getCmd
}

type setCmd struct {
    key, value string
    done       chan struct{}
}

type getCmd struct {
    key   string
    result chan string
}
```

### Fix 5: Ensure lock and unlock are paired in all code paths

```go
// Wrong — missing unlock on error
func process(mu *sync.RWMutex, data map[string]string, key string) {
    mu.Lock()
    if key == "" {
        return // Lock not released
    }
    data[key] = "value"
    mu.Unlock()
}

// Correct — defer ensures unlock in all paths
func process(mu *sync.RWMutex, data map[string]string, key string) {
    mu.Lock()
    defer mu.Unlock()
    if key == "" {
        return
    }
    data[key] = "value"
}
```

## Examples

```go
// This triggers: panic: sync: RWMutex is not locked
package main

import "sync"

func main() {
    var mu sync.RWMutex
    mu.Lock()
    mu.Unlock()
    mu.Unlock() // Double unlock
}
```

## Related Errors

- [concurrent-map-write]({{< relref "/languages/go/concurrent-map-write" >}}) — concurrent writes to map without mutex.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked on locks.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck on mutex.

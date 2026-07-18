---
title: "[Solution] Go sync Error — How to Fix"
description: "Fix Go sync errors. Handle WaitGroup, Once, Map, and synchronization primitives."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go sync Error

Fix Go sync errors. Handle WaitGroup, Once, Map, and synchronization primitives.

## Why It Happens

- WaitGroup counter goes negative because of Add/Done mismatch
- sync.Once does not re-run after panic in the function
- sync.Map is used incorrectly causing unexpected behavior
- Mutex is not properly unlocked causing deadlocks

## Common Error Messages

```
sync: negative WaitGroup counter
```
```
sync: WaitGroup is reused before previous Wait has returned
```
```
sync: unlock of unlocked mutex
```
```
sync: RWMutex is locked for writing while reading
```

## How to Fix It

### Solution 1: Use WaitGroup correctly

```go
var wg sync.WaitGroup
for _, item := range items {
    wg.Add(1)
    go func(item Item) {
        defer wg.Done()
        process(item)
    }(item)
}
wg.Wait()
```

### Solution 2: Use sync.Once

```go
var once sync.Once
var instance *Database

func GetDB() *Database {
    once.Do(func() {
        instance = connectDB()
    })
    return instance
}
```

### Solution 3: Use sync.Map correctly

```go
var cache sync.Map
cache.Store("key", "value")
if v, ok := cache.Load("key"); ok {
    fmt.Println(v.(string))
}
cache.Delete("key")
```

### Solution 4: Use mutex for simple locking

```go
var mu sync.Mutex
var counter int
func increment() {
    mu.Lock()
    defer mu.Unlock()
    counter++
}
```

## Common Scenarios

- WaitGroup panics because Add is called after Wait
- sync.Once does not run the function again after it panics
- sync.Map is not the right choice for most use cases

## Prevent It

- Always call wg.Add before starting goroutines
- Handle panics inside sync.Once functions
- Prefer sync.Mutex or sync.RWMutex for most concurrent access patterns

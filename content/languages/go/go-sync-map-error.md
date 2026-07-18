---
title: "[Solution] Go sync.Map Error — How to Fix"
description: "Fix Go sync.Map errors. Handle concurrent access patterns, type assertions, range iteration, and stale value problems."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go sync.Map Error

Fix Go sync.Map errors. Handle concurrent access patterns, type assertions, range iteration, and stale value problems.

## Why It Happens

- Type assertions on sync.Map values fail because stored type does not match expected type
- sync.Map is used for a small number of keys where a mutex-protected map would be more efficient
- Values stored in sync.Map become stale and are never cleaned up leading to memory growth
- Range iteration over sync.Map misses concurrent writes happening during iteration

## Common Error Messages

```
interface conversion: interface {} is <type>, not <type>
```
```
panic: sync: negative WaitGroup counter
```
```
runtime error: invalid memory address or nil pointer dereference
```
```
sync: concurrent map read and map write
```

## How to Fix It

### Solution 1: Use type assertions with ok check

```go
var cache sync.Map
cache.Store("key", 42)
if val, ok := cache.Load("key"); ok {
    if num, ok := val.(int); ok {
        fmt.Println("value:", num)
    }
}
```

### Solution 2: Use LoadOrStore to prevent duplicates

```go
var userCache sync.Map
func GetOrCreateUser(id string) (*User, error) {
    val, loaded := userCache.LoadOrStore(id, &User{ID: id})
    user := val.(*User)
    if !loaded {
        if err := fetchUserFromDB(user); err != nil {
            userCache.Delete(id)
            return nil, err
        }
    }
    return user, nil
}
```

### Solution 3: Use a typed wrapper for type safety

```go
type TypedMap[K comparable, V any] struct{ m sync.Map }
func (t *TypedMap[K, V]) Load(key K) (V, bool) {
    val, ok := t.m.Load(key)
    if !ok { var zero V; return zero, false }
    return val.(V), true
}
```

### Solution 4: Clean up stale entries periodically

```go
func cleanup(m *sync.Map, maxAge time.Duration) {
    m.Range(func(key, value interface{}) bool {
        entry := value.(*CacheEntry)
        if time.Since(entry.LastAccess) > maxAge {
            m.Delete(key)
        }
        return true
    })
}
```

## Common Scenarios

- A web server caches sessions in sync.Map but nil values cause panic
- A metrics collector uses sync.Map but memory grows unbounded
- A concurrent cache uses sync.Map but performs worse than RWMutex

## Prevent It

- Always use comma-ok idiom when loading from sync.Map
- Use a typed wrapper to avoid manual type assertions
- Consider RWMutex for small maps instead of sync.Map

---
title: "[Solution] Swift Sendable Concurrency Access Warning Fix"
description: "Fix Swift Sendable protocol warnings when accessing shared mutable state across threads."
languages: ["swift"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sendable", "concurrency", "thread-safety", "actor", "swift"]
weight: 5
---

# Swift Sendable: Concurrent Access Warning Fix

A Swift Sendable error occurs when you access shared mutable state from multiple threads without proper synchronization.

## What This Error Means

The Sendable protocol marks types as safe to transfer across concurrency domains. Warnings/errors appear in Swift 6 strict concurrency mode when non-sendable types are shared unsafely.

## Common Causes

- Mutable class instances shared across threads
- Non-sendable closures passed to concurrent code
- Global variables accessed from multiple threads
- Missing Sendable conformance on value types

## How to Fix

### 1. Make value types Sendable

```swift
// CORRECT: Structs are implicitly Sendable
struct Message: Sendable {
    let id: Int
    let text: String
}
```

### 2. Use actors for mutable state

```swift
// WRONG: Shared mutable state
class Cache {
    var data: [String: Any] = [:]  // Unsafe
}

// CORRECT: Use actor
actor Cache {
    private var data: [String: Any] = [:]

    func get(_ key: String) -> Any? { data[key] }
    func set(_ key: String, _ value: Any) { data[key] = value }
}
```

### 3. Mark closures as @Sendable

```swift
// CORRECT: Explicit @Sendable closures
func process(_ handler: @escaping @Sendable (Result<Data, Error>) -> Void) {
    URLSession.shared.dataTask(with: url) { data, response, error in
        handler(.success(data ?? Data()))
    }.resume()
}
```

### 4. Use @unchecked Sendable carefully

```swift
// CORRECT: When you can guarantee thread safety
final class ThreadSafeCounter: @unchecked Sendable {
    private let lock = NSLock()
    private var _count = 0

    var count: Int {
        lock.lock()
        defer { lock.unlock() }
        return _count
    }

    func increment() {
        lock.lock()
        _count += 1
        lock.unlock()
    }
}
```

## Related Errors

- [Actor Isolation Error](actor-isolation-error-v2) — actor boundary issues
- [Swift Concurrency Error](swift-concurrency-error-v2) — general concurrency
- [Memory Access Error](memory-access-error) — EXC_BAD_ACCESS

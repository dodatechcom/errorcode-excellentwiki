---
title: "[Solution] Swift.Concurrency error: Actor-isolated function cannot be called"
description: "Fix Swift Concurrency actor isolation errors. Learn why actor-isolated functions cannot be called from synchronous contexts and how to properly use async/await with actors."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "swift"
tags: ["swift", "concurrency", "async-await", "actor-isolation"]
severity: "error"
---

# Swift.Concurrency error: Actor-isolated function cannot be called

## Error Message

```
Actor-isolated instance method 'updateData()' can not be referenced from a nonisolated context
```

## Common Causes

- Calling an actor-isolated synchronous function from a non-isolated context
- Accessing actor-isolated properties without using await
- Mixing old GCD dispatch patterns with actor-based concurrency
- Forgetting to make the calling context async when invoking actor methods

## Solutions

### Solution 1: Use await when calling actor-isolated methods

When you need to call a method on an actor from outside, mark the call site as async and use await.

```swift
actor NetworkManager {
    private var cache: [String: Data] = [:]

    func fetchData(from url: URL) async throws -> Data {
        if let cached = cache[url.absoluteString] {
            return cached
        }
        let (data, _) = try await URLSession.shared.data(from: url)
        cache[url.absoluteString] = data
        return data
    }
}

// Non-isolated caller
class AppController {
    private let manager = NetworkManager()

    func loadData() async {
        do {
            let data = try await manager.fetchData(from: myURL)
            print("Received \(data.count) bytes")
        } catch {
            print("Fetch failed: \(error)")
        }
    }
}
```

### Solution 2: Mark the calling context as @Sendable or nonisolated

If you need to call actor-isolated code from a context that cannot be async, use nonisolated or run it inside a Task.

```swift
actor Counter {
    var value = 0

    func increment() {
        value += 1
    }
}

struct CounterView: View {
    @State private var displayCount = 0
    let counter = Counter()

    var body: some View {
        Button("Increment") {
            Task {
                await counter.increment()
                displayCount = await counter.value
            }
        }
    }
}
```

### Solution 3: Use withCheckedContinuation for bridging callback-based APIs

When integrating callback-based APIs with actor-isolated code, use continuations to bridge the gap safely.

```swift
actor LocationService {
    func requestLocation() async -> CLLocation? {
        await withCheckedContinuation { continuation in
            let manager = CLLocationManager()
            manager.requestLocation()
            // Bridge callback to continuation
            // continuation.resume(returning: location)
        }
    }
}
```

## Prevention Tips

- Always use await when accessing actor-isolated properties or methods
- Use Task { } blocks to bridge synchronous code with actor-isolated async calls
- Avoid mixing DispatchQueue.global() with actor-isolated functions
- Use the @MainActor annotation when actor work must update the UI

## Related Errors

- [Swift actor isolation error]({{< relref "/languages/swift/swift-actor-error" >}})
- [Swift async sequence error]({{< relref "/languages/swift/swift-async-error" >}})
- [Combine error]({{< relref "/languages/swift/combine-error" >}})

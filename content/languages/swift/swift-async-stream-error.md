---
title: "[Solution] Swift AsyncStream Error — Continuation Misuse & Buffering"
description: "Fix Swift AsyncStream errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 100
---

When working with `AsyncStream`, continuation misuse or incorrect buffering policies can cause missed values, unexpected backpressure, or streams that never terminate.

## Common Causes

```swift
// Forgetting to finish the continuation
let stream = AsyncStream<String> { continuation in
    continuation.yield("hello")
    // Missing: continuation.finish()
}

// Using wrong buffering policy
let stream = AsyncStream<Int>(bufferingPolicy: .unbounded) { continuation in
    // Unbounded can consume excessive memory
}
```

## How to Fix

**1. Always finish the continuation**

```swift
let stream = AsyncStream<String> { continuation in
    continuation.yield("hello")
    continuation.yield("world")
    continuation.finish()
}

for await value in stream {
    print(value)
}
```

**2. Use appropriate buffering policy**

```swift
let stream = AsyncStream<Int>(bufferingPolicy: .bufferingNewest(1)) { continuation in
    for i in 0..<100 {
        continuation.yield(i)
    }
    continuation.finish()
}
```

**3. Use `AsyncStream.makeStream` (Swift 5.9+)**

```swift
let (stream, continuation) = AsyncStream<String>.makeStream()

Task {
    continuation.yield("hello")
    continuation.yield("world")
    continuation.finish()
}

for await value in stream {
    print(value)
}
```

**4. Yield values from background work**

```swift
let stream = AsyncStream<Data> { continuation in
    Task {
        for await data in networkStream {
            continuation.yield(data)
        }
        continuation.finish()
    }
}
```

**5. Handle onTermination**

```swift
let stream = AsyncStream<String> { continuation in
    continuation.onTermination = { _ in
        print("Stream terminated")
    }
    continuation.yield("value")
    continuation.finish()
}
```

## Examples

An `AsyncStream` with correct lifecycle management:
```swift
func numbers() -> AsyncStream<Int> {
    AsyncStream { continuation in
        Task {
            for i in 1...10 {
                continuation.yield(i)
                try await Task.sleep(for: .milliseconds(100))
            }
            continuation.finish()
        }
    }
}
```

## Related Errors

- [AsyncSequence Iteration Error](/languages/swift/swift-async-sequence-error)
- [Task Group Error](/languages/swift/swift-task-group-error)
- [Task Cancellation](/languages/swift/swift-task-cancellation)

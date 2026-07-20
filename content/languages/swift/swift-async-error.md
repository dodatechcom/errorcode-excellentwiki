---
title: "[Solution] Swift.AsyncSequence error: Invalid async sequence"
description: "Fix Swift AsyncSequence errors. Learn why async sequences fail and how to properly create, consume, and transform async sequences in Swift."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "swift"
tags: ["swift", "async-sequence", "concurrency", "iteration"]
severity: "error"
---

# Swift.AsyncSequence error: Invalid async sequence

## Error Message

```
Type 'AsyncStream<Int>' does not conform to protocol 'AsyncSequence'. Ensure the value conforms to AsyncSequence and that 'Element' is properly associated.
```

## Common Causes

- Using a non-async type where AsyncSequence is required
- Failing to properly type the Element associated type in a custom AsyncSequence
- Consuming an async sequence with a synchronous for-in loop instead of for await
- Creating an AsyncStream without a proper continuation-based build block

## Solutions

### Solution 1: Use for await to iterate over async sequences

Async sequences must be consumed using for await-in, not a regular for-in loop.

```swift
let numbers = AsyncStream<Int> { continuation in
    Task {
        for i in 1...10 {
            continuation.yield(i)
            try await Task.sleep(for: .milliseconds(100))
        }
        continuation.finish()
    }
}

func consumeNumbers() async {
    for await number in numbers {
        print("Got number: \(number)")
    }
    print("Sequence finished")
}
```

### Solution 2: Implement AsyncSequence correctly in custom types

When creating a custom async sequence, conform to the AsyncSequence protocol and implement the AsyncIterator protocol.

```swift
struct CountdownSequence: AsyncSequence {
    typealias Element = Int
    let start: Int

    func makeAsyncIterator() -> AsyncIterator {
        AsyncIterator(current: start)
    }

    struct AsyncIterator: AsyncIteratorProtocol {
        var current: Int

        mutating func next() async -> Int? {
            guard current > 0 else { return nil }
            let value = current
            current -= 1
            try await Task.sleep(for: .seconds(1))
            return value
        }
    }
}

func countdown() async {
    for await count in CountdownSequence(start: 5) {
        print("\(count)...")
    }
    print("Liftoff!")
}
```

### Solution 3: Transform async sequences with built-in operators

Use map, filter, and compactMap on AsyncSequence to build data pipelines just like with Combine.

```swift
func processLogs() async {
    let logLines = makeLogSource()
        .map { $0.trimmingCharacters(in: .whitespaces) }
        .filter { !$0.isEmpty }
        .prefix(100)

    for await line in logLines {
        print("Log: \(line)")
    }
}

func makeLogSource() -> AsyncStream<String> {
    AsyncStream { continuation in
        Task {
            for i in 1...200 {
                continuation.yield("Line \(i): sample log entry")
            }
            continuation.finish()
        }
    }
}
```

## Prevention Tips

- Always use for await-in to consume AsyncSequence, never plain for-in
- Implement both makeAsyncIterator and AsyncIteratorProtocol for custom sequences
- Use Task.sleep to simulate delays in async sequences for testing
- Apply map and filter operators to build reusable async data pipelines

## Related Errors

- [Swift concurrency error]({{< relref "/languages/swift/swift-concurrency-error" >}})
- [Swift actor isolation error]({{< relref "/languages/swift/swift-actor-error" >}})
- [Combine error]({{< relref "/languages/swift/combine-error" >}})

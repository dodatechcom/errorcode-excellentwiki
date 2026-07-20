---
title: "[Solution] Swift AsyncSequence Error — Iteration & next() Throws"
description: "Fix Swift AsyncSequence iteration errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 101
---

`AsyncSequence` iteration via `for await` can throw, fail silently, or produce unexpected results when the underlying sequence terminates abnormally or throws unhandled errors.

## Common Causes

```swift
// Unhandled throws in for-await loop
for await value in someAsyncSequence {
    // If the sequence throws, this crashes without try
}

// Not consuming all values before termination
let task = Task {
    for await value in stream {
        process(value)
    }
}
// Task cancelled before all values consumed
```

## How to Fix

**1. Always use try with for-await when the sequence throws**

```swift
do {
    for try await value in throwingSequence {
        print(value)
    }
} catch {
    print("Sequence failed: \(error)")
}
```

**2. Wrap iteration in a Task for proper lifecycle**

```swift
let task = Task {
    do {
        for try await value in networkStream {
            await processValue(value)
        }
    } catch is CancellationError {
        print("Iteration cancelled")
    } catch {
        print("Unexpected error: \(error)")
    }
}
```

**3. Use `prefix` or `first` to limit consumption**

```swift
let firstFive = stream.prefix(5)
for await value in firstFive {
    print(value)
}
```

**4. Implement custom AsyncSequence correctly**

```swift
struct Counter: AsyncSequence {
    typealias Element = Int
    let count: Int

    func makeAsyncIterator() -> AsyncIterator {
        AsyncIterator(count: count)
    }

    struct AsyncIterator: AsyncIteratorProtocol {
        var current = 0
        let count: Int

        mutating func next() async -> Int? {
            guard current < count else { return nil }
            current += 1
            return current
        }
    }
}
```

**5. Handle termination with onTermination**

```swift
for await value in stream {
    print(value)
}
print("Sequence completed")
```

## Examples

Chaining multiple async sequences:
```swift
let results = numbers()
    .filter { $0 % 2 == 0 }
    .map { $0 * 2 }

for try await result in results {
    print(result)
}
```

## Related Errors

- [AsyncStream Error](/languages/swift/swift-async-stream-error)
- [Task Cancellation](/languages/swift/swift-task-cancellation)
- [Task Group Error](/languages/swift/swift-task-group-error)

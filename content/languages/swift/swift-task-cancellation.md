---
title: "[Solution] Swift Task Cancellation — isCancelled & checkCancellation"
description: "Fix Swift task cancellation errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 103
---

Task cancellation errors occur when tasks don't properly check `Task.isCancelled`, fail to use `checkCancellation()`, or don't respond to cancellation signals.

## Common Causes

```swift
// Not checking cancellation
Task {
    while true {
        processData() // Never checks if cancelled
    }
}

// Throwing from cancellation without proper handling
try await Task.sleep(for: .seconds(5))
// Throws CancellationError but caller doesn't catch it
```

## How to Fix

**1. Check Task.isCancelled periodically**

```swift
Task {
    while !Task.isCancelled {
        await processNextItem()
    }
    await cleanup()
}
```

**2. Use checkCancellation for immediate abort**

```swift
Task {
    try await Task.checkCancellation()
    let data = try await fetchData()
    try await Task.checkCancellation()
    try await processData(data)
}
```

**3. Handle CancellationError in callers**

```swift
do {
    try await performLongTask()
} catch is CancellationError {
    print("Task was cancelled, cleaning up")
} catch {
    print("Other error: \(error)")
}
```

**4. Add cancellation handlers**

```swift
let task = Task {
    await withTaskCancellationHandler {
        try await performWork()
    } onCancel: {
        print("Cancellation requested")
    }
}
```

**5. Cooperate with cancellation in async sequences**

```swift
func processItems() async throws {
    for try await item in stream {
        try Task.checkCancellation()
        await process(item)
    }
}
```

## Examples

Cancellation-aware background processor:
```swift
actor BackgroundProcessor {
    func process(_ items: [Item]) async {
        for item in items {
            guard !Task.isCancelled else { return }
            await processItem(item)
        }
    }
}
```

## Related Errors

- [AsyncStream Error](/languages/swift/swift-async-stream-error)
- [Task Group Error](/languages/swift/swift-task-group-error)
- [MainActor Error](/languages/swift/swift-mainactor-error)

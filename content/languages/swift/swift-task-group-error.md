---
title: "[Solution] Swift TaskGroup Error — Child Task Failure & Management"
description: "Fix Swift TaskGroup errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 102
---

`TaskGroup` errors occur when child tasks throw, `addTask` is misused, or `cancelAll` doesn't properly propagate cancellation to child tasks.

## Common Causes

```swift
// Not handling child task errors
await withTaskGroup(of: String.self) { group in
    group.addTask { throw MyError() }
    for await value in group {
        // Unhandled error from child
    }
}

// Calling cancelAll without awaiting results
group.cancelAll()
// Child tasks may not have cleaned up
```

## How to Fix

**1. Handle errors in the group iteration**

```swift
await withTaskGroup(of: String.self) { group in
    group.addTask { throw MyError() }
    for await result in group {
        switch result {
        case .success(let value):
            print(value)
        case .failure(let error):
            print("Child failed: \(error)")
        }
    }
}
```

**2. Use throwingTaskGroup for error propagation**

```swift
do {
    try await withThrowingTaskGroup(of: String.self) { group in
        group.addTask { "result" }
        for try await value in group {
            print(value)
        }
    }
} catch {
    print("Group failed: \(error)")
}
```

**3. Cancel and wait for cleanup**

```swift
await withTaskGroup(of: Void.self) { group in
    group.addTask {
        try await Task.sleep(for: .seconds(10))
    }
    group.cancelAll()
    await group.waitForAll()
}
```

**4. Set result type for error handling**

```swift
await withTaskGroup(of: Result<String, Error>.self) { group in
    group.addTask {
        do {
            let result = try await fetchData()
            return .success(result)
        } catch {
            return .failure(error)
        }
    }
    for await result in group {
        // Handle each result
    }
}
```

**5. Limit concurrent tasks**

```swift
await withTaskGroup(of: Data.self) { group in
    for url in urls {
        group.addTask {
            let (data, _) = try await URLSession.shared.data(from: url)
            return data
        }
        if group.taskCount > 5 {
            await group.next()
        }
    }
}
```

## Examples

Parallel URL fetching with error handling:
```swift
func fetchAll(_ urls: [URL]) async throws -> [Data] {
    try await withThrowingTaskGroup(of: Data.self) { group in
        for url in urls {
            group.addTask {
                let (data, _) = try await URLSession.shared.data(from: url)
                return data
            }
        }
        var results: [Data] = []
        for try await data in group {
            results.append(data)
        }
        return results
    }
}
```

## Related Errors

- [Task Cancellation](/languages/swift/swift-task-cancellation)
- [AsyncStream Error](/languages/swift/swift-async-stream-error)
- [MainActor Error](/languages/swift/swift-mainactor-error)

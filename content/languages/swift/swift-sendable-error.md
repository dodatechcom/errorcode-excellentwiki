---
title: "[Solution] Swift Sendable Error — Closure Capture & Conformance"
description: "Fix Swift @Sendable function errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 107
---

`@Sendable` errors occur when closures capture non-Sendable types, cross isolation boundaries incorrectly, or fail to conform to `Sendable`.

## Common Causes

```swift
// Capturing non-Sendable in @Sendable closure
class MutableState { var value = 0 }

Task { @Sendable in
    let state = MutableState() // Error: non-Sendable capture
}

// Missing Sendable conformance
struct MyData {
    let items: [String]
    // Error: struct with non-Sendable stored properties
}
```

## How to Fix

**1. Mark classes Sendable or use actors**

```swift
final class MutableState: @unchecked Sendable {
    var value = 0
    private let lock = NSLock()
    
    func increment() {
        lock.lock()
        defer { lock.unlock() }
        value += 1
    }
}
```

**2. Use Sendable structs**

```swift
struct UserData: Sendable {
    let id: UUID
    let name: String
    let email: String
}
```

**3. Use @Sendable for closures crossing boundaries**

```swift
let handler: @Sendable (Result<Data, Error>) -> Void = { result in
    // This closure may be called from any context
}
```

**4. Avoid capturing mutable state**

```swift
Task {
    let value = await computeValue() // Capture immutable
    await MainActor.run {
        label.text = value
    }
}
```

**5. Use nonisolated for Sendable conformance**

```swift
actor MyActor: Sendable {
    func process() async -> String {
        "result"
    }
}
```

## Examples

Proper Sendable usage:
```swift
struct Message: Sendable {
    let content: String
    let timestamp: Date
}

Task { @Sendable in
    let message = Message(content: "Hello", timestamp: .now)
    await send(message)
}
```

## Related Errors

- [MainActor Error](/languages/swift/swift-mainactor-error)
- [Nonisolated Error](/languages/swift/swift-nonisolated-error)
- [Task Cancellation](/languages/swift/swift-task-cancellation)

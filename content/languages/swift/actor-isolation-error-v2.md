---
title: "[Solution] Swift Actor Isolation: Non-Sendable Type Error Fix"
description: "Fix Swift actor isolation errors when passing non-sendable types across actor boundaries."
languages: ["swift"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["actor", "isolation", "sendable", "concurrency", "swift"]
weight: 5
---

# Swift Actor Isolation: Non-Sendable Type Error Fix

A Swift actor isolation error occurs when you pass a non-sendable type across actor isolation boundaries.

## What This Error Means

Actors protect shared mutable state by serializing access. When crossing actor boundaries, only Sendable types can be safely passed. Non-sendable types (classes, closures) trigger warnings or errors in Swift 6 strict concurrency mode.

## Common Causes

- Passing class instances between actors
- Capturing non-sendable values in actor-isolated closures
- Using non-sendable types in async actor methods
- Mixing @MainActor and global actor isolation

## How to Fix

### 1. Use structs for actor messages

```swift
// WRONG: Passing class across actor boundary
class UserData { var name: String = "" }
actor AccountActor {
    func update(_ data: UserData) { }  // Warning
}

// CORRECT: Use Sendable struct
struct UserData: Sendable {
    let name: String
}
actor AccountActor {
    func update(_ data: UserData) { }  // Safe
}
```

### 2. Mark types as @unchecked Sendable

```swift
// CORRECT: When class must cross boundaries
class ThreadPool: @unchecked Sendable {
    func execute(_ work: @escaping @Sendable () -> Void) { }
}
```

### 3. Isolate to specific actors

```swift
// CORRECT: Use @MainActor for UI types
@MainActor
class ViewController: UIViewController {
    func updateUI() { }
}

// Non-isolated method can call MainActor
func refresh() async {
    await MainActor.run {
        viewController.updateUI()
    }
}
```

### 4. Use actor methods for state access

```swift
// CORRECT: Access state through actor methods
actor Counter {
    private var count = 0

    func increment() -> Int {
        count += 1
        return count
    }
}
```

## Related Errors

- [Sendable Error](sendable-error-v2) — Sendable protocol issues
- [Swift Concurrency Error](swift-concurrency-error-v2) — general concurrency
- [SwiftUI State Error](swiftui-state-error-v2) — UI state issues

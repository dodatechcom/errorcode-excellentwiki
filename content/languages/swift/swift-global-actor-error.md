---
title: "[Solution] Swift GlobalActor Error — Custom Actor Isolation"
description: "Fix Swift custom global actor errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 105
---

Custom global actor errors occur when `@GlobalActor` is misused, actor inference fails, or isolation boundaries are crossed incorrectly.

## Common Causes

```swift
// Incorrect global actor definition
@globalActor
struct MyActor {
    static let shared = MyActor()
}

// Missing actor isolation on properties
actor MyService {
    func process() {
        // Accessing non-isolated state from isolated context
    }
}
```

## How to Fix

**1. Define a proper custom global actor**

```swift
@globalActor
struct DatabaseActor {
    static let shared = DatabaseActor()
    private init() {}
}

@DatabaseActor
class DatabaseManager {
    var connection: DatabaseConnection?
    func connect() async throws {
        connection = try await DatabaseConnection.open()
    }
}
```

**2. Use nonisolated for shared access**

```swift
actor Counter {
    private var count = 0
    
    nonisolated var description: String {
        "Counter"
    }
    
    func increment() {
        count += 1
    }
}
```

**3. Isolate with the correct actor**

```swift
@DatabaseActor
func performDatabaseWork() async throws {
    try await dbManager.save(context)
}

@MainActor
func updateUI() async throws {
    let result = try await performDatabaseWork()
    view.update(with: result)
}
```

**4. Sendable conformance across actors**

```swift
struct UserData: Sendable {
    let id: UUID
    let name: String
}

@MyActor
class DataManager {
    func process(_ data: UserData) async {
        // Safe to cross boundaries
    }
}
```

**5. Proper actor reentrancy handling**

```swift
actor Processor {
    func process() async {
        let value = await compute()
        // Check state hasn't changed due to reentrancy
        updateState(value)
    }
}
```

## Examples

Custom global actor for networking:
```swift
@globalActor
struct NetworkActor {
    static let shared = NetworkActor()
}

@NetworkActor
class APIClient {
    private let session = URLSession.shared
    
    func fetch<T: Decodable>(_ url: URL) async throws -> T {
        let (data, _) = try await session.data(from: url)
        return try JSONDecoder().decode(T.self, from: data)
    }
}
```

## Related Errors

- [MainActor Error](/languages/swift/swift-mainactor-error)
- [Nonisolated Error](/languages/swift/swift-nonisolated-error)
- [Sendable Error](/languages/swift/swift-sendable-error)

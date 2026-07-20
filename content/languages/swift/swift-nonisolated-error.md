---
title: "[Solution] Swift nonisolated Error — Accessing Isolated State"
description: "Fix Swift nonisolated function errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 106
---

`nonisolated` function errors occur when non-isolated code tries to access actor-isolated state, or when `nonisolated` is used incorrectly on actors.

## Common Causes

```swift
actor MyActor {
    var data: [String] = []
    
    // Error: Cannot access isolated property
    nonisolated func getData() -> [String] {
        return data // Compile error
    }
}
```

## How to Fix

**1. Return Sendable values from nonisolated**

```swift
actor MyActor {
    var data: [String] = []
    
    nonisolated func count() -> Int {
        // Only for computed properties that don't need state
        return 0
    }
    
    func getData() -> [String] {
        return data
    }
}
```

**2. Use await to call actor methods from nonisolated**

```swift
func processActor(_ actor: MyActor) async {
    let data = await actor.getData() // Properly awaits
    print(data)
}
```

**3. Nonisolated for protocol conformances**

```swift
protocol Identifiable {
    var id: String { get }
}

actor MyModel: Identifiable {
    nonisolated let id: String
    
    init(id: String) {
        self.id = id
    }
}
```

**4. Sendable parameters for cross-isolation calls**

```swift
actor Processor {
    func process(_ input: String) async -> String {
        return input.uppercased()
    }
}

nonisolated func sendWork(to processor: Processor, input: String) async {
    let result = await processor.process(input)
    print(result)
}
```

**5. Use nonisolated(unsafe) for safe properties**

```swift
actor MyActor {
    nonisolated(unsafe) static let shared = MyActor()
    var data: Int = 0
}
```

## Examples

Proper actor isolation pattern:
```swift
actor DataStore {
    private var items: [Item] = []
    
    nonisolated var isEmpty: Bool {
        // This won't compile - needs async version
        return false
    }
    
    var isEmptyAsync: Bool {
        items.isEmpty
    }
    
    func count() -> Int {
        items.count
    }
}
```

## Related Errors

- [MainActor Error](/languages/swift/swift-mainactor-error)
- [Global Actor Error](/languages/swift/swift-global-actor-error)
- [Sendable Error](/languages/swift/swift-sendable-error)

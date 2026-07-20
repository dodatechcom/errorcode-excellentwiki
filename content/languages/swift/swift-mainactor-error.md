---
title: "[Solution] Swift MainActor Error — Global Actor Isolation Failure"
description: "Fix Swift MainActor isolation errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 104
---

`@MainActor` inference failures occur when UI updates happen off the main thread, or when crossing actor boundaries without proper isolation.

## Common Causes

```swift
// Updating UI from background context
Task {
    let data = try await fetchData()
    label.text = data.title // Error: mutation from non-main actor
}

// Missing @MainActor annotation
class ViewModel {
    func updateUI() {
        // Called from background, accesses @MainActor properties
    }
}
```

## How to Fix

**1. Annotate UI classes with @MainActor**

```swift
@MainActor
class ViewModel: ObservableObject {
    @Published var title = ""
    func update() async {
        title = await fetchData().title // Safe
    }
}
```

**2. Use MainActor.run for off-context updates**

```swift
Task {
    let data = try await fetchData()
    await MainActor.run {
        label.text = data.title
    }
}
```

**3. Annotate specific methods with @MainActor**

```swift
class Controller {
    @MainActor
    func updateUI(with data: Model) {
        view.configure(with: data)
    }
}
```

**4. Use @Sendable for closures crossing boundaries**

```swift
Task { @Sendable in
    let result = await backgroundWork()
    await MainActor.run {
        updateView(with: result)
    }
}
```

**5. MainActor-isolated property access**

```swift
@MainActor
var currentUIState: UIState = .idle

func handleUpdate() async {
    let newState = await computeNewState()
    await MainActor.run {
        currentUIState = newState
    }
}
```

## Examples

Proper MainActor usage in SwiftUI:
```swift
@MainActor
class AppViewModel: ObservableObject {
    @Published var items: [Item] = []
    
    func load() async {
        items = try await APIClient.fetchItems()
    }
}
```

## Related Errors

- [Global Actor Error](/languages/swift/swift-global-actor-error)
- [Nonisolated Error](/languages/swift/swift-nonisolated-error)
- [Sendable Error](/languages/swift/swift-sendable-error)

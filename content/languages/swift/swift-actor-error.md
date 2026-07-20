---
title: "[Solution] Swift.Actor isolation error: Cannot access actor-isolated property"
description: "Fix Swift Actor isolation property access errors. Learn why accessing actor-isolated properties fails from non-isolated contexts and how to use await and nonisolated correctly."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "swift"
tags: ["swift", "actor", "isolation", "concurrency"]
severity: "error"
---

# Swift.Actor isolation error: Cannot access actor-isolated property

## Error Message

```
Actor-isolated property 'userCount' can not be referenced from a nonisolated context
```

## Common Causes

- Accessing an actor-isolated stored property from outside the actor without await
- Trying to read actor state in a computed property that is not marked nonisolated
- Using a class-level delegate callback to access actor-isolated data
- Accessing actor-isolated properties in synchronous SwiftUI view bodies without async context

## Solutions

### Solution 1: Use await to access actor-isolated properties

When you must read an actor-isolated property from outside, use await in an async context.

```swift
actor UserStore {
    var users: [String: UserProfile] = [:]
    var userCount: Int { users.count }

    func addUser(_ profile: UserProfile) {
        users[profile.id] = profile
    }
}

class AppViewModel: ObservableObject {
    private let store = UserStore()

    func refreshCount() async {
        let count = await store.userCount
        print("Total users: \(count)")
    }

    func addUser(name: String) async {
        let profile = UserProfile(id: UUID().uuidString, name: name)
        await store.addUser(profile)
    }
}
```

### Solution 2: Expose actor state through nonisolated async methods

Create nonisolated methods that return copies of actor state so callers do not need direct property access.

```swift
actor Inventory {
    private var stock: [String: Int] = [:]

    func updateStock(item: String, quantity: Int) {
        stock[item, default: 0] += quantity
    }

    nonisolated func snapshot() async -> [String: Int] {
        await stock
    }
}

func checkInventory() async {
    let inventory = Inventory()
    let snapshot = await inventory.snapshot()
    for (item, qty) in snapshot {
        print("\(item): \(qty) in stock")
    }
}
```

### Solution 3: Use MainActor to bridge actor state to SwiftUI views

Annotate your view model with @MainActor and use Task to fetch actor state, keeping UI updates safe.

```swift
@MainActor
class DashboardViewModel: ObservableObject {
    @Published var notifications: [String] = []
    private let notificationActor = NotificationActor()

    func loadNotifications() async {
        let items = await notificationActor.fetchAll()
        notifications = items
    }
}

actor NotificationActor {
    func fetchAll() -> [String] {
        ["New message", "Update available", "System alert"]
    }
}

struct DashboardView: View {
    @StateObject private var viewModel = DashboardViewModel()

    var body: some View {
        List(viewModel.notifications, id: \.self) { text in
            Text(text)
        }
        .task {
            await viewModel.loadNotifications()
        }
    }
}
```

## Prevention Tips

- Always use await when accessing properties from outside an actor
- Use nonisolated for methods that do not need actor-isolated state
- Keep actor state private and expose it through safe async accessors
- Use @MainActor on view models that bridge actor state to SwiftUI

## Related Errors

- [Swift concurrency error]({{< relref "/languages/swift/swift-concurrency-error" >}})
- [Swift async sequence error]({{< relref "/languages/swift/swift-async-error" >}})
- [Combine error]({{< relref "/languages/swift/combine-error" >}})

---
title: "[Solution] SwiftUI.NavigationPath: Invalid navigation path"
description: "Fix SwiftUI NavigationPath invalid path errors. Learn why programmatic navigation fails and how to correctly use NavigationPath with NavigationStack."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "swift"
tags: ["swift", "swiftui", "navigation", "navigationpath"]
severity: "error"
---

# SwiftUI.NavigationPath: Invalid navigation path

## Error Message

```
NavigationPath: Attempted to append a value of type 'DetailView' which is notodable to any known hashable type. Ensure that all values appended to NavigationPath conform to Hashable.
```

## Common Causes

- Appending a type that does not conform to Hashable to NavigationPath
- Calling navigationDestination without a matching type for the appended value
- Forgetting to bind the NavigationPath to NavigationStack(path:)

## Solutions

### Solution 1: Make appended values conform to Hashable

Every value you append to a NavigationPath must conform to both Codable and Hashable so the navigation stack can track destinations.

```swift
struct Item: Hashable, Codable {
    let id: UUID
    let name: String
}

struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List {
                Button("Go to Item") {
                    let item = Item(id: UUID(), name: "Sample")
                    path.append(item)
                }
            }
            .navigationDestination(for: Item.self) { item in
                ItemDetailView(item: item)
            }
        }
    }
}
```

### Solution 2: Bind path to NavigationStack and register all destinations

Pass the path binding to NavigationStack(path:) and register navigationDestination for every type you might append.

```swift
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            HomeView()
                .navigationDestination(for: Route.self) { route in
                    switch route {
                    case .settings:
                        SettingsView()
                    case .profile(let userId):
                        ProfileView(userId: userId)
                    }
                }
        }
    }
}

enum Route: Hashable {
    case settings
    case profile(String)
}
```

### Solution 3: Use Codable serialization for persistence

NavigationPath supports Codable so you can save and restore navigation state across app launches.

```swift
class NavigationState: ObservableObject {
    @Published var path = NavigationPath()

    func save() -> Data? {
        try? path.codable.encode()
    }

    func restore(from data: Data) {
        if let codable = try? NavigationPath.CodableRepresentation(from: data) {
            path = NavigationPath(codable)
        }
    }
}

struct AppView: View {
    @StateObject private var navState = NavigationState()

    var body: some View {
        NavigationStack(path: $navState.path) {
            HomeView()
        }
    }
}
```

## Prevention Tips

- Always use Hashable types when appending to NavigationPath
- Register navigationDestination for every Hashable type you append
- Use Codable enums to represent complex navigation routes
- Test programmatic navigation on actual devices, not just previews

## Related Errors

- [SwiftUI state error]({{< relref "/languages/swift/swiftui-state-error" >}})
- [SwiftUI list error]({{< relref "/languages/swift/swiftui-list-error" >}})
- [Combine error]({{< relref "/languages/swift/combine-error" >}})

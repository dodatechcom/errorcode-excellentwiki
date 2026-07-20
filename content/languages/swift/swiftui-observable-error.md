---
title: "[Solution] SwiftUI @Observable Error — Property Observation (iOS 17+)"
description: "Fix SwiftUI @Observable errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 114
---

`@Observable` errors occur when properties aren't properly observed, `@Bindable` is misused, or observation tracking fails to detect changes.

## Common Causes

```swift
// Missing @Observable macro
class ViewModel {
    var items: [Item] = [] // Not observed
}

// Using @Bindable incorrectly
@Observable
class ViewModel {
    var name = ""
}

struct ContentView: View {
    @Bindable var viewModel: ViewModel // Should be @State or @StateObject
}
```

## How to Fix

**1. Use @Observable macro (iOS 17+)**

```swift
@Observable
class ViewModel {
    var items: [Item] = []
    var isLoading = false
    
    func load() async {
        isLoading = true
        items = try await APIClient.fetchItems()
        isLoading = false
    }
}
```

**2. Use @Bindable for two-way binding**

```swift
@Observable
class Settings {
    var volume = 50
    var brightness = 100
}

struct SettingsView: View {
    @Bindable var settings: Settings
    
    var body: some View {
        Form {
            Slider(value: $settings.volume, in: 0...100)
            Slider(value: $settings.brightness, in: 0...100)
        }
    }
}
```

**3. Use @State for view-owned objects**

```swift
struct ContentView: View {
    @State private var viewModel = ViewModel()
    
    var body: some View {
        List(viewModel.items) { item in
            Text(item.name)
        }
    }
}
```

**4. WithEnvironment for environment injection**

```swift
@Observable
class AppModel {
    var user: User?
}

struct ParentView: View {
    @State var appModel = AppModel()
    
    var body: some View {
        ChildView()
            .environment(appModel)
    }
}

struct ChildView: View {
    @Environment(AppModel.self) var appModel
}
```

**5. Observation tracking with withObservationTracking**

```swift
withObservationTracking {
    let _ = viewModel.items
} onChange: {
    print("Items changed")
}
```

## Examples

Complete @Observable pattern:
```swift
@Observable
class ShoppingCart {
    var items: [CartItem] = []
    
    var total: Double {
        items.reduce(0) { $0 + $1.price }
    }
    
    func add(_ item: Product) {
        items.append(CartItem(product: item))
    }
    
    func remove(at offsets: IndexSet) {
        items.remove(atOffsets: offsets)
    }
}
```

## Related Errors

- [Environment Error](/languages/swift/swiftui-environment-error)
- [Binding Error](/languages/swift/swiftui-binding-error)
- [Dependency Error](/languages/swift/swiftui-dependency-error)

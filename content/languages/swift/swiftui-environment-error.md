---
title: "[Solution] SwiftUI Environment Error — @Environment & EnvironmentObject"
description: "Fix SwiftUI environment errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 110
---

SwiftUI environment errors occur when `@EnvironmentObject` isn't provided, `@Environment` values are missing, or environment values aren't propagated correctly.

## Common Causes

```swift
// EnvironmentObject not provided
class ViewModel: ObservableObject {
    @Published var items: [Item] = []
}

struct ChildView: View {
    @EnvironmentObject var viewModel: ViewModel // Crashes if not injected
}

// Environment value not found
@Environment(\.colorScheme) var colorScheme
```

## How to Fix

**1. Provide EnvironmentObject in parent**

```swift
@main
struct MyApp: App {
    @StateObject var viewModel = ViewModel()
    
    var body: some Scene {
        WindowGroup {
            ChildView()
                .environmentObject(viewModel)
        }
    }
}
```

**2. Use default values for environment**

```swift
@Environment(\.colorScheme) var colorScheme

var body: some View {
    Text("Hello")
        .foregroundStyle(colorScheme == .dark ? .white : .black)
}
```

**3. Create custom environment key**

```swift
struct IsLoggedInKey: EnvironmentKey {
    static let defaultValue = false
}

extension EnvironmentValues {
    var isLoggedIn: Bool {
        get { self[IsLoggedInKey.self] }
        set { self[IsLoggedInKey.self] = newValue }
    }
}

// Usage
@Environment(\.isLoggedIn) var isLoggedIn
```

**4. Override environment values**

```swift
var body: some View {
    ChildView()
        .environment(\.colorScheme, .dark)
        .environment(\.locale, Locale(identifier: "fr"))
}
```

**5. Use @ObservedObject for view-scoped objects**

```swift
struct ChildView: View {
    @ObservedObject var viewModel: ViewModel // Not auto-injected
    
    var body: some View {
        List(viewModel.items) { item in
            Text(item.name)
        }
    }
}
```

## Examples

Complete environment setup:
```swift
struct ThemeKey: EnvironmentKey {
    static let defaultValue = Theme.light
}

extension EnvironmentValues {
    var theme: Theme {
        get { self[ThemeKey.self] }
        set { self[ThemeKey.self] = newValue }
    }
}

struct AppView: View {
    @State private var theme: Theme = .light
    
    var body: some View {
        ContentView()
            .environment(\.theme, theme)
    }
}
```

## Related Errors

- [Preference Error](/languages/swift/swiftui-preference-error)
- [Binding Error](/languages/swift/swiftui-binding-error)
- [Observable Error](/languages/swift/swiftui-observable-error)

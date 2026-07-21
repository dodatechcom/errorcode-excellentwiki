---
title: "[Solution] SwiftUI @SceneStorage State Restoration Error"
description: "Fix SwiftUI @SceneStorage state restoration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @SceneStorage State Restoration Error

SceneStorage state restoration errors occur when the state is not properly restored, when the state is not persisted, or when the state does not match the scene lifecycle.

## Common Causes
- State not restored
- State not persisted
- State does not match scene lifecycle
- State type not supported

## How to Fix
1. Ensure state is restored properly
2. Persist state correctly
3. Match state to scene lifecycle
4. Use supported types

```swift
struct ContentView: View {
    @SceneStorage("scrollPosition") private var scrollPosition: Double = 0
    @SceneStorage("selectedTab") private var selectedTab = 0

    var body: some View {
        TabView(selection: $selectedTab) {
            HomeView().tag(0)
            SettingsView().tag(1)
        }
    }
}
```

## Examples
```swift
// State restoration in NavigationStack:
struct ContentView: View {
    @SceneStorage("navigationPath") private var navigationPath: Data?

    var body: some View {
        NavigationStack {
            ListView()
        }
    }
}

// Custom Codable restoration:
@SceneStorage("state") private var appState: AppState?
```

---
title: "[Solution] SwiftUI NavigationStack Pop Error"
description: "Fix NavigationStack pop-to-root and navigation dismissal errors in SwiftUI."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI NavigationStack Pop Error

NavigationStack pop operations fail when the navigation path does not match expected state or when programmatic navigation conflicts with user-initiated navigation.

## Common Causes
- Navigation path not properly bound
- Attempting to pop beyond available views
- Conflicting programmatic and interactive navigation
- Path binding type mismatch

## How to Fix
1. Bind navigation path to @State variable
2. Check path count before popping
3. Use path.removeLast() or path = NavigationPath()
4. Ensure type consistency between path and views

```swift
// Navigation with programmatic pop:
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            Button("Go Deep") { path.append("detail") }
            Button("Pop to Root") { path = NavigationPath() }
            .navigationDestination(for: String.self) { value in
                Text(value)
            }
        }
    }
}
```

## Examples
```swift
// Navigation management:
struct ContentView: View {
    @State private var path = NavigationPath()

    func popToRoot() {
        path = NavigationPath()
    }

    func popLast() {
        guard !path.isEmpty else { return }
        path.removeLast()
    }

    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Detail 1", value: "d1")
                NavigationLink("Detail 2", value: "d2")
            }
            .navigationDestination(for: String.self) { val in
                Text(val)
            }
        }
    }
}
```

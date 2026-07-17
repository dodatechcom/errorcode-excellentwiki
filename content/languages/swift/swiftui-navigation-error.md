---
title: "[Solution] Swift SwiftUI NavigationLink Error Fix"
description: "Fix Swift SwiftUI NavigationLink errors. Learn why NavigationLink fails and how to handle navigation properly."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A SwiftUI NavigationLink error occurs when navigation fails due to improper configuration, missing NavigationStack, or programmatic navigation issues. NavigationLink requires a NavigationStack or NavigationView as an ancestor.

## Common Causes

- Missing NavigationStack/NavigationView
- NavigationLink inside wrong container
- Programmatic navigation not working
- Multiple NavigationLinks conflicting

## How to Fix

```swift
// WRONG: NavigationLink without NavigationStack
struct ContentView: View {
    var body: some View {
        NavigationLink("Go to Detail", destination: DetailView())  // Not working
    }
}

// CORRECT: Wrap in NavigationStack
struct ContentView: View {
    var body: some View {
        NavigationStack {
            NavigationLink("Go to Detail", destination: DetailView())
        }
    }
}
```

```swift
// WRONG: Programmatic navigation not working
@State var isActive = false
NavigationLink("Go", destination: DetailView(), isActive: $isActive)  // Not triggering

// CORRECT: Use NavigationLink with value (iOS 16+)
NavigationLink("Go", value: "detail")

// Or use navigationDestination
.navigationDestination(for: String.self) { value in
    if value == "detail" {
        DetailView()
    }
}
```

```swift
// WRONG: Multiple NavigationLinks in List
List {
    NavigationLink("Item 1", destination: DetailView())
    NavigationLink("Item 2", destination: DetailView())  // May conflict
}

// CORRECT: Use ForEach with NavigationLink
List {
    ForEach(items) { item in
        NavigationLink(destination: DetailView(item: item)) {
            Text(item.name)
        }
    }
}
```

## Examples

```swift
// Example 1: Basic NavigationStack
NavigationStack {
    List {
        NavigationLink("Detail 1", destination: DetailView())
        NavigationLink("Detail 2", destination: DetailView())
    }
}

// Example 2: Programmatic navigation (iOS 16+)
@State private var path = NavigationPath()

NavigationStack(path: $path) {
    Button("Go to Detail") {
        path.append("detail")
    }
    .navigationDestination(for: String.self) { value in
        DetailView()
    }
}

// Example 3: Navigation with data
NavigationLink(destination: DetailView(item: selectedItem)) {
    ItemRow(item: selectedItem)
}
```

## Related Errors

- [SwiftUI state error](swiftui-state-error) — state management issues
- [SwiftUI list error](swiftui-list-error) — list rendering issues
- [SwiftUI navigation error](swiftui-navigation-error) — navigation issues

---
title: "[Solution] SwiftUI .id Modifier Error"
description: "Fix SwiftUI .id modifier view identity and re-render errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .id Modifier Error

ID modifier errors occur when the id is not properly set, when the id causes unnecessary re-renders, or when the id does not match the content.

## Common Causes
- ID not set
- ID causes unnecessary re-renders
- ID does not match content
- ID not updating

## How to Fix
1. Set id properly
2. Avoid unnecessary re-renders
3. Match id to content
4. Update id

```swift
struct ContentView: View {
    @State private var refreshID = UUID()

    var body: some View {
        ContentView()
            .id(refreshID)
    }
}
```

## Examples
```swift
// Force re-render
.id(UUID())

// Reset navigation
NavigationStack {
    ContentView()
        .id(UUID())
}

// Conditional identity
.id(isEditing ? "editing" : "normal")

// List identity
List(items) { item in
    ItemRow(item: item)
}
.id(items.count)
```

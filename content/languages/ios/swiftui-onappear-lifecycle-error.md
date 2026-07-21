---
title: "[Solution] SwiftUI .onAppear Lifecycle Error"
description: "Fix SwiftUI .onAppear view lifecycle and timing errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .onAppear Lifecycle Error

onAppear errors occur when the appearance handler is called at the wrong time, when the handler is called multiple times, or when the handler does not match the view lifecycle.

## Common Causes
- Handler called at wrong time
- Handler called multiple times
- Handler does not match lifecycle
- Handler not called at all

## How to Fix
1. Handle appearance properly
2. Prevent duplicate calls
3. Match view lifecycle
4. Ensure handler is called

```swift
struct ContentView: View {
    @State private var items: [Item] = []

    var body: some View {
        List(items) { item in
            Text(item.name)
        }
        .onAppear {
            loadItems()
        }
    }
}
```

## Examples
```swift
// onAppear vs task:
.onAppear { /* Synchronous */ }
.task { /* Async */ }

// Prevent duplicate calls:
.onAppear {
    guard !hasLoaded else { return }
    hasLoaded = true
    loadItems()
}

// With animation:
.onAppear {
    withAnimation { isShowing = true }
}
```

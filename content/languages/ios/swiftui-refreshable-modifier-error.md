---
title: "[Solution] SwiftUI .refreshable Modifier Error"
description: "Fix SwiftUI .refreshable pull-to-refresh modifier errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .refreshable Modifier Error

Refreshable modifier errors occur when the refresh action is not properly configured, when the refresh does not complete, or when the refresh indicator does not appear.

## Common Causes
- Refresh action not configured
- Refresh does not complete
- Refresh indicator not appearing
- Refresh conflicts with content

## How to Fix
1. Configure refresh action properly
2. Ensure refresh completes
3. Show refresh indicator
4. Ensure refresh is compatible with content

```swift
struct ContentView: View {
    @State private var items: [Item] = []

    var body: some View {
        List(items) { item in
            Text(item.name)
        }
        .refreshable {
            await loadItems()
        }
    }

    func loadItems() async {
        items = try await API.fetchItems()
    }
}
```

## Examples
```swift
// With animation:
.refreshable {
    withAnimation {
        items = try await API.fetchItems()
    }
}

// With delay:
.refreshable {
    try await Task.sleep(nanoseconds: 1_000_000_000)
    items = try await API.fetchItems()
}

// Custom refresh control:
.refreshable {
    await refresh()
}
```

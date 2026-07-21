---
title: "[Solution] SwiftUI .task Modifier Async Error"
description: "Fix SwiftUI .task modifier async operation lifecycle errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .task Modifier Async Error

Task modifier errors occur when the async operation is not properly managed, when the task is cancelled unexpectedly, or when the task does not complete before the view disappears.

## Common Causes
- Async operation not managed
- Task cancelled unexpectedly
- Task does not complete
- Task not triggered

## How to Fix
1. Manage async operation properly
2. Handle task cancellation
3. Ensure task completion
4. Trigger task appropriately

```swift
struct ContentView: View {
    @State private var items: [Item] = []

    var body: some View {
        List(items) { item in
            Text(item.name)
        }
        .task {
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
// With value observation:
.task(id: searchQuery) {
    await performSearch(query: searchQuery)
}

// With cancellation handling:
.task {
    for await update in updates {
        // Process updates
    }
}
.onDisappear { /* Task automatically cancelled */ }

// With priority:
.task(priority: .userInitiated) {
    await loadData()
}
```

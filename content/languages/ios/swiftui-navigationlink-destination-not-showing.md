---
title: "[Solution] SwiftUI NavigationLink Destination Not Showing"
description: "Fix SwiftUI NavigationLink not navigating to destination view when tapped."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI NavigationLink Destination Not Showing

NavigationLink destination may not appear if the navigation stack is not properly configured or if the link is nested incorrectly.

## Common Causes
- Missing NavigationStack or NavigationView wrapper
- NavigationLink inside ScrollView without proper context
- Programmatic navigation not triggering
- Multiple NavigationLinks sharing same state

## How to Fix
1. Wrap content in NavigationStack (iOS 16+)
2. Ensure NavigationLink is a direct child of NavigationStack
3. Use isActive binding for programmatic navigation
4. Check that the destination view is correctly specified

```swift
// Correct setup:
NavigationStack {
    List(items) { item in
        NavigationLink(value: item) {
            Text(item.name)
        }
    }
    .navigationDestination(for: Item.self) { item in
        ItemDetailView(item: item)
    }
}
```

## Examples
```swift
// iOS 16+ NavigationStack:
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Go to Detail", value: "detail")
            }
            .navigationDestination(for: String.self) { value in
                Text("Detail: \(value)")
            }
        }
    }
}
```

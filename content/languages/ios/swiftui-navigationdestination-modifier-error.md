---
title: "[Solution] SwiftUI .navigationDestination Modifier Error"
description: "Fix SwiftUI .navigationDestination modifier navigation push errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .navigationDestination Modifier Error

NavigationDestination modifier errors occur when the destination is not properly configured, when the navigation does not push, or when the navigation does not match the design.

## Common Causes
- Destination not configured
- Navigation does not push
- Navigation not matching design
- Navigation not triggered

## How to Fix
1. Configure destination properly
2. Ensure navigation pushes
3. Match design specifications
4. Trigger navigation correctly

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Detail", value: "detail")
            }
            .navigationDestination(for: String.self) { value in
                Text("Detail: \(value)")
            }
        }
    }
}
```

## Examples
```swift
// Multiple destinations:
.navigationDestination(for: String.self) { value in
    Text("String: \(value)")
}
.navigationDestination(for: Int.self) { value in
    Text("Int: \(value)")
}

// With data:
.navigationDestination(for: Item.self) { item in
    DetailView(item: item)
}

// Programmatic navigation:
.navigationDestination(isPresented: $showDetail) {
    DetailView()
}
```

---
title: "[Solution] SwiftUI matchedGeometryEffect Namespace Error"
description: "Fix SwiftUI matchedGeometryEffect namespace not found or undefined errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI matchedGeometryEffect Namespace Error

Namespace errors occur when @Namespace is not declared, when it is declared in the wrong scope, or when the matchedGeometryEffect references a namespace that is not accessible.

## Common Causes
- @Namespace not declared in view
- Namespace declared in wrong view scope
- Namespace not passed to child views
- Multiple namespaces with same ID

## How to Fix
1. Declare @Namespace in the view that uses matchedGeometryEffect
2. Pass namespace to child views using environment
3. Ensure unique IDs within a namespace
4. Share namespace between source and destination views

```swift
// Correct namespace usage:
struct ContentView: View {
    @Namespace private var animation
    @State private var isExpanded = false

    var body: some View {
        if isExpanded {
            RoundedRectangle(cornerRadius: 20)
                .matchedGeometryEffect(id: "shape", in: animation)
        } else {
            Circle()
                .matchedGeometryEffect(id: "shape", in: animation)
        }
    }
}
```

## Examples
```swift
// Namespace in shared scope:
struct TabBar: View {
    @Namespace private var animation
    @State private var selectedTab = 0

    var body: some View {
        ZStack(alignment: .bottom) {
            // Content views
            TabView(selection: $selectedTab) { ... }

            // Custom tab bar
            HStack {
                ForEach(tabs) { tab in
                    if selectedTab == tab.id {
                        Indicator()
                            .matchedGeometryEffect(id: "indicator", in: animation)
                    }
                }
            }
        }
    }
}
```

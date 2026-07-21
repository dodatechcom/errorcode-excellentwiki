---
title: "[Solution] SwiftUI .scrollTargetLayout Modifier Error"
description: "Fix SwiftUI .scrollTargetLayout modifier scroll target layout configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollTargetLayout Modifier Error

ScrollTargetLayout modifier errors occur when the layout is not properly configured, when the layout conflicts with the scroll content, or when the layout does not match the design.

## Common Causes
- Layout not configured
- Layout conflicts with content
- Layout not matching design
- Layout not updating with content

## How to Fix
1. Configure layout properly
2. Ensure layout is compatible with content
3. Match design specifications
4. Update layout with content

```swift
struct ContentView: View {
    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: 0) {
                ForEach(items) { item in
                    ItemView(item: item)
                        .frame(width: 300)
                }
            }
            .scrollTargetLayout()
        }
        .scrollTargetBehavior(.paging)
    }
}
```

## Examples
```swift
// With paging
.scrollTargetLayout()
.scrollTargetBehavior(.paging)

// With snapping
.scrollTargetLayout()
.scrollTargetBehavior(.snapping)

// Custom layout
.scrollTargetLayout()
.scrollTargetBehavior(.viewAligned)
```

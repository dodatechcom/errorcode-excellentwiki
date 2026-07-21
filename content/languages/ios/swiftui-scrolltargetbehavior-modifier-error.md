---
title: "[Solution] SwiftUI .scrollTargetBehavior Modifier Error"
description: "Fix SwiftUI .scrollTargetBehavior modifier scroll paging and snapping errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollTargetBehavior Modifier Error

ScrollTargetBehavior modifier errors occur when the behavior is not properly configured, when the behavior conflicts with the scroll content, or when the behavior does not match the design.

## Common Causes
- Behavior not configured
- Behavior conflicts with content
- Behavior not matching design
- Behavior not updating with content

## How to Fix
1. Configure behavior properly
2. Ensure behavior is compatible with content
3. Match design specifications
4. Update behavior with content

```swift
struct ContentView: View {
    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack {
                ForEach(items) { item in
                    ItemView(item: item)
                        .frame(width: 300)
                }
            }
        }
        .scrollTargetBehavior(.paging)
    }
}
```

## Examples
```swift
// Paging
.scrollTargetBehavior(.paging)

// Snapping
.scrollTargetBehavior(.snapping)

// Custom alignment
.scrollTargetBehavior(.paging(alignment: .center))

// View-aligned
.scrollTargetBehavior(.viewAligned)
```

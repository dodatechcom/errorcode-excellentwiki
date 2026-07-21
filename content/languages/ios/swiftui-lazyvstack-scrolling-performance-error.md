---
title: "[Solution] SwiftUI LazyVStack Scrolling Performance Error"
description: "Fix performance issues with LazyVStack causing janky scrolling in SwiftUI lists."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI LazyVStack Scrolling Performance Error

LazyVStack performance degrades when views are too complex, when heavy computations occur in the view body, or when images are not properly cached.

## Common Causes
- Complex views inside LazyVStack performing heavy work
- Images loaded without caching
- State changes causing unnecessary view redraws
- Missing EquatableView or Identifiable conformance

## How to Fix
1. Simplify views inside LazyVStack
2. Use async image loading with caching
3. Minimize state changes that affect many rows
4. Use EquatableView for static content

```swift
// Optimized LazyVStack:
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemRow(item: item) // Keep row view simple
                .equatable() // Prevent unnecessary redraws
        }
    }
}
```

## Examples
```swift
// Performance-optimized list:
struct OptimizedList: View {
    let items: [Item]

    var body: some View {
        ScrollView {
            LazyVStack(spacing: 0) {
                ForEach(items) { item in
                    ItemRow(item: item)
                        .id(item.id)
                }
            }
        }
    }
}

struct ItemRow: View, Equatable {
    let item: Item
    static func == (lhs: ItemRow, rhs: ItemRow) -> Bool {
        lhs.item.id == rhs.item.id && lhs.item.title == rhs.item.title
    }
    var body: some View {
        Text(item.title).padding()
    }
}
```

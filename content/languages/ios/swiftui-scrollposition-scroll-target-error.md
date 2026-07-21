---
title: "[Solution] SwiftUI ScrollPosition Scroll Target Error"
description: "Fix SwiftUI scroll position and scroll target configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI ScrollPosition Scroll Target Error

Scroll target errors occur when the scroll position does not match the target, when the scroll target ID is invalid, or when multiple scroll positions conflict.

## Common Causes
- Scroll target ID not matching list items
- Multiple scroll targets active simultaneously
- Scroll position not updated on navigation
- ScrollView and List using incompatible scroll APIs

## How to Fix
1. Ensure scroll target ID matches an item in the list
2. Use only one scroll position per scroll view
3. Update scroll position when content changes
4. Use correct scroll API for your container

```swift
// Scroll to position:
ScrollViewReader { proxy in
    ScrollView {
        LazyVStack {
            ForEach(items) { item in
                Text(item.name).id(item.id)
            }
        }
    }
    .scrollTargetLayout()
}
```

## Examples
```swift
// Programmatic scroll:
ScrollViewReader { proxy in
    VStack {
        Button("Scroll to Top") {
            withAnimation { proxy.scrollTo(topID, anchor: .top) }
        }
        ScrollView {
            LazyVStack {
                ForEach(items) { item in
                    ItemRow(item: item).id(item.id)
                }
            }
        }
    }
}
```

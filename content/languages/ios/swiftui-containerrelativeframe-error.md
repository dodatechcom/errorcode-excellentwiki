---
title: "[Solution] SwiftUI .containerRelativeFrame Error"
description: "Fix SwiftUI containerRelativeFrame modifier sizing errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .containerRelativeFrame Error

containerRelativeFrame fails when the container is not properly identified, when the size is calculated before layout is complete, or when multiple modifiers conflict.

## Common Causes
- Container identifier not matching actual container
- Size calculated before view layout
- Multiple frame modifiers conflicting
- Container not in the view hierarchy

## How to Fix
1. Ensure container identifier matches the intended container
2. Use geometryReader or other layout tools for sizing
3. Apply containerRelativeFrame as the outermost frame modifier
4. Verify container is in the view hierarchy

```swift
// containerRelativeFrame usage:
ScrollView(.horizontal) {
    LazyHStack {
        ForEach(items) { item in
            ItemView(item: item)
                .containerRelativeFrame(.horizontal)
        }
    }
}
```

## Examples
```swift
// Paged horizontal scroll:
ScrollView(.horizontal) {
    LazyHStack(spacing: 0) {
        ForEach(pages) { page in
            PageView(page: page)
                .containerRelativeFrame(.horizontal)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.paging)
```

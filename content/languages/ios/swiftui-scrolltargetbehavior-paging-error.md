---
title: "[Solution] SwiftUI .scrollTargetBehavior Paging Error"
description: "Fix SwiftUI scroll target behavior paging configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollTargetBehavior Paging Error

Paging behavior fails when the scroll target is not properly configured, when the content size does not match the page size, or when the paging behavior conflicts with other scroll modifiers.

## Common Causes
- Scroll target layout not configured
- Content size not matching page dimensions
- Paging behavior conflicts with other modifiers
- Container scroll view not properly configured

## How to Fix
1. Configure scrollTargetLayout on the content
2. Ensure content fills the page dimensions
3. Remove conflicting scroll modifiers
4. Test paging with different content sizes

```swift
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

## Examples
```swift
// Vertical paging:
ScrollView {
    LazyVStack(spacing: 0) {
        ForEach(pages) { page in
            PageView(page: page)
                .containerRelativeFrame(.vertical)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.paging)
```

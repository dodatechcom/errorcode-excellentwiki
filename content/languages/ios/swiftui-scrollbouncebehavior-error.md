---
title: "[Solution] SwiftUI .scrollBounceBehavior Error"
description: "Fix SwiftUI scroll bounce behavior configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollBounceBehavior Error

Scroll bounce behavior errors occur when the bounce configuration conflicts with content size, when the modifier is applied to the wrong container, or when it conflicts with content insets.

## Common Causes
- Bounce behavior conflicting with content size
- Modifier on wrong view in hierarchy
- Content insets preventing bounce
- Always bouncing but content fits

## How to Fix
1. Set bounce behavior based on content size
2. Apply modifier to the scroll container
3. Adjust content insets for proper bounce
4. Test with different content sizes

```swift
// Always bounce:
ScrollView {
    // Content
}
.scrollBounceBehavior(.basedOnSize)

// Never bounce:
ScrollView {
    // Content
}
.scrollBounceBehavior(.always)
```

## Examples
```swift
// Conditional bounce:
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}
.scrollBounceBehavior(.basedOnSize) // Only bounces when content is smaller than viewport
```

---
title: "[Solution] SwiftUI .containerRelativeFrame Size Error"
description: "Fix SwiftUI containerRelativeFrame size calculation and layout errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .containerRelativeFrame Size Error

Size calculation errors occur when the container frame is not properly calculated, when the size does not match the expected dimensions, or when the size conflicts with other layout modifiers.

## Common Causes
- Container frame not calculated correctly
- Size not matching expected dimensions
- Size conflicts with other modifiers
- Container not in the view hierarchy

## How to Fix
1. Verify container frame calculation
2. Ensure size matches expected dimensions
3. Resolve conflicts with other modifiers
4. Ensure container is in view hierarchy

```swift
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
// Container relative frame with specific size:
ItemView(item: item)
    .containerRelativeFrame(.horizontal, { length, axis, geometry, anchor in
        length * 0.8
    })
```

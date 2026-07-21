---
title: "[Solution] SwiftUI .toolbarItemPlacement Principal Error"
description: "Fix SwiftUI toolbar item placement principal configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .toolbarItemPlacement Principal Error

Principal placement errors occur when the principal item conflicts with the title, when the placement is not visible, or when the placement conflicts with other navigation bar items.

## How to Fix
1. Ensure principal item does not conflict with title
2. Verify placement visibility
3. Avoid conflicts with other toolbar items
4. Test on different device sizes

```swift
.toolbar {
    ToolbarItem(placement: .principal) {
        Text("Title")
            .font(.headline)
    }
}
```

## Examples
```swift
// Principal item with custom view:
.toolbar {
    ToolbarItem(placement: .principal) {
        VStack {
            Text("Title")
                .font(.headline)
            Text("Subtitle")
                .font(.caption)
                .foregroundColor(.secondary)
        }
    }
}
```

---
title: "[Solution] SwiftUI .scrollIndicatorsFlash Modifier Error"
description: "Fix SwiftUI scroll indicator flash animation configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollIndicatorsFlash Modifier Error

Scroll indicator flash fails when the modifier is not properly triggered, when the scroll view does not support indicator flashing, or when the flash conflicts with other scroll behaviors.

## Common Causes
- Modifier not triggered on scroll events
- Scroll view not supporting indicator flash
- Flash duration not matching expectations
- Multiple scroll indicators conflicting

## How to Fix
1. Trigger flash on appropriate events
2. Ensure scroll view supports indicator flash
3. Adjust flash timing if needed
4. Use single scroll view for flash behavior

```swift
// Flash scroll indicators:
@State private var flashIndicators = false

ScrollView {
    // Content
}
.scrollIndicatorsFlash(trigger: flashIndicators)

// Trigger flash:
Button("Flash") { flashIndicators.toggle() }
```

## Examples
```swift
// Flash on content change:
@State private var items: [Item] = []

ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}
.scrollIndicatorsFlash(trigger: items.count)
```

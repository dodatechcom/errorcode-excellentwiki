---
title: "[Solution] SwiftUI .shadow Modifier Error"
description: "Fix SwiftUI .shadow modifier view shadow configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .shadow Modifier Error

Shadow modifier errors occur when the shadow is not properly configured, when the shadow does not match the content, or when the shadow does not update with content changes.

## Common Causes
- Shadow not configured
- Shadow does not match content
- Shadow not updating
- Shadow not matching design

## How to Fix
1. Configure shadow properly
2. Ensure shadow matches content
3. Update shadow with content changes
4. Match design specifications

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello")
            .shadow(radius: 5)
    }
}
```

## Examples
```swift
// Simple shadow
.shadow(radius: 5)

// With color and offset
.shadow(color: .black.opacity(0.3), radius: 5, x: 0, y: 3)

// Multiple shadows
.shadow(color: .black.opacity(0.1), radius: 10, x: 0, y: 5)
.shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 10)

// Conditional shadow
.shadow(radius: isHighlighted ? 10 : 0)
```

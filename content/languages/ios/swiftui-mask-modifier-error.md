---
title: "[Solution] SwiftUI .mask Modifier Error"
description: "Fix SwiftUI .mask modifier view masking shape errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .mask Modifier Error

Mask modifier errors occur when the mask is not properly configured, when the mask does not match the content, or when the mask does not update with content changes.

## Common Causes
- Mask not configured
- Mask does not match content
- Mask not updating
- Mask not matching design

## How to Fix
1. Configure mask properly
2. Ensure mask matches content
3. Update mask with content changes
4. Match design specifications

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello World")
            .mask {
                LinearGradient(colors: [.white, .clear], startPoint: .leading, endPoint: .trailing)
            }
    }
}
```

## Examples
```swift
// Text mask
Text("Hello")
    .foregroundStyle(.blue)
    .mask {
        LinearGradient(colors: [.white, .clear], startPoint: .leading, endPoint: .trailing)
    }

// Shape mask
Image("photo")
    .mask {
        Circle()
    }

// Animated mask
Image("photo")
    .mask {
        Rectangle()
            .frame(width: showFull ? .infinity : 0)
    }
```

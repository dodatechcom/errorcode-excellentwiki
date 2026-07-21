---
title: "[Solution] SwiftUI .contentShape Modifier Error"
description: "Fix SwiftUI .contentShape modifier hit testing shape errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .contentShape Modifier Error

ContentShape modifier errors occur when the shape is not properly configured, when the shape does not match the visible content, or when the shape does not update with content changes.

## Common Causes
- Shape not configured
- Shape does not match visible content
- Shape not updating
- Shape not matching design

## How to Fix
1. Configure shape properly
2. Ensure shape matches visible content
3. Update shape with content changes
4. Match design specifications

```swift
struct ContentView: View {
    var body: some View {
        Text("Tap me")
            .contentShape(Rectangle())
            .onTapGesture { print("Tapped") }
    }
}
```

## Examples
```swift
// Circle shape
Image(systemName: "star")
    .contentShape(Circle())
    .onTapGesture { }

// Custom shape
Text("Hello")
    .contentShape(RoundedRectangle(cornerRadius: 10))
    .onTapGesture { }

// Invisible hit area
Rectangle()
    .fill(.clear)
    .contentShape(Rectangle())
    .onTapGesture { }
```

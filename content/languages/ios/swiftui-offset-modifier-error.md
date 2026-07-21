---
title: "[Solution] SwiftUI .offset Modifier Error"
description: "Fix SwiftUI .offset modifier view position offset errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .offset Modifier Error

Offset modifier errors occur when the offset is not properly applied, when the offset does not animate, or when the offset conflicts with layout.

## Common Causes
- Offset not applied
- Offset not animating
- Offset conflicts with layout
- Offset not updating

## How to Fix
1. Apply offset properly
2. Ensure offset animates
3. Resolve conflicts with layout
4. Update offset

```swift
struct ContentView: View {
    @State private var isOffset = false

    var body: some View {
        Text("Hello")
            .offset(x: isOffset ? 50 : 0, y: isOffset ? 50 : 0)
            .animation(.easeInOut, value: isOffset)
    }
}
```

## Examples
```swift
// Horizontal offset
.offset(x: 50)

// Vertical offset
.offset(y: 50)

// Both offsets
.offset(x: 50, y: 50)

// Animated offset
.animation(.spring(), value: isOffset)
```

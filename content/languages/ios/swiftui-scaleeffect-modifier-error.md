---
title: "[Solution] SwiftUI .scaleEffect Modifier Error"
description: "Fix SwiftUI .scaleEffect modifier view scaling and size transform errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scaleEffect Modifier Error

ScaleEffect modifier errors occur when the scale is not properly applied, when the scale does not animate, or when the scale conflicts with layout.

## Common Causes
- Scale not applied
- Scale not animating
- Scale conflicts with layout
- Scale not updating

## How to Fix
1. Apply scale properly
2. Ensure scale animates
3. Resolve conflicts with layout
4. Update scale

```swift
struct ContentView: View {
    @State private var isScaled = false

    var body: some View {
        Text("Hello")
            .scaleEffect(isScaled ? 1.5 : 1.0)
            .animation(.spring(), value: isScaled)
    }
}
```

## Examples
```swift
// Uniform scale
.scaleEffect(isScaled ? 1.5 : 1.0)

// Non-uniform scale
.scaleEffect(x: 2.0, y: 1.0)

// Anchor point
.scaleEffect(1.5, anchor: .topLeading)

// Animated scale
.animation(.spring(response: 0.6, dampingFraction: 0.7), value: isScaled)
```

---
title: "[Solution] SwiftUI .opacity Modifier Error"
description: "Fix SwiftUI .opacity modifier view transparency and visibility errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .opacity Modifier Error

Opacity modifier errors occur when the opacity is not properly set, when the opacity does not animate, or when the opacity conflicts with other modifiers.

## Common Causes
- Opacity not set
- Opacity not animating
- Opacity conflicts with modifiers
- Opacity not updating

## How to Fix
1. Set opacity properly
2. Ensure opacity animates
3. Resolve conflicts with modifiers
4. Update opacity

```swift
struct ContentView: View {
    @State private var isVisible = true

    var body: some View {
        Text("Hello")
            .opacity(isVisible ? 1 : 0)
            .animation(.easeInOut, value: isVisible)
    }
}
```

## Examples
```swift
// Conditional opacity
.opacity(isVisible ? 1 : 0)

// Animated opacity
.animation(.easeInOut(duration: 0.3), value: isVisible)

// Partial opacity
.opacity(0.5)

// Hide without layout shift
.opacity(isVisible ? 1 : 0)
```

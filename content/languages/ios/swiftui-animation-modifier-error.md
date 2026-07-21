---
title: "[Solution] SwiftUI .animation Modifier Error"
description: "Fix SwiftUI .animation modifier view animation configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .animation Modifier Error

Animation modifier errors occur when the animation is not properly configured, when the animation does not trigger, or when the animation does not match the design.

## Common Causes
- Animation not configured
- Animation not triggering
- Animation not matching design
- Animation not updating

## How to Fix
1. Configure animation properly
2. Ensure animation triggers
3. Match design specifications
4. Update animation

```swift
struct ContentView: View {
    @State private var isAnimating = false

    var body: some View {
        Circle()
            .frame(width: isAnimating ? 200 : 100)
            .animation(.spring(), value: isAnimating)
    }
}
```

## Examples
```swift
// Implicit animation
.animation(.easeInOut(duration: 0.3), value: isAnimating)

// With curve
.animation(.easeInOut(duration: 0.5), value: isAnimating)

// Spring animation
.animation(.spring(response: 0.6, dampingFraction: 0.7), value: isAnimating)

// Repeat animation
.animation(.linear(duration: 1).repeatForever(autoreverses: true), value: isAnimating)
```

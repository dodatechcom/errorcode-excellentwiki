---
title: "[Solution] SwiftUI .animation Trigger Error"
description: "Fix SwiftUI animation trigger configuration and timing errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .animation Trigger Error

Animation trigger fails when the animation modifier is placed incorrectly, when the trigger value does not change, or when the animation type is incompatible with the view change.

## Common Causes
- Animation modifier not connected to trigger
- Trigger value not changing
- Animation type incompatible with view change
- Multiple animation modifiers conflicting

## How to Fix
1. Connect animation to trigger value properly
2. Ensure trigger value actually changes
3. Use compatible animation types
4. Apply animation to the correct view

```swift
// Animation on value change:
Text("Hello")
    .offset(x: isExpanded ? 100 : 0)
    .animation(.spring(), value: isExpanded)

// With explicit animation:
withAnimation(.easeInOut(duration: 0.3)) {
    isExpanded.toggle()
}
```

## Examples
```swift
// Multiple animations:
Circle()
    .frame(width: isLarge ? 200 : 100)
    .animation(.spring(response: 0.6, dampingFraction: 0.7), value: isLarge)
    .foregroundColor(isRed ? .red : .blue)
    .animation(.easeIn(duration: 0.2), value: isRed)
```

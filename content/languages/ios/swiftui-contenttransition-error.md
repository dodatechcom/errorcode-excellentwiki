---
title: "[Solution] SwiftUI .contentTransition Error"
description: "Fix SwiftUI content transition animation errors in iOS views."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .contentTransition Error

Content transitions fail when applied to incompatible view types, when the transition type does not match the content change, or when combined with incompatible modifiers.

## Common Causes
- Transition type not matching content change
- Content transition incompatible with view type
- Multiple transitions conflicting
- Transition applied to views without animation context

## How to Fix
1. Match transition type to content change type
2. Use compatible transitions for the view
3. Apply transitions individually
4. Ensure animation context exists

```swift
// Content transition:
Text(displayText)
    .contentTransition(.numericText())
    .animation(.smooth, value: displayText)

// Combined with animation:
withAnimation(.easeInOut) {
    counter += 1
}
```

## Examples
```swift
// Multiple content transitions:
Text("\(count)")
    .contentTransition(.numericText())

Text(newTitle)
    .contentTransition(.opacity)

Image(systemName: iconName)
    .contentTransition(.symbolEffect(.replace))
```

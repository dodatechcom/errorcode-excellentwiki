---
title: "[Solution] SwiftUI .scrollDismissesKeyboard Error"
description: "Fix SwiftUI keyboard dismissal behavior when scrolling in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollDismissesKeyboard Error

Keyboard does not dismiss when scrolling because the scrollDismissesKeyboard modifier is not applied or the scroll view does not properly handle keyboard dismissal.

## Common Causes
- scrollDismissesKeyboard modifier not applied
- ScrollView not in the correct view hierarchy
- Keyboard dismissal mode conflicts with other behaviors
- Text field not properly connected to keyboard

## How to Fix
1. Apply .scrollDismissesKeyboard(.interactively) to ScrollView
2. Ensure ScrollView is the scrollable container
3. Use appropriate dismissal mode for your use case
4. Test with different keyboard types

```swift
ScrollView {
    VStack {
        ForEach(items) { item in
            Text(item.name)
        }
    }
}
.scrollDismissesKeyboard(.interactively)
```

## Examples
```swift
// Different dismissal modes:
ScrollView {
    // Dismiss on drag
}.scrollDismissesKeyboard(.automatically)

ScrollView {
    // Dismiss interactively
}.scrollDismissesKeyboard(.interactively)

ScrollView {
    // Never dismiss
}.scrollDismissesKeyboard(.never)
```

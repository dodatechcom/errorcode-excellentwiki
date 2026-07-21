---
title: "[Solution] SwiftUI .scrollDismissesKeyboard Interactive Error"
description: "Fix SwiftUI interactive keyboard dismissal configuration errors in scroll views."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollDismissesKeyboard Interactive Error

Interactive keyboard dismissal fails when the modifier is not properly configured, when the keyboard is not dismissible, or when the scroll view does not support interactive dismissal.

## Common Causes
- Modifier not set to .interactively
- Keyboard type does not support interactive dismissal
- ScrollView content too short for interaction
- Multiple keyboard dismissal modifiers conflicting

## How to Fix
1. Set scrollDismissesKeyboard to .interactively
2. Verify keyboard type supports interactive dismissal
3. Ensure scroll view content is long enough
4. Remove conflicting keyboard dismissal modifiers

```swift
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            TextField("Type here", text: binding)
        }
    }
}
.scrollDismissesKeyboard(.interactively)
```

## Examples
```swift
// Interactive dismissal with form:
Form {
    ForEach(1...20, id: \.self) { i in
        TextField("Field \(i)", text: $text)
    }
}
.scrollDismissesKeyboard(.interactively)
```

---
title: "[Solution] SwiftUI Accessibility Label Error"
description: "Fix SwiftUI accessibility label and hint configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Accessibility Label Error

Accessibility labels fail when they are empty, when the modifier is applied incorrectly, or when dynamic content is not properly described for VoiceOver users.

## Common Causes
- Accessibility label is empty or not descriptive
- Modifier order causes label to not apply
- Dynamic content not updating accessibility
- Hidden elements still exposed to VoiceOver

## How to Fix
1. Provide meaningful, descriptive accessibility labels
2. Apply accessibility modifiers after content modifiers
3. Update accessibility labels when content changes
4. Use .accessibilityHidden(true) for decorative elements

```swift
// Proper accessibility:
Image("photo")
    .resizable()
    .accessibilityLabel("User profile photo")

// Dynamic accessibility:
Text(item.name)
    .accessibilityLabel("Name: \(item.name)")
    .accessibilityHint("Double tap to edit")
```

## Examples
```swift
// Complete accessibility example:
Button(action: deleteItem) {
    Image(systemName: "trash")
}
.accessibilityLabel("Delete item")
.accessibilityHint("Removes the selected item permanently")

// Grouped accessibility:
VStack {
    Text("Total")
    Text("$42.00")
}
.accessibilityElement(children: .combine)
.accessibilityLabel("Total price: 42 dollars")
```

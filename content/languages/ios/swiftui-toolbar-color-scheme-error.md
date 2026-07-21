---
title: "[Solution] SwiftUI .toolbar Color Scheme Error"
description: "Fix SwiftUI toolbar color scheme configuration errors in iOS 16+."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .toolbar Color Scheme Error

Toolbar color scheme errors occur when the modifier is not properly applied to the navigation view, when the color scheme conflicts with the system appearance, or when the modifier is not available on the target iOS version.

## Common Causes
- Modifier not on navigation view
- Color scheme conflicts with system
- iOS version does not support modifier
- Multiple color scheme modifiers conflicting

## How to Fix
1. Apply modifier to the navigation view
2. Coordinate with system appearance
3. Check iOS version availability
4. Use only one color scheme modifier

```swift
NavigationStack {
    List { }
    .toolbarColorScheme(.dark, for: .navigationBar)
}

// Light toolbar:
NavigationStack {
    List { }
    .toolbarColorScheme(.light, for: .navigationBar)
}
```

## Examples
```swift
// Conditional color scheme:
NavigationStack {
    ScrollView {
        // Content
    }
    .toolbarColorScheme(isDarkMode ? .dark : .light, for: .navigationBar)
    .toolbarBackground(.visible, for: .navigationBar)
}
```

---
title: "[Solution] SwiftUI .persistentSystemOverlays Modifier Error"
description: "Fix SwiftUI .persistentSystemOverlays modifier system overlay errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .persistentSystemOverlays Modifier Error

PersistentSystemOverlays modifier errors occur when the overlay is not properly configured, when the overlay conflicts with the layout, or when the overlay does not match the design.

## Common Causes
- Overlay not configured
- Overlay conflicts with layout
- Overlay not matching design
- Overlay not updating with content

## How to Fix
1. Configure overlay properly
2. Ensure overlay is compatible with layout
3. Match design specifications
4. Update overlay with content

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello")
            .persistentSystemOverlays(.hidden)
    }
}
```

## Examples
```swift
// Show overlays
.persistentSystemOverlays(.visible)

// Hide overlays
.persistentSystemOverlays(.hidden)

// Automatic
.persistentSystemOverlays(.automatic)
```

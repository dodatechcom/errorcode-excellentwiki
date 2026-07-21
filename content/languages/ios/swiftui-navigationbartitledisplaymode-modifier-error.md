---
title: "[Solution] SwiftUI .navigationBarTitleDisplayMode Modifier Error"
description: "Fix SwiftUI .navigationBarTitleDisplayMode modifier navigation bar title display mode errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .navigationBarTitleDisplayMode Modifier Error

NavigationBarTitleDisplayMode modifier errors occur when the display mode is not properly configured, when the mode conflicts with the navigation bar, or when the mode does not match the design.

## Common Causes
- Display mode not configured
- Mode conflicts with navigation bar
- Mode not matching design
- Mode not updating

## How to Fix
1. Configure display mode properly
2. Ensure mode is compatible with navigation bar
3. Match design specifications
4. Update mode

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            Text("Content")
                .navigationTitle("Title")
                .navigationBarTitleDisplayMode(.inline)
        }
    }
}
```

## Examples
```swift
// Large title
.navigationBarTitleDisplayMode(.large)

// Automatic
.navigationBarTitleDisplayMode(.automatic)

// Inline
.navigationBarTitleDisplayMode(.inline)
```

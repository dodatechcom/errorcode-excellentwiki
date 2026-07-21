---
title: "[Solution] SwiftUI .navigationTitle Modifier Error"
description: "Fix SwiftUI .navigationTitle modifier navigation bar title errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .navigationTitle Modifier Error

NavigationTitle modifier errors occur when the title is not properly configured, when the title conflicts with the navigation bar, or when the title does not match the design.

## Common Causes
- Title not configured
- Title conflicts with navigation bar
- Title not matching design
- Title not updating

## How to Fix
1. Configure title properly
2. Ensure title is compatible with navigation bar
3. Match design specifications
4. Update title

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            Text("Content")
                .navigationTitle("My Title")
        }
    }
}
```

## Examples
```swift
// String title
.navigationTitle("Settings")

// Localized title
.navigationTitle(LocalizedStringKey("settings_title"))

// Display mode
.navigationTitle("Title")
.navigationBarTitleDisplayMode(.inline)
```

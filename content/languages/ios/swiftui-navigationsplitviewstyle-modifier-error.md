---
title: "[Solution] SwiftUI .navigationSplitViewStyle Modifier Error"
description: "Fix SwiftUI .navigationSplitViewStyle modifier split view appearance style errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .navigationSplitViewStyle Modifier Error

NavigationSplitViewStyle modifier errors occur when the style is not properly configured, when the style conflicts with the split view, or when the style does not match the design.

## Common Causes
- Style not configured
- Style conflicts with split view
- Style not matching design
- Style not updating

## How to Fix
1. Configure style properly
2. Ensure style is compatible with split view
3. Match design specifications
4. Update style

```swift
struct ContentView: View {
    var body: some View {
        NavigationSplitView {
            List(1...5, id: \.self) { i in
                NavigationLink("Item \(i)", value: i)
            }
        } detail: {
            Text("Detail")
        }
        .navigationSplitViewStyle(.balanced)
    }
}
```

## Examples
```swift
// Balanced
.navigationSplitViewStyle(.balanced)

// Automatic
.navigationSplitViewStyle(.automatic)

// Columns only
.navigationSplitViewStyle(.columnsOnly)
```

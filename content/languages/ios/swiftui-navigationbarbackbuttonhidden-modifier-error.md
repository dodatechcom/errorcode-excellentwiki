---
title: "[Solution] SwiftUI .navigationBarBackButtonHidden Modifier Error"
description: "Fix SwiftUI .navigationBarBackButtonHidden modifier navigation back button visibility errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .navigationBarBackButtonHidden Modifier Error

NavigationBarBackButtonHidden modifier errors occur when the back button is not properly hidden, when the hiding conflicts with navigation, or when the hiding does not match the design.

## Common Causes
- Back button not hidden
- Hiding conflicts with navigation
- Hiding not matching design
- Hiding not updating

## How to Fix
1. Hide back button properly
2. Ensure hiding is compatible with navigation
3. Match design specifications
4. Update hiding

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            Text("Content")
                .navigationBarBackButtonHidden(true)
        }
    }
}
```

## Examples
```swift
// Always hidden
.navigationBarBackButtonHidden(true)

// Conditional
.navigationBarBackButtonHidden(isFirstScreen)

// Hidden with custom back button
.navigationBarBackButtonHidden(true)
.toolbar {
    ToolbarItem(placement: .navigationBarLeading) {
        Button("Back") { }
    }
}
```

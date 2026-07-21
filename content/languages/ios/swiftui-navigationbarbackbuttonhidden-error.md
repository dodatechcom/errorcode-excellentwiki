---
title: "[Solution] SwiftUI .navigationBarBackButtonHidden Error"
description: "Fix SwiftUI navigation bar back button hidden configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .navigationBarBackButtonHidden Error

Back button hiding fails when the modifier is applied to the wrong view, when the navigation controller does not support the configuration, or when the back button is needed for user navigation.

## Common Causes
- Modifier applied to wrong view in hierarchy
- Navigation controller not supporting hidden back button
- User cannot navigate back without back button
- Modifier conflicts with custom back button

## How to Fix
1. Apply modifier to the destination view
2. Ensure navigation stack supports the configuration
3. Provide alternative navigation for hidden back button
4. Use custom back button when hiding default

```swift
// Hide back button:
DetailView()
    .navigationBarBackButtonHidden(true)

// Hide and provide custom navigation:
DetailView()
    .navigationBarBackButtonHidden(true)
    .toolbar {
        ToolbarItem(placement: .navigationBarLeading) {
            Button("Back") { path.removeLast() }
        }
    }
```

## Examples
```swift
// Conditional back button hiding:
struct DetailView: View {
    @Environment(\.dismiss) var dismiss
    @Binding var path: NavigationPath
    let isModal: Bool

    var body: some View {
        Text("Detail")
            .navigationBarBackButtonHidden(isModal)
            .toolbar {
                if isModal {
                    ToolbarItem(placement: .navigationBarLeading) {
                        Button("Close") { dismiss() }
                    }
                }
            }
    }
}
```

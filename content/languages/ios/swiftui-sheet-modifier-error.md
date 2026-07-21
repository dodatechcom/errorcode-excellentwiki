---
title: "[Solution] SwiftUI .sheet Modifier Error"
description: "Fix SwiftUI .sheet modifier modal presentation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .sheet Modifier Error

Sheet modifier errors occur when the sheet is not properly presented, when the sheet does not dismiss, or when the sheet conflicts with the view hierarchy.

## Common Causes
- Sheet not presented
- Sheet does not dismiss
- Sheet conflicts with hierarchy
- Sheet not matching design

## How to Fix
1. Present sheet properly
2. Ensure sheet dismisses
3. Ensure sheet is compatible with hierarchy
4. Match design specifications

```swift
struct ContentView: View {
    @State private var showSheet = false

    var body: some View {
        Button("Show Sheet") { showSheet = true }
            .sheet(isPresented: $showSheet) {
                Text("Sheet Content")
            }
    }
}
```

## Examples
```swift
// With detents:
.sheet(isPresented: $showSheet) {
    Text("Sheet")
        .presentationDetents([.medium, .large])
}

// With custom height:
.sheet(isPresented: $showSheet) {
    Text("Sheet")
        .presentationDetents([.height(200)])
}

// With drag indicator:
.sheet(isPresented: $showSheet) {
    Text("Sheet")
        .presentationDragIndicator(.visible)
}
```

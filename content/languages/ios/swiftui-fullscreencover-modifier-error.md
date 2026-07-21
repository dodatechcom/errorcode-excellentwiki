---
title: "[Solution] SwiftUI .fullScreenCover Modifier Error"
description: "Fix SwiftUI .fullScreenCover modifier full-screen presentation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .fullScreenCover Modifier Error

FullScreenCover modifier errors occur when the cover is not properly presented, when the cover does not dismiss, or when the cover conflicts with the view hierarchy.

## Common Causes
- Cover not presented
- Cover does not dismiss
- Cover conflicts with hierarchy
- Cover not matching design

## How to Fix
1. Present cover properly
2. Ensure cover dismisses
3. Ensure cover is compatible with hierarchy
4. Match design specifications

```swift
struct ContentView: View {
    @State private var showCover = false

    var body: some View {
        Button("Show Cover") { showCover = true }
            .fullScreenCover(isPresented: $showCover) {
                Text("Full Screen Cover")
            }
    }
}
```

## Examples
```swift
// Dismiss cover:
.fullScreenCover(isPresented: $showCover) {
    VStack {
        Text("Cover")
        Button("Dismiss") { showCover = false }
    }
}

// With custom transition:
.fullScreenCover(isPresented: $showCover) {
    Text("Cover")
        .transition(.slide)
}
```

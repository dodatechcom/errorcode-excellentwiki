---
title: "[Solution] SwiftUI .toolbar Modifier Error"
description: "Fix SwiftUI .toolbar modifier toolbar placement and content errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .toolbar Modifier Error

Toolbar modifier errors occur when the toolbar content is not properly placed, when the toolbar conflicts with navigation, or when the toolbar does not match the design.

## Common Causes
- Toolbar content not placed
- Toolbar conflicts with navigation
- Toolbar not matching design
- Toolbar not appearing

## How to Fix
1. Place toolbar content properly
2. Ensure toolbar is compatible with navigation
3. Match design specifications
4. Ensure toolbar appears

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            Text("Hello")
                .toolbar {
                    ToolbarItem(placement: .navigationBarTrailing) {
                        Button("Edit") { }
                    }
                }
        }
    }
}
```

## Examples
```swift
// Multiple toolbar items:
.toolbar {
    ToolbarItem(placement: .navigationBarLeading) {
        Button("Back") { }
    }
    ToolbarItem(placement: .navigationBarTrailing) {
        Button("Save") { }
    }
}

// Custom toolbar:
.toolbar {
    ToolbarItem(placement: .bottomBar) {
        HStack {
            Button("Share") { }
            Spacer()
            Button("Delete") { }
        }
    }
}
```
